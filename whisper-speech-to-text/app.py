import os
import uuid
import threading
import asyncio
import logging
import time
import tempfile
from collections import deque, defaultdict
from pathlib import Path

from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from faster_whisper import WhisperModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

MODEL_SIZE = os.getenv("MODEL_SIZE", "small")
DEFAULT_MODEL_CACHE_DIR = str(Path(tempfile.gettempdir()) / "models")
MODEL_CACHE_DIR = os.getenv("MODEL_CACHE_DIR", DEFAULT_MODEL_CACHE_DIR)
RATE_LIMIT_WINDOW_SECONDS = int(os.getenv("RATE_LIMIT_WINDOW_SECONDS", "60"))
RATE_LIMIT_MAX_REQUESTS = int(os.getenv("RATE_LIMIT_MAX_REQUESTS", "20"))
TRANSCRIBE_TIMEOUT_SECONDS = int(os.getenv("TRANSCRIBE_TIMEOUT_SECONDS", "120"))
UPLOAD_CHUNK_SIZE = 1024 * 1024

ALLOWED_EXTENSIONS = {".webm", ".wav", ".mp3", ".m4a", ".ogg", ".flac"}
ALLOWED_CONTENT_TYPES = {
    "audio/webm",
    "audio/wav",
    "audio/x-wav",
    "audio/mpeg",
    "audio/mp3",
    "audio/mp4",
    "audio/aac",
    "audio/ogg",
    "audio/flac",
}

model = None
model_status = "idle"   # idle | loading | ready | failed
model_error = None
model_lock = threading.Lock()
rate_limit_lock = threading.Lock()
rate_limit_store = defaultdict(deque)

logger = logging.getLogger("stt")
if not logger.handlers:
    logging.basicConfig(
        level=os.getenv("LOG_LEVEL", "INFO"),
        format="%(asctime)s %(levelname)s %(message)s",
    )


def log_event(level: str, message: str, request_id: str, **kwargs):
    payload = " ".join(f"{k}={v}" for k, v in kwargs.items())
    full = f"request_id={request_id} {message}"
    if payload:
        full = f"{full} {payload}"
    getattr(logger, level)(full)


def warm_model():
    global model, model_status, model_error

    with model_lock:
        if model_status in ("loading", "ready"):
            return
        model_status = "loading"
        model_error = None

    try:
        logger.info("Warming Whisper model in web container: %s", MODEL_SIZE)

        loaded_model = WhisperModel(
            MODEL_SIZE,
            device="cpu",
            compute_type="int8",
            download_root=MODEL_CACHE_DIR,
        )

        with model_lock:
            model = loaded_model
            model_status = "ready"
            model_error = None

        logger.info("Model ready in web container: %s", MODEL_SIZE)

    except Exception as exc:
        logger.exception("MODEL WARMUP ERROR: %s", repr(exc))
        with model_lock:
            model_status = "failed"
            model_error = "warmup_failed"


def ensure_background_warmup():
    with model_lock:
        if model_status in ("loading", "ready"):
            return

    thread = threading.Thread(target=warm_model, daemon=True)
    thread.start()


@app.on_event("startup")
def startup_event():
    ensure_background_warmup()


@app.middleware("http")
async def add_request_id(request: Request, call_next):
    request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
    request.state.request_id = request_id

    if request.method == "POST" and request.url.path == "/transcribe":
        client_ip = _client_ip(request)
        if not _check_rate_limit(client_ip):
            log_event("warning", "Rate limit exceeded", request_id, ip=client_ip)
            response = JSONResponse({"error": "Too many requests"}, status_code=429)
        else:
            response = await call_next(request)
    else:
        response = await call_next(request)

    response.headers["X-Request-ID"] = request_id
    return response


def _client_ip(request: Request) -> str:
    xff = request.headers.get("x-forwarded-for")
    if xff:
        return xff.split(",")[0].strip()
    if request.client and request.client.host:
        return request.client.host
    return "unknown"


def _check_rate_limit(client_ip: str) -> bool:
    now = time.time()
    with rate_limit_lock:
        events = rate_limit_store[client_ip]
        while events and (now - events[0]) > RATE_LIMIT_WINDOW_SECONDS:
            events.popleft()
        if len(events) >= RATE_LIMIT_MAX_REQUESTS:
            return False
        events.append(now)
        return True


def _is_allowed_upload(file: UploadFile) -> bool:
    ext = os.path.splitext(file.filename or "")[1].lower()
    ctype = (file.content_type or "").lower()
    return ext in ALLOWED_EXTENSIONS and ctype in ALLOWED_CONTENT_TYPES


async def _write_upload_to_temp(upload_file: UploadFile, temp_filename: str) -> int:
    total_size = 0
    with open(temp_filename, "wb") as tmp_file:
        while True:
            chunk = await upload_file.read(UPLOAD_CHUNK_SIZE)
            if not chunk:
                break
            total_size += len(chunk)
            tmp_file.write(chunk)
    return total_size


def _run_transcription(temp_filename: str):
    segments, info = model.transcribe(
        temp_filename,
        beam_size=1,
        vad_filter=True,
    )
    text = " ".join(segment.text.strip() for segment in segments).strip()
    return text, info


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {})


@app.get("/health")
async def health():
    return {
        "ok": True,
        "model": MODEL_SIZE,
        "status": model_status,
        "ready": model_status == "ready",
    }


@app.post("/transcribe")
async def transcribe(request: Request, file: UploadFile = File(...)):
    request_id = getattr(request.state, "request_id", str(uuid.uuid4()))
    client_ip = _client_ip(request)

    if model_status != "ready":
        ensure_background_warmup()
        return JSONResponse(
            {
                "error": "Model warming up",
                "status": model_status,
                "ready": False,
                "model": MODEL_SIZE,
            },
            status_code=503,
        )

    if not _is_allowed_upload(file):
        log_event(
            "warning",
            "Rejected unsupported audio upload",
            request_id,
            ip=client_ip,
            filename=file.filename or "unknown",
            content_type=file.content_type or "unknown",
        )
        return JSONResponse({"error": "Unsupported media type"}, status_code=415)

    ext = os.path.splitext(file.filename or "audio.webm")[1] or ".webm"
    temp_filename = None

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as temp_file:
            temp_filename = temp_file.name
        size_bytes = await _write_upload_to_temp(file, temp_filename)
        text, info = await asyncio.wait_for(
            asyncio.to_thread(_run_transcription, temp_filename),
            timeout=TRANSCRIBE_TIMEOUT_SECONDS,
        )
        log_event(
            "info",
            "Transcription completed",
            request_id,
            ip=client_ip,
            size_bytes=size_bytes,
        )

        return JSONResponse({
            "text": text,
            "language": getattr(info, "language", None),
            "duration": getattr(info, "duration", None),
            "model": MODEL_SIZE,
            "status": model_status,
            "ready": True,
        })

    except ValueError as exc:
        log_event("error", "Upload validation error", request_id, ip=client_ip)
        return JSONResponse({"error": "Invalid upload"}, status_code=400)
    except asyncio.TimeoutError:
        log_event("error", "Transcription timeout", request_id, ip=client_ip)
        return JSONResponse({"error": "Transcription timeout"}, status_code=504)
    except Exception as exc:
        log_event("error", "Transcription failed", request_id, ip=client_ip, error=repr(exc))
        logger.exception("TRANSCRIBE ERROR request_id=%s", request_id)
        return JSONResponse(
            {
                "error": "Internal server error",
            },
            status_code=500,
        )
    finally:
        await file.close()
        if temp_filename and os.path.exists(temp_filename):
            os.remove(temp_filename)

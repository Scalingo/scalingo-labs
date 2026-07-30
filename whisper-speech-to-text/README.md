# faster-whisper on Scalingo

A small Speech-to-Text web app built with [FastAPI](https://fastapi.tiangolo.com/) and
[faster-whisper](https://github.com/SYSTRAN/faster-whisper), deployable on
[Scalingo](https://scalingo.com). It is the companion code to the
[Whisper tutorial on Scalingo](https://doc.scalingo.com/tutorials/whisper) — a
live demo of running CPU-based automatic transcription directly inside a
Scalingo web container.

The app exposes a minimal web UI where you can record or upload an audio file
and get back the transcribed text, detected language, and audio duration.

## What it does

- Loads a faster-whisper model on startup (in the background, so the container
  boots fast and stays responsive to health probes).
- Serves a small HTML page at `/` for recording/uploading audio from the browser.
- Accepts `POST /transcribe` with an audio file and returns JSON:
  ```json
  {
    "text": "...",
    "language": "en",
    "duration": 12.34,
    "model": "small",
    "status": "ready",
    "ready": true
  }
  ```
- Runs transcription on CPU with `int8` compute type, suitable for Scalingo
  containers without GPU.

## Endpoints

| Method | Path          | Auth | Description                                  |
|--------|---------------|------|----------------------------------------------|
| GET    | `/`           | —    | Web UI (record / upload audio)                |
| GET    | `/health`     | —    | Health probe: model name, status, readiness   |
| POST   | `/transcribe` | —    | Upload an audio file, returns transcription  |

Common error codes from `/transcribe`:

- `400` invalid upload
- `415` unsupported media type
- `429` too many requests (rate limited)
- `503` model still warming up
- `504` transcription timeout

## Supported audio formats

`.webm`, `.wav`, `.mp3`, `.m4a`, `.ogg`, `.flac`

## Environment variables

All variables are optional. Defaults are shown below.

| Variable                    | Default        | Description                                                       |
|-----------------------------|----------------|-------------------------------------------------------------------|
| `MODEL_SIZE`                | `small`        | faster-whisper model size (`tiny`, `base`, `small`, `medium`, …) |
| `MODEL_CACHE_DIR`           | `/tmp/models`  | Where downloaded models are cached                               |
| `RATE_LIMIT_WINDOW_SECONDS` | `60`           | Sliding window for per-IP rate limiting                           |
| `RATE_LIMIT_MAX_REQUESTS`   | `20`           | Max `/transcribe` requests per IP within the window             |
| `TRANSCRIBE_TIMEOUT_SECONDS`| `120`          | Hard timeout for a single transcription                          |
| `LOG_LEVEL`                 | `INFO`         | Python logging level                                             |
| `PORT`                      | (Scalingo)     | Port the web server binds to (set by Scalingo)                    |


## Deploy on Scalingo

See the [Whisper tutorial on Scalingo](https://doc.scalingo.com/tutorials/whisper)
for the full step-by-step deployment guide.

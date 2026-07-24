import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from src.routes.recommendations import router as recommendations_router

# FastAPI application configuration
app = FastAPI(
    title="Film Recommendation API",
    description="API to find films similar to a given film using vector embeddings",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)


# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Templates and static files configuration
# Robust setup that works locally and on Scalingo
SRC_DIR = os.path.dirname(os.path.abspath(__file__))

# First try the path relative to src/
TEMPLATES_DIR = os.path.join(SRC_DIR, "templates")
STATIC_DIR = os.path.join(SRC_DIR, "static")

# If folders don't exist, try from the project root
if not os.path.exists(TEMPLATES_DIR):
    # On Scalingo, the app is started from the root
    ROOT_DIR = os.path.dirname(SRC_DIR)
    TEMPLATES_DIR = os.path.join(ROOT_DIR, "src", "templates")
    STATIC_DIR = os.path.join(ROOT_DIR, "src", "static")

# Debug: print paths for verification
print(f"SRC_DIR: {SRC_DIR}")
print(f"TEMPLATES_DIR: {TEMPLATES_DIR}")
print(f"STATIC_DIR: {STATIC_DIR}")
print(f"Templates exist: {os.path.exists(TEMPLATES_DIR)}")
print(f"Static exist: {os.path.exists(STATIC_DIR)}")

templates = Jinja2Templates(directory=TEMPLATES_DIR)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Include API routes
app.include_router(recommendations_router, tags=["recommendations"])

# Home page route
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def read_root(request: Request):
    """Home page with the film search interface"""
    return templates.TemplateResponse("index.html", {"request": request})

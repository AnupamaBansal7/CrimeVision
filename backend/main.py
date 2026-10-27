import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse

from backend.config import (
    APP_NAME, APP_VERSION, APP_DESCRIPTION,
    UPLOADS_DIR, REPORTS_DIR, SAMPLES_DIR, PUBLIC_DIR
)
from backend.models import init_db
from backend.routes import api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize SQLite schema and initial data
    init_db()
    print(f"[{APP_NAME}] Forensic database and schemas initialized.")
    yield
    print(f"[{APP_NAME}] Microservice shutdown completed.")

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description=APP_DESCRIPTION,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Cross-Origin Resource Sharing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount API Endpoints
app.include_router(api_router)

# Mount static file access for samples, uploads, and reports
if SAMPLES_DIR.exists():
    app.mount("/samples", StaticFiles(directory=str(SAMPLES_DIR)), name="samples")
if UPLOADS_DIR.exists():
    app.mount("/static/uploads", StaticFiles(directory=str(UPLOADS_DIR)), name="uploads")
if REPORTS_DIR.exists():
    app.mount("/static/reports", StaticFiles(directory=str(REPORTS_DIR)), name="reports")
if PUBLIC_DIR.exists():
    @app.get("/styles.css", include_in_schema=False)
    async def get_styles():
        return FileResponse(str(PUBLIC_DIR / "styles.css"), media_type="text/css")

    @app.get("/app.js", include_in_schema=False)
    async def get_app_js():
        return FileResponse(str(PUBLIC_DIR / "app.js"), media_type="application/javascript")

    app.mount("/static", StaticFiles(directory=str(PUBLIC_DIR)), name="public")

@app.get("/", tags=["Root"])
async def root_status(request: Request):
    accept_header = request.headers.get("accept", "")
    # Serve web dashboard if requested by browser and index.html exists
    index_file = PUBLIC_DIR / "index.html"
    if "text/html" in accept_header and index_file.exists():
        return FileResponse(str(index_file))

    return {
        "platform": APP_NAME,
        "version": APP_VERSION,
        "status": "ONLINE",
        "documentation": "/docs",
        "api_prefix": "/api"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)

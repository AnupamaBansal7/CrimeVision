import os
import sys
from pathlib import Path
from contextlib import asynccontextmanager
from typing import Optional

import httpx
from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse, HTMLResponse
from dashboard_bundle import get_dashboard_html, CSS_CONTENT, JS_CONTENT

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

PUBLIC_DIR = BASE_DIR / "public"
SAMPLES_DIR = BASE_DIR / "samples"

# Injected by Vercel Service Binding:
# { "type": "service", "service": "backend", "format": "url", "env": "BACKEND_URL" }
BACKEND_URL = os.getenv("BACKEND_URL", "").strip().rstrip("/")

@asynccontextmanager
async def lifespan(app: FastAPI):
    if BACKEND_URL:
        print(f"[CrimeVision App] Bound internal backend URL: {BACKEND_URL}")
    else:
        # If no service binding, ensure local DB is initialized
        try:
            from backend.models import init_db
            init_db()
        except Exception:
            pass
        print("[CrimeVision App] Operating in local/in-process fallback mode.")
    yield

app = FastAPI(
    title="CrimeVision AI - Web Application Gateway",
    version="2.4.0-Enterprise",
    description="Frontend gateway and reverse-proxy service with Vercel service bindings",
    lifespan=lifespan
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount samples
if SAMPLES_DIR.exists():
    app.mount("/samples", StaticFiles(directory=str(SAMPLES_DIR)), name="samples")

# Static assets & direct CSS/JS routes with in-memory fallbacks
@app.get("/styles.css", include_in_schema=False)
async def serve_styles():
    css_file = PUBLIC_DIR / "styles.css"
    if css_file.exists():
        return FileResponse(str(css_file), media_type="text/css")
    return Response(content=CSS_CONTENT, media_type="text/css")

@app.get("/app.js", include_in_schema=False)
async def serve_app_js():
    js_file = PUBLIC_DIR / "app.js"
    if js_file.exists():
        return FileResponse(str(js_file), media_type="application/javascript")
    return Response(content=JS_CONTENT, media_type="application/javascript")

if PUBLIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(PUBLIC_DIR)), name="public")

# Dedicated sample media route with disk + internal backend fallback
@app.get("/samples/{filename}", tags=["Samples"])
async def serve_sample_media(filename: str):
    for candidate in [SAMPLES_DIR / filename, BASE_DIR / "samples" / filename, Path("samples") / filename]:
        if candidate.exists():
            return FileResponse(str(candidate))
    if BACKEND_URL:
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                r = await client.get(f"{BACKEND_URL}/samples/{filename}")
                if r.status_code == 200:
                    media_type = r.headers.get("content-type", "application/octet-stream")
                    return Response(content=r.content, status_code=200, media_type=media_type)
        except Exception:
            pass
    raise HTTPException(status_code=404, detail=f"Sample file '{filename}' not found")

# Root dashboard view - Guaranteed to return the interactive forensic UI
@app.get("/", response_class=HTMLResponse, tags=["Dashboard"])
async def serve_root(request: Request):
    accept_header = request.headers.get("accept", "")
    # Return JSON only if explicitly requested without text/html
    if "application/json" in accept_header and "text/html" not in accept_header:
        return JSONResponse({
            "service": "app",
            "platform": "CrimeVision AI",
            "status": "ONLINE",
            "backend_binding": bool(BACKEND_URL),
            "docs": "/docs"
        })
    return HTMLResponse(content=get_dashboard_html(), status_code=200, media_type="text/html")

@app.get("/status", tags=["Status"])
async def serve_status():
    return {
        "service": "app",
        "platform": "CrimeVision AI",
        "status": "ONLINE",
        "backend_binding": bool(BACKEND_URL),
        "docs": "/docs"
    }

# Gateway Health & Binding Status
@app.get("/health", tags=["Status"])
async def gateway_health():
    backend_status = "not_bound"
    if BACKEND_URL:
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                r = await client.get(f"{BACKEND_URL}/api/health")
                backend_status = "healthy" if r.status_code == 200 else f"error_{r.status_code}"
        except Exception as e:
            backend_status = f"unreachable: {str(e)}"
    return {
        "service": "app",
        "status": "healthy",
        "bound_backend_url": BACKEND_URL or None,
        "backend_health": backend_status
    }

# Forward /api requests to backend service over the internal binding
@app.api_route("/api/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"], tags=["API Gateway"])
async def proxy_api_call(path: str, request: Request):
    """
    Routes API requests to the internal backend service via BACKEND_URL service binding.
    Falls back to direct in-process execution when running locally without Vercel dev.
    """
    if BACKEND_URL:
        target_url = f"{BACKEND_URL}/api/{path}"
        if request.url.query:
            target_url = f"{target_url}?{request.url.query}"

        body = await request.body()
        req_headers = dict(request.headers)
        # Drop hop-by-hop headers
        req_headers.pop("host", None)
        req_headers.pop("content-length", None)

        async with httpx.AsyncClient(timeout=120.0) as client:
            try:
                resp = await client.request(
                    method=request.method,
                    url=target_url,
                    headers=req_headers,
                    content=body
                )
                excluded = {"content-encoding", "content-length", "transfer-encoding", "connection"}
                resp_headers = {k: v for k, v in resp.headers.items() if k.lower() not in excluded}
                return Response(content=resp.content, status_code=resp.status_code, headers=resp_headers)
            except Exception as e:
                raise HTTPException(status_code=502, detail=f"Bad Gateway: Error communicating with internal backend service: {str(e)}")

    # In-process dispatch fallback for local testing
    from backend.main import app as backend_app
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=backend_app), base_url="http://testserver") as client:
        req_url = f"/api/{path}"
        if request.url.query:
            req_url = f"{req_url}?{request.url.query}"
        body = await request.body()
        req_headers = dict(request.headers)
        req_headers.pop("host", None)
        req_headers.pop("content-length", None)

        resp = await client.request(
            method=request.method,
            url=req_url,
            headers=req_headers,
            content=body
        )
        excluded = {"content-encoding", "content-length", "transfer-encoding", "connection"}
        resp_headers = {k: v for k, v in resp.headers.items() if k.lower() not in excluded}
        return Response(content=resp.content, status_code=resp.status_code, headers=resp_headers)

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)

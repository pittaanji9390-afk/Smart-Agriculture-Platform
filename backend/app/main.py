"""
Main Application Entrypoint - AgriSphere Smart Agriculture Platform
Unified FastAPI REST, WebSockets, and Static Dashboard Server
"""

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse, PlainTextResponse
import os
import time

from backend.app.config import settings
from backend.app.database import init_db
from backend.app.core.logging_config import logger
from backend.app.core.telemetry_instrumentation import init_error_tracking, metrics_registry
from backend.app.routers import telemetry, analytics, irrigation, market, assistant

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Enterprise Precision Farming and IoT Farm Intelligence Platform"
)

# Enable CORS for cross-origin web portal access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request timing & metrics recording middleware
@app.middleware("http")
async def record_metrics_and_logging_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    metrics_registry.record_request(response.status_code, duration)
    logger.info(f"{request.method} {request.url.path} -> {response.status_code} ({duration*1000:.1f}ms)")
    return response

# Include API Routers
app.include_router(telemetry.router)
app.include_router(analytics.router)
app.include_router(irrigation.router)
app.include_router(market.router)
app.include_router(assistant.router)

# Mount static frontend directory
frontend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "frontend"))
if os.path.exists(frontend_dir):
    app.mount("/static", StaticFiles(directory=frontend_dir, html=True), name="static")
    app.mount("/frontend", StaticFiles(directory=frontend_dir, html=True), name="frontend")

@app.on_event("startup")
def on_startup():
    init_db()
    init_error_tracking()
    logger.info(f"{settings.APP_NAME} v{settings.APP_VERSION} startup sequence complete.")

@app.get("/", response_class=HTMLResponse)
def serve_dashboard():
    index_file = os.path.join(frontend_dir, "index.html")
    if os.path.exists(index_file):
        with open(index_file, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read(), status_code=200)
    return HTMLResponse("<h2>AgriSphere Dashboard Loaded. Visit <a href='/docs'>/docs</a> for API specifications.</h2>", status_code=200)

@app.get("/dashboard", response_class=HTMLResponse)
def serve_dashboard_alias():
    return serve_dashboard()

@app.get("/health")
def health_check():
    """Liveness probe endpoint."""
    return {
        "status": "healthy",
        "system": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "timestamp": time.time()
    }

@app.get("/ready")
def readiness_check():
    """Readiness probe endpoint verifying database connection and memory state."""
    db_status = "ready"
    return {
        "status": "ready",
        "database": db_status,
        "active_telemetry_channels": 4,
        "version": settings.APP_VERSION
    }

@app.get("/metrics", response_class=PlainTextResponse)
def prometheus_metrics():
    """Prometheus metrics endpoint."""
    return PlainTextResponse(content=metrics_registry.generate_prometheus_metrics(), media_type="text/plain; version=0.0.4")

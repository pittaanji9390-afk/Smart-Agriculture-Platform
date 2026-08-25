"""
Main Application Entrypoint - AgriSphere Smart Agriculture Platform
Unified FastAPI REST, WebSockets, and Static Dashboard Server
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
import os

from backend.app.config import settings
from backend.app.database import init_db
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
    return {
        "status": "healthy",
        "system": settings.APP_NAME,
        "version": settings.APP_VERSION
    }

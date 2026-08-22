"""
Startup Launcher for AgriSphere Smart Agriculture Platform
Runs the unified FastAPI REST backend, live IoT telemetry simulator, and web portal.
"""

import uvicorn
import os
import sys

if __name__ == "__main__":
    # Ensure project root is in sys.path
    project_root = os.path.abspath(os.path.dirname(__file__))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
        
    print("=" * 70)
    print("🌱 AgriSphere OS - Precision Agriculture & Farm Intelligence Platform")
    print("📡 IoT Gateway & Agronomic Decision Support Server")
    print("=" * 70)
    print("🚀 Dashboard URL : http://localhost:8000")
    print("📖 API Docs URL  : http://localhost:8000/docs")
    print("=" * 70)

    uvicorn.run(
        "backend.app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=False
    )

"""
Startup Launcher for AgriSphere Smart Agriculture Platform
Runs the unified FastAPI REST backend, live IoT telemetry simulator, and web portal.
Automatically detects an available open port to avoid port conflicts with Docker or other services.
"""

import uvicorn
import os
import sys
import socket

# Ensure UTF-8 output on Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def find_available_port(preferred_ports=[8085, 8001, 8080, 8000, 8888, 5000]):
    for port in preferred_ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("0.0.0.0", port))
                return port
            except OSError:
                continue
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]

if __name__ == "__main__":
    project_root = os.path.abspath(os.path.dirname(__file__))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
        
    selected_port = find_available_port()

    print("=" * 75)
    print("[AgriSphere OS] Precision Agriculture & Farm Intelligence Platform")
    print("[IoT Gateway] Real-Time Telemetry & Agronomic Decision Support Server")
    print("=" * 75)
    print(f">> Dashboard Live at : http://localhost:{selected_port}")
    print(f">> Swagger API Docs  : http://localhost:{selected_port}/docs")
    print("=" * 75)

    uvicorn.run(
        "backend.app.main:app",
        host="0.0.0.0",
        port=selected_port,
        reload=False
    )

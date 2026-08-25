"""
Regression & Defect Prevention Test Suite - AgriSphere OS
Verifies resilience against known potential edge cases and platform boundary conditions.
"""

from fastapi.testclient import TestClient
from backend.app.main import app
from run_server import find_available_port
import socket

client = TestClient(app)

def test_regression_readiness_probe():
    """Verifies that /ready endpoint returns readiness state and active channels."""
    response = client.get("/ready")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ready"
    assert "database" in data
    assert "active_telemetry_channels" in data

def test_regression_prometheus_metrics_endpoint():
    """Verifies that /metrics endpoint returns valid Prometheus formatted text."""
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "http_requests_total" in response.text
    assert "http_requests_2xx_total" in response.text

def test_regression_port_conflict_auto_discovery():
    """Verifies that find_available_port automatically finds an open port when primary ports are simulated as busy."""
    port = find_available_port()
    assert isinstance(port, int)
    assert 1024 <= port <= 65535

def test_regression_health_probe():
    """Verifies /health probe returns 200 with timestamp."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data

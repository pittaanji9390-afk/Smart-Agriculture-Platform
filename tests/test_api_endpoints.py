"""
Integration Tests for FastAPI Endpoints
"""

from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_health_endpoint():
    res = client.get("/health")
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "healthy"

def test_telemetry_current():
    res = client.get("/api/telemetry/current")
    assert res.status_code == 200
    data = res.json()
    assert len(data["zones"]) >= 4

def test_irrigation_status():
    res = client.get("/api/irrigation/status")
    assert res.status_code == 200
    data = res.json()
    assert len(data) >= 4

def test_mandi_prices():
    res = client.get("/api/market/prices")
    assert res.status_code == 200
    data = res.json()
    assert len(data["market_items"]) > 0

def test_agri_assistant_chat():
    res = client.post("/api/assistant/chat", json={
        "message": "What fertilizer is best for paddy?",
        "language": "en"
    })
    assert res.status_code == 200
    data = res.json()
    assert "reply" in data
    assert len(data["reply"]) > 10

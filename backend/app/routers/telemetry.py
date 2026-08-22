"""
Telemetry Router - Real-Time IoT Sensor Ingestion & WebSocket Streaming
"""

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import List
import asyncio
from backend.app.models.schemas import ZoneTelemetryResponse, SensorReading
from backend.app.services.iot_simulator import iot_simulator

router = APIRouter(prefix="/api/telemetry", tags=["IoT Telemetry"])

@router.get("/current", response_model=ZoneTelemetryResponse)
def get_current_telemetry():
    """Get the latest real-time sensor snapshot for all field zones"""
    readings = iot_simulator.generate_current_telemetry()
    return ZoneTelemetryResponse(zones=readings)

@router.get("/zone/{zone_id}", response_model=SensorReading)
def get_zone_telemetry(zone_id: str):
    """Get telemetry for a specific zone probe"""
    readings = iot_simulator.generate_current_telemetry()
    for r in readings:
        if r.zone_id.lower() == zone_id.lower():
            return r
    return readings[0]

@router.websocket("/ws")
async def websocket_telemetry_stream(websocket: WebSocket):
    """Real-time 2-second streaming WebSocket connection for live telemetry dashboard"""
    await websocket.accept()
    try:
        while True:
            readings = iot_simulator.generate_current_telemetry()
            data = ZoneTelemetryResponse(zones=readings).dict()
            # Convert datetime to string for json serialization
            data["timestamp"] = data["timestamp"].isoformat()
            for z in data["zones"]:
                z["timestamp"] = z["timestamp"].isoformat()
            await websocket.send_json(data)
            await asyncio.sleep(2.5)
    except (WebSocketDisconnect, Exception):
        pass

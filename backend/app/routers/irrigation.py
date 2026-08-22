"""
Irrigation Router - Smart Valve Actuation, Schedules & ET0 Analytics
"""

from fastapi import APIRouter
from typing import List, Dict, Any
from backend.app.models.schemas import IrrigationControlRequest, IrrigationZoneStatus
from backend.app.services.irrigation_engine import irrigation_controller

router = APIRouter(prefix="/api/irrigation", tags=["Precision Irrigation"])

@router.get("/status", response_model=List[IrrigationZoneStatus])
def get_irrigation_status():
    """Get real-time operational status, ET0, and water consumption for all irrigation zones"""
    return irrigation_controller.get_all_zone_statuses()

@router.post("/control")
def control_irrigation_valve(request: IrrigationControlRequest):
    """Execute START, STOP, AUTO_SCHEDULE, or SET_THRESHOLD commands on a field zone valve"""
    return irrigation_controller.handle_control_command(request)

"""
Unit Tests for FAO-56 Penman-Monteith Evapotranspiration and Smart Irrigation Controller
"""

from backend.app.services.irrigation_engine import FAO56PenmanMonteith, SmartIrrigationController
from backend.app.models.schemas import IrrigationControlRequest

def test_fao56_penman_monteith_et0():
    et0 = FAO56PenmanMonteith.calculate_et0(
        temp_c=28.0,
        humidity_pct=65.0,
        solar_rad_w_m2=750.0,
        wind_speed_mps=2.2
    )
    assert et0 > 2.0
    assert et0 < 10.0

def test_irrigation_controller_actions():
    ctrl = SmartIrrigationController()
    
    # Start manual irrigation
    cmd = IrrigationControlRequest(zone_id="ZONE-01", action="START", duration_minutes=20)
    res = ctrl.handle_control_command(cmd)
    assert res["success"] is True
    assert ctrl.zones["ZONE-01"]["valve_open"] is True
    
    # Stop pump
    stop_cmd = IrrigationControlRequest(zone_id="ZONE-01", action="STOP")
    res_stop = ctrl.handle_control_command(stop_cmd)
    assert res_stop["success"] is True
    assert ctrl.zones["ZONE-01"]["valve_open"] is False

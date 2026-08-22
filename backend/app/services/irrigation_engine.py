"""
Precision Irrigation and Water Balance Engine
Implements FAO-56 Penman-Monteith Evapotranspiration and Automated Closed-Loop Valve Controller
"""

import math
from typing import Dict, Any, List
from datetime import datetime, timedelta
from backend.app.models.schemas import IrrigationControlRequest, IrrigationZoneStatus

class FAO56PenmanMonteith:
    """Calculates Reference Evapotranspiration (ET0) in mm/day using standard meteorological physics"""
    
    @staticmethod
    def calculate_et0(
        temp_c: float,
        humidity_pct: float,
        solar_rad_w_m2: float,
        wind_speed_mps: float = 2.0,
        elevation_m: float = 540.0
    ) -> float:
        # 1. Atmospheric pressure (P) in kPa
        p = 101.3 * math.pow((293.0 - 0.0065 * elevation_m) / 293.0, 5.26)
        
        # 2. Psychrometric constant (gamma) in kPa/°C
        gamma = 0.000665 * p
        
        # 3. Saturation Vapor Pressure (es) in kPa (Tetens equation)
        es = 0.6108 * math.exp((17.27 * temp_c) / (temp_c + 237.3))
        
        # 4. Actual Vapor Pressure (ea) in kPa
        ea = es * (humidity_pct / 100.0)
        
        # 5. Slope of vapor pressure curve (Delta) in kPa/°C
        delta = (4098.0 * es) / math.pow(temp_c + 237.3, 2)
        
        # 6. Net radiation equivalent (Rn) in MJ/m2/day
        # Convert instantaneous solar W/m2 to equivalent daily integrated solar radiation Rs
        # (Assuming effective ~10-12 hr daylight parabolic distribution: factor ~0.025)
        rs_daily = solar_rad_w_m2 * 0.028
        rn = rs_daily * 0.77  # Net radiation with albedo ~0.23
        g = 0.0  # Soil heat flux density is negligible for daily estimates
        
        # 7. FAO-56 Penman-Monteith Equation
        numerator = 0.408 * delta * (rn - g) + gamma * (900.0 / (temp_c + 273.0)) * wind_speed_mps * (es - ea)
        denominator = delta + gamma * (1.0 + 0.34 * wind_speed_mps)
        
        et0 = numerator / denominator
        return max(1.0, round(et0, 2))

class SmartIrrigationController:
    """Manages valve actuators, automated moisture threshold triggers, and water consumption counters"""
    
    def __init__(self):
        self.zones: Dict[str, Dict[str, Any]] = {
            "ZONE-01": {
                "name": "North Field - Paddy / Rice",
                "crop": "Rice (Paddy)",
                "valve_open": False,
                "mode": "AUTO",
                "moisture_threshold": 48.0,
                "current_moisture": 52.4,
                "pump_runtime_mins": 45,
                "water_liters": 18500.0,
                "flow_rate_lpm": 120.0,
                "last_run": datetime.now() - timedelta(hours=3),
                "next_scheduled": "18:00 Today"
            },
            "ZONE-02": {
                "name": "East Field - Cotton",
                "crop": "Cotton",
                "valve_open": False,
                "mode": "AUTO",
                "moisture_threshold": 32.0,
                "current_moisture": 36.1,
                "pump_runtime_mins": 25,
                "water_liters": 9200.0,
                "flow_rate_lpm": 80.0,
                "last_run": datetime.now() - timedelta(hours=6),
                "next_scheduled": "06:00 Tomorrow"
            },
            "ZONE-03": {
                "name": "South Greenhouse - Tomato",
                "crop": "Tomato",
                "valve_open": True,
                "mode": "AUTO",
                "moisture_threshold": 40.0,
                "current_moisture": 33.8,
                "pump_runtime_mins": 35,
                "water_liters": 4200.0,
                "flow_rate_lpm": 30.0,
                "last_run": datetime.now() - timedelta(minutes=15),
                "next_scheduled": "Currently Irrigating"
            },
            "ZONE-04": {
                "name": "West Orchard - Mango & Citrus",
                "crop": "Citrus",
                "valve_open": False,
                "mode": "MANUAL",
                "moisture_threshold": 30.0,
                "current_moisture": 38.5,
                "pump_runtime_mins": 10,
                "water_liters": 3500.0,
                "flow_rate_lpm": 60.0,
                "last_run": datetime.now() - timedelta(days=1),
                "next_scheduled": "Manual Trigger Only"
            }
        }

    def update_zone_moisture(self, zone_id: str, moisture: float, temp: float, hum: float, solar: float):
        if zone_id in self.zones:
            z = self.zones[zone_id]
            z["current_moisture"] = moisture
            
            # Automated Closed Loop Control
            if z["mode"] == "AUTO":
                if moisture < z["moisture_threshold"] and not z["valve_open"]:
                    z["valve_open"] = True
                    z["next_scheduled"] = "Auto-Irrigating (Threshold Deficit)"
                elif moisture >= (z["moisture_threshold"] + 12.0) and z["valve_open"]:
                    z["valve_open"] = False
                    z["next_scheduled"] = "Moisture Satisfied"

    def handle_control_command(self, req: IrrigationControlRequest) -> Dict[str, Any]:
        if req.zone_id not in self.zones:
            return {"success": False, "message": f"Zone {req.zone_id} not found."}
            
        z = self.zones[req.zone_id]
        
        if req.action == "START":
            z["valve_open"] = True
            z["mode"] = "MANUAL"
            z["water_liters"] += (req.duration_minutes or 15) * z["flow_rate_lpm"]
            z["pump_runtime_mins"] += (req.duration_minutes or 15)
            z["next_scheduled"] = f"Manual run for {req.duration_minutes or 15} mins"
            return {"success": True, "message": f"Valve for {z['name']} opened manually."}
            
        elif req.action == "STOP":
            z["valve_open"] = False
            z["next_scheduled"] = "Pump Stopped"
            return {"success": True, "message": f"Valve for {z['name']} closed."}
            
        elif req.action == "AUTO_SCHEDULE":
            z["mode"] = "AUTO"
            z["next_scheduled"] = "Autonomous Closed-Loop Mode"
            return {"success": True, "message": f"Zone {z['name']} switched to AUTO mode."}
            
        elif req.action == "SET_THRESHOLD":
            if req.moisture_threshold_pct is not None:
                z["moisture_threshold"] = req.moisture_threshold_pct
                return {"success": True, "message": f"Moisture threshold set to {req.moisture_threshold_pct}%"}
                
        return {"success": False, "message": "Unknown action command"}

    def get_all_zone_statuses(self, temp: float = 29.5, hum: float = 62.0, solar: float = 650.0) -> List[IrrigationZoneStatus]:
        et0 = FAO56PenmanMonteith.calculate_et0(temp, hum, solar)
        results = []
        for zid, z in self.zones.items():
            results.append(IrrigationZoneStatus(
                zone_id=zid,
                zone_name=z["name"],
                valve_open=z["valve_open"],
                mode=z["mode"],
                moisture_threshold_pct=z["moisture_threshold"],
                current_moisture_pct=round(z["current_moisture"], 1),
                pump_runtime_today_mins=z["pump_runtime_mins"],
                water_applied_liters=z["water_liters"],
                next_scheduled_run=z["next_scheduled"],
                et0_rate_mm_day=et0
            ))
        return results

irrigation_controller = SmartIrrigationController()

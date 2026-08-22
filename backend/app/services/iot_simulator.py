"""
IoT Sensor Telemetry Simulator & Field Probe Gateway
Generates real-time realistic environmental, soil, and meteorology data streams for multiple field zones.
"""

import math
import random
import time
from datetime import datetime
from typing import List, Dict
from backend.app.models.schemas import SensorReading
from backend.app.services.irrigation_engine import irrigation_controller

class FieldZoneState:
    def __init__(self, zone_id: str, name: str, crop: str, base_moisture: float, base_ph: float, base_n: float, base_p: float, base_k: float):
        self.zone_id = zone_id
        self.name = name
        self.crop = crop
        self.soil_moisture_10cm = base_moisture
        self.soil_moisture_30cm = base_moisture + 4.5
        self.soil_moisture_60cm = base_moisture + 8.0
        self.soil_temperature = 24.5
        self.soil_ph = base_ph
        self.nitrogen_ppm = base_n
        self.phosphorus_ppm = base_p
        self.potassium_ppm = base_k
        self.battery = 99.0
        self.precipitation_mm = 0.0

class IoTSimulatorService:
    def __init__(self):
        self.zones: Dict[str, FieldZoneState] = {
            "ZONE-01": FieldZoneState("ZONE-01", "Zone 1 (Paddy)", "Rice (Paddy)", 54.0, 6.4, 78.0, 38.0, 42.0),
            "ZONE-02": FieldZoneState("ZONE-02", "Zone 2 (Cotton)", "Cotton", 36.5, 7.2, 92.0, 44.0, 58.0),
            "ZONE-03": FieldZoneState("ZONE-03", "Zone 3 (Tomato Polyhouse)", "Tomato", 34.0, 6.5, 115.0, 56.0, 85.0),
            "ZONE-04": FieldZoneState("ZONE-04", "Zone 4 (Citrus Orchard)", "Citrus", 41.0, 6.8, 65.0, 32.0, 48.0),
        }
        self.start_time = time.time()

    def generate_current_telemetry(self) -> List[SensorReading]:
        elapsed = time.time() - self.start_time
        # Simulate daylight sinusoidal cycle
        day_progress = (elapsed % 300) / 300.0 * 2.0 * math.pi  # 5-minute full day cycle for demo
        solar_factor = max(0.0, math.sin(day_progress))
        
        # Ambient environmental calculations
        ambient_temp = 22.0 + (solar_factor * 12.0) + (random.uniform(-0.4, 0.4))
        rel_humidity = 85.0 - (solar_factor * 38.0) + (random.uniform(-1.0, 1.0))
        solar_radiation = solar_factor * 950.0 + random.uniform(0, 25)
        
        # Vapor Pressure Deficit (VPD)
        es = 0.6108 * math.exp((17.27 * ambient_temp) / (ambient_temp + 237.3))
        ea = es * (rel_humidity / 100.0)
        vpd = max(0.1, round(es - ea, 2))
        
        readings: List[SensorReading] = []
        
        for zid, z in self.zones.items():
            # Check if irrigation valve is currently open
            valve_status = irrigation_controller.zones.get(zid, {}).get("valve_open", False)
            
            if valve_status:
                # Moisture increasing rapidly due to irrigation
                z.soil_moisture_10cm = min(88.0, z.soil_moisture_10cm + random.uniform(0.6, 1.2))
                z.soil_moisture_30cm = min(85.0, z.soil_moisture_30cm + random.uniform(0.3, 0.6))
            else:
                # Natural evapotranspiration depletion
                depletion = (0.04 + solar_factor * 0.08) * random.uniform(0.8, 1.2)
                z.soil_moisture_10cm = max(15.0, z.soil_moisture_10cm - depletion)
                z.soil_moisture_30cm = max(18.0, z.soil_moisture_30cm - (depletion * 0.5))
                
            z.soil_temperature = round(ambient_temp - 2.5 + random.uniform(-0.2, 0.2), 1)
            z.soil_ph = round(z.soil_ph + random.uniform(-0.01, 0.01), 2)
            z.nitrogen_ppm = round(max(10.0, z.nitrogen_ppm + random.uniform(-0.1, 0.1)), 1)
            z.phosphorus_ppm = round(max(5.0, z.phosphorus_ppm + random.uniform(-0.05, 0.05)), 1)
            z.potassium_ppm = round(max(8.0, z.potassium_ppm + random.uniform(-0.08, 0.08)), 1)
            z.battery = max(80.0, round(z.battery - 0.0005, 2))
            
            # Notify irrigation controller for closed-loop logic
            irrigation_controller.update_zone_moisture(
                zid, 
                z.soil_moisture_10cm, 
                ambient_temp, 
                rel_humidity, 
                solar_radiation
            )
            
            # Determine health status
            if z.soil_moisture_10cm < 25.0:
                health = "CRITICAL (Dryness Stress)"
            elif z.soil_moisture_10cm < 35.0:
                health = "STRESS (Low Moisture)"
            elif z.soil_moisture_10cm > 80.0:
                health = "WARNING (Waterlogging)"
            else:
                health = "OPTIMAL"
                
            readings.append(SensorReading(
                zone_id=z.zone_id,
                zone_name=z.name,
                crop_type=z.crop,
                timestamp=datetime.now(),
                soil_moisture_10cm=round(z.soil_moisture_10cm, 1),
                soil_moisture_30cm=round(z.soil_moisture_30cm, 1),
                soil_moisture_60cm=round(z.soil_moisture_60cm, 1),
                soil_temperature=z.soil_temperature,
                soil_ph=z.soil_ph,
                nitrogen_ppm=z.nitrogen_ppm,
                phosphorus_ppm=z.phosphorus_ppm,
                potassium_ppm=z.potassium_ppm,
                ambient_temperature=round(ambient_temp, 1),
                relative_humidity=round(rel_humidity, 1),
                solar_radiation_w_m2=round(solar_radiation, 1),
                precipitation_mm=round(z.precipitation_mm, 1),
                vpd_kpa=vpd,
                battery_level_pct=z.battery,
                health_status=health
            ))
            
        return readings

iot_simulator = IoTSimulatorService()

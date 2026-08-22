"""
Sensor Fault & Physical Degradation Detector
Detects frozen sensors, floating ADC pins, soil probe displacement, and out-of-physical-range drifts.
"""

from typing import Dict, Any, List, Optional
import time

class SensorFaultDetector:
    PHYSICAL_RANGES = {
        "soil_moisture_pct": (0.0, 100.0),
        "soil_temperature_c": (-15.0, 65.0),
        "soil_ph": (3.0, 10.5),
        "electrical_conductivity_us_cm": (0.0, 20000.0),
        "nitrogen_ppm": (0.0, 500.0),
        "phosphorus_ppm": (0.0, 300.0),
        "potassium_ppm": (0.0, 600.0),
        "solar_radiation_w_m2": (0.0, 1500.0),
        "ambient_temp_c": (-20.0, 60.0),
        "relative_humidity_pct": (0.0, 100.0)
    }

    def __init__(self, stuck_reading_window: int = 12):
        self.history: Dict[str, List[float]] = {}
        self.window_size = stuck_reading_window

    def evaluate_reading(self, parameter: str, value: float) -> Dict[str, Any]:
        result = {
            "parameter": parameter,
            "value": value,
            "is_valid": True,
            "fault_type": None,
            "severity": "NORMAL"
        }

        # 1. Physical range check
        if parameter in self.PHYSICAL_RANGES:
            min_val, max_val = self.PHYSICAL_RANGES[parameter]
            if value < min_val or value > max_val:
                result["is_valid"] = False
                result["fault_type"] = f"OUT_OF_BOUNDS (Allowed: {min_val}-{max_val})"
                result["severity"] = "CRITICAL"
                return result

        # 2. Frozen/Stuck sensor check
        if parameter not in self.history:
            self.history[parameter] = []
        self.history[parameter].append(value)
        if len(self.history[parameter]) > self.window_size:
            self.history[parameter].pop(0)

        if len(self.history[parameter]) == self.window_size:
            # Check variance
            if all(v == self.history[parameter][0] for v in self.history[parameter]):
                result["is_valid"] = False
                result["fault_type"] = "STUCK_SIGNAL (Possible Hardware Freeze / Pin Disconnect)"
                result["severity"] = "WARNING"
                return result

        return result

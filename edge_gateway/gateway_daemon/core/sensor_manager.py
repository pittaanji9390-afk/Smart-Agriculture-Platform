"""
Edge Sensor Manager & Multi-Bus Ingestion Coordinator
Aggregates Modbus RS-485, I2C, SPI, and Analog ADC sensor channels on gateway hardware.
"""

import time
from typing import Dict, Any, List
from edge_gateway.gateway_daemon.core.kalman_filter import TelemetryKalmanFilter
from edge_gateway.gateway_daemon.core.fault_detector import SensorFaultDetector
from edge_gateway.gateway_daemon.core.edge_buffer import EdgeTelemetryBuffer

class EdgeSensorManager:
    def __init__(self, node_id: str = "GW-NODE-ALPHA", buffer_db: str = "edge_buffer.db"):
        self.node_id = node_id
        self.buffer = EdgeTelemetryBuffer(buffer_db)
        self.fault_detector = SensorFaultDetector()
        
        # Kalman filters for smooth output
        self.filters = {
            "soil_moisture": TelemetryKalmanFilter(1e-4, 1e-2),
            "soil_temp": TelemetryKalmanFilter(1e-4, 1e-2),
            "soil_ph": TelemetryKalmanFilter(1e-5, 1e-3),
            "ambient_temp": TelemetryKalmanFilter(1e-4, 1e-2),
            "humidity": TelemetryKalmanFilter(1e-4, 1e-2),
        }

    def process_raw_telemetry(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        processed = {
            "node_id": self.node_id,
            "timestamp": time.time(),
            "metrics": {},
            "faults": []
        }

        for param, raw_val in raw_data.items():
            # Validate
            fault_check = self.fault_detector.evaluate_reading(param, raw_val)
            if not fault_check["is_valid"]:
                processed["faults"].append(fault_check)

            # Apply Kalman Filter if configured
            if param in self.filters:
                filtered_val = self.filters[param].update(raw_val)
                processed["metrics"][param] = round(filtered_val, 2)
            else:
                processed["metrics"][param] = raw_val

        # Persist to local store-and-forward buffer
        self.buffer.push_reading(self.node_id, processed)
        return processed

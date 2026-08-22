"""
Unit Tests for Edge Decoders, Fault Detectors & Kalman Filters
"""

from edge_gateway.gateway_daemon.core.kalman_filter import TelemetryKalmanFilter
from edge_gateway.gateway_daemon.core.fault_detector import SensorFaultDetector

def test_kalman_filter_smoothing():
    kf = TelemetryKalmanFilter()
    noisy_stream = [45.0, 48.0, 43.0, 46.0, 44.0, 47.0]
    smoothed = [kf.update(v) for v in noisy_stream]
    assert len(smoothed) == 6
    assert abs(smoothed[-1] - 45.5) < 3.0

def test_sensor_fault_detector():
    detector = SensorFaultDetector()
    
    # Valid reading
    normal = detector.evaluate_reading("soil_moisture_pct", 52.0)
    assert normal["is_valid"] is True
    
    # Out of bounds
    invalid = detector.evaluate_reading("soil_moisture_pct", 150.0)
    assert invalid["is_valid"] is False
    assert invalid["severity"] == "CRITICAL"

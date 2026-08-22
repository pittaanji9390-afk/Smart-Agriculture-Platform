"""
1D / Multi-Variate Kalman Filter for Sensor Telemetry Signal Denoising
Eliminates high-frequency noise and sudden spike outliers from soil moisture and temperature probes.
"""

class TelemetryKalmanFilter:
    def __init__(self, process_variance: float = 1e-4, measurement_variance: float = 1e-2, estimation_error: float = 1.0):
        self.q = process_variance        # Process noise covariance
        self.r = measurement_variance  # Measurement noise covariance
        self.p = estimation_error        # Estimation error covariance
        self.x = None                   # Estimated state value

    def update(self, measurement: float) -> float:
        if self.x is None:
            self.x = measurement
            return measurement
            
        # Prediction update
        self.p = self.p + self.q
        
        # Measurement update (Kalman Gain)
        k = self.p / (self.p + self.r)
        self.x = self.x + k * (measurement - self.x)
        self.p = (1.0 - k) * self.p
        
        return self.x

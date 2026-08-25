"""
Observability, Error Tracking & Prometheus Metrics Instrumentation - AgriSphere OS
"""

import os
import time
from typing import Dict, Any, Callable
from fastapi import Request, Response
from backend.app.core.logging_config import logger

# -----------------------------------------------------------------------------
# Error Tracking Initialization (Sentry SDK / OpenTelemetry)
# -----------------------------------------------------------------------------
def init_error_tracking():
    """Initializes Sentry error tracking if SENTRY_DSN is configured in environment."""
    sentry_dsn = os.getenv("SENTRY_DSN")
    if sentry_dsn:
        try:
            import sentry_sdk
            sentry_sdk.init(
                dsn=sentry_dsn,
                traces_sample_rate=1.0,
                profiles_sample_rate=1.0,
                environment=os.getenv("ENVIRONMENT", "production"),
                release=os.getenv("APP_VERSION", "2.5.0")
            )
            logger.info("Sentry error tracking initialized successfully.")
        except ImportError:
            logger.warning("sentry-sdk not installed, error tracking in fallback mode.")
    else:
        logger.info("SENTRY_DSN not configured. Running with standard exception logging.")

# -----------------------------------------------------------------------------
# In-Memory Prometheus Metrics Counter & Histogram
# -----------------------------------------------------------------------------
class PrometheusMetricsRegistry:
    def __init__(self):
        self.request_count = 0
        self.request_duration_seconds_sum = 0.0
        self.http_2xx_count = 0
        self.http_4xx_count = 0
        self.http_5xx_count = 0
        self.active_websocket_connections = 0
        self.telemetry_packets_processed = 0

    def record_request(self, status_code: int, duration: float):
        self.request_count += 1
        self.request_duration_seconds_sum += duration
        if 200 <= status_code < 300:
            self.http_2xx_count += 1
        elif 400 <= status_code < 500:
            self.http_4xx_count += 1
        elif status_code >= 500:
            self.http_5xx_count += 1

    def generate_prometheus_metrics(self) -> str:
        avg_latency = (self.request_duration_seconds_sum / self.request_count) if self.request_count > 0 else 0.0
        return (
            "# HELP http_requests_total Total number of HTTP requests processed\n"
            "# TYPE http_requests_total counter\n"
            f"http_requests_total {self.request_count}\n\n"
            "# HELP http_requests_2xx_total Total successful 2xx responses\n"
            "# TYPE http_requests_2xx_total counter\n"
            f"http_requests_2xx_total {self.http_2xx_count}\n\n"
            "# HELP http_requests_4xx_total Total client error 4xx responses\n"
            "# TYPE http_requests_4xx_total counter\n"
            f"http_requests_4xx_total {self.http_4xx_count}\n\n"
            "# HELP http_requests_5xx_total Total server error 5xx responses\n"
            "# TYPE http_requests_5xx_total counter\n"
            f"http_requests_5xx_total {self.http_5xx_count}\n\n"
            "# HELP http_request_duration_seconds_sum Total request latency sum\n"
            "# TYPE http_request_duration_seconds_sum gauge\n"
            f"http_request_duration_seconds_sum {self.request_duration_seconds_sum:.4f}\n\n"
            "# HELP http_request_avg_latency_seconds Average request latency in seconds\n"
            "# TYPE http_request_avg_latency_seconds gauge\n"
            f"http_request_avg_latency_seconds {avg_latency:.4f}\n\n"
            "# HELP agrisphere_active_websockets Active IoT telemetry WebSocket sessions\n"
            "# TYPE agrisphere_active_websockets gauge\n"
            f"agrisphere_active_websockets {self.active_websocket_connections}\n\n"
            "# HELP agrisphere_telemetry_packets_total Total sensor telemetry packets parsed\n"
            "# TYPE agrisphere_telemetry_packets_total counter\n"
            f"agrisphere_telemetry_packets_total {self.telemetry_packets_processed}\n"
        )

metrics_registry = PrometheusMetricsRegistry()

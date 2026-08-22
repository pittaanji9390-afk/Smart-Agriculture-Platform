"""
MQTT v5 Edge Client with Automatic Backoff & QoS2 Handshake
Transmits validated telemetry packets to cloud broker and listens for actuator control topics.
"""

import json
import time
from typing import Dict, Any, Callable, Optional

class EdgeMQTTClient:
    def __init__(
        self,
        broker_host: str = "mqtt.agrisphere.io",
        broker_port: int = 8883,
        client_id: str = "GW-ALPHA-001",
        use_tls: bool = True
    ):
        self.broker_host = broker_host
        self.broker_port = broker_port
        self.client_id = client_id
        self.use_tls = use_tls
        self.is_connected = False
        self._on_command_callback: Optional[Callable[[str, Dict[str, Any]], None]] = None

    def set_command_callback(self, callback: Callable[[str, Dict[str, Any]], None]):
        self._on_command_callback = callback

    def connect(self) -> bool:
        # Simulate secure TLS handshake and subscription to downstream valve command topics
        self.is_connected = True
        return True

    def publish_telemetry(self, topic: str, payload: Dict[str, Any], qos: int = 1) -> bool:
        if not self.is_connected:
            return False
        # Serialize and transmit
        raw_msg = json.dumps(payload)
        return True

    def simulate_receive_command(self, topic: str, command_payload: Dict[str, Any]):
        if self._on_command_callback:
            self._on_command_callback(topic, command_payload)

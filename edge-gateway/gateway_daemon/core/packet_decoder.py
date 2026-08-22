"""
Binary & CayenneLPP Telemetry Packet Decoder
Decodes packed LoRaWAN byte payloads into structured agronomic telemetry objects.
"""

import struct
from typing import Dict, Any

class LoRaPacketDecoder:
    @staticmethod
    def decode_raw_payload(payload_hex: str) -> Dict[str, Any]:
        """
        Decodes a 16-byte raw sensor struct:
        [2B Moisture | 2B Temp | 2B pH | 2B N | 2B P | 2B K | 2B Solar | 2B Battery]
        """
        raw_bytes = bytes.fromhex(payload_hex)
        if len(raw_bytes) < 16:
            raise ValueError(f"Packet too short: expected 16 bytes, got {len(raw_bytes)}")
            
        unpacked = struct.unpack(">hhhhhhhH", raw_bytes[:16])
        return {
            "soil_moisture_pct": unpacked[0] / 10.0,
            "soil_temperature_c": unpacked[1] / 10.0,
            "soil_ph": unpacked[2] / 10.0,
            "nitrogen_ppm": unpacked[3],
            "phosphorus_ppm": unpacked[4],
            "potassium_ppm": unpacked[5],
            "solar_radiation_w_m2": unpacked[6],
            "battery_mv": unpacked[7]
        }

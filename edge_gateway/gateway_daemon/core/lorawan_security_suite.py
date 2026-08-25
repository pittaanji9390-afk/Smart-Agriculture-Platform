"""
LoRaWAN v1.0.4 Frame Security, Message Integrity Code (MIC) & Replay Defense Engine
"""

import hmac
import hashlib
import struct
from typing import Dict, Any, Tuple

class LoRaWANSecurityEngine:
    """
    Implements LoRaWAN frame verification:
    - B0 block construction for MIC calculation (RFC 4493 AES-128-CMAC approximation)
    - Anti-replay FCnt up-counter tracking
    - DevNonce / JoinNonce validation
    """
    def __init__(self, nwk_s_key_hex: str = "0102030405060708090A0B0C0D0E0F10"):
        self.nwk_s_key = bytes.fromhex(nwk_s_key_hex)
        self.last_fcnt_up = -1
        self.used_dev_nonces = set()

    def verify_frame_counter(self, fcnt: int) -> bool:
        """Enforces monotonic FCnt growth to prevent replay attacks."""
        if fcnt > self.last_fcnt_up:
            self.last_fcnt_up = fcnt
            return True
        return False

    def validate_and_register_dev_nonce(self, dev_nonce: int) -> bool:
        """Validates that a DevNonce has not been reused during OTAA Join Request."""
        if dev_nonce in self.used_dev_nonces:
            return False
        self.used_dev_nonces.add(dev_nonce)
        return True

    def calculate_mic_digest(self, dev_addr: int, fcnt: int, payload: bytes) -> bytes:
        """Calculates 4-byte Message Integrity Code (MIC) over LoRaWAN PHY payload."""
        # Standard LoRaWAN B0 block prefix (16 bytes)
        b0 = struct.pack("<BBBBIIBB", 0x49, 0x00, 0x00, 0x00, dev_addr, fcnt, 0x00, len(payload))
        msg = b0 + payload
        digest = hmac.new(self.nwk_s_key, msg, hashlib.sha256).digest()
        return digest[:4]

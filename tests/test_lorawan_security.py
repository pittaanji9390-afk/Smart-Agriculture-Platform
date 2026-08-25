"""
Unit Tests for LoRaWAN Security & Anti-Replay Engine
"""

from edge_gateway.gateway_daemon.core.lorawan_security_suite import LoRaWANSecurityEngine

def test_lorawan_fcnt_anti_replay():
    sec = LoRaWANSecurityEngine()
    assert sec.verify_frame_counter(0) is True
    assert sec.verify_frame_counter(1) is True
    assert sec.verify_frame_counter(1) is False  # Replay attempt
    assert sec.verify_frame_counter(0) is False  # Rollback attempt
    assert sec.verify_frame_counter(5) is True

def test_lorawan_dev_nonce_uniqueness():
    sec = LoRaWANSecurityEngine()
    assert sec.validate_and_register_dev_nonce(1001) is True
    assert sec.validate_and_register_dev_nonce(1002) is True
    assert sec.validate_and_register_dev_nonce(1001) is False # Duplicate DevNonce

def test_lorawan_mic_generation():
    sec = LoRaWANSecurityEngine()
    mic = sec.calculate_mic_digest(dev_addr=0x260114AA, fcnt=12, payload=b"\x01\x67\x01\x10")
    assert len(mic) == 4

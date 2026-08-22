"""
Industrial Modbus TCP Master Protocol Adapter
Interfaces with commercial smart agricultural irrigation PLCs, Variable Frequency Drives (VFDs), and fertigation dosing pumps.
"""

import socket
import struct
import time
from typing import List, Optional, Tuple

class ModbusTCPMaster:
    def __init__(self, host: str = "192.168.1.100", port: int = 502, timeout: float = 3.0):
        self.host = host
        self.port = port
        self.timeout = timeout
        self._sock: Optional[socket.socket] = None
        self._transaction_id = 0

    def connect(self) -> bool:
        try:
            self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._sock.settimeout(self.timeout)
            self._sock.connect((self.host, self.port))
            return True
        except Exception as e:
            self._sock = None
            return False

    def close(self):
        if self._sock:
            try:
                self._sock.close()
            except Exception:
                pass
            self._sock = None

    def _get_next_transaction_id(self) -> int:
        self._transaction_id = (self._transaction_id + 1) & 0xFFFF
        return self._transaction_id

    def read_holding_registers(self, unit_id: int, start_register: int, count: int) -> Tuple[bool, List[int]]:
        """Function 0x03: Read Holding Registers"""
        if not self._sock and not self.connect():
            return False, []

        tid = self._get_next_transaction_id()
        # Modbus Application Protocol (MBAP) Header (7 bytes) + PDU (5 bytes)
        # TransactionID (2B), ProtocolID (2B = 0), Length (2B = 6), UnitID (1B), Func (1B = 0x03), StartAddr (2B), Count (2B)
        pdu = struct.pack(">HHHBBHH", tid, 0x0000, 0x0006, unit_id, 0x03, start_register, count)

        try:
            self._sock.sendall(pdu)
            header = self._sock.recv(7)
            if len(header) < 7:
                return False, []

            rx_tid, rx_pid, rx_len, rx_uid = struct.unpack(">HHHB", header)
            pdu_resp = self._sock.recv(rx_len - 1)
            if len(pdu_resp) < 2:
                return False, []

            func_code = pdu_resp[0]
            if func_code & 0x80:
                # Modbus Exception
                return False, []

            byte_count = pdu_resp[1]
            register_bytes = pdu_resp[2:2 + byte_count]
            registers = [
                struct.unpack(">H", register_bytes[i:i + 2])[0]
                for i in range(0, len(register_bytes), 2)
            ]
            return True, registers
        except Exception:
            self.close()
            return False, []

    def write_single_coil(self, unit_id: int, coil_address: int, state: bool) -> bool:
        """Function 0x05: Write Single Coil (Pump / Solenoid Valve Control)"""
        if not self._sock and not self.connect():
            return False

        tid = self._get_next_transaction_id()
        coil_val = 0xFF00 if state else 0x0000
        pdu = struct.pack(">HHHBBHH", tid, 0x0000, 0x0006, unit_id, 0x05, coil_address, coil_val)

        try:
            self._sock.sendall(pdu)
            resp = self._sock.recv(12)
            return len(resp) >= 12
        except Exception:
            self.close()
            return False

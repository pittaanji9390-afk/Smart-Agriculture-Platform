"""
Edge Telemetry SQLite Store-and-Forward Buffer
Ensures zero data loss during rural cellular or LoRaWAN communication outages.
"""

import sqlite3
import json
import time
from typing import List, Dict, Any, Optional

class EdgeTelemetryBuffer:
    def __init__(self, db_path: str = "edge_telemetry_cache.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS buffered_telemetry (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    node_id TEXT NOT NULL,
                    payload_json TEXT NOT NULL,
                    captured_timestamp REAL NOT NULL,
                    retry_count INTEGER DEFAULT 0,
                    is_synced INTEGER DEFAULT 0
                )
            """)
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_sync ON buffered_telemetry(is_synced, captured_timestamp)")
            conn.commit()

    def push_reading(self, node_id: str, payload: Dict[str, Any]) -> int:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO buffered_telemetry (node_id, payload_json, captured_timestamp, retry_count, is_synced)
                VALUES (?, ?, ?, 0, 0)
            """, (node_id, json.dumps(payload), time.time()))
            conn.commit()
            return cursor.lastrowid

    def get_pending_batch(self, batch_size: int = 50) -> List[Dict[str, Any]]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, node_id, payload_json, captured_timestamp, retry_count
                FROM buffered_telemetry
                WHERE is_synced = 0
                ORDER BY captured_timestamp ASC
                LIMIT ?
            """, (batch_size,))
            rows = cursor.fetchall()
            return [
                {
                    "id": r[0],
                    "node_id": r[1],
                    "payload": json.loads(r[2]),
                    "timestamp": r[3],
                    "retries": r[4]
                }
                for r in rows
            ]

    def mark_as_synced(self, record_ids: List[int]):
        if not record_ids:
            return
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            placeholders = ",".join("?" for _ in record_ids)
            cursor.execute(f"""
                UPDATE buffered_telemetry
                SET is_synced = 1
                WHERE id IN ({placeholders})
            """, record_ids)
            conn.commit()

    def purge_synced_older_than(self, seconds: float = 604800.0): # 7 days default
        threshold = time.time() - seconds
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM buffered_telemetry WHERE is_synced = 1 AND captured_timestamp < ?", (threshold,))
            conn.commit()

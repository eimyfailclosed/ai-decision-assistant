import sqlite3
from typing import Any, Dict
from pathlib import Path
import json
from datetime import datetime

DB_PATH = Path("audit.sqlite")

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS audit (
            audit_id TEXT PRIMARY KEY,
            ts TEXT NOT NULL,
            input TEXT NOT NULL,
            final TEXT NOT NULL
        )
        """)
        conn.commit()

def audit_log(audit_id: str, user_input: Dict[str, Any], final: Dict[str, Any]):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT OR REPLACE INTO audit (audit_id, ts, input, final) VALUES (?, ?, ?, ?)",
            (
                audit_id,
                datetime.utcnow().isoformat(),
                json.dumps(user_input, ensure_ascii=False),
                json.dumps(final, ensure_ascii=False),
            ),
        )
        conn.commit()

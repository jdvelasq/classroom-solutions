"""Aplica una política explícita de retención sin destruir el dato de origen."""

import json
from datetime import date, timedelta
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
RETENTION_DAYS = 90


def apply_retention_policy(as_of):
    """La fecha de corte explícita permite explicar y repetir una decisión de retención."""

    cutoff = as_of - timedelta(days=RETENTION_DAYS)
    events = json.loads((ROOT_DIR / "data" / "events.json").read_text())
    retained = []
    expired = []

    for event in events:
        event_date = date.fromisoformat(event["event_date"])
        if event_date >= cutoff:
            retained.append(event)
        else:
            expired.append({"event_id": event["event_id"], "reason": "retention_period_expired"})

    return {"cutoff": cutoff.isoformat(), "retained": retained, "expired": expired}

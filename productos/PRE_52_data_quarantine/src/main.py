"""Separa registros inválidos sin descartar la evidencia necesaria para corregirlos."""

import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]


def quarantine_invalid_records():
    """La cuarentena protege la salida válida y permite investigar el dato rechazado."""

    records = json.loads((ROOT_DIR / "data" / "records.json").read_text())
    valid = [record for record in records if record["amount"] >= 0]
    quarantined = [dict(record, rejection_reason="amount_must_be_non_negative") for record in records if record["amount"] < 0]
    return {"valid": valid, "quarantined": quarantined}

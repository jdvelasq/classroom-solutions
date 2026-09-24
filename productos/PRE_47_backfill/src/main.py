"""Selecciona un periodo histórico explícito para reprocesarlo."""

import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]


def select_backfill(start_date, end_date):
    """Un rango declarado evita que el reproceso histórico afecte periodos no previstos."""

    events = json.loads((ROOT_DIR / "data" / "events.json").read_text())
    return [event["id"] for event in events if start_date <= event["date"] <= end_date]

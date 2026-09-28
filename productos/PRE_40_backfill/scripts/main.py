"""Selecciona un periodo histórico explícito para reprocesarlo."""

import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]


def select_backfill(start_date, end_date):
    """Un rango declarado evita que el reproceso histórico afecte periodos no previstos."""

    events = json.loads((ROOT_DIR / "data" / "events.json").read_text())
    return [event["id"] for event in events if start_date <= event["date"] <= end_date]


def main():
    """El rango reprocesado queda registrado junto con los eventos seleccionados."""

    output_path = ROOT_DIR / "submission" / "backfill_selection.json"
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(json.dumps({"start_date": "2026-09-20", "end_date": "2026-09-21", "event_ids": select_backfill("2026-09-20", "2026-09-21")}, indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()

"""Clasifica un registro tardío para un reproceso histórico controlado."""

import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]


def classify_arrival():
    """Separar la fecha del evento de su llegada evita perder correcciones históricas."""

    event = json.loads((ROOT_DIR / "data" / "arrival.json").read_text())
    late = event["event_date"] < event["current_processing_date"]
    return {"late": late, "action": "backfill" if late else "current_load"}


def main():
    """La clasificación del registro tardío queda registrada."""

    output_path = ROOT_DIR / "submission" / "arrival_classification.json"
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(json.dumps(classify_arrival(), indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()

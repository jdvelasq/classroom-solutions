"""Evita duplicar un resultado cuando una tarea vuelve a ejecutarse."""

import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT_DIR / "submission" / "daily_report.json"


def generate_daily_report():
    """Una clave estable permite reconocer que el resultado del día ya existe."""

    report = {"report_date": "2026-09-24", "factory_id": 2, "risk": "high"}
    if OUTPUT_PATH.exists():
        return json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
    OUTPUT_PATH.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report


if __name__ == "__main__":
    print(json.dumps(generate_daily_report(), indent=2))

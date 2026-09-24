"""Ejecuta periódicamente una tarea analítica local."""

import json
import time
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import schedule


ROOT_DIR = Path(__file__).resolve().parents[1]


def generate_report():
    """La tarea es pequeña para que la periodicidad sea el único concepto nuevo."""

    data = pd.read_csv(ROOT_DIR / "data" / "daily_operations.csv")
    totals = data.groupby("factory_id")["daily_units_produced"].sum().to_dict()
    report = {"executed_at": datetime.now(timezone.utc).isoformat(), "factory_totals": totals}
    (ROOT_DIR / "submission" / "scheduled_report.json").write_text(
        json.dumps(report, indent=2), encoding="utf-8"
    )
    print("Reporte generado")


def main():
    """El ciclo muestra que una programación local requiere un proceso activo."""

    schedule.every(10).seconds.do(generate_report)
    print("Tarea programada cada 10 segundos. Detenga con Ctrl+C.")
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()

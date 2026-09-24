"""Orquesta dos tareas pequeñas de un flujo analítico con Prefect."""

import json
from pathlib import Path

import pandas as pd
from prefect import flow, task


ROOT_DIR = Path(__file__).resolve().parents[1]


@task(retries=1)
def load_operations():
    """La tarea aislada hace visible el punto de recuperación del flujo."""

    return pd.read_csv(ROOT_DIR / "data" / "daily_operations.csv")


@task
def summarize_operations(data):
    """Separar la transformación permite observar cada parte del proceso."""

    return data.groupby("factory_id")["daily_units_produced"].sum().to_dict()


@flow
def operations_flow():
    """El flujo declara la dependencia entre cargar datos y producir el indicador."""

    totals = summarize_operations(load_operations())
    report_path = ROOT_DIR / "submission" / "prefect_report.json"
    report_path.write_text(json.dumps({"factory_totals": totals}, indent=2), encoding="utf-8")
    return totals


if __name__ == "__main__":
    operations_flow()

"""Ejecuta un flujo mínimo desde datos de entrada hasta una salida publicada."""

import json
from pathlib import Path

import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[1]


def run_pipeline():
    """El flujo completo permite detectar fallas entre componentes que funcionan aislados."""

    data = pd.read_csv(ROOT_DIR / "data" / "daily_operations.csv")
    totals = data.groupby("factory_id")["daily_units_produced"].sum().to_dict()
    output = ROOT_DIR / "submission" / "factory_totals.json"
    output.write_text(json.dumps({"factory_totals": totals}))
    return output

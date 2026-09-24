"""Genera un indicador simple que será comprobado por una sesión de Nox."""

import json
from pathlib import Path

import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[1]


def main():
    """El cálculo conocido permite concentrar el taller en el ambiente automatizado."""

    data = pd.read_csv(ROOT_DIR / "data" / "daily_operations.csv")
    totals = data.groupby("factory_id")["daily_units_produced"].sum().to_dict()
    (ROOT_DIR / "submission" / "report.json").write_text(
        json.dumps({"factory_totals": totals}, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()

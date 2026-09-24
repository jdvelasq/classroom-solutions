"""Genera un indicador simple dentro de un contenedor."""

import json
from pathlib import Path

import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[1]


def summarize_by_factory(dataframe):
    """El cálculo conocido permite concentrar el taller en el empaquetamiento."""

    return (
        dataframe.groupby("factory_id", as_index=False)["daily_units_produced"]
        .sum()
        .rename(columns={"daily_units_produced": "total_units_produced"})
    )


def main():
    """El reporte fuera del contenedor permite inspeccionar la ejecución."""

    data = pd.read_csv(ROOT_DIR / "data" / "daily_operations.csv")
    report = {"factory_totals": summarize_by_factory(data).to_dict(orient="records")}
    output_path = ROOT_DIR / "submission" / "factory_report.json"
    output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

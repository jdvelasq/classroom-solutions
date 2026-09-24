"""Genera un indicador simple que la acción verificará automáticamente."""

import json
import sys
from pathlib import Path

import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[1]


def summarize_by_factory(dataframe):
    """La métrica conocida permite centrar la atención en la automatización."""

    return (
        dataframe.groupby("factory_id", as_index=False)["daily_units_produced"]
        .sum()
        .rename(columns={"daily_units_produced": "total_units_produced"})
    )


def main():
    """Deja evidencia de las versiones con las que se obtuvo el resultado."""

    data = pd.read_csv(ROOT_DIR / "data" / "daily_operations.csv")
    report = {
        "python_version": sys.version.split()[0],
        "pandas_version": pd.__version__,
        "factory_totals": summarize_by_factory(data).to_dict(orient="records"),
    }
    output_path = ROOT_DIR / "submission" / "environment_report.json"
    output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()

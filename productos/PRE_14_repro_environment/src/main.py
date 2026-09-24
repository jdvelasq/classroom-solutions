"""Genera un indicador sencillo dentro de un ambiente reproducible."""

import json
import sys
from pathlib import Path

import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[1]


def summarize_by_factory(dataframe):
    """Resume una métrica conocida para concentrar el taller en el ambiente."""

    return (
        dataframe.groupby("factory_id", as_index=False)["daily_units_produced"]
        .sum()
        .rename(columns={"daily_units_produced": "total_units_produced"})
    )


def main():
    """Deja evidencia de las versiones con las que se obtuvo el resultado."""

    data = pd.read_csv(ROOT_DIR / "data" / "daily_operations.csv")
    summary = summarize_by_factory(data)
    report = {
        "python_version": sys.version.split()[0],
        "pandas_version": pd.__version__,
        "factory_totals": summary.to_dict(orient="records"),
    }

    output_path = ROOT_DIR / "submission" / "environment_report.json"
    output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

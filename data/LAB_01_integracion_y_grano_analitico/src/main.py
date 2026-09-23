"""Integra fuentes operativas reales preservando el grano fábrica-día."""

import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def main():
    throughput = pd.read_csv(ROOT / "data/machine_throughput_export.csv")
    uptime = pd.read_csv(ROOT / "data/machine_uptime_export.csv")
    ambient = pd.read_csv(ROOT / "data/factory_ambient_export.csv")
    machine_day = throughput.merge(
        uptime, on=["factory_id", "machine_id", "factory_date"], validate="one_to_one"
    )
    result = machine_day.groupby(["factory_id", "factory_date"], as_index=False).agg(
        units_produced=("daily_units_produced", "sum"),
        average_hours_operational=("hours_operational", "mean"),
    )
    assert not result[["factory_id", "factory_date"]].duplicated().any()
    result = result.merge(
        ambient,
        left_on=["factory_id", "factory_date"],
        right_on=["factory_id", "date_measured"],
        validate="one_to_one",
    ).drop(columns="date_measured")
    output = ROOT / "submission"
    output.mkdir(exist_ok=True)
    result.to_csv(output / "factory_daily_operations.csv", index=False)
    report = {
        "source_units": int(throughput.daily_units_produced.sum()),
        "output_units": int(result.units_produced.sum()),
        "row_count": len(result),
        "grain": "factory_id,factory_date",
    }
    (output / "reconciliation.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    return result, report


if __name__ == "__main__":
    main()

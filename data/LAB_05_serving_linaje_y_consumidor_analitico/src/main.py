"""Prepara una vista de serving y documenta su procedencia."""

import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def main():
    request = {"consumer": "operations_dashboard", "grain": "factory_date,factory_id", "owner": "analytics_team"}
    production = pd.read_csv(ROOT / "data/machine_throughput_export.csv")
    view = production.groupby(["factory_date", "factory_id"], as_index=False).daily_units_produced.sum()
    output = ROOT / "submission"; output.mkdir(exist_ok=True)
    view.to_csv(output / "factory_daily_serving_view.csv", index=False)
    manifest = {"consumer": request["consumer"], "grain": request["grain"], "owner": request["owner"], "schema": {"factory_date": "date", "factory_id": "integer", "daily_units_produced": "number"}, "source_asset": "machine_throughput"}
    (output / "serving_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lineage = pd.DataFrame([["machine_throughput", "factory_daily_serving_view", "aggregate daily production by factory"]], columns=["source", "target", "transformation"])
    serving_edge = lineage.loc[lineage.target == "factory_daily_serving_view"]
    assert len(serving_edge) == 1
    assert serving_edge.source.iloc[0] == manifest["source_asset"]
    lineage.to_csv(output / "lineage.csv", index=False)
    return view, manifest, lineage


if __name__ == "__main__":
    main()

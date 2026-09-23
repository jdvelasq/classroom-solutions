"""Prepara una vista de serving y documenta su procedencia."""

import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def main():
    request = json.loads((ROOT / "data/consumer_request.json").read_text())
    sales = pd.read_csv(ROOT / "data/sales_curated.csv")
    view = sales.groupby(["sale_date", "region"], as_index=False).amount.sum()
    output = ROOT / "submission"; output.mkdir(exist_ok=True)
    view.to_csv(output / "sales_serving_view.csv", index=False)
    manifest = {"consumer": request["consumer"], "grain": request["grain"], "owner": request["owner"], "schema": {"sale_date": "date", "region": "string", "amount": "number"}, "source_asset": "sales_curated"}
    (output / "serving_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lineage = pd.read_csv(ROOT / "data/transformations.csv")
    serving_edge = lineage.loc[lineage.target == "sales_serving_view"]
    assert len(serving_edge) == 1
    assert serving_edge.source.iloc[0] == manifest["source_asset"]
    lineage.to_csv(output / "lineage.csv", index=False)
    return view, manifest, lineage


if __name__ == "__main__":
    main()

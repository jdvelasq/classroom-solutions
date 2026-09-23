"""Integra líneas y órdenes preservando el grano cliente-mes."""

import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def main():
    orders = pd.read_csv(ROOT / "data/orders.csv", parse_dates=["order_date"])
    lines = pd.read_csv(ROOT / "data/order_lines.csv")
    segments = pd.read_csv(ROOT / "data/segments.csv")
    detailed = lines.merge(orders, on="order_id", validate="many_to_one")
    detailed["month"] = detailed["order_date"].dt.to_period("M").astype(str)
    result = detailed.groupby(["customer_id", "month"], as_index=False).amount.sum()
    result = result.merge(segments, on="customer_id", validate="many_to_one")
    result = result[["customer_id", "month", "segment", "amount"]]
    output = ROOT / "submission"
    output.mkdir(exist_ok=True)
    result.to_csv(output / "customer_month_sales.csv", index=False)
    report = {"source_amount": float(lines.amount.sum()), "output_amount": float(result.amount.sum()), "row_count": len(result)}
    (output / "reconciliation.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return result, report


if __name__ == "__main__":
    main()

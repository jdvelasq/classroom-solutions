"""Prepara interfaces de datos con el grano adecuado para cada consumidor."""

import sqlite3
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).parents[1]


def build_submission():
    curated = pd.DataFrame([["T1", "2026-01-01", "C1", "Cafe", "Alimentos", 20], ["T2", "2026-01-02", "C2", "Pan", "Alimentos", 10], ["T3", "2026-01-03", "C1", "Cuaderno", "Oficina", 15]], columns=["transaction_id", "transaction_date", "customer_id", "product_name", "product_category", "sales_amount"])
    mart = curated.groupby("product_category", as_index=False).sales_amount.sum().sort_values("product_category")
    curated.to_csv(ROOT / "submission/sales_detail.csv", index=False)
    with sqlite3.connect(ROOT / "submission/sales_serving.db") as database:
        mart.to_sql("category_sales", database, index=False, if_exists="replace")
    pd.DataFrame([["sales_detail", "one row per transaction", "CSV", "analyst"], ["category_sales", "one row per category", "SQLite", "dashboard"]], columns=["dataset", "grain", "interface", "consumer"]).to_csv(ROOT / "submission/serving_manifest.csv", index=False)


if __name__ == "__main__":
    build_submission()

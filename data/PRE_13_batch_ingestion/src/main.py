"""Ingiere dos fuentes pequeñas en una capa raw reproducible."""
import sqlite3
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).parents[1]
TRANSACTIONS, PRODUCTS = ROOT / "data/transactions.csv", ROOT / "data/products.db"
RAW, REPORT = ROOT / "temp/raw", ROOT / "submission/ingestion_report.csv"


def build_submission():
    transactions = pd.DataFrame([["T801","2026-01-03","C001","P100",2,18],["T802","2026-01-05","C002","P200",1,9.5],["T803","2026-01-08","C001","P300",3,7.25],["T804","2026-01-12","C003","P100",1,18]], columns=["transaction_id","transaction_date","customer_id","product_id","quantity","unit_price"])
    transactions.to_csv(TRANSACTIONS, index=False)
    PRODUCTS.unlink(missing_ok=True)
    with sqlite3.connect(PRODUCTS) as db:
        db.execute("CREATE TABLE products(product_id TEXT PRIMARY KEY, product_name TEXT, product_category TEXT)")
        db.executemany("INSERT INTO products VALUES (?, ?, ?)", [("P100","Cafe","Alimentos"),("P200","Pan","Alimentos"),("P300","Cuaderno","Oficina")])
        products = pd.read_sql_query("SELECT * FROM products ORDER BY product_id", db)
    RAW.mkdir(parents=True, exist_ok=True)
    transactions.to_parquet(RAW / "transactions.parquet", index=False, engine="pyarrow"); products.to_parquet(RAW / "products.parquet", index=False, engine="pyarrow")
    pd.DataFrame([["transactions","file",len(transactions),"SUCCESS",str(RAW / "transactions.parquet")],["products","database",len(products),"SUCCESS",str(RAW / "products.parquet")]], columns=["source_name","source_type","row_count","status","output_path"]).to_csv(REPORT, index=False)


if __name__ == "__main__": build_submission()

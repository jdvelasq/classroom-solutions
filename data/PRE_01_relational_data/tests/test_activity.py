import csv
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent))
from notebook_runner import execute_notebook

OUTPUT, SOURCE = ROOT / "submission/sales.db", ROOT / "data/sales.csv"


def setup_module():
    execute_notebook(ROOT / "notebooks/notebook.ipynb")


def test_relational_delivery_reconstructs_the_flat_source():
    with sqlite3.connect(OUTPUT) as connection, SOURCE.open(newline="", encoding="utf-8") as file:
        tables = {row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        assert tables == {"customers", "orders", "products", "order_items"}
        rebuilt = connection.execute(
            """SELECT o.order_id, o.order_date, c.customer_id, c.customer_name, c.customer_city,
                      p.product_id, p.product_name, p.category, p.unit_price, i.quantity
                 FROM orders o JOIN customers c USING(customer_id)
                 JOIN order_items i USING(order_id) JOIN products p USING(product_id)
                 ORDER BY o.order_id, p.product_id"""
        ).fetchall()
        source = list(csv.DictReader(file))
        expected = sorted((r["order_id"], r["order_date"], r["customer_id"], r["customer_name"], r["customer_city"], r["product_id"], r["product_name"], r["category"], float(r["unit_price"]), int(r["quantity"])) for r in source)
        assert rebuilt == expected


def test_foreign_keys_reject_an_invalid_order():
    with sqlite3.connect(OUTPUT) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        try:
            connection.execute("INSERT INTO orders VALUES ('O9999', '2026-02-01', 'C999')")
        except sqlite3.IntegrityError:
            return
    raise AssertionError("SQLite accepted an order for a nonexistent customer")

import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent / "tests"))
from notebook_runner import execute_notebook


def setup_module():
    execute_notebook(ROOT / "notebooks/notebook.ipynb")


def test_serving_interfaces_have_distinct_grains():
    with sqlite3.connect(ROOT / "submission/sales_serving.db") as db:
        assert db.execute("SELECT COUNT(*) FROM category_sales").fetchone()[0] == 2

import sqlite3
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("pre24", ROOT / "src/main.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def setup_module():
    MODULE.build_submission()


def test_serving_interfaces_have_distinct_grains():
    with sqlite3.connect(ROOT / "submission/sales_serving.db") as db:
        assert db.execute("SELECT COUNT(*) FROM category_sales").fetchone()[0] == 2

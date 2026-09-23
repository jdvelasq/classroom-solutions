import sqlite3
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent / "tests"))
from notebook_runner import execute_notebook

MART = ROOT / "submission/factory_mart.db"


def setup_module():
    execute_notebook(ROOT / "notebooks/notebook.ipynb")


def test_fact_grain_and_total_units_reconcile_with_source():
    source = pd.read_csv(ROOT / "data/machine_throughput_export.csv")
    with sqlite3.connect(MART) as mart:
        assert mart.execute("SELECT COUNT(*) FROM fact_operations").fetchone()[
            0
        ] == len(source)
        assert (
            mart.execute(
                "SELECT SUM(daily_units_produced) FROM fact_operations"
            ).fetchone()[0]
            == source.daily_units_produced.sum()
        )


def test_star_schema_references_existing_dimensions():
    with sqlite3.connect(MART) as mart:
        tables = {
            r[0]
            for r in mart.execute("SELECT name FROM sqlite_master WHERE type='table'")
        }
        assert tables == {"dim_factory", "dim_machine", "dim_date", "fact_operations"}
        assert (
            mart.execute(
                "SELECT COUNT(*) FROM fact_operations WHERE factory_key IS NULL OR machine_key IS NULL OR date_key IS NULL"
            ).fetchone()[0]
            == 0
        )

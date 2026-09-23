import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent))
from notebook_runner import execute_notebook


def setup_module():
    execute_notebook(ROOT / "notebooks/notebook.ipynb")


def test_lineage_identifies_downstream_dependencies():
    with (ROOT / "submission/lineage.csv").open() as file:
        rows = list(csv.DictReader(file))
    assert rows[0]["source_dataset"] == "raw_transactions"
    assert rows[-1]["target_dataset"] == "sales_dashboard"

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent))
from notebook_runner import execute_notebook


def setup_module():
    execute_notebook(ROOT / "notebooks/notebook.ipynb")


def test_every_requirement_has_coverage():
    with (ROOT / "submission/requirement_coverage.csv").open() as file:
        rows = list(csv.DictReader(file))
    assert rows and all(row["status"] == "PASS" for row in rows)

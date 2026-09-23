import sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent / "tests"))
from notebook_runner import execute_notebook


def setup_module():
    execute_notebook(ROOT / "notebooks/notebook.ipynb")


def test_partitioned_aggregation_matches_logical_reference():
    output = pd.read_parquet(ROOT / "submission/event_counts.parquet")
    assert output.event_count.sum() == len(pd.read_csv(ROOT / "data/truck_events.csv.gz"))

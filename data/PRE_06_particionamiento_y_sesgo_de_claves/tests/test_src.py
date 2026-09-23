"""El sesgo debe ser observable y el combiner debe reducir pares."""

import csv
from pathlib import Path

from data.tests.notebook_runner import execute_notebook


PRE = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = PRE / "submission"


def test_makes_skew_and_preaggregation_visible():
    execute_notebook(PRE / "notebooks" / "notebook.ipynb")
    with (SUBMISSION_DIR / "partition_loads.csv").open(encoding="utf-8") as file:
        loads = list(csv.DictReader(file))
    with (SUBMISSION_DIR / "shuffle_comparison.csv").open(encoding="utf-8") as file:
        shuffle = next(csv.DictReader(file))
    assert max(int(row["account_key_load"]) for row in loads) > max(int(row["event_key_load"]) for row in loads)
    assert int(shuffle["pairs_after_local_combiner"]) < int(shuffle["raw_pairs"])
    assert (SUBMISSION_DIR / "partition_loads.csv").exists()
    assert (SUBMISSION_DIR / "shuffle_comparison.csv").exists()

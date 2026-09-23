"""Pruebas del caso Drivers por clave--valor."""

import csv
from pathlib import Path

from data.tests.notebook_runner import execute_notebook


PRE = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = PRE / "submission"


def test_reproduces_the_driver_summary():
    execute_notebook(PRE / "notebooks" / "notebook.ipynb")
    with (SUBMISSION_DIR / "summary.csv").open(encoding="utf-8") as file:
        rows = list(csv.DictReader(file))
    assert len(rows) == 34
    assert {"driverId", "name", "hours-logged", "miles-logged"} <= set(rows[0])


def test_builds_the_same_derived_questions():
    execute_notebook(PRE / "notebooks" / "notebook.ipynb")
    assert (SUBMISSION_DIR / "below_average_hours.csv").exists()
    with (SUBMISSION_DIR / "top10_drivers.csv").open(encoding="utf-8") as file:
        assert len(list(csv.DictReader(file))) == 10

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent / "tests"))
from notebook_runner import execute_notebook

OUTPUT = ROOT / "submission/factory_daily_performance.csv"


def setup_module():
    execute_notebook(ROOT / "notebooks/notebook.ipynb")


def test_output_has_one_row_per_factory_and_day():
    output = pd.read_csv(OUTPUT)
    assert output[["factory_id", "factory_date"]].duplicated().sum() == 0
    assert list(output.columns) == [
        "factory_id",
        "factory_date",
        "units_produced",
        "average_hours_operational",
        "machines_reported",
        "employees",
        "temp",
        "humidity",
        "pressure",
    ]
    assert len(output) > 1000


def test_production_reconciles_with_the_machine_source():
    output = pd.read_csv(OUTPUT)
    source = pd.read_csv(ROOT / "data/machine_throughput_export.csv")
    assert output.units_produced.sum() == source.daily_units_produced.sum()
    assert output.employees.gt(0).all()

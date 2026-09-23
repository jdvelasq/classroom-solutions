import csv
import importlib.util
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("pre22", ROOT / "src/main.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def setup_module():
    MODULE.build_submission()

def test_arrival_order_and_delayed_event_are_preserved():
    with (ROOT/"submission/consumed_events.csv").open() as f:r=list(csv.DictReader(f))
    assert [x["event_id"] for x in r]==["E1","E2","E3","E4"] and r[2]["is_delayed"]=="True"

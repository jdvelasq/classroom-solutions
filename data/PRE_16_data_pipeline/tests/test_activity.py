import importlib.util
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("pre16", ROOT / "src/main.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def setup_module():
    MODULE.build_submission()


def test_curated_output_is_analytics_ready():
    curated = pd.read_csv(ROOT / "submission/factory_daily.csv")
    assert curated[["factory_id", "factory_date"]].duplicated().sum() == 0
    assert curated.notna().all().all()
    assert len(curated) > 1000


def test_pipeline_reconciles_production_and_records_layers():
    curated = pd.read_csv(ROOT / "submission/factory_daily.csv")
    throughput = pd.read_csv(ROOT / "data/machine_throughput_export.csv")
    report = pd.read_csv(ROOT / "submission/pipeline_report.csv")
    assert curated.units_produced.sum() == throughput.daily_units_produced.sum()
    assert report.stage.tolist() == ["raw", "staging", "curated"]
    assert report.status.tolist() == ["SUCCESS", "SUCCESS", "SUCCESS"]

import importlib.util
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]; SPEC = importlib.util.spec_from_file_location("pre08", ROOT / "src/main.py"); MODULE = importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MODULE)
def setup_module(): MODULE.build_submission()
def test_raw_layer_preserves_both_sources():
    assert len(pd.read_csv(ROOT / "data/transactions.csv")) == len(pd.read_parquet(ROOT / "temp/raw/transactions.parquet")) == 4
    assert len(pd.read_parquet(ROOT / "temp/raw/products.parquet")) == 3
def test_report_records_each_successful_ingestion():
    report = pd.read_csv(ROOT / "submission/ingestion_report.csv")
    assert report.source_name.tolist() == ["transactions", "products"] and report.status.tolist() == ["SUCCESS", "SUCCESS"]

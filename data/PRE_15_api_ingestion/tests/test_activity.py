import importlib.util
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]; SPEC=importlib.util.spec_from_file_location("pre09",ROOT/"src/main.py"); MODULE=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MODULE)
def setup_module(): MODULE.build_submission()
def test_pages_are_complete_and_unique():
    reviews=pd.read_parquet(ROOT/"submission/reviews.parquet"); assert len(reviews)==12 and reviews.review_id.is_unique
def test_transient_failure_is_reported_as_one_retry():
    assert pd.read_csv(ROOT/"submission/api_ingestion_report.csv").iloc[0].retry_count==1

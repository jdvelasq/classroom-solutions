import importlib.util
from pathlib import Path
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]; SPEC=importlib.util.spec_from_file_location("pre10", ROOT/"src/main.py"); MODULE=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MODULE)
def setup_module(): MODULE.build_submission()
def test_curated_output_is_analytics_ready():
    sales=pd.read_parquet(ROOT/"submission/sales_curated.parquet")
    assert sales.transaction_id.is_unique and len(sales)==4 and sales.product_name.notna().all()
    assert (sales.sales_amount == sales.quantity * sales.unit_price).all()
def test_pipeline_records_all_layers():
    report=pd.read_csv(ROOT/"submission/pipeline_report.csv")
    assert report.stage.tolist()==["raw","staging","curated"] and report.status.tolist()==["SUCCESS"]*3

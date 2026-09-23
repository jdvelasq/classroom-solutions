import sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent))
from notebook_runner import execute_notebook


def setup_module():
    execute_notebook(ROOT / "notebooks/notebook.ipynb")


def test_partitioned_aggregation_matches_logical_reference():
    output = pd.read_parquet(ROOT / "submission/category_sales.parquet")
    assert output.to_dict("records") == [
        {"product_category": "Alimentos", "sales_amount": 30},
        {"product_category": "Oficina", "sales_amount": 20},
    ]

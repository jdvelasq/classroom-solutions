"""Pipeline pequeño y reproducible: raw, staging y curated."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).parents[1]
DATA, PIPELINE, SUBMISSION = ROOT / "data", ROOT / "temp/pipeline", ROOT / "submission"


def build_submission():
    transactions = pd.DataFrame([["T1001","2026-03-01","P100","2","18.0"],["T1002","2026-03-02","P200","1","9.5"],["T1003","2026-03-03","P300","3","7.25"],["T1004","2026-03-04","P100","1","18.0"]], columns=["transaction_id","transaction_date","product_id","quantity","unit_price"])
    products = pd.DataFrame([["P100","Cafe","Alimentos"],["P200","Pan","Alimentos"],["P300","Cuaderno","Oficina"]], columns=["product_id","product_name","product_category"])
    transactions.to_csv(DATA / "transactions.csv", index=False); products.to_csv(DATA / "products.csv", index=False)
    raw, staging, curated = PIPELINE / "raw", PIPELINE / "staging", PIPELINE / "curated"
    for path in (raw, staging, curated): path.mkdir(parents=True, exist_ok=True)
    transactions.to_parquet(raw / "transactions.parquet", index=False, engine="pyarrow"); products.to_parquet(raw / "products.parquet", index=False, engine="pyarrow")
    staged = transactions.assign(transaction_date=pd.to_datetime(transactions.transaction_date), quantity=lambda x: x.quantity.astype(int), unit_price=lambda x: x.unit_price.astype(float))
    staged.to_parquet(staging / "transactions.parquet", index=False, engine="pyarrow")
    sales = staged.merge(products, on="product_id", how="left", validate="many_to_one")
    assert sales.product_name.notna().all()
    sales["sales_amount"] = sales.quantity * sales.unit_price
    columns = ["transaction_id","transaction_date","product_id","product_name","product_category","quantity","unit_price","sales_amount"]
    sales = sales[columns].sort_values("transaction_id")
    sales.to_parquet(curated / "sales.parquet", index=False, engine="pyarrow"); sales.to_parquet(SUBMISSION / "sales_curated.parquet", index=False, engine="pyarrow")
    pd.DataFrame([["raw",len(transactions)+len(products),len(transactions)+len(products),"SUCCESS"],["staging",len(transactions),len(staged),"SUCCESS"],["curated",len(staged),len(sales),"SUCCESS"]], columns=["stage","input_rows","output_rows","status"]).to_csv(SUBMISSION / "pipeline_report.csv", index=False)


if __name__ == "__main__": build_submission()

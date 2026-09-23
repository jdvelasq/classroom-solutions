"""Simula una API paginada con un fallo transitorio y la ingiere."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).parents[1]
OUTPUT, REPORT = ROOT / "submission/reviews.parquet", ROOT / "submission/api_ingestion_report.csv"
PAGES = [[{"review_id":f"R{p}{i}","product_id":f"P{i}","rating":i % 5 + 1,"review_date":"2026-02-01","review_text":"review"} for i in range(1,5)] for p in range(1,4)]

def response(page, attempt):
    if page == 2 and attempt == 1: return 500, {}
    return 200, {"page":page,"page_size":4,"total_pages":len(PAGES),"items":PAGES[page-1]}

def build_submission():
    records, retries, page = [], 0, 1
    while True:
        for attempt in range(1,4):
            status, payload = response(page, attempt)
            if status == 200: break
            retries += 1
        else: raise RuntimeError("La API no se recuperó")
        records.extend(payload["items"])
        if page == payload["total_pages"]: break
        page += 1
    frame = pd.DataFrame(records); assert frame.review_id.is_unique
    frame.to_parquet(OUTPUT, index=False, engine="pyarrow")
    pd.DataFrame([["reviews_api",page,len(frame),retries,"SUCCESS",str(OUTPUT)]], columns=["source_name","pages_requested","records_retrieved","retry_count","status","output_path"]).to_csv(REPORT,index=False)

if __name__ == "__main__": build_submission()

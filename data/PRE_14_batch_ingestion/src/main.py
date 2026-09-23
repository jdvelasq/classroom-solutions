"""Ingiere archivos operativos por lote y conserva su capa raw."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).parents[1]
DATA, RAW, REPORT = ROOT / "data", ROOT / "temp/raw", ROOT / "submission/ingestion_report.csv"
SOURCES = {"machine_throughput": "machine_throughput_export.csv", "machine_uptime": "machine_uptime_export.csv", "factory_ambient": "factory_ambient_export.csv"}

def build_submission():
    RAW.mkdir(parents=True, exist_ok=True)
    results = []
    for source_name, filename in SOURCES.items():
        frame = pd.read_csv(DATA / filename)
        output = RAW / f"{source_name}.parquet"
        frame.to_parquet(output, index=False)
        results.append((source_name, "file", len(frame), "SUCCESS", str(output)))
    pd.DataFrame(results, columns=["source_name", "source_type", "row_count", "status", "output_path"]).to_csv(REPORT, index=False)

if __name__ == "__main__":
    build_submission()

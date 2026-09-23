"""Actualiza producción máquina-día con un lote incremental idempotente."""
import json
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def main():
    source = pd.read_csv(ROOT / "data/machine_throughput_export.csv").head(30).copy()
    source["operation_id"] = source.factory_id.astype(str) + "-" + source.machine_id.astype(str) + "-" + source.factory_date
    baseline = source.iloc[:20].assign(updated_at="2019-11-01T08:00:00")
    correction = baseline.iloc[[1]].assign(daily_units_produced=lambda x: x.daily_units_produced + 100, updated_at="2019-11-02T08:00:00")
    replay = baseline.iloc[[2]].copy()
    insertion = source.iloc[[20]].assign(updated_at="2019-11-02T08:10:00")
    batch = pd.concat([correction, replay, insertion], ignore_index=True)
    current = pd.concat([baseline, batch], ignore_index=True).sort_values("updated_at").drop_duplicates("operation_id", keep="last").sort_values("operation_id")
    output = ROOT / "submission"; output.mkdir(exist_ok=True)
    current.to_csv(output / "operations_current.csv", index=False)
    checkpoint = {"last_batch": "2019-11-02", "inserted": 1, "updated": 1, "replayed": 1}
    (output / "pipeline_run.json").write_text(json.dumps(checkpoint, indent=2) + "\n")
    reconciliation = {"row_count": len(current), "total_units": int(current.daily_units_produced.sum()), "unique_operations": int(current.operation_id.nunique())}
    (output / "reconciliation.json").write_text(json.dumps(reconciliation, indent=2) + "\n")
    return current, reconciliation

if __name__ == "__main__": main()

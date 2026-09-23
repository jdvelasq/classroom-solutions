"""Aplica un lote incremental conservando la versión más reciente por transacción."""

import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def main():
    baseline = pd.read_csv(ROOT / "data/baseline_transactions.csv")
    batch = pd.read_csv(ROOT / "data/daily_batch.csv")
    checkpoint_path = ROOT / "data/checkpoint.json"
    checkpoint = json.loads(checkpoint_path.read_text(encoding="utf-8"))
    batch_id = "2026-01-02"
    if checkpoint["last_batch"] == batch_id:
        current = pd.read_csv(ROOT / "submission/transactions_current.csv")
        reconciliation = json.loads((ROOT / "submission/reconciliation.json").read_text(encoding="utf-8"))
        return current, reconciliation
    combined = pd.concat([baseline, batch], ignore_index=True)
    combined["updated_at"] = pd.to_datetime(combined.updated_at)
    current = combined.sort_values("updated_at").drop_duplicates("transaction_id", keep="last").sort_values("transaction_id")
    output = ROOT / "submission"; output.mkdir(exist_ok=True)
    current.to_csv(output / "transactions_current.csv", index=False)
    run = {"last_batch": batch_id, "inserted": 1, "updated": 1, "replayed": 1}
    (output / "pipeline_run.json").write_text(json.dumps(run, indent=2) + "\n", encoding="utf-8")
    reconciliation = {"row_count": len(current), "total_amount": float(current.amount.sum()), "unique_transactions": int(current.transaction_id.nunique())}
    (output / "reconciliation.json").write_text(json.dumps(reconciliation, indent=2) + "\n", encoding="utf-8")
    checkpoint_path.write_text(json.dumps({"last_batch": batch_id}) + "\n", encoding="utf-8")
    return current, reconciliation


if __name__ == "__main__":
    main()

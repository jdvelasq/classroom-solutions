"""Actualiza una tabla de clientes con un lote incremental e idempotente."""

import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).parents[1]
OUTPUT = ROOT / "submission/customers_current.csv"
REPORT = ROOT / "submission/incremental_report.csv"
CHECKPOINT = ROOT / "temp/checkpoint.json"


def build_submission():
    """Aplica inserciones, actualizaciones y eventos ya procesados de forma explícita."""
    current = pd.DataFrame(
        [
            ["C1", "Ana", "Basic", "2026-09-01T09:00:00"],
            ["C2", "Luis", "Premium", "2026-09-01T09:00:00"],
            ["C3", "Mariana", "Basic", "2026-09-01T09:00:00"],
        ],
        columns=["customer_id", "customer_name", "segment", "updated_at"],
    )
    changes = pd.DataFrame(
        [
            ["C2", "Luis Gomez", "Corporate", "2026-09-16T10:00:00"],
            ["C3", "Mariana", "Basic", "2026-09-01T09:00:00"],
            ["C4", "Diego", "Premium", "2026-09-16T10:30:00"],
        ],
        columns=current.columns,
    )
    actions = []
    for row in changes.itertuples(index=False):
        exists = current.customer_id.eq(row.customer_id)
        if not exists.any():
            current = pd.concat(
                [current, pd.DataFrame([row], columns=current.columns)],
                ignore_index=True,
            )
            actions.append("INSERT")
        elif current.loc[exists, "updated_at"].iloc[0] < row.updated_at:
            current.loc[exists] = list(row)
            actions.append("UPDATE")
        else:
            actions.append("UNCHANGED")
    current.sort_values("customer_id").to_csv(OUTPUT, index=False)
    pd.DataFrame(
        [
            [action, actions.count(action)]
            for action in ["INSERT", "UPDATE", "UNCHANGED"]
        ],
        columns=["action", "record_count"],
    ).to_csv(REPORT, index=False)
    CHECKPOINT.parent.mkdir(exist_ok=True)
    CHECKPOINT.write_text(json.dumps({"high_water_mark": "2026-09-16T10:30:00"}))


if __name__ == "__main__":
    build_submission()

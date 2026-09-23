"""Valida el contrato y separa registros aceptados de cuarentena."""

import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def main():
    contract = json.loads((ROOT / "data/customer_contract.json").read_text(encoding="utf-8"))
    frame = pd.read_csv(ROOT / "data/customer_feed.csv", dtype={"customer_id": "string", "segment": "string"})
    missing = sorted(set(contract["required_columns"]) - set(frame.columns))
    if missing:
        raise ValueError(f"Columnas requeridas ausentes: {missing}")
    age = pd.to_numeric(frame.age, errors="coerce")
    reasons = pd.Series("", index=frame.index, dtype="string")
    reasons = reasons.mask(frame.customer_id.duplicated(keep=False), "duplicate_customer_id")
    reasons = reasons.mask(age.isna(), "missing_age")
    reasons = reasons.mask((age < 18) | (age > 100), "invalid_age")
    reasons = reasons.mask(~frame.segment.isin(contract["segments"]), "invalid_segment")
    accepted = frame.loc[reasons == ""].copy()
    quarantined = frame.loc[reasons != ""].copy()
    quarantined["reason"] = reasons.loc[quarantined.index]
    output = ROOT / "submission"; output.mkdir(exist_ok=True)
    accepted.to_csv(output / "accepted_customers.csv", index=False)
    quarantined.to_csv(output / "quarantined_customers.csv", index=False)
    report = {"input_rows": len(frame), "accepted_rows": len(accepted), "quarantined_rows": len(quarantined), "reasons": quarantined.reason.value_counts().to_dict()}
    (output / "quality_report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


if __name__ == "__main__":
    main()

"""Valida un lote tributario real y conserva las infracciones en cuarentena."""

import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def main():
    source = pd.read_csv(ROOT / "data/vemont.csv").query("zipcode != 0").head(40).copy()
    feed = pd.concat(
        [
            source,
            source.iloc[[0, 1]].assign(agi_stub=[7, 1], N1=[-1, source.iloc[1].N1]),
        ],
        ignore_index=True,
    )
    key = feed[["zipcode", "agi_stub"]].duplicated(keep=False)
    violations = pd.DataFrame(
        {
            "invalid_state": feed.STATE.ne("VT") | feed.STATEFIPS.ne(50),
            "invalid_income_group": ~feed.agi_stub.between(1, 6),
            "duplicate_postal_income_key": key,
            "negative_return_count": feed.N1.lt(0),
        }
    )
    reasons = violations.apply(lambda row: "|".join(row.index[row].tolist()), axis=1)
    accepted, quarantined = (
        feed.loc[reasons.eq("")].copy(),
        feed.loc[reasons.ne("")].copy(),
    )
    quarantined["reason"] = reasons.loc[quarantined.index]
    output = ROOT / "submission"
    output.mkdir(exist_ok=True)
    accepted.to_csv(output / "accepted_tax_records.csv", index=False)
    quarantined.to_csv(output / "quarantined_tax_records.csv", index=False)
    report = {
        "input_rows": len(feed),
        "accepted_rows": len(accepted),
        "quarantined_rows": len(quarantined),
        "reasons": violations.sum().astype(int).to_dict(),
    }
    (output / "quality_report.json").write_text(json.dumps(report, indent=2) + "\n")
    return report


if __name__ == "__main__":
    main()

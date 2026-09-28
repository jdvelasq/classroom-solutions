"""Evalúa si un dato está suficientemente fresco para una decisión operativa."""

import json
from datetime import date
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]


def main():
    """La frescura explícita evita usar datos viejos sin advertencia."""

    status = json.loads((ROOT_DIR / "data" / "source_status.json").read_text())
    age = (date.fromisoformat(status["checked_at"]) - date.fromisoformat(status["data_as_of"])).days
    report = {"age_days": age, "maximum_age_days": status["maximum_age_days"], "alert": age > status["maximum_age_days"]}
    (ROOT_DIR / "submission" / "freshness_report.json").write_text(json.dumps(report), encoding="utf-8")


if __name__ == "__main__":
    main()

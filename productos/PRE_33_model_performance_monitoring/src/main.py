"""Monitorea el desempeño de predicciones cuando llegan los resultados reales."""

import json
from pathlib import Path

import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[1]
MINIMUM_ACCURACY = 0.75


def main():
    """La calidad real del modelo solo puede observarse después de conocer el resultado."""

    outcomes = pd.read_csv(ROOT_DIR / "data" / "production_outcomes.csv")
    accuracy = float((outcomes["prediction"] == outcomes["actual"]).mean())
    report = {
        "observations": len(outcomes),
        "accuracy": accuracy,
        "minimum_accuracy": MINIMUM_ACCURACY,
        "alert": accuracy < MINIMUM_ACCURACY,
    }
    (ROOT_DIR / "submission" / "performance_report.json").write_text(
        json.dumps(report, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()

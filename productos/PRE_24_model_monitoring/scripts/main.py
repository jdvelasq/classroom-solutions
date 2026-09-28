"""Produce una alerta operativa cuando los datos de producción cambian."""

import json
from pathlib import Path

import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[1]
ALERT_THRESHOLD = 1.0


def compare_feature(reference, production, feature):
    """Una medida simple hace visible la necesidad de vigilar la entrada real."""

    reference_mean = reference[feature].mean()
    reference_std = reference[feature].std()
    production_mean = production[feature].mean()
    standardized_difference = abs(production_mean - reference_mean) / reference_std
    return {
        "feature": feature,
        "reference_mean": float(reference_mean),
        "production_mean": float(production_mean),
        "standardized_difference": float(standardized_difference),
        "alert": bool(standardized_difference > ALERT_THRESHOLD),
    }


def main():
    """El reporte separa una señal de monitoreo de una decisión de reentrenamiento."""

    reference = pd.read_csv(ROOT_DIR / "data" / "reference.csv")
    production = pd.read_csv(ROOT_DIR / "data" / "production.csv")
    features = [column for column in reference.columns if column != "quality"]
    comparisons = [compare_feature(reference, production, feature) for feature in features]
    alerts = [comparison["feature"] for comparison in comparisons if comparison["alert"]]
    report = {"threshold": ALERT_THRESHOLD, "alerts": alerts, "features": comparisons}

    output_path = ROOT_DIR / "submission" / "monitoring_report.json"
    output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

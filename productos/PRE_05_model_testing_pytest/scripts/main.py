# Uso: python3 src/main.py

import json
import pickle
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, balanced_accuracy_score, roc_auc_score


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
MIN_ACCURACY = 0.70
MIN_BALANCED_ACCURACY = 0.70
MIN_AUC = 0.80


def load_model_and_test_set():
    # El artefacto se carga congelado para evaluar su operación, no para volver a entrenarlo.

    with (ACTIVITY_DIR / "ESTIMATOR.pkl").open("rb") as file:
        model = pickle.load(file)
    test_set = pd.read_csv(ACTIVITY_DIR / "data" / "model_test_set.csv")
    features = list(model.feature_names_in_)
    return model, test_set.loc[:, features], test_set["target"], features


def model_metrics(model, inputs, target):
    # Las métricas convierten un umbral operativo acordado en una condición verificable.

    predictions = model.predict(inputs)
    probabilities = model.predict_proba(inputs)[:, 1]
    return {
        "accuracy": float(accuracy_score(target, predictions)),
        "balanced_accuracy": float(balanced_accuracy_score(target, predictions)),
        "auc": float(roc_auc_score(target, probabilities)),
    }


def main() -> None:
    # El reporte preserva la evidencia de la verificación para una revisión posterior.

    model, inputs, target, features = load_model_and_test_set()
    metrics = model_metrics(model, inputs, target)
    report = {"features": features, "holdout_rows": len(inputs), "metrics": metrics}
    report_path = ACTIVITY_DIR / "submission" / "model_test_report.json"
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Reporte generado: {report_path.name}")


if __name__ == "__main__":
    main()

# Uso: python3 src/main.py

import json
import pickle
from pathlib import Path

import pandas as pd
from sklearn.ensemble import IsolationForest


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
MAX_ANOMALY_RATE = 0.15


def assess_inputs(training_inputs: pd.DataFrame, candidate_inputs: pd.DataFrame):
    # La compatibilidad se evalúa frente a las entradas conocidas, no frente a una intuición visual.

    detector = IsolationForest(contamination=0.05, random_state=0)
    detector.fit(training_inputs)
    anomaly_rate = float((detector.predict(candidate_inputs) == -1).mean())
    return anomaly_rate, anomaly_rate <= MAX_ANOMALY_RATE


def load_inputs():
    # Las columnas se leen del artefacto para evitar evaluar un conjunto con una interfaz distinta.

    with (ACTIVITY_DIR / "ESTIMATOR.pkl").open("rb") as file:
        estimator = pickle.load(file)
    features = list(estimator.feature_names_in_)
    data_dir = ACTIVITY_DIR / "data"
    return (
        pd.read_csv(data_dir / "training_inputs.csv").loc[:, features],
        pd.read_csv(data_dir / "new_inputs.csv").loc[:, features],
        features,
    )


def main() -> None:
    # El reporte permite revisar la decisión de compatibilidad antes de habilitar el scoring.

    training_inputs, new_inputs, features = load_inputs()
    shifted_inputs = new_inputs.assign(texture_mean=lambda dataframe: dataframe["texture_mean"] + 100)
    new_rate, new_compatible = assess_inputs(training_inputs, new_inputs)
    shifted_rate, shifted_compatible = assess_inputs(training_inputs, shifted_inputs)
    report = {
        "features": features,
        "new_inputs": {"anomaly_rate": new_rate, "compatible": new_compatible},
        "shifted_inputs": {"anomaly_rate": shifted_rate, "compatible": shifted_compatible},
    }
    report_path = ACTIVITY_DIR / "submission" / "input_distribution_report.json"
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Reporte generado: {report_path.name}")


if __name__ == "__main__":
    main()

import pickle
from pathlib import Path

import pandas as pd
from sklearn.ensemble import IsolationForest


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
MAX_ANOMALY_RATE = 0.15


def load_model_features(model_path: Path) -> list[str]:
    with model_path.open("rb") as file:
        estimator = pickle.load(file)

    return list(estimator.feature_names_in_)


def select_model_inputs(dataframe: pd.DataFrame, features: list[str]) -> pd.DataFrame:
    if set(dataframe.columns) != set(features):
        raise ValueError("Las columnas de entrada no coinciden con las del modelo.")

    return dataframe.loc[:, features]


def assess_new_inputs(
    training_inputs: pd.DataFrame, new_inputs: pd.DataFrame
) -> tuple[float, bool]:
    detector = IsolationForest(contamination=0.05, random_state=0)
    detector.fit(training_inputs)

    anomaly_rate = (detector.predict(new_inputs) == -1).mean()
    return anomaly_rate, anomaly_rate <= MAX_ANOMALY_RATE


def main() -> None:
    features = load_model_features(ACTIVITY_DIR / "estimator.pkl")
    training_inputs = pd.read_csv(ACTIVITY_DIR / "data" / "training_inputs.csv")
    new_inputs = pd.read_csv(ACTIVITY_DIR / "data" / "new_inputs.csv")

    training_inputs = select_model_inputs(training_inputs, features)
    new_inputs = select_model_inputs(new_inputs, features)
    anomaly_rate, is_compatible = assess_new_inputs(training_inputs, new_inputs)

    print(f"Tasa de entradas inusuales: {anomaly_rate:.2%}")
    print(f"Entradas compatibles: {'sí' if is_compatible else 'no'}")


if __name__ == "__main__":
    main()

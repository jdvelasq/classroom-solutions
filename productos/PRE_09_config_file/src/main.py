import json
import pickle
from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score, balanced_accuracy_score


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
# Las opciones admitidas convierten el archivo de configuración en un contrato verificable.

ALLOWED_DATASETS = ("train", "test", "prod")


def load_dataset_name(config_path: Path) -> str:
    # La decisión queda fuera del código para poder conservar y revisar cada ejecución.

    with config_path.open(encoding="utf-8") as file:
        config = json.load(file)

    dataset = config.get("dataset")
    if dataset not in ALLOWED_DATASETS:
        allowed_values = ", ".join(ALLOWED_DATASETS)
        raise ValueError(
            f"El valor de 'dataset' debe ser uno de: {allowed_values}."
        )

    return dataset


def main() -> None:
    # El artefacto se ejecuta igual; solo cambia la configuración declarada.

    dataset = load_dataset_name(ACTIVITY_DIR / "config.json")
    data_path = ACTIVITY_DIR / "data" / dataset / "sentences.csv.gz"

    dataframe = pd.read_csv(data_path)

    with (ACTIVITY_DIR / "estimator.pkl").open("rb") as file:
        estimator = pickle.load(file)

    predictions = estimator.predict(dataframe["phrase"])
    accuracy = accuracy_score(dataframe["target"], predictions)
    balanced_accuracy = balanced_accuracy_score(dataframe["target"], predictions)

    print(f"Conjunto: {dataset}")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Balanced accuracy: {balanced_accuracy:.4f}")


if __name__ == "__main__":
    main()

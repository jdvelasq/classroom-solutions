import argparse
import pickle
from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score, balanced_accuracy_score


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
# Los valores admitidos evitan que una ejecución reproducible dependa de nombres improvisados.

ALLOWED_DATASETS = ("train", "test", "prod")


def parse_arguments() -> argparse.Namespace:
    # El parámetro permite ejecutar el mismo artefacto en contextos de datos distintos sin editarlo.

    parser = argparse.ArgumentParser(
        description="Calcula métricas para uno de los conjuntos disponibles."
    )
    parser.add_argument(
        "dataset",
        choices=ALLOWED_DATASETS,
        help="Conjunto a evaluar: train, test o prod.",
    )
    return parser.parse_args()


def main() -> None:
    # El modelo se mantiene fijo para que cambie solo el conjunto elegido en cada ejecución.

    arguments = parse_arguments()
    data_path = ACTIVITY_DIR / "data" / arguments.dataset / "sentences.csv.gz"

    dataframe = pd.read_csv(data_path)

    with (ACTIVITY_DIR / "estimator.pkl").open("rb") as file:
        estimator = pickle.load(file)

    predictions = estimator.predict(dataframe["phrase"])
    accuracy = accuracy_score(dataframe["target"], predictions)
    balanced_accuracy = balanced_accuracy_score(dataframe["target"], predictions)

    print(f"Conjunto: {arguments.dataset}")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Balanced accuracy: {balanced_accuracy:.4f}")


if __name__ == "__main__":
    main()

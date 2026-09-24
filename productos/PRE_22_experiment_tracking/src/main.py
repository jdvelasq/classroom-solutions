"""Registra una corrida analítica para poder recuperarla y compararla después."""

import argparse
import json
import pickle
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier


ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT_DIR / "data" / "winequality-red.csv"
EXPERIMENTS_DIR = ROOT_DIR / "submission" / "experiments"


def parse_arguments():
    """Las opciones acotadas evitan distraer la actividad con el diseño del modelo."""

    parser = argparse.ArgumentParser()
    parser.add_argument("--model", choices=["tree", "knn"], required=True)
    parser.add_argument("--run-id")
    return parser.parse_args()


def build_model(model_name):
    """Dos alternativas bastan para hacer visible el valor de comparar corridas."""

    if model_name == "tree":
        return DecisionTreeClassifier(max_depth=4, random_state=123)
    return KNeighborsClassifier(n_neighbors=7)


def prepare_data():
    """La misma partición permite atribuir diferencias al modelo y no a los datos."""

    data = pd.read_csv(DATA_PATH)
    features = data.drop(columns="quality")
    target = data["quality"]
    return train_test_split(
        features, target, test_size=0.25, random_state=123, stratify=target
    )


def save_run(run_id, model_name, model, x_train, x_test, y_train, y_test, accuracy):
    """Cada corrida conserva insumos, configuración, resultado y modelo recuperable."""

    run_dir = EXPERIMENTS_DIR / run_id
    data_dir = run_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=False)

    x_train.assign(quality=y_train).to_csv(data_dir / "train.csv", index=False)
    x_test.assign(quality=y_test).to_csv(data_dir / "test.csv", index=False)
    (run_dir / "config.json").write_text(
        json.dumps({"model": model_name, "random_state": 123, "test_size": 0.25}, indent=2),
        encoding="utf-8",
    )
    (run_dir / "metrics.json").write_text(
        json.dumps({"test_accuracy": accuracy}, indent=2), encoding="utf-8"
    )
    with (run_dir / "model.pkl").open("wb") as output_file:
        pickle.dump(model, output_file)

    return run_dir


def update_index(run_id, model_name, accuracy):
    """Un índice permite ver y recuperar corridas sin explorar carpeta por carpeta."""

    index_path = EXPERIMENTS_DIR / "index.json"
    index = json.loads(index_path.read_text(encoding="utf-8")) if index_path.exists() else []
    index.append(
        {
            "run_id": run_id,
            "model": model_name,
            "test_accuracy": accuracy,
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
    )
    index_path.write_text(json.dumps(index, indent=2), encoding="utf-8")


def main():
    """Una corrida deja artefactos comparables sin exigir conocer el algoritmo."""

    arguments = parse_arguments()
    run_id = arguments.run_id or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    x_train, x_test, y_train, y_test = prepare_data()
    model = build_model(arguments.model)
    model.fit(x_train, y_train)
    accuracy = accuracy_score(y_test, model.predict(x_test))

    run_dir = save_run(
        run_id, arguments.model, model, x_train, x_test, y_train, y_test, accuracy
    )
    update_index(run_id, arguments.model, accuracy)
    print(f"Corrida guardada en: {run_dir}")
    print(f"Exactitud de prueba: {accuracy:.3f}")


if __name__ == "__main__":
    main()

"""Estima el valor de reventa de vehículos usados."""

from pathlib import Path
import json
import pickle

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ACTIVITY_DIR / "data"
SUBMISSION_DIR = ACTIVITY_DIR / "submission"
FEATURES = ["Age", "Present_Price", "Driven_kms", "Fuel_Type", "Selling_type", "Transmission", "Owner"]


def prepare_data(frame):
    """Construye variables disponibles para estimar el valor de reventa."""
    data = frame.copy()
    data["Age"] = 2021 - data["Year"]
    return data


def main():
    """
    Un concesionario de vehículos usados quiere estimar a qué precio podrá
    revender un carro antes de ofrecerlo, a partir de información que conoce
    al recibirlo. Los archivos `data/train_data.csv.gz` (211 vehículos) y
    `data/test_data.csv.gz` (90 vehículos) tienen una fila por vehículo, con
    el modelo (`Car_Name`), el año de fabricación (`Year`), el precio de
    reventa (`Selling_Price`), el precio del vehículo nuevo
    (`Present_Price`), el kilometraje (`Driven_kms`), el combustible
    (`Fuel_Type`), el tipo de vendedor (`Selling_type`), la transmisión
    (`Transmission`) y el número de propietarios anteriores (`Owner`). Los
    precios están en lakhs de rupias. Los datos se recolectaron en 2021.

    Construya un modelo de regresión que estime `Selling_Price`. Entrénelo
    solamente con el conjunto de entrenamiento y use el conjunto de prueba
    únicamente para evaluarlo. Usted decide qué variables usar y cómo
    transformarlas, pero no puede usar `Selling_Price` como entrada.

    Genere tres archivos en `submission/`:

    1. `test_predictions.csv`, sin el índice de Pandas, con una fila por
       vehículo del conjunto de prueba, en el mismo orden del archivo, y las
       columnas `actual_price` (el `Selling_Price` observado) y
       `predicted_price` (la estimación del modelo).

    2. `metrics.json`, con dos llaves: `test_mae`, el error absoluto medio
       sobre el conjunto de prueba, y `test_r2`, el coeficiente de
       determinación R² sobre el mismo conjunto.

    3. `model.pkl`, con el modelo entrenado guardado con `pickle`.

    Escriba su solución en la función `main()`, que debe generar los tres
    archivos al ejecutarse.

    Ejemplo del formato de `test_predictions.csv`:

        actual_price,predicted_price
        4.75,6.9533
        7.25,7.4968
        ...

    Ejemplo del formato de `metrics.json`:

        {
          "test_mae": 1.4542,
          "test_r2": 0.7898
        }
    """
    train = prepare_data(pd.read_csv(DATA_DIR / "train_data.csv.gz"))
    test = prepare_data(pd.read_csv(DATA_DIR / "test_data.csv.gz"))
    categorical = ["Fuel_Type", "Selling_type", "Transmission"]
    model = Pipeline([
        ("features", ColumnTransformer([("categorical", OneHotEncoder(handle_unknown="ignore"), categorical)], remainder="passthrough")),
        ("regression", LinearRegression()),
    ])
    model.fit(train[FEATURES], train["Selling_Price"])
    predictions = model.predict(test[FEATURES])
    SUBMISSION_DIR.mkdir(exist_ok=True)
    pd.DataFrame({"actual_price": test["Selling_Price"], "predicted_price": predictions}).to_csv(SUBMISSION_DIR / "test_predictions.csv", index=False)
    metrics = {"test_mae": mean_absolute_error(test["Selling_Price"], predictions), "test_r2": r2_score(test["Selling_Price"], predictions)}
    (SUBMISSION_DIR / "metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    with (SUBMISSION_DIR / "model.pkl").open("wb") as file:
        pickle.dump(model, file)


if __name__ == "__main__":
    main()

"""Prioriza solicitudes de crédito según la probabilidad de incumplimiento."""

from pathlib import Path
import json
import pickle

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, balanced_accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ACTIVITY_DIR / "data"
SUBMISSION_DIR = ACTIVITY_DIR / "submission"
TARGET = "default payment next month"


def prepare_data(frame):
    """Retira el identificador y conserva información disponible antes del pago."""
    data = frame.rename(columns={TARGET: "default"}).drop(columns="ID")
    data["EDUCATION"] = data["EDUCATION"].where(data["EDUCATION"].le(4), 4)
    return data


def main():
    """
    Un banco revisa manualmente parte de sus clientes de tarjeta de crédito
    para anticiparse a los incumplimientos, pero el equipo solo alcanza a
    revisar el 20 % de los casos. Se necesita una lista que indique a quién
    revisar primero. Los archivos `data/train_data.csv.gz` (21.000 clientes)
    y `data/test_data.csv.gz` (9.000 clientes) tienen una fila por cliente,
    con un identificador (`ID`), el cupo (`LIMIT_BAL`), variables
    demográficas (`SEX`, `EDUCATION`, `MARRIAGE`, `AGE`), el estado de pago
    de los últimos seis meses (`PAY_0`, `PAY_2`, ..., `PAY_6`), los montos
    facturados (`BILL_AMT1`, ..., `BILL_AMT6`), los montos pagados
    (`PAY_AMT1`, ..., `PAY_AMT6`) y la variable
    `default payment next month`, que vale 1 si el cliente incumplió el pago
    del mes siguiente y 0 en caso contrario.

    Construya un modelo que estime la probabilidad de incumplimiento de cada
    cliente. Entrénelo solamente con el conjunto de entrenamiento y use el
    conjunto de prueba únicamente para evaluarlo. El identificador `ID` no
    es información del cliente y no debe usarse como entrada.

    Use estas definiciones sobre el conjunto de prueba:

    - Umbral de priorización (`priority_threshold`): el percentil 80 de las
      probabilidades estimadas.
    - Cliente priorizado: un cliente cuya probabilidad es mayor o igual que
      el umbral de priorización.
    - Predicción de incumplimiento: 1 si la probabilidad es mayor o igual
      que 0.5 y 0 en caso contrario.

    Genere tres archivos en `submission/`:

    1. `priority_applications.csv`, sin el índice de Pandas, con una fila por
       cliente del conjunto de prueba y las columnas `application_id` (la
       posición de la fila en `data/test_data.csv.gz`, empezando en 0),
       `default_probability` y `priority` (`True` si el cliente está
       priorizado y `False` en otro caso). Ordene las filas por
       `default_probability`, de mayor a menor.

    2. `metrics.json`, con tres llaves: `test_balanced_accuracy`, la exactitud
       balanceada de la predicción de incumplimiento; `test_average_precision`,
       la precisión promedio calculada con las probabilidades; y
       `priority_threshold`.

    3. `model.pkl`, con el modelo entrenado guardado con `pickle`.

    Escriba su solución en la función `main()`, que debe generar los tres
    archivos al ejecutarse.

    Ejemplo del formato de `priority_applications.csv`:

        application_id,default_probability,priority
        4073,0.9962,True
        269,0.9958,True
        ...

    Ejemplo del formato de `metrics.json`:

        {
          "test_balanced_accuracy": 0.6662,
          "test_average_precision": 0.5008,
          "priority_threshold": 0.5754
        }
    """
    train = prepare_data(pd.read_csv(DATA_DIR / "train_data.csv.gz"))
    test = prepare_data(pd.read_csv(DATA_DIR / "test_data.csv.gz"))
    features = train.columns.drop("default")
    model = Pipeline([("scale", StandardScaler()), ("classifier", LogisticRegression(max_iter=2000, class_weight="balanced"))])
    model.fit(train[features], train["default"])
    probability = model.predict_proba(test[features])[:, 1]
    threshold = float(pd.Series(probability).quantile(0.80))
    priority = pd.DataFrame({"application_id": test.index, "default_probability": probability})
    priority["priority"] = priority["default_probability"].ge(threshold)
    priority = priority.sort_values("default_probability", ascending=False)
    predictions = (probability >= 0.5).astype(int)
    metrics = {"test_balanced_accuracy": balanced_accuracy_score(test["default"], predictions), "test_average_precision": average_precision_score(test["default"], probability), "priority_threshold": threshold}
    SUBMISSION_DIR.mkdir(exist_ok=True)
    priority.to_csv(SUBMISSION_DIR / "priority_applications.csv", index=False)
    (SUBMISSION_DIR / "metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    with (SUBMISSION_DIR / "model.pkl").open("wb") as file:
        pickle.dump(model, file)


if __name__ == "__main__":
    main()

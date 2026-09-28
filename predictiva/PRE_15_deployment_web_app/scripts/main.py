"""Publica un modelo ya entrenado mediante una aplicación web."""

import pickle
from pathlib import Path

import pandas as pd
from flask import Flask, render_template, request


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = ACTIVITY_DIR / "HOUSE_PREDICTOR.pkl"
FEATURES = [
    "bedrooms",
    "bathrooms",
    "sqft_living",
    "sqft_lot",
    "floors",
    "waterfront",
    "condition",
]

app = Flask(__name__)


def load_model():
    """Carga el modelo que otra etapa ya dejó listo para servir."""
    with MODEL_PATH.open("rb") as file:
        return pickle.load(file)


def predict_price(form):
    """Transforma los valores del formulario en una predicción de precio."""
    house = {
        "bedrooms": int(form["bedrooms"]),
        "bathrooms": float(form["bathrooms"]),
        "sqft_living": float(form["sqft_living"]),
        "sqft_lot": float(form["sqft_lot"]),
        "floors": float(form["floors"]),
        "waterfront": int(form["waterfront"] == "yes"),
        "condition": int(form["condition"]),
    }
    feature_row = pd.DataFrame([house], columns=FEATURES)
    return round(float(load_model().predict(feature_row)[0][0]), 2)


@app.route("/", methods=["GET", "POST"])
def index():
    """Muestra el formulario y el resultado de una solicitud válida."""
    prediction = None
    error = None
    if request.method == "POST":
        try:
            prediction = predict_price(request.form)
        except (KeyError, ValueError):
            error = "Revise los valores ingresados antes de calcular la predicción."
    return render_template("index.html", prediction=prediction, error=error)


if __name__ == "__main__":
    app.run(debug=True)

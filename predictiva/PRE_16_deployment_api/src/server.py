"""Sirve predicciones de precio mediante una API HTTP."""

import pickle
from pathlib import Path

import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = ACTIVITY_DIR / "submission" / "house_predictor.pkl"
FEATURES = ["bedrooms", "bathrooms", "sqft_living", "sqft_lot", "floors", "waterfront", "condition"]


class HouseFeatures(BaseModel):
    """Define el contrato de datos que recibe la API."""
    bedrooms: int = Field(ge=0)
    bathrooms: float = Field(ge=0)
    sqft_living: float = Field(gt=0)
    sqft_lot: float = Field(gt=0)
    floors: float = Field(gt=0)
    waterfront: int = Field(ge=0, le=1)
    condition: int = Field(ge=1, le=5)


def load_model():
    """Carga el modelo entrenado por otro proceso del curso."""
    with MODEL_PATH.open("rb") as file:
        return pickle.load(file)


def predict_price(features: HouseFeatures):
    """Transforma una solicitud válida en una predicción serializable."""
    feature_row = pd.DataFrame([features.model_dump()], columns=FEATURES)
    prediction = load_model().predict(feature_row)
    return float(prediction[0][0])


app = FastAPI(title="House price prediction API")


@app.get("/health")
def health():
    """Confirma que el servicio está disponible."""
    return {"status": "available"}


@app.post("/predict")
def predict(features: HouseFeatures):
    """Devuelve una predicción para una vivienda con datos validados."""
    return {"predicted_price": predict_price(features)}

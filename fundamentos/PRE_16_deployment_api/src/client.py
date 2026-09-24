"""Consume la API de predicción desde otro proceso."""

import requests

API_URL = "http://127.0.0.1:8000/predict"


def make_request(api_url=API_URL):
    """Envía características de una vivienda y devuelve la respuesta JSON."""
    house = {"bedrooms": 3, "bathrooms": 2, "sqft_living": 1800, "sqft_lot": 2200, "floors": 1, "waterfront": 0, "condition": 3}
    response = requests.post(api_url, json=house, timeout=5)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(make_request())

"""Completa el sentimiento faltante en reseñas reales de Amazon."""

import pickle
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = ACTIVITY_DIR / "data" / "amazon_cells_labelled.tsv"
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def main():
    """
    Una tienda en línea recibió miles de reseñas de teléfonos celulares y
    accesorios, pero solo una pequeña parte fue etiquetada a mano como
    positiva o negativa. Se necesita completar la etiqueta de las demás. El
    archivo `data/amazon_cells_labelled.tsv` tiene 14.609 reseñas, una por
    línea, en dos columnas separadas por tabulador y sin encabezado: el texto
    de la reseña y su sentimiento (1 si es positiva y 0 si es negativa). Solo
    1.000 reseñas tienen el sentimiento; en las demás la segunda columna está
    vacía.

    Construya un clasificador de texto entrenado con las reseñas etiquetadas
    y úselo para completar el sentimiento de las reseñas que no lo tienen.
    Las etiquetas observadas no deben cambiar.

    Genere dos archivos en `submission/`:

    1. `completed_reviews.csv`, sin el índice de Pandas, con todas las
       reseñas del archivo original, en el mismo orden, y las columnas
       `review` (el texto) y `sentiment` (0 o 1, como número entero). Ninguna
       fila puede quedar sin sentimiento.

    2. `model.pkl`, con el clasificador entrenado guardado con `pickle`. El
       modelo debe recibir una lista de textos y retornar el sentimiento de
       cada uno.

    Escriba su solución en la función `main()`, que debe generar los dos
    archivos al ejecutarse.

    Ejemplo del formato de `completed_reviews.csv`:

        review,sentiment
        I try not to adjust the volume setting to avoid that I turn ...,0
        So there is no way for me to plug it in here in the US unless ...,0
        "Good case, Excellent value.",1
        ...
    """
    reviews = pd.read_csv(DATA_PATH, sep="\t", names=["review", "sentiment"])
    tagged_reviews = reviews.loc[reviews["sentiment"].notna()].copy()
    untagged_reviews = reviews.loc[reviews["sentiment"].isna()].copy()
    model = Pipeline(
        [
            ("vectorizer", TfidfVectorizer(stop_words="english", ngram_range=(1, 2))),
            ("classifier", LogisticRegression(max_iter=2000)),
        ]
    )
    model.fit(tagged_reviews["review"], tagged_reviews["sentiment"])
    untagged_reviews["sentiment"] = model.predict(untagged_reviews["review"])
    completed_reviews = pd.concat([tagged_reviews, untagged_reviews]).sort_index()
    completed_reviews["sentiment"] = completed_reviews["sentiment"].astype(int)
    SUBMISSION_DIR.mkdir(exist_ok=True)
    completed_reviews.to_csv(SUBMISSION_DIR / "completed_reviews.csv", index=False)
    with (SUBMISSION_DIR / "model.pkl").open("wb") as file:
        pickle.dump(model, file)


if __name__ == "__main__":
    main()

"""Genera recomendaciones con filtrado colaborativo usuario-usuario."""

from pathlib import Path

import numpy as np
import pandas as pd


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = ACTIVITY_DIR / "data" / "customer_products.csv"
SUBMISSION_DIR = ACTIVITY_DIR / "submission"
TARGET_CUSTOMER = "C10"


def cosine_similarity(matrix):
    """Calcula similitud coseno entre filas sin ocultar el cálculo central."""
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    normalized = np.divide(matrix, norms, out=np.zeros_like(matrix, dtype=float), where=norms != 0)
    return normalized @ normalized.T


def main():
    purchases = pd.read_csv(DATA_PATH)
    customer_product = pd.crosstab(purchases["customer_id"], purchases["product"])
    similarity = pd.DataFrame(cosine_similarity(customer_product.to_numpy()), index=customer_product.index, columns=customer_product.index)
    similarity.to_csv(SUBMISSION_DIR / "customer_similarity.csv") if SUBMISSION_DIR.exists() else None
    target_vector = customer_product.loc[TARGET_CUSTOMER]
    neighbor_weights = similarity.loc[TARGET_CUSTOMER].drop(TARGET_CUSTOMER)
    neighbor_products = customer_product.drop(TARGET_CUSTOMER)
    predicted_scores = neighbor_products.T.dot(neighbor_weights) / neighbor_weights.sum()
    recommendations = pd.DataFrame({"product": predicted_scores.index, "predicted_preference": predicted_scores.values, "already_owned": target_vector.values.astype(bool)})
    recommendations = recommendations.loc[~recommendations["already_owned"]].sort_values("predicted_preference", ascending=False)
    neighbors = neighbor_weights.sort_values(ascending=False).rename("similarity").reset_index().rename(columns={"index": "neighbor_customer"})
    SUBMISSION_DIR.mkdir(exist_ok=True)
    customer_product.reset_index().to_csv(SUBMISSION_DIR / "customer_product_matrix.csv", index=False)
    similarity.to_csv(SUBMISSION_DIR / "customer_similarity.csv")
    neighbors.to_csv(SUBMISSION_DIR / "nearest_neighbors.csv", index=False)
    recommendations.to_csv(SUBMISSION_DIR / "recommendations.csv", index=False)


if __name__ == "__main__":
    main()

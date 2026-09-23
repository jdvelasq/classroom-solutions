"""Completa el sentimiento faltante en reseñas reales de Amazon."""

from pathlib import Path
import pickle

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = ACTIVITY_DIR / "data" / "amazon_cells_labelled.tsv"
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def main():
    reviews = pd.read_csv(DATA_PATH, sep="\t", names=["review", "sentiment"])
    tagged_reviews = reviews.loc[reviews["sentiment"].notna()].copy()
    untagged_reviews = reviews.loc[reviews["sentiment"].isna()].copy()
    model = Pipeline([("vectorizer", TfidfVectorizer(stop_words="english", ngram_range=(1, 2))), ("classifier", LogisticRegression(max_iter=2000))])
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

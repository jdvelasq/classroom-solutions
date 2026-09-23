"""Clasifica sentimiento en reseñas reales de Amazon."""

from pathlib import Path
import json
import pickle

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = ACTIVITY_DIR / "data" / "amazon_cells_labelled.tsv"
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def main():
    reviews = pd.read_csv(DATA_PATH, sep="\t", names=["review", "sentiment"]).dropna()
    train, test = train_test_split(reviews, test_size=0.25, stratify=reviews["sentiment"], random_state=17)
    model = Pipeline([("vectorizer", TfidfVectorizer(stop_words="english", ngram_range=(1, 2))), ("classifier", LogisticRegression(max_iter=2000))])
    model.fit(train["review"], train["sentiment"])
    predicted = model.predict(test["review"])
    results = test.assign(predicted_sentiment=predicted)
    SUBMISSION_DIR.mkdir(exist_ok=True)
    results.to_csv(SUBMISSION_DIR / "test_predictions.csv", index=False)
    (SUBMISSION_DIR / "metrics.json").write_text(json.dumps({"test_f1": f1_score(test["sentiment"], predicted)}, indent=2), encoding="utf-8")
    with (SUBMISSION_DIR / "model.pkl").open("wb") as file:
        pickle.dump(model, file)


if __name__ == "__main__":
    main()

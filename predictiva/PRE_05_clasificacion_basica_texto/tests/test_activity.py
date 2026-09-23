import json
from pathlib import Path
import pickle

import pandas as pd
from sklearn.metrics import accuracy_score, balanced_accuracy_score, f1_score
from sklearn.model_selection import train_test_split



def test_saved_classifier_generalizes_across_sentiment_classes():
    dataframe = pd.read_csv(
        "data/sentences.csv.gz",
        index_col=False,
        compression="gzip",
    )

    _, X_test, _, y_test = train_test_split(
        dataframe.phrase,
        dataframe.target,
        test_size=0.3,
        random_state=0,
        stratify=dataframe.target,
    )

    with Path("submission/clf.pkl").open("rb") as file:
        clf = pickle.load(file)

    with Path("submission/vectorizer.pkl").open("rb") as file:
        vectorizer = pickle.load(file)

    predicted_proba = clf.predict_proba(vectorizer.transform(X_test))
    predictions = clf.predict(vectorizer.transform(X_test))
    accuracy = accuracy_score(
        y_true=y_test,
        y_pred=predictions,
    )

    assert accuracy > 0.83
    assert balanced_accuracy_score(y_test, predictions) > 0.72
    assert f1_score(y_test, predictions, average="macro") > 0.75
    assert predicted_proba.shape == (len(y_test), 3)
    assert (abs(predicted_proba.sum(axis=1) - 1) < 1e-9).all()

    with Path("submission/metrics.json").open(encoding="utf-8") as file:
        metrics = json.load(file)

    assert metrics["test_size"] == len(y_test)
    assert abs(metrics["test_accuracy"] - accuracy) < 1e-12

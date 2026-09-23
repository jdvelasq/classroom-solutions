import json
from pathlib import Path
import pickle

from sklearn import datasets  # type: ignore
from sklearn.metrics import accuracy_score  # type: ignore
from sklearn.model_selection import train_test_split  # type: ignore


def test_saved_classifier_generalizes_and_preserves_probabilities():
    digits = datasets.load_digits(return_X_y=True)
    data, target = digits

    _, X_test, _, y_test = train_test_split(
        data,
        target,
        test_size=0.5,
        random_state=0,
        stratify=target,
    )

    estimator_path = Path("submission/estimator.pkl")
    metrics_path = Path("submission/metrics.json")

    assert estimator_path.exists()
    assert metrics_path.exists()

    with estimator_path.open("rb") as file:
        new_clf = pickle.load(file)

    predicted_proba = new_clf.predict_proba(X_test)
    accuracy = accuracy_score(
        y_true=y_test,
        y_pred=new_clf.predict(X_test),
    )

    assert accuracy > 0.95
    assert predicted_proba.shape == (len(y_test), 10)
    assert (abs(predicted_proba.sum(axis=1) - 1) < 1e-9).all()

    with metrics_path.open(encoding="utf-8") as file:
        metrics = json.load(file)

    assert metrics["test_size"] == len(y_test)
    assert abs(metrics["test_accuracy"] - accuracy) < 1e-12

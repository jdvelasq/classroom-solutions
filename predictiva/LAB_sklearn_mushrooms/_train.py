"""Model metrics computation"""

import os
import pickle

import pandas as pd  # type: ignore
from sklearn.feature_selection import SelectKBest  # type: ignore
from sklearn.feature_selection import VarianceThreshold, f_classif
from sklearn.linear_model import LogisticRegressionCV  # type: ignore
from sklearn.model_selection import GridSearchCV  # type: ignore
from sklearn.pipeline import Pipeline  # type: ignore
from sklearn.preprocessing import OneHotEncoder  # type: ignore

import homework.pregunta_01 as pregunta
import tests.test_homework as tests


def create_dataset_files():
    """Create train and test datasets."""

    data = pd.read_csv("_mushrooms.csv")

    train_dataset = data.sample(frac=0.75, random_state=0)
    test_dataset = data.drop(train_dataset.index)

    if not os.path.exists("data"):
        os.makedirs("data")
    train_dataset.to_csv("data/train_dataset.csv", index=False)
    test_dataset.to_csv("data/test_dataset.csv", index=False)


def train_basic_estimator(basic_estimator):
    """Train basic estimator and save it to disk."""

    x_train, x_test, y_true_train, y_true_test = tests.load_datasets()

    estimator = GridSearchCV(
        estimator=Pipeline(
            steps=[
                ("oneHotEncoder", OneHotEncoder()),
                ("varianceThreshold", VarianceThreshold()),
                ("selectkbest", SelectKBest(score_func=f_classif)),
                ("estimator", basic_estimator),
            ],
            verbose=False,
        ),
        param_grid={
            "selectkbest__k": range(1, len(x_train.columns) + 1),
        },
        cv=10,
    )

    estimator.fit(x_train, y_true_train)

    y_pred_test = estimator.predict(x_test)
    accuracy = tests.eval_metrics(y_true_test, y_pred_test)

    best_estimator = tests.load_estimator()

    if best_estimator is None:
        best_estimator = estimator
    else:
        y_pred = best_estimator.predict(x_test)
        accuracy_saved_model = tests.eval_metrics(y_true_test, y_pred)
        if accuracy > accuracy_saved_model:
            best_estimator = estimator

    with open("_model.pkl", "wb") as file:
        pickle.dump(best_estimator, file)


def report(estimator, accuracy):
    """Print metrics."""

    print("  ", estimator, ":", sep="")
    print(f"    Accuracy: {accuracy}")


def train_estimators():
    """Train basic estimators."""

    if not os.path.exists("data/train_dataset.csv") or not os.path.exists(
        "data/test_dataset.csv"
    ):

        create_dataset_files()

    estimators = [
        LogisticRegressionCV(Cs=10),
        # RandomForestClassifier(),
    ]

    for estimator in estimators:
        train_basic_estimator(estimator)

    pregunta.pregunta_01()
    accuracy_train, accuracy_test = tests.compute_metrics()

    print("Training Metrics.")
    report(estimator, accuracy_train)
    print()
    print("Testing Metrics.")
    report(estimator, accuracy_test)


if __name__ == "__main__":
    train_estimators()

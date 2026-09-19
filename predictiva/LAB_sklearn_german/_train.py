"""Model metrics computation"""

import os
import pickle
import test

import pandas as pd
from sklearn.compose import make_column_selector, make_column_transformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest, VarianceThreshold, f_classif
from sklearn.linear_model import LogisticRegressionCV
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


def create_dataset_files():
    """Create train and test datasets."""

    data = pd.read_csv("german.csv")

    train_dataset = data.sample(frac=0.75, random_state=0)
    test_dataset = data.drop(train_dataset.index)
    train_dataset.to_csv("train_dataset.csv", index=False)
    test_dataset.to_csv("test_dataset.csv", index=False)


def train_basic_estimator(basic_estimator):
    """Train basic estimator and save it to disk."""

    x_train, x_test, y_true_train, y_true_test = test.load_datasets()

    estimator = GridSearchCV(
        estimator=Pipeline(
            steps=[
                (
                    "columntransfomer",
                    make_column_transformer(
                        (
                            OneHotEncoder(),
                            make_column_selector(dtype_include=object),
                        ),
                        remainder="passthrough",
                    ),
                ),
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
    accuracy = test.eval_metrics(y_true_test, y_pred_test)

    best_estimator = test.load_estimator()

    if best_estimator is None:
        best_estimator = estimator
    else:
        y_pred = best_estimator.predict(x_test)
        accuracy_saved_model = test.eval_metrics(y_true_test, y_pred)
        if accuracy > accuracy_saved_model:
            best_estimator = estimator

    with open("model.pkl", "wb") as file:
        pickle.dump(best_estimator, file)


def report(estimator, accuracy):
    """Print metrics."""

    print("  ", estimator, ":", sep="")
    print(f"    Accuracy: {accuracy}")


def train_estimators():
    """Train basic estimators."""

    if not os.path.exists("train_dataset.csv") or not os.path.exists(
        "test_dataset.csv"
    ):

        create_dataset_files()

    estimators = [
        LogisticRegressionCV(Cs=10, max_iter=10000),
        RandomForestClassifier(),
    ]

    for estimator in estimators:
        train_basic_estimator(estimator)

    accuracy_train, accuracy_test = test.compute_metrics()

    print("Training Metrics.")
    report(estimator, accuracy_train)
    print()
    print("Testing Metrics.")
    report(estimator, accuracy_test)


if __name__ == "__main__":
    train_estimators()
    test.run_grading()

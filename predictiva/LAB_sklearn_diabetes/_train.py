"""Model metrics computation"""

import os
import pickle

from sklearn.datasets import load_diabetes  # type: ignore
from sklearn.ensemble import RandomForestRegressor  # type: ignore
from sklearn.feature_selection import SelectKBest, f_regression  # type: ignore
from sklearn.linear_model import LinearRegression  # type: ignore
from sklearn.model_selection import GridSearchCV  # type: ignore
from sklearn.pipeline import Pipeline  # type: ignore

import tests.test_homework as test


def create_dataset_files():
    """Create train and test datasets."""

    data = load_diabetes(as_frame=True)["frame"]

    train_dataset = data.sample(frac=0.7, random_state=0)
    test_dataset = data.drop(train_dataset.index)
    train_dataset.to_csv("data/train_dataset.csv", index=False)
    test_dataset.to_csv("data/test_dataset.csv", index=False)


def train_basic_estimator(basic_estimator):
    """Train basic estimator and save it to disk."""

    x_train, x_test, y_true_train, y_true_test = test.load_datasets()

    estimator = GridSearchCV(
        estimator=Pipeline(
            steps=[
                ("selectkbest", SelectKBest(score_func=f_regression)),
                ("estimator", basic_estimator),
            ],
            verbose=False,
        ),
        param_grid={
            "selectkbest__k": range(1, len(x_train.columns) + 1),
        },
        cv=10,
        scoring="neg_mean_squared_error",
    )

    estimator.fit(x_train, y_true_train)

    y_pred_test = estimator.predict(x_test)
    mse, _, _ = test.eval_metrics(y_true_test, y_pred_test)

    best_estimator = test.load_estimator()

    if best_estimator is None:
        best_estimator = estimator
    else:
        y_pred = best_estimator.predict(x_test)
        mse_saved_model, _, _ = test.eval_metrics(y_true_test, y_pred)
        if mse < mse_saved_model:
            best_estimator = estimator

    with open("_model.pkl", "wb") as file:
        pickle.dump(best_estimator, file)


def report(estimator, mse, mae, r2):
    """Print metrics."""

    print("  ", estimator, ":", sep="")
    print(f"    MSE: {mse}")
    print(f"    MAE: {mae}")
    print(f"     R2: {r2}")


def train_estimators():
    """Train basic estimators."""

    if not os.path.exists("data/train_dataset.csv") or not os.path.exists(
        "data/test_dataset.csv"
    ):

        create_dataset_files()

    estimators = [
        LinearRegression(),
        RandomForestRegressor(),
    ]

    for estimator in estimators:
        train_basic_estimator(estimator)

    (
        mse_train,
        mae_train,
        r2_train,
        mse_test,
        mae_test,
        r2_test,
    ) = test.compute_metrics()

    print("Training Metrics.")
    report(estimator, mse_train, mae_train, r2_train)
    print()
    print("Testing Metrics.")
    report(estimator, mse_test, mae_test, r2_test)


if __name__ == "__main__":
    train_estimators()

import pickle

import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

def test_01():

    dataset = pd.read_csv("data/auto_mpg.csv")
    dataset = dataset.dropna()
    dataset["Origin"] = dataset["Origin"].map(
        {1: "USA", 2: "Europe", 3: "Japan"},
    )
    _, test_dataset = train_test_split(
        dataset,
        train_size=0.8,
        random_state=0,
    )

    y_true = test_dataset.pop("MPG")

    with open("submission/mlp.pkl", "rb") as file:
        mlp = pickle.load(file)

    with open("submission/features_preprocessor.pkl", "rb") as file:
        features_preprocessor = pickle.load(file)

    standarized_dataset = features_preprocessor.transform(test_dataset)
    y_pred = mlp.predict(standarized_dataset)

    mse = mean_squared_error(
        y_true=y_true,
        y_pred=y_pred,
    )

    assert mse < 8.0

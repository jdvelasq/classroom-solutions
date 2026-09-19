"""Data generator for the homework."""

import os
from pprint import pprint

import pandas as pd  # type: ignore


def make_data_dirs():
    """Create directories for the dataset."""
    for directory in ["train", "test"]:
        for target in ["positive", "negative", "neutral"]:
            os.makedirs(f"input/{directory}/{target}", exist_ok=True)


def load_dataset():
    """Load the original dataset from the file."""
    return pd.read_csv(
        "_sentences.csv.zip",
        compression="zip",
    )


def split_dataset(dataset):
    """Split the dataset into train and test."""
    train_dataset = dataset.sample(frac=0.8, random_state=0)
    test_dataset = dataset.drop(train_dataset.index)
    return train_dataset, test_dataset


def create_files(dataset, directory):
    """Create files with the sentences."""
    for target in ["positive", "negative", "neutral"]:
        df = dataset[dataset["target"] == target].reset_index(drop=True)
        for index, row in df.iterrows():
            with open(
                f"input/{directory}/{target}/{index:04d}.txt",
                "w",
                encoding="utf-8",
            ) as f:
                f.write(row["phrase"])


def save_dataset(dataset, filename):
    """Save the dataset to a CSV file."""
    os.makedirs("output/", exist_ok=True)
    dataset.to_csv("output/" + filename, index=False)


def compress_directory(directory):
    """Compress the directory into a zip file."""
    os.system(f"zip -r {directory}.zip {directory}")
    os.system(f"rm -rf {directory}")


def print_test_results(train_dataset, test_dataset):
    """Print the results of the test."""
    print()
    print("Train dataset:")
    pprint(train_dataset["target"].value_counts())
    print()
    print("Test dataset:")
    pprint(test_dataset["target"].value_counts())
    print(train_dataset.reset_index(drop=True).head().to_markdown())


def run():
    """Generate datasets for the homework."""

    make_data_dirs()
    dataset = load_dataset()
    train_dataset, test_dataset = split_dataset(dataset)
    save_dataset(train_dataset, "train_dataset.csv")
    save_dataset(test_dataset, "test_dataset.csv")

    create_files(train_dataset, "train")
    create_files(test_dataset, "test")
    print_test_results(train_dataset, test_dataset)
    compress_directory("input")


if __name__ == "__main__":
    run()

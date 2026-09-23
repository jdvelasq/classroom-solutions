"""Construye los entregables verificables del taller de tokenización."""

import json
from pathlib import Path

import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from scipy import sparse
from sklearn.feature_extraction.text import CountVectorizer


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = ACTIVITY_DIR / "data" / "sentences.csv.gz"
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def normalize(text):
    return " ".join(text.lower().split())


def main():
    dataframe = pd.read_csv(DATA_PATH, compression="gzip")
    dataframe["normalized_text"] = dataframe["phrase"].map(normalize)
    dataframe["tokens"] = dataframe["normalized_text"].map(word_tokenize)
    dataframe["tokens"] = dataframe["tokens"].map(
        lambda tokens: [token for token in tokens if token.isalpha()]
    )
    dataframe["processed_text"] = dataframe["tokens"].map(" ".join)

    vectorizer = CountVectorizer(min_df=2)
    matrix = vectorizer.fit_transform(dataframe["processed_text"])
    vocabulary = pd.DataFrame(
        {
            "token": vectorizer.get_feature_names_out(),
            "document_frequency": (matrix > 0).sum(axis=0).A1,
        }
    )

    SUBMISSION_DIR.mkdir(exist_ok=True)
    dataframe.drop(columns="tokens").to_csv(
        SUBMISSION_DIR / "tokenized_sentences.csv", index=False
    )
    vocabulary.to_csv(SUBMISSION_DIR / "vocabulary.csv", index=False)
    sparse.save_npz(SUBMISSION_DIR / "document_term_matrix.npz", matrix)
    with (SUBMISSION_DIR / "matrix_metadata.json").open("w", encoding="utf-8") as file:
        json.dump(
            {
                "documents": matrix.shape[0],
                "terms": matrix.shape[1],
                "minimum_document_frequency": 2,
            },
            file,
            indent=2,
        )


if __name__ == "__main__":
    main()

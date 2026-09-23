import json
from pathlib import Path

import pandas as pd
from scipy import sparse


def test_text_representation_is_complete_and_model_ready():
    source = pd.read_csv("data/sentences.csv.gz", compression="gzip")
    processed = pd.read_csv("submission/tokenized_sentences.csv")
    vocabulary = pd.read_csv("submission/vocabulary.csv")
    matrix = sparse.load_npz("submission/document_term_matrix.npz")

    assert len(processed) == len(source)
    assert list(processed.columns) == [
        "phrase",
        "target",
        "normalized_text",
        "processed_text",
    ]
    assert processed["processed_text"].str.len().gt(0).all()
    assert matrix.shape == (len(source), len(vocabulary))
    assert matrix.nnz > len(source)
    assert vocabulary["token"].is_unique
    assert vocabulary["document_frequency"].ge(2).all()


def test_matrix_metadata_describes_the_persisted_representation():
    with Path("submission/matrix_metadata.json").open(encoding="utf-8") as file:
        metadata = json.load(file)

    matrix = sparse.load_npz("submission/document_term_matrix.npz")
    assert metadata["documents"] == matrix.shape[0]
    assert metadata["terms"] == matrix.shape[1]
    assert metadata["minimum_document_frequency"] == 2

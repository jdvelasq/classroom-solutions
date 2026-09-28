from pathlib import Path


def test_01():
    assert Path("submission/document_term_matrix.npz").is_file()
    assert Path("submission/matrix_metadata.json").is_file()
    assert Path("submission/tokenized_sentences.csv").is_file()
    assert Path("submission/vocabulary.csv").is_file()

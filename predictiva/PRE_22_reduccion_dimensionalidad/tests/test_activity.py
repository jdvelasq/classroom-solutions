from pathlib import Path


def test_01():
    assert Path("submission/digits_pca.png").is_file()
    assert Path("submission/digits_tsne.png").is_file()
    assert Path("submission/digits_umap.png").is_file()

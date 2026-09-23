import os

def test_01():

    assert os.path.exists("submission/digits_pca.png")
    assert os.path.exists("submission/digits_tsne.png")
    assert os.path.exists("submission/digits_umap.png")

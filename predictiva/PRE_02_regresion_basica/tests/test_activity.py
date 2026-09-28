from pathlib import Path


def test_01():
    assert Path("submission/features_preprocessor.pkl").is_file()
    assert Path("submission/flexible_features_preprocessor.pkl").is_file()
    assert Path("submission/linear_flexible_model.pkl").is_file()
    assert Path("submission/mlp.pkl").is_file()
    assert Path("submission/model_comparison.csv").is_file()

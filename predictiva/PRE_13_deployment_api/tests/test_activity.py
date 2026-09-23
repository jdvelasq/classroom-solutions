from pathlib import Path


def test_api_activity_has_a_server_client_and_model_artifact():
    assert Path("src/api_server.py").exists()
    assert Path("src/api_client.py").exists()
    assert Path("src/train_model.py").exists()
    assert Path("submission/house_predictor.pkl").exists()

from pathlib import Path


def test_01():
    assert Path("submission/cluster-selection.csv").is_file()
    assert Path("submission/demanda-comercial-clusters.csv").is_file()
    assert Path("submission/demanda-comercial-dias.csv").is_file()
    assert Path("submission/demanda-comercial-patrones-ejemplo.png").is_file()
    assert Path("submission/demanda-comercial-perfiles.png").is_file()
    assert Path("submission/demanda-comercial.png").is_file()
    assert Path("submission/perfil-recibido.csv").is_file()

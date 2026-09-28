from ..src.main import pregunta_01, pregunta_02


def test_01():
    assert pregunta_01() == "Hola mundo cruel!"


def test_02():
    assert pregunta_02() == "Hello cruel world!"

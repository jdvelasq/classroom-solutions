"""Verifica que los objetivos automatizados apunten al flujo correcto."""

from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]


def test_makefile_exposes_report_and_test_targets():
    """Los nombres breves reducen errores al repetir tareas operativas."""

    makefile = (PRE_DIR / "Makefile").read_text(encoding="utf-8")

    assert "report:" in makefile
    assert "test:" in makefile
    assert "python3 src/main.py" in makefile

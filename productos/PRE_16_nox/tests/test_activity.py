"""Verifica que la actividad defina una sesión aislada de pruebas."""

from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]


def test_nox_session_installs_and_runs_product_test():
    """La automatización debe declarar ambiente, dependencias y prueba concreta."""

    noxfile = (PRE_DIR / "noxfile.py").read_text(encoding="utf-8")

    assert "@nox.session" in noxfile
    assert "def tests(session):" in noxfile
    assert 'session.install("--requirement", "requirements.txt", "pytest")' in noxfile
    assert 'session.run("pytest", "tests/test_report.py")' in noxfile

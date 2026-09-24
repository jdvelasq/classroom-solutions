"""Verifica que CI ejecute la sesión Nox del repositorio."""

from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]


def test_workflow_runs_nox_on_push_and_pull_request():
    """La misma automatización debe ejecutarse antes y después de integrar cambios."""

    workflow = (PRE_DIR / "data" / "repository_template" / ".github" / "workflows" / "tests.yml").read_text(encoding="utf-8")

    assert "push:" in workflow
    assert "pull_request:" in workflow
    assert "python -m pip install nox" in workflow
    assert "python -m nox -s tests" in workflow

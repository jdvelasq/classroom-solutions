"""Verifica que el taller entregue una automatización de integración continua."""

from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
WORKFLOW_PATH = (
    PRE_DIR / "data" / "repository_template" / ".github" / "workflows" / "quality.yml"
)


def test_workflow_runs_the_repository_quality_test():
    """El flujo debe activarse al publicar y al proponer cambios."""

    workflow = WORKFLOW_PATH.read_text(encoding="utf-8")

    assert "push:" in workflow
    assert "pull_request:" in workflow
    assert "actions/checkout@v4" in workflow
    assert "actions/setup-python@v5" in workflow
    assert "python -m venv .venv" in workflow
    assert "python -m pip install --requirement requirements.txt" in workflow
    assert "python -m unittest discover" in workflow

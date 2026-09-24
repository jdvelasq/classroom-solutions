# Uso: python3 -m pytest -q tests/test_activity.py

import subprocess
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
PRACTICE_REPOSITORY = ACTIVITY_DIR / "temp" / "pull_request_case"
EXPECTED_LINE = "- Responsable: líder de operaciones."
EXPECTED_COMMIT = "docs: define product owner"


def run_git(*arguments: str) -> str:
    # La prueba revisa el historial local actualizado después de la integración remota.

    result = subprocess.run(
        ["git", *arguments], cwd=PRACTICE_REPOSITORY, check=True, capture_output=True, text=True
    )
    return result.stdout.strip()


def test_main_contains_the_pull_request_change():
    # El resultado verificable es que main recibe el cambio revisado, no solo una rama publicada.

    assert PRACTICE_REPOSITORY.is_dir()
    assert run_git("branch", "--show-current") == "main"
    assert EXPECTED_LINE in (PRACTICE_REPOSITORY / "product_card.md").read_text(encoding="utf-8")
    assert EXPECTED_COMMIT in run_git("log", "--all", "--format=%s")

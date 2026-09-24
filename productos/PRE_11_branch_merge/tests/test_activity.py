# Uso: python3 -m pytest -q tests/test_activity.py

import subprocess
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
PRACTICE_REPOSITORY = ACTIVITY_DIR / "temp" / "branch_merge_case"
EXPECTED_LINE = "- Consumidor: equipo de mantenimiento."
EXPECTED_COMMIT = "docs: define product consumer"
EXPECTED_MERGE = "merge: add product consumer"


def run_git(*arguments: str) -> str:
    # El historial demuestra que el cambio se desarrolló en una rama y terminó integrado.

    result = subprocess.run(
        ["git", *arguments], cwd=PRACTICE_REPOSITORY, check=True, capture_output=True, text=True
    )
    return result.stdout.strip()


def test_main_contains_the_merged_change():
    # Main debe contener el resultado integrado, no solo una modificación local sin historial.

    assert PRACTICE_REPOSITORY.is_dir()
    assert run_git("branch", "--show-current") == "main"
    assert EXPECTED_LINE in (PRACTICE_REPOSITORY / "product_card.md").read_text(encoding="utf-8")
    assert run_git("log", "-1", "--format=%s") == EXPECTED_MERGE


def test_history_keeps_the_branch_commit():
    # El commit de la rama deja una evidencia recuperable de la contribución antes de la fusión.

    assert EXPECTED_COMMIT in run_git("log", "--all", "--format=%s")

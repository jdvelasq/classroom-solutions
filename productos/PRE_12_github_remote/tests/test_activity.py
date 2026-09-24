# Uso: python3 -m pytest -q tests/test_activity.py

import subprocess
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
PRACTICE_REPOSITORY = ACTIVITY_DIR / "temp" / "github_remote_case"


def run_git(*arguments: str) -> str:
    # La configuración local evidencia que el producto puede compartir su historial con un remoto.

    result = subprocess.run(
        ["git", *arguments], cwd=PRACTICE_REPOSITORY, check=True, capture_output=True, text=True
    )
    return result.stdout.strip()


def test_repository_has_a_github_origin_and_main_commit():
    # El origen remoto y el commit inicial son los requisitos locales previos al primer push.

    assert PRACTICE_REPOSITORY.is_dir()
    assert run_git("branch", "--show-current") == "main"
    assert "github.com" in run_git("remote", "get-url", "origin")
    assert run_git("log", "-1", "--format=%s") == "chore: create product card"

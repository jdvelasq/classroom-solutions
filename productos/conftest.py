"""Restaura los repositorios de referencia requeridos por las prácticas Git."""

import subprocess
from pathlib import Path

import pytest


PRODUCTOS_DIR = Path(__file__).resolve().parent
REFERENCE_REPOSITORIES = {
    "PRE_10_version_control": ("version_control_case", "version_control_case.bundle"),
    "PRE_11_branch_merge": ("branch_merge_case", "branch_merge_case.bundle"),
    "PRE_12_github_remote": ("github_remote_case", "github_remote_case.bundle"),
    "PRE_13_pull_request": ("pull_request_case", "pull_request_case.bundle"),
}


@pytest.fixture(autouse=True)
def reference_repository(request, monkeypatch, tmp_path_factory):
    # Si el estudiante ya realizó la práctica, la prueba revisa su repositorio sin modificarlo.

    activity = Path(str(request.fspath)).resolve().parents[1].name
    reference = REFERENCE_REPOSITORIES.get(activity)
    if reference is None:
        return

    repository_name, bundle_name = reference
    activity_dir = PRODUCTOS_DIR / activity
    student_repository = activity_dir / "temp" / repository_name
    if student_repository.is_dir():
        return

    # En una copia docente limpia se valida un clon temporal del artefacto versionado.

    repository = tmp_path_factory.mktemp(activity) / repository_name
    bundle = activity_dir / "data" / bundle_name
    subprocess.run(
        ["git", "clone", "--quiet", str(bundle), str(repository)],
        check=True,
    )
    if activity == "PRE_12_github_remote":
        # Un bundle preserva commits y ramas, pero no la configuración local del remoto.

        subprocess.run(
            ["git", "remote", "set-url", "origin", "https://github.com/curso/pre12-github-remote.git"],
            cwd=repository,
            check=True,
        )
    monkeypatch.setattr(request.module, "PRACTICE_REPOSITORY", repository)

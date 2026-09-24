# Uso: python3 -m pytest -q tests/test_activity.py

import subprocess
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
PRACTICE_REPOSITORY = ACTIVITY_DIR / "temp" / "version_control_case"
EXPECTED_LINE = "- Unidad de medida: unidades producidas por fábrica y día."
EXPECTED_MESSAGE = "docs: define unit of measure"


def run_git(*arguments: str) -> str:
    # La prueba consulta el historial real para verificar que el cambio quedó recuperable.

    result = subprocess.run(
        ["git", *arguments],
        cwd=PRACTICE_REPOSITORY,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def test_practice_repository_contains_the_requested_commit():
    # El cambio solo cuenta como versionado cuando existe en un repositorio y en su historial.

    assert PRACTICE_REPOSITORY.is_dir()
    assert run_git("rev-parse", "--is-inside-work-tree") == "true"
    assert run_git("log", "-1", "--format=%s") == EXPECTED_MESSAGE


def test_product_card_contains_the_defined_unit_of_measure():
    # La evidencia de Git se complementa con el contenido que motivó el cambio.

    product_card = PRACTICE_REPOSITORY / "product_card.md"
    assert product_card.is_file()
    assert EXPECTED_LINE in product_card.read_text(encoding="utf-8")

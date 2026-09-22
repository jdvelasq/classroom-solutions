"""Configuración de Pytest independiente de la ubicación de cada actividad."""

import re
from pathlib import Path

import pytest


ACTIVITY_PREFIX = re.compile(r"^(?:PRE|LAB)_[^/]+(?:/|$)")


@pytest.fixture(autouse=True)
def activity_root(request, monkeypatch):
    """Ejecuta cada prueba desde la raíz del PRE o LAB que la contiene."""
    test_file = Path(str(request.fspath)).resolve()
    if test_file.parent.name != "tests":
        return

    root = test_file.parents[1]
    monkeypatch.chdir(root)

    # Algunas pruebas históricas almacenan rutas en constantes globales que
    # comienzan con el nombre del PRE o LAB. Se reemplaza ese prefijo por la
    # ubicación real de la actividad, sin depender de su posición en el repo.
    module = request.module
    for name, value in vars(module).items():
        if not isinstance(value, str) or not ACTIVITY_PREFIX.match(value):
            continue
        relative_path = ACTIVITY_PREFIX.sub("", value)
        setattr(module, name, str(root / relative_path))

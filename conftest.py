"""Configuración de Pytest independiente de la ubicación de cada actividad."""

import re
import sys
from pathlib import Path

import pytest


ACTIVITY_PREFIX = re.compile(r"^(?:PRE|LAB)_[^/]+(?:/|$)")
ACTIVITY_DIR = re.compile(r"^(?:PRE|LAB)_")
REPO_ROOT = Path(__file__).resolve().parent
TEST_AREAS = {
    "data",
    "fundamentos",
    "descriptiva",
    "predictiva",
    "prescriptiva",
    "productos",
}

# Módulos locales (p. ej. ``src.main``) importados por cada módulo de prueba.
_LOCAL_MODULES = {}
# ``sys.path`` antes de que los módulos de prueba agreguen sus carpetas.
_ORIGINAL_SYS_PATH = list(sys.path)


def pytest_ignore_collect(collection_path, config):
    """Recolecta únicamente las carpetas de ``TEST_AREAS``."""
    path = Path(collection_path).resolve()
    try:
        relative = path.relative_to(REPO_ROOT)
    except ValueError:
        return None
    if not relative.parts or relative.parts[0] in TEST_AREAS:
        return None
    return True


def _activity_local_modules():
    """Módulos importados desde una actividad con un nombre no único.

    Cada actividad agrega su carpeta a ``sys.path`` e importa paquetes con
    nombres genéricos (``src``, ``notebook_runner``...). Si quedan en
    ``sys.modules``, la siguiente actividad reutilizaría los de la anterior.
    """
    local = {}
    for name, module in list(sys.modules.items()):
        if name.split(".")[0] in TEST_AREAS:
            continue
        # Los paquetes de espacio de nombres no tienen ``__file__``.
        locations = [getattr(module, "__file__", None)]
        locations += list(getattr(module, "__path__", None) or [])
        if any(_inside_activity(location) for location in locations if location):
            local[name] = module
    return local


def _inside_activity(location):
    try:
        relative = Path(location).resolve().relative_to(REPO_ROOT)
    except ValueError:
        return False
    return any(ACTIVITY_DIR.match(part) for part in relative.parts)


def _swap_local_modules(modules):
    for name in _activity_local_modules():
        del sys.modules[name]
    sys.modules.update(modules)


def pytest_collectstart(collector):
    """Importa cada módulo de prueba sin módulos locales de otra actividad."""
    if isinstance(collector, pytest.Module):
        # Una carpeta de otra actividad en ``sys.path`` podría ocultar el
        # ``src`` propio (sobre todo si este no tiene ``__init__.py``).
        sys.path[:] = [
            entry for entry in sys.path
            if entry in _ORIGINAL_SYS_PATH or not _inside_activity(entry)
        ]
        _swap_local_modules({})


def pytest_collectreport(report):
    """Guarda los módulos locales que importó el módulo de prueba."""
    if report.nodeid.endswith(".py"):
        _LOCAL_MODULES[report.nodeid] = _activity_local_modules()


@pytest.fixture(autouse=True)
def activity_root(request, monkeypatch):
    """Ejecuta cada prueba desde la raíz del PRE o LAB que la contiene."""
    module_nodeid = request.node.nodeid.split("::")[0]
    _swap_local_modules(_LOCAL_MODULES.get(module_nodeid, {}))

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

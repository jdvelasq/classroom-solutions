"""Verifica que el PRE declare tareas, flujo y política de reintento."""

from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]


def test_prefect_flow_defines_observable_tasks():
    """La orquestación debe separar las tareas y expresar una recuperación básica."""

    source = (PRE_DIR / "src" / "main.py").read_text(encoding="utf-8")

    assert "from prefect import flow, task" in source
    assert "@task(retries=1)" in source
    assert "@flow" in source
    assert "def operations_flow():" in source

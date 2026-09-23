"""Ejecuta en orden las celdas de código de un notebook docente local."""

import os
from pathlib import Path

import nbformat


def execute_notebook(path: Path) -> None:
    """Ejecuta un notebook desde su propia carpeta, sin estado oculto."""
    path = path.resolve()
    notebook = nbformat.read(path, as_version=4)
    previous_directory = Path.cwd()
    try:
        os.chdir(path.parent)
        namespace = {"__name__": "__main__"}
        for cell in notebook.cells:
            if cell.cell_type == "code":
                exec(cell.source, namespace)
    finally:
        os.chdir(previous_directory)

"""Conteo de palabras con las etapas explícitas de MapReduce."""

from pathlib import Path
import shutil
import string


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ACTIVITY_DIR / "data"
INPUT_DIR = ACTIVITY_DIR / "temp" / "input"
OUTPUT_DIR = ACTIVITY_DIR / "temp" / "output"


def run_word_count() -> Path:
    """
    Construya un conteo de palabras con las etapas de MapReduce.

    Copie los textos de ``data/`` a ``temp/input/``. Después, lea cada línea,
    convierta el texto a minúsculas, elimine puntuación y genere pares
    ``(palabra, 1)``. Ordene los pares por palabra, reduzca sumando los valores
    de cada clave y escriba el resultado tabulado en
    ``temp/output/part-00000``. Cree también el marcador
    ``temp/output/_SUCCESS``.

    ``temp/`` contiene resultados temporales de ejecución y no constituye una
    entrega persistente del taller.
    """
    if INPUT_DIR.exists():
        shutil.rmtree(INPUT_DIR)
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    INPUT_DIR.mkdir(parents=True)
    OUTPUT_DIR.mkdir(parents=True)

    for source_file in sorted(DATA_DIR.glob("*.txt")):
        shutil.copyfile(source_file, INPUT_DIR / source_file.name)

    records = []
    for input_file in sorted(INPUT_DIR.glob("*.txt")):
        with input_file.open(encoding="utf-8") as file:
            records.extend(file.readlines())

    pairs = []
    for line in records:
        clean_line = line.lower().translate(str.maketrans("", "", string.punctuation))
        pairs.extend((word, 1) for word in clean_line.split())

    sorted_pairs = sorted(pairs)
    counts = []
    for word, value in sorted_pairs:
        if counts and counts[-1][0] == word:
            counts[-1] = (word, counts[-1][1] + value)
        else:
            counts.append((word, value))

    output_file = OUTPUT_DIR / "part-00000"
    with output_file.open("w", encoding="utf-8") as file:
        for word, count in counts:
            file.write(f"{word}\t{count}\n")
    (OUTPUT_DIR / "_SUCCESS").touch()

    return output_file
    # raise NotImplementedError


if __name__ == "__main__":
    run_word_count()

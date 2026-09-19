# pylint: disable=import-outside-toplevel
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from pprint import pprint

import pandas as pd  # type: ignore


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    df = pd.read_csv(
        "files/input/data.csv",
        names=["col1", "col2", "col3", "col4", "col5"],
        sep="\t",
    )
    result = int(df["col2"].sum())

    print("--------------- Pregunta 01 ---------------")
    pprint(result)
    print()


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

    df = pd.read_csv(
        "files/input/data.csv",
        names=["col1", "col2", "col3", "col4", "col5"],
        sep="\t",
    )

    result = df["col1"].value_counts()
    result = result.sort_index()
    result = result.reset_index().values
    result = result.tolist()
    result = [(str(x[0]), x[1]) for x in result]

    print("--------------- Pregunta 02 ---------------")
    pprint(result)
    print()


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    df = pd.read_csv(
        "files/input/data.csv",
        names=["col1", "col2", "col3", "col4", "col5"],
        sep="\t",
    )

    result = df.groupby("col1")["col2"].sum()
    result = result.sort_index()
    result = result.reset_index().values
    result = result.tolist()
    result = [(str(x[0]), x[1]) for x in result]

    print("--------------- Pregunta 03 ---------------")
    pprint(result)
    print()


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """

    df = pd.read_csv(
        "files/input/data.csv",
        names=["col1", "col2", "col3", "col4", "col5"],
        sep="\t",
    )
    df["col3"] = df["col3"].str[5:7]
    result = df["col3"].value_counts().sort_index()
    result = [(i, int(v)) for i, v in zip(result.index, result.values)]

    print("--------------- Pregunta 04 ---------------")
    pprint(result)
    print()


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

    df = pd.read_csv(
        "files/input/data.csv",
        names=["col1", "col2", "col3", "col4", "col5"],
        sep="\t",
    )
    r = df.groupby("col1")["col2"].agg(["max", "min"])

    result = [(a, b, c) for a, b, c in zip(r.index, r["max"], r["min"])]

    print("--------------- Pregunta 05 ---------------")
    pprint(result)
    print()


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """

    df = pd.read_csv(
        "files/input/data.csv",
        names=["col1", "col2", "col3", "col4", "col5"],
        sep="\t",
    )

    df = df[["col5"]]
    df["col5"] = df["col5"].str.split(",")
    df = df.explode("col5")
    df["col6"] = df["col5"].str.split(":").str[1]
    df["col6"] = df["col6"].astype(int)
    df["col5"] = df["col5"].str.split(":").str[0]
    r = df.groupby("col5").agg({"col6": ["min", "max"]})
    r.columns = ["min", "max"]

    result = [(a, b, c) for a, b, c in zip(r.index, r["min"], r["max"])]

    print("--------------- Pregunta 06 ---------------")
    pprint(result)
    print()


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """

    df = pd.read_csv(
        "files/input/data.csv",
        names=["col1", "col2", "col3", "col4", "col5"],
        sep="\t",
    )

    r = df[["col1", "col2"]].groupby("col2").agg(list)

    result = [(a, b) for a, b in zip(r.index, r["col1"])]

    print("--------------- Pregunta 07 ---------------")
    pprint(result)
    print()


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

    df = pd.read_csv(
        "files/input/data.csv",
        names=["col1", "col2", "col3", "col4", "col5"],
        sep="\t",
    )

    r = df[["col1", "col2"]].groupby("col2").agg(list)
    r["col1"] = r["col1"].apply(lambda x: sorted(list(set(x))))

    result = [(a, b) for a, b in zip(r.index, r["col1"])]

    print("--------------- Pregunta 08 ---------------")
    pprint(result)
    print()


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """

    df = pd.read_csv(
        "files/input/data.csv",
        names=["col1", "col2", "col3", "col4", "col5"],
        sep="\t",
    )
    df = df[["col5"]]
    df["col5"] = df["col5"].str.split(",")
    df = df.explode("col5")
    df["col5"] = df["col5"].str.split(":").str[0]
    r = df["col5"].value_counts().to_dict()

    result = {a: r[a] for a in sorted(r.keys())}

    print("--------------- Pregunta 09 ---------------")
    pprint(result)
    print()


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """

    df = pd.read_csv(
        "files/input/data.csv",
        names=["col1", "col2", "col3", "col4", "col5"],
        sep="\t",
    )
    df = df[["col1", "col4", "col5"]]
    df["col4"] = df["col4"].str.split(",")
    df["col4"] = df["col4"].map(len)
    df["col5"] = df["col5"].str.split(",")
    df["col5"] = df["col5"].map(len)
    result = [(a, b, c) for a, b, c in zip(df["col1"], df["col4"], df["col5"])]

    print("--------------- Pregunta 10 ---------------")
    pprint(result)
    print()


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """

    df = pd.read_csv(
        "files/input/data.csv",
        names=["col1", "col2", "col3", "col4", "col5"],
        sep="\t",
    )
    df = df[["col4", "col2"]]
    df["col4"] = df["col4"].str.split(",")
    df = df.explode("col4")
    r = df.groupby("col4").agg({"col2": "sum"})
    result = {a: b for a, b in zip(sorted(r.index), r["col2"])}

    print("--------------- Pregunta 11 ---------------")
    pprint(result)
    print()


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """

    df = pd.read_csv(
        "files/input/data.csv",
        names=["col1", "col2", "col3", "col4", "col5"],
        sep="\t",
    )
    df = df[["col1", "col5"]]
    df["col5"] = df["col5"].str.split(",")
    df["col5"] = df["col5"].map(lambda x: [i.split(":") for i in x])
    df["col5"] = df["col5"].map(lambda x: [int(i[1]) for i in x])
    df["col5"] = df["col5"].map(sum)
    result = df.groupby("col1").agg({"col5": "sum"})
    result = {a: b for a, b in zip(sorted(result.index), result["col5"])}

    print("--------------- Pregunta 12 ---------------")
    pprint(result)
    print()


def run():
    """Print all answers"""

    pregunta_01()
    pregunta_02()
    pregunta_03()
    pregunta_04()
    pregunta_05()
    pregunta_06()
    pregunta_07()
    pregunta_08()
    pregunta_09()
    pregunta_10()
    pregunta_11()
    pregunta_12()


run()

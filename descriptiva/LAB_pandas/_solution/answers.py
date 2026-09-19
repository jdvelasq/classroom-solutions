"""Homework answers."""

from pprint import pprint

import pandas as pd  # type: ignore


def answer_pregunta_01():
    """Answer"""

    tbl0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    result = len(tbl0)

    print("------------ Pregunta 01 ------------")
    pprint(result)
    print()


def answer_pregunta_02():
    """Answer"""

    tbl0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    result = len(tbl0.columns)

    print("------------ Pregunta 02 ------------")
    pprint(result)
    print()


def answer_pregunta_03():
    """Answer"""

    tbl0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    result = tbl0.c1.value_counts().sort_index()

    print("------------ Pregunta 03 ------------")
    pprint(result)
    print()


def answer_pregunta_04():
    """Answer"""

    tbl0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    tbl0 = tbl0[["c1", "c2"]]
    result = tbl0.groupby("c1").mean()["c2"]

    print("------------ Pregunta 04 ------------")
    pprint(result)
    print()


def answer_pregunta_05():
    """Answer"""

    tbl0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    result = tbl0.groupby("c1").max()["c2"]

    print("------------ Pregunta 05 ------------")
    pprint(result)
    print()


def answer_pregunta_06():
    """Answer"""

    tbl1 = pd.read_csv("files/input/tbl1.tsv", sep="\t")
    result = tbl1.c4.str.upper().drop_duplicates().sort_values().tolist()

    print("------------ Pregunta 06 ------------")
    pprint(result)
    print()


def answer_pregunta_07():
    """Answer"""

    tbl0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    result = tbl0.groupby("c1").sum()["c2"].sort_index()

    print("------------ Pregunta 07 ------------")
    pprint(result)
    print()


def answer_pregunta_08():
    """Answer"""

    tbl0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    r = tbl0.copy()
    r["suma"] = r["c0"] + r["c2"]
    result = r

    print("------------ Pregunta 08 ------------")
    pprint(result)
    print()


def answer_pregunta_09():
    """Answer"""

    tbl0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    r = tbl0.copy()
    r["year"] = r["c3"].str.split("-").str[0]
    result = r

    print("------------ Pregunta 09 ------------")
    pprint(result)
    print()


def answer_pregunta_10():
    """Answer"""

    tbl0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    r = tbl0[["c1", "c2"]].groupby("c1").agg(list)
    r["c2"] = r["c2"].apply(lambda x: ":".join([str(i) for i in sorted(x)]))
    result = r

    print("------------ Pregunta 10 ------------")
    pprint(result)
    print()


def answer_pregunta_11():
    """Answer"""

    tbl1 = pd.read_csv("files/input/tbl1.tsv", sep="\t")
    r = tbl1.copy()
    r = r.groupby("c0", as_index=False).agg(list)
    r["c4"] = r["c4"].apply(lambda x: ",".join([str(i) for i in sorted(x)]))
    result = r

    print("------------ Pregunta 11 ------------")
    pprint(result)
    print()


def answer_pregunta_12():
    """Answer"""

    tbl2 = pd.read_csv("files/input/tbl2.tsv", sep="\t")
    r = tbl2.copy()
    r["c5b"] = r["c5b"].astype(str)
    r["c5"] = r["c5a"] + ":" + r["c5b"]
    r = r.groupby("c0", as_index=False).agg(list)
    r["c5"] = r["c5"].apply(lambda x: ",".join([str(i) for i in sorted(x)]))
    r = r[["c0", "c5"]]
    result = r

    print("------------ Pregunta 12 ------------")
    pprint(result)
    print()


def answer_pregunta_13():
    """Answer"""

    tbl0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    tbl2 = pd.read_csv("files/input/tbl2.tsv", sep="\t")
    r = tbl0.merge(tbl2, on="c0")
    r = r.groupby("c1").sum()["c5b"]
    result = r

    print("------------ Pregunta 13 ------------")
    pprint(result)
    print()


def run():
    """Run all answers."""
    answer_pregunta_01()
    answer_pregunta_02()
    answer_pregunta_03()
    answer_pregunta_04()
    answer_pregunta_05()
    answer_pregunta_06()
    answer_pregunta_07()
    answer_pregunta_08()
    answer_pregunta_09()
    answer_pregunta_10()
    answer_pregunta_11()
    answer_pregunta_12()
    answer_pregunta_13()


if __name__ == "__main__":
    run()

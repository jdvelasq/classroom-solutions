"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import os

import matplotlib.pyplot as plt
import pandas as pd  # type: ignore


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `news.png` que está ubicado en la raíz de este
    repo.

    El gráfico debe salvarse al archivo `news.png` en la carpeta `plots`.
    Es decir, su ubicación es `plots/news.png`.

    """

    df = pd.read_csv("files/input/news.csv", index_col=0)
    plt.Figure()

    colors = {
        "Television": "dimgray",
        "Newspaper": "grey",
        "Internet": "tab:blue",
        "Radio": "lightgrey",
    }

    linewidths = {
        "Television": 2,
        "Newspaper": 2,
        "Internet": 3,
        "Radio": 2,
    }

    zorder = {
        "Television": 1,
        "Newspaper": 1,
        "Internet": 2,
        "Radio": 1,
    }

    for col in df.columns:
        plt.plot(
            df[col],
            color=colors[col],
            linewidth=linewidths[col],
            zorder=zorder[col],
        )

    plt.suptitle("How people get their news", fontsize=16)
    plt.title(
        "An increasing proportion cite the internet as their primary news source",
        fontdict={"fontsize": 8},
    )

    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    # add year values to the x-axis
    plt.xticks(
        ticks=df.index,
        labels=df.index,
        ha="center",
    )

    # add points to the init of each line
    for col in df.columns:
        first_year = df.index[0]
        last_year = df.index[-1]
        plt.scatter(
            x=first_year,
            y=df[col][first_year],
            color=colors[col],
            zorder=zorder[col],
        )

        plt.text(
            first_year - 0.2,
            df[col][first_year],
            col + " " + str(df[col][first_year]) + "%",
            ha="right",
            va="center",
            color=colors[col],
        )

        plt.scatter(
            x=last_year,
            y=df[col][last_year],
            color=colors[col],
        )

        plt.text(
            last_year + 0.2,
            df[col][last_year],
            str(df[col][last_year]) + "%",
            ha="left",
            va="center",
            color=colors[col],
        )

    plt.tight_layout()
    plt.savefig("news.png")

    if not os.path.exists("plots"):
        os.makedirs("plots", exist_ok=True)
    plt.savefig("plots/news.png")

"""Demuestra una selección reproducible mediante una semilla declarada."""

import random


def select_sample(seed):
    """La semilla declarada permite repetir una decisión aleatoria al investigar un resultado."""

    generator = random.Random(seed)
    return generator.sample(["factory-1", "factory-2", "factory-3", "factory-4"], 2)

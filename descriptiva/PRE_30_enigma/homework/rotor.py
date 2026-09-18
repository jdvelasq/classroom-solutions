"""
Implementa el rotor de la máquina Enigma. El rotor es un componente que realiza
un mapeo interno fijo entre las 26 letras del alfabeto. En la Enigma militar
existían cinco rotores. Cada rotor tenía un cableado interno distinto y uno o
más puntos de muesca que determinaban cuándo debía avanzar el siguiente rotor,
generando el efecto de “odómetro”. El mapeo no podia ser cambiado por el
usuario.

El operador podía seleccionar el orden en el que se montaban los rotores,
definir su posición inicialy ajustar la configuración del
anillo interno (Ringstellung). Estas variaciones, combinadas con los demás
componentes de la máquina, incrementaban de forma exponencial el espacio de
claves posibles.

A diferencia del plugboard y del reflector, cada rotor gira una posición con
cada pulsación de tecla, alterando dinámicamente el recorrido de la señal y
produciendo asi una sustitución distinta en cada paso.

"""

import random

from homework.constants import LETTERS


def permute_letters(seed):
    """Crea una permutación aleatoria de la cadena dada."""

    random.seed(seed)
    return "".join(random.sample(LETTERS, len(LETTERS)))


ROTOR_1 = permute_letters(seed=10)
ROTOR_2 = permute_letters(seed=20)
ROTOR_3 = permute_letters(seed=30)
ROTOR_4 = permute_letters(seed=40)
ROTOR_5 = permute_letters(seed=50)


def apply_rotor_forward(letter, rotor, offset):
    """Aplica el rotor hacia adelante a una letra dada."""

    index = LETTERS.index(letter)
    index = index + offset
    if index >= len(LETTERS):
        index = index - len(LETTERS)

    return rotor[index]


def apply_rotor_backward(letter, rotor, offset):
    """Aplica el rotor hacia atrás a una letra dada."""

    index = rotor.index(letter)
    index = index - offset
    if index < 0:
        index = index + len(LETTERS)

    return LETTERS[index]


def apply_rotation(machine):
    """Aplica la rotación a la máquina Enigma."""

    machine["offsets"][0] += 1

    for i in range(len(machine["offsets"])):

        if machine["offsets"][i] >= len(LETTERS):
            machine["offsets"][i] = 0
            if i < len(machine["offsets"]) - 1:
                machine["offsets"][i + 1] += 1

    return machine

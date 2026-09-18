"""Implementa la máquina Enigma."""

from homework.constants import LETTERS
from homework.plugboard import apply_plugboard
from homework.reflector import apply_reflector
from homework.rotor import apply_rotation, apply_rotor_backward, apply_rotor_forward


def make_enigma_machine(rotors, reflector, plugboard):
    """Crea una instancia de la máquina Enigma con los rotores, reflector y plugboard dados."""

    return {
        "rotors": rotors,
        "reflector": reflector,
        "plugboard": plugboard,
    }


def initialize_enigma_machine(machine, offsets=None):
    """Inicializa la máquina Enigma con los offsets dados para los rotores."""

    if offsets is None:
        offsets = [0] * len(machine["rotors"])

    machine["offsets"] = [LETTERS.index(letter) for letter in offsets]
    return machine


def apply_enigma_machine(letter, machine):
    """Aplica la máquina Enigma a una letra dada."""

    letter = apply_plugboard(letter, machine["plugboard"])

    machine = apply_rotation(machine)

    for rotor, offset in zip(machine["rotors"], machine["offsets"]):
        letter = apply_rotor_forward(letter, rotor, offset)

    letter = apply_reflector(letter, machine["reflector"])

    for rotor, offset in zip(reversed(machine["rotors"]), reversed(machine["offsets"])):
        letter = apply_rotor_backward(letter, rotor, offset)

    letter = apply_plugboard(letter, machine["plugboard"])

    return letter

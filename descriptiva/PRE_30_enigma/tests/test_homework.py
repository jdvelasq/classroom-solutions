"""Autograding script."""

# pylint: disable=broad-exception-raised


from homework.constants import LETTERS
from homework.enigma_machine import (
    apply_enigma_machine,
    initialize_enigma_machine,
    make_enigma_machine,
)
from homework.plugboard import apply_plugboard, make_plugboard
from homework.reflector import REFLECTOR_A, REFLECTOR_B, REFLECTOR_C, apply_reflector
from homework.rotor import (
    ROTOR_1,
    ROTOR_2,
    ROTOR_3,
    ROTOR_4,
    ROTOR_5,
    apply_rotation,
    apply_rotor_backward,
    apply_rotor_forward,
)


def test_plugboard():

    mapping = make_plugboard(seed=42, n=13)

    assert len(mapping) == len(LETTERS)
    assert set(mapping) == set(LETTERS)
    assert mapping != LETTERS

    for letter in LETTERS:
        mapped_letter = apply_plugboard(letter, mapping)
        assert apply_plugboard(mapped_letter, mapping) == letter


def test_reflector():

    assert REFLECTOR_A != REFLECTOR_B
    assert REFLECTOR_A != REFLECTOR_C
    assert REFLECTOR_B != REFLECTOR_C

    for letter in LETTERS:
        reflected_letter = apply_reflector(letter, REFLECTOR_A)
        assert apply_reflector(reflected_letter, REFLECTOR_A) == letter


def test_rotor():

    assert ROTOR_1 != ROTOR_2
    assert ROTOR_1 != ROTOR_3
    assert ROTOR_1 != ROTOR_4
    assert ROTOR_1 != ROTOR_5
    assert ROTOR_2 != ROTOR_3
    assert ROTOR_2 != ROTOR_4
    assert ROTOR_2 != ROTOR_5
    assert ROTOR_3 != ROTOR_4
    assert ROTOR_3 != ROTOR_5
    assert ROTOR_4 != ROTOR_5

    for letter in LETTERS:
        rotated_letter = apply_rotor_forward(letter, ROTOR_1, 0)
        assert apply_rotor_backward(rotated_letter, ROTOR_1, 0) == letter

    for letter in LETTERS:
        rotated_letter = apply_rotor_forward(letter, ROTOR_1, 5)
        assert apply_rotor_backward(rotated_letter, ROTOR_1, 5) == letter


def test_rotation():

    machine = {"offsets": [0, 0, 0]}
    machine = apply_rotation(machine)
    assert machine["offsets"] == [1, 0, 0]

    machine = {"offsets": [1, 0, 0]}
    machine = apply_rotation(machine)
    assert machine["offsets"] == [2, 0, 0]

    machine = {"offsets": [25, 0, 0]}
    machine = apply_rotation(machine)
    assert machine["offsets"] == [0, 1, 0]

    machine = {"offsets": [25, 1, 0]}
    machine = apply_rotation(machine)
    assert machine["offsets"] == [0, 2, 0]

    machine = {"offsets": [25, 25, 0]}
    machine = apply_rotation(machine)
    assert machine["offsets"] == [0, 0, 1]

    machine = {"offsets": [22, 23, 24]}
    machine = apply_rotation(machine)
    assert machine["offsets"] == [23, 23, 24]

    machine = {"offsets": [25, 25, 25]}
    machine = apply_rotation(machine)
    assert machine["offsets"] == [0, 0, 0]

    machine = {"offsets": [25, 25, 25]}
    machine = apply_rotation(machine)
    assert machine["offsets"] == [0, 0, 0]


def test_machine():

    machine = make_enigma_machine(
        rotors=[ROTOR_1, ROTOR_2, ROTOR_3],
        reflector=REFLECTOR_A,
        plugboard=make_plugboard(seed=42, n=8),
    )

    # Chequea una letra individual A <-> R

    machine = initialize_enigma_machine(machine, offsets=["A", "A", "A"])
    letter = apply_enigma_machine("A", machine)
    assert letter == "P"

    machine = initialize_enigma_machine(machine, offsets=["A", "A", "A"])
    letter = apply_enigma_machine("P", machine)
    assert letter == "A"

    # Chequea una secuencia de letras

    machine = initialize_enigma_machine(machine, offsets=["A", "A", "A"])
    letter = apply_enigma_machine("A", machine)
    assert letter == "P"
    letter = apply_enigma_machine("B", machine)
    assert letter == "K"
    letter = apply_enigma_machine("B", machine)
    assert letter == "Y"

    assert machine["offsets"] == [3, 0, 0]

    machine = initialize_enigma_machine(machine, offsets=["A", "A", "A"])
    letter = apply_enigma_machine("P", machine)
    assert letter == "A"
    letter = apply_enigma_machine("K", machine)
    assert letter == "B"
    letter = apply_enigma_machine("Y", machine)
    assert letter == "B"


#

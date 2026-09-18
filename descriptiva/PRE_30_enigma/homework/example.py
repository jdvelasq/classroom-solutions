"""Ejemplo del uso de la máquina Enigma."""

from homework.enigma_machine import (
    apply_enigma_machine,
    initialize_enigma_machine,
    make_enigma_machine,
)
from homework.plugboard import make_plugboard
from homework.reflector import REFLECTOR_B
from homework.rotor import (
    ROTOR_1,
    ROTOR_3,
    ROTOR_5,
)

#
# El libro de claves diario especifica:
# - El plugboard
# - Los rotores usados y su orden (note que son 5 disponibles)
# - El reflector usado (A, B o C)
# - La posición inicial de los rotores, por ejmemplo "B", "Z", "K"
#   Siempre es la posicion inicial para cada mensaje
#


def process_message(message, encrypt=True):
    """Encripta un mensaje usando la máquina Enigma dada."""

    machine = make_enigma_machine(
        plugboard=make_plugboard(seed=42, n=8),
        rotors=[
            ROTOR_1,
            ROTOR_5,
            ROTOR_3,
        ],
        reflector=REFLECTOR_B,
    )

    machine = initialize_enigma_machine(machine, offsets=["B", "Z", "K"])

    #
    # Para cada mensaje se definia una clave inicial de tres letras
    #
    key = message[:3]
    message = message[3:]

    key_0 = apply_enigma_machine(key[0], machine)
    key_1 = apply_enigma_machine(key[1], machine)
    key_2 = apply_enigma_machine(key[2], machine)

    #
    # con las tres letras se reposiiconaban los rotores
    #
    if encrypt:
        machine = initialize_enigma_machine(machine, offsets=[key[0], key[1], key[2]])
    else:
        machine = initialize_enigma_machine(machine, offsets=[key_0, key_1, key_2])

    #
    # se codificaba el mensaje
    #
    encrypted_message = key_0 + key_1 + key_2
    for letter in message:
        encrypted_letter = apply_enigma_machine(letter, machine)
        encrypted_message += encrypted_letter

    return encrypted_message


if __name__ == "__main__":

    message = "ABCHOLAMUNDOCRUEL"

    encrypted_message = process_message(message, encrypt=True)
    decrypted_message = process_message(encrypted_message, encrypt=False)

    print()
    print(f"     Mensaje original : {' '.join(list(message))}")
    print(f"   Mensaje encriptado : {' '.join(list(encrypted_message))}")
    print(f"Mensaje desencriptado : {' '.join(list(decrypted_message))}")
    print()

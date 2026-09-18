"""
Implementa el reflector de la máquina Enigma. El reflector es un componente que
realiza un mapeo simétrico entre pares de letras (por ejemplo, B <-> Z). A
diferencia del plugboard, el reflector remapea la totalidad del alfabeto,
asegurando que cada letra siempre se intercambie exactamente por otra distinta.

En la maquina enigma existian tres reflectores: A, B y C. Cada uno de estos
reflectores realiza un mapeo diferente, proporcionando así una capa adicional
de complejidad al sistema de encriptación.

El libro de claves diario especificaba qué reflector debía utilizarse en cada
dia.

"""

from homework.plugboard import apply_plugboard, make_plugboard

REFLECTOR_A = make_plugboard(seed=1, n=13)
REFLECTOR_B = make_plugboard(seed=2, n=13)
REFLECTOR_C = make_plugboard(seed=3, n=13)


def apply_reflector(letter, reflector):
    """Aplica el reflector a una letra dada."""

    return apply_plugboard(letter, reflector)

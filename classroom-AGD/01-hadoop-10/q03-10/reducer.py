#
# Pregunta
# ===========================================================================
#
# Escriba un job de hadoop (en Python) que ordene el archivo `data.csv` por
# la segunda columna, de menor a mayor.
#
import sys
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
for line in sys.stdin:
    _, val = line.split("\t") 
    val = val[:-1] if val[-1] == '\n' else val
    sys.stdout.write("{}\n".format(val))

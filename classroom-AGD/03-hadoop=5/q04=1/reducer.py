#
# Pregunta
# ===========================================================================
#
# Escriba un job de hadoop (en Python) que ordene el archivo `data.csv`  por 
# letra y valor (3ra columna).
#
import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
for line in sys.stdin:
    line = line.replace('\n', '')
    key, val = line.split("\t") 
    sys.stdout.write("{}\n".format(val))    
#
# Pregunta
# ===========================================================================
#
# Escriba un job de hadoop (en Python) que ordene el archivo `data.csv` por
# la segunda columna, de menor a mayor.
#
import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
for line in sys.stdin:
    k = line.split(',')[1]
    k = k[:-1] if k[-1] == '\n' else k
    line = line[:-1] if line[-1] == '\n' else line
    sys.stdout.write("{}\t{}\n".format( k, line))
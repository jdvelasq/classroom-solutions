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
    row = line.split(' ')
    row = [x for x in row if x != '']
    key = row[0] + row[2].rjust(5, '0')
    sys.stdout.write("{}---{}\n".format(key, line))

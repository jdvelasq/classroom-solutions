#
# Pregunta
# ===========================================================================
#
# Escriba un job de hadoop (en Python) que obtenga los 5 registros con 
# valores más pequeños en la tercera columna del  archivo `data.csv`.  
#
import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
for i, line in enumerate(sys.stdin):
    line = line.replace('\n', '')
    key, val = line.split("\t") 
    sys.stdout.write("{}\n".format(val)) 
    if i > 4:
        break
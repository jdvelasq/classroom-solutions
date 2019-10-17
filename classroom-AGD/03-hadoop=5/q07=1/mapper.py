#
# Pregunta
# ===========================================================================
#
# Escriba un job de hadoop (en Python) que obtenga las letras asociadas 
# (columna 2) a cada clave (columna 1) del  archivo `data.csv`.  
#
import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
for line in sys.stdin:
    line = line.replace('\n', '')
    key, val = line.split("\t") 
    val = val.split(',')
    for value in val:
        sys.stdout.write("{}\t{}\n".format(value.strip(), key.strip()))
        
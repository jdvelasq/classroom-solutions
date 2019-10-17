#
# Pregunta
# ===========================================================================
#
# Escriba un job de hadoop (en Python) que compute los valores máximo y 
# mínimo de la tercera columna por letra, para el archivo `data.csv`.
#
import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
curkey = None
total = 0
for line in sys.stdin:
    key, values = line.split("\t") 
    values = values.split(',')
    a = float(values[0])
    b = float(values[1])
    if key == curkey: 
        maximum = max(maximum, a)
        minimum = min(minimum, b)
    else:
        if curkey is not None:
            sys.stdout.write("{}\t{}\t{}\n".format(curkey, maximum, minimum))     
        curkey = key
        maximum = a
        minimum = b
sys.stdout.write("{}\t{}\t{}\n".format(curkey, maximum, minimum))
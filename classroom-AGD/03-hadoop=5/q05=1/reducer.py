#
# Pregunta
# ===========================================================================
#
# Escriba un job de hadoop (en Python) que compute la suma y el promedio de 
# la tercera columna por letra del  archivo `data.csv`.  
#
import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
curkey = None
suma = 0
cant = 0
for line in sys.stdin:
    key, values = line.split("\t") 
    values = values.split(',')
    a = float(values[0])
    b = float(values[1])
    if key == curkey: 
        suma += a 
        cant += b
    else:
        if curkey is not None:
            sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, suma / cant)) 
        curkey = key
        suma = a
        cant = b
sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, suma / cant)) 
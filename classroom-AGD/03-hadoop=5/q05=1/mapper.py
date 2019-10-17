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
for line in sys.stdin:
    line = line.replace('\n', '')
    line = line.split(' ')
    line = [x for x in line if x != '']
    sys.stdout.write("{}\t{},1\n".format(line[0], line[2]))
#
# Pregunta
# =============================================================================
#
# El arachivo credit.csv contiene 1000 registros sobre aprobación de creditos. 
# El archivo codebook.txt contiene la descripcion de los 20 atributos que 
# recopilan la información sobre el credito y la salud financiera del 
# solicitante. 
#
# Escriba el codigo del mapper y el reducer que implemente un job de hadoop 
# (en Python) que compute la cantidad de registros por cada tipo del atributo 
# `credit_history`.
#
import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

for line in sys.stdin:
    sys.stdout.write("{}\t1\n".format( line.split(',')[2] ))

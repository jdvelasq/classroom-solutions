#
# Pregunta
# =============================================================================
#
# El arachivo credit.csv contiene 1000 registros sobre aprobación de creditos. 
# El archivo codebook.txt contiene la descripcion de los 20 atributos que 
# recopilan la información sobre el credito y la salud financiera del 
# solicitante. 
#  
# Escriba un job de hadoop (en Python) que compute el valor máximo 
# del monto (`amount`) del crédito que ha solicitado una persona 
# por cada tipo de destino (`purpose`) del crédito.
#
import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
for line in sys.stdin:
    sys.stdout.write("{}\t{}\n".format( line.split(',')[3], line.split(',')[4] ))

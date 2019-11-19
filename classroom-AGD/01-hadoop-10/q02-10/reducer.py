#
# Pregunta
# =============================================================================
#
# El archivo credit.csv contiene 1000 registros sobre aprobación de creditos. 
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
#  >>> Escriba el codigo del reducer a partir de este punto <<<
#

curkey = None
total = 0

for line in sys.stdin:
    
    key, val = line.split("\t") 
    val = int(val)
    
    if key == curkey: 
        total = max(total, val)  
    else:
        if curkey is not None:
            sys.stdout.write("{}\t{}\n".format(curkey, total)) 
        
        curkey = key
        total = val

sys.stdout.write("{}\t{}\n".format(curkey, total))
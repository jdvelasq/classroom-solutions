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
curkey = None
docs = []
for line in sys.stdin:
    line = line.replace('\n', '')
    key, val = line.split("\t") 
    if key == curkey: 
        docs.append(val)
    else:
        if curkey is not None:
            sys.stdout.write("{}\t{}\n".format(curkey, ','.join(docs)))             
        curkey = key
        docs = [val]
sys.stdout.write("{}\t{}\n".format(curkey, ','.join(docs))) 
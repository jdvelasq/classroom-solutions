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
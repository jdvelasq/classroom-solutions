import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
for line in sys.stdin:
    line = line.replace('\n', '')
    key, val = line.split("---") 
    sys.stdout.write("{}\n".format(val))     

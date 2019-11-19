import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
for line in sys.stdin:
    sys.stdout.write("{}\t{}\n".format( line.split(',')[3], line.split(',')[4] ))

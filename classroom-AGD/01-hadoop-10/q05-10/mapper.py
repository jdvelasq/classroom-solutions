import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
for line in sys.stdin:
    month = line.split(' ')
    month = [x for x in month if x != ''][1]
    month = month.split('-')[1]
    sys.stdout.write("{}\t1\n".format(month))
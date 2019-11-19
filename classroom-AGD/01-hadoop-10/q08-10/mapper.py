import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
for line in sys.stdin:
    line = line.replace('\n', '')
    line = line.split(' ')
    line = [x for x in line if x != '']
    sys.stdout.write("{}\t{},1\n".format(line[0], line[2]))
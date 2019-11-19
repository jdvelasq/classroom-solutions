import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
for line in sys.stdin:
    line = line.replace('\n', '')
    row = line.split(' ')
    row = [x for x in row if x != '']
    key = row[2].rjust(3, '0')
    sys.stdout.write("{}\t{}\n".format(key, line))
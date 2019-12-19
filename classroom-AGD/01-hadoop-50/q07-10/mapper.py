import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
for line in sys.stdin:
    line = line.replace('\n', '')
    line = line.replace('\t', '')
    row = line.split(' ')
    row = [x for x in row if x != '']
    key = row[0] + row[2].rjust(5, '0')
    sys.stdout.write("{}---{}\n".format(key, line))

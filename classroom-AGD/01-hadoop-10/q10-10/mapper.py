import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
for line in sys.stdin:
    line = line.replace('\n', '')
    key, val = line.split("\t") 
    val = val.split(',')
    for value in val:
        sys.stdout.write("{}\t{}\n".format(value.strip(), key.strip()))
        
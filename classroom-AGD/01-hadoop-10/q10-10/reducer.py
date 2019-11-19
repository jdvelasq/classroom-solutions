import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
curkey = None
docs = []
for line in sys.stdin:
    line = line.replace('\n', '')
    key, val = line.split("\t")
    val = int(val)
    if key == curkey: 
        docs.append(val)
    else:
        if curkey is not None:
            sys.stdout.write("{}\t{}\n".format(curkey, ','.join(
                [str(x) for x in sorted(docs)])))             
        curkey = key
        docs = [val]
sys.stdout.write("{}\t{}\n".format(curkey, ','.join(
    [str(x) for x in sorted(docs)]))) 
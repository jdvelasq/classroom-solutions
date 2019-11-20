#
#  Pregunta
#  ===========================================================================
#
# Escriba un programa en Python que transforme el archivo data.tsv al formato 
# nativo de Apache Hive; esto es, usando los caracteres que usa Apache Hive 
# internamente para separar los distintos elementos de un registro.
#
# * Llame las columnas c1, c2 y así sucesivamente.
#
# * Los campos internos de las columnas se llaman c11 y así sucesivamente.
#
# * La columna 2 es un ARRAY y la columna 3 es un MAP.
#
# >>> Escriba su respuesta a partir de este punto <<<
#
u = load 'data.tsv' using PigStorage() 
    as (c1:chararray, 
        c2:chararray, 
        c3:int);
g = GROUP u BY c1;
w = FOREACH g GENERATE group, COUNT(u);
dump w;
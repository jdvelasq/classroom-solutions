--
--  Pregunta
--  ===========================================================================
--
-- Ordene el archivo `data.tsv`  por letra y valor (3ra columna).
-- Imprima el resultado usando dump.
--
--  >>> Escriba el codigo del mapper a partir de este punto <<<
--
u = load 'data.tsv' using PigStorage() 
    as (c1:chararray, 
        c2:chararray, 
        c3:int);
g = ORDER u BY c1, c3;
dump g;

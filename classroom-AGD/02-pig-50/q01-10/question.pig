--
--  Pregunta
--  ===========================================================================
--
-- Para el archivo `data.tsv` compute la cantidad de registros por letra. 
-- Imprima el resultado usando dump.
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
u = load 'data.tsv' using PigStorage() 
    as (c1:chararray, 
        c2:chararray, 
        c3:int);
g = GROUP u BY c1;
w = FOREACH g GENERATE group, COUNT(u);
dump w;
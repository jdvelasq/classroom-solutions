--
--  Pregunta
--  ===========================================================================
--
-- Para el archivo `data.tsv` compute la cantidad de registros por letra de la 
-- columna 2 y clave de al columna 3; esto es, por ejemplo, la cantidad de 
-- registros en tienen la letra `b` en la columna 2 y la clave `jjj` en la 
-- columna 3 es:
--
--   ((b,jjj), 216)
--
-- Imprima el resultado usando dump.
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
u = LOAD 'data.tsv' using PigStorage() 
    AS (col1:CHARARRAY, 
        col2:BAG{}, 
        col3:MAP[]);
c2 = FOREACH u GENERATE FLATTEN(col2) AS k2, FLATTEN(KEYSET(col3)) AS k3;    
w = GROUP c2 BY ($0, $1);
x = FOREACH w GENERATE group, COUNT(c2);
DUMP x;


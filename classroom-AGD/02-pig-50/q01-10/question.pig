-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` compute la cantidad de registros por letra. 
-- Escriba el resultado a la carpeta `output` del directorio actual.
--
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
u = LOAD 'data.tsv' USING PigStorage() 
    AS (c1:chararray, 
        c2:chararray, 
        c3:int);
g = GROUP u BY c1;
w = FOREACH g GENERATE group, COUNT(u);
STORE w INTO 'output';
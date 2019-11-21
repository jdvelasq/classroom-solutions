-- Pregunta
-- ===========================================================================
-- 
-- Obtenga los cinco (5) valores más pequeños de la 3ra columna.
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
-- >>> Escriba su respuesta a partir de este punto <<<
--
u = load 'data.tsv' using PigStorage() 
    as (c1:chararray, 
        c2:chararray, 
        c3:int);
g = FOREACH u GENERATE c3;
h = ORDER g BY c3;
k = LIMIT h 5;
fs -rm -f -r output;
STORE k INTO 'output';

-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` Calcule la cantidad de registros por clave de la 
-- columna 3. En otras palabras, cuántos registros hay que tengan la clave 
-- `aaa`?
-- 
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
u = LOAD 'data.tsv' using PigStorage() 
    AS (c1:CHARARRAY, 
        c2:BAG{}, 
        c3:MAP[]);
v = FOREACH u GENERATE FLATTEN(c3) AS letter;    
w = GROUP v BY letter;
x = FOREACH w GENERATE group, COUNT(v);
STORE x INTO 'output' USING PigStorage(',');
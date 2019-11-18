--
--  Pregunta
--  ===========================================================================
--
-- Para el archivo `data.tsv` Calcule la cantidad de registros por clave de la 
-- columna 3. En otras palabras, cuántos registros hay que tengan la clave 
-- `aaa`?
--
-- Imprima el resultado usando dump.
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
DUMP x;

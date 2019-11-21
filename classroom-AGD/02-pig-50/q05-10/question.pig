
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
u = LOAD 'data.tsv' using PigStorage() 
    AS (c1:CHARARRAY, 
        c2:BAG{}, 
        c3:MAP[]);
v = FOREACH u GENERATE FLATTEN(c2) AS letter;    
w = GROUP v BY letter;
x = FOREACH w GENERATE group, COUNT(v);
DUMP x;

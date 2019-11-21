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


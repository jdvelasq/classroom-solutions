--
-- >>> Escriba su respuesta a partir de este punto <<<
--
u = LOAD 'data.tsv' using PigStorage() 
    AS (c1:CHARARRAY, 
        c2:BAG{}, 
        c3:MAP[]);
v = FOREACH u GENERATE c1, COUNT_STAR(c2), SIZE(c3);    
DUMP v;

-- Pregunta
-- ===========================================================================
-- 
-- Ordene el archivo `data.tsv`  por letra y valor (3ra columna).
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
--  >>> Escriba el codigo del mapper a partir de este punto <<<
-- 
u = load 'data.tsv' using PigStorage() 
    as (c1:chararray, 
        c2:chararray, 
        c3:int);
g = ORDER u BY c1, c3;
fs -rm -f -r output;
STORE g INTO 'output';

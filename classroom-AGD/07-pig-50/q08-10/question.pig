--
--  Pregunta
--  ===========================================================================
--
-- Para responder la pregunta use el archivo `data.csv`.
--
-- Escriba el código equivalente a la siguiente consulta en SQL.
-- 
--     SELECT
--         color
--     FROM 
--         u 
--     WHERE 
--         color 
--     LIKE 'b%';
--
u = LOAD 'data.csv' USING PigStorage(',') 
    AS (id:int, 
        firstname:CHARARRAY, 
        surname:CHARARRAY, 
        birthday:CHARARRAY, 
        color:CHARARRAY, 
        quantity:INT);
--
-- >>> Escriba su respuesta a partir de este punto <<<
--

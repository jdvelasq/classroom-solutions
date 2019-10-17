--
--  Pregunta
--  ===========================================================================
-- 
-- Para responder la pregunta use el archivo `data.csv`.
--
-- Escriba el código equivalente a la siguiente consulta SQL.
-- 
--     SELECT 
--         birthday, 
--         DATE_FORMAT(birthday, "yyyy"),
--         DATE_FORMAT(birthday, "yy"),
--     FROM 
--         persons
--     LIMIT
--         5;
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

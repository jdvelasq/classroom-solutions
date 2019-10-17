--
--  Pregunta
--  ===========================================================================
-- 
-- Para responder la pregunta use el archivo `data.csv`.
--
-- Cuente la cantidad de personas nacidas por año.
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

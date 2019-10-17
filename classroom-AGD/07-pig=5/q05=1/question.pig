--
--  Pregunta
--  ===========================================================================
--
-- Para responder la pregunta use el archivo `data.csv`.

-- Genere una relación con el apellido y su longitud. Ordene por longitud y por apellido. Obtenga la siguiente salida.
--
--    (Hamilton,8)
--    (Garrett,7)
--    (Holcomb,7)
--    (Coffey,6)
--    (Conway,6)
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

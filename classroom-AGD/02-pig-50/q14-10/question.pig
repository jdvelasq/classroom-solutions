--
--  Pregunta
--  ===========================================================================
--
-- Para responder la pregunta use el archivo `data.csv`.
--
-- Escriba el código que genere la siguiente salida.
--
--    (Hamilton,HAMILTON,hamilton)
--    (Holcomb,HOLCOMB,holcomb)
--    (Garrett,GARRETT,garrett)
--    (Fry,FRY,fry)
--    (Conway,CONWAY,conway)
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

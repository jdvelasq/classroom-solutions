-- 
-- Pregunta
-- ===========================================================================
--
-- Para resolver esta pregunta use el archivo `data.tsv`.
--
-- Compute la cantidad de registros por cada letra de la columna 1.
-- Escriba el resultado ordenado por letra. 
--
-- Escriba el resultado a la carpeta `output` de directorio de trabajo.
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
DROP TABLE IF EXISTS datatbl;
CREATE TABLE datatbl(
    c1 string,
    c2 string,
    c3 int
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t';
LOAD DATA LOCAL INPATH 'data.tsv' OVERWRITE INTO TABLE datatbl;

INSERT OVERWRITE DIRECTORY 'output'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
SELECT c1, count(*) FROM datatbl group by c1 ORDER By c1;


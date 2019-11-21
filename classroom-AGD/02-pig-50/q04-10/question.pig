-- Pregunta
-- ===========================================================================
-- 
-- El archivo `truck_event_text_partition.csv` tiene la siguiente estructura:
-- 
--   driverId       INT
--   truckId        INT
--   eventTime      STRING
--   eventType      STRING
--   longitude      DOUBLE
--   latitude       DOUBLE
--   eventKey       STRING
--   correlationId  STRING
--   driverName     STRING
--   routeId        BIGINT
--   routeName      STRING
--   eventDate      STRING
-- 
-- Escriba un script en Pig que carge los datos y obtenga los primeros 10 
-- registros. Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
-- 
--  >>> Escriba su respuesta a partir de este punto <<<
-- 
u = load 'truck_event_text_partition.csv' using PigStorage() 
    as (driverId:INT,
        truckId:INT,
        eventTime:CHARARRAY,
        eventType:CHARARRAY,
        longitude:DOUBLE,
        latitude:DOUBLE,
        eventKey:CHARARRAY,
        correlationId:CHARARRAY,
        driverName:CHARARRAY,
        routeId:CHARARRAY,
        routeName:CHARARRAY,
        eventDate:CHARARRAY);
k = LIMIT u 5;
STORE k INTO 'output';
# PRE_03 — Consultas básicas en MapReduce

## Problema

Usar la copia local de `data/tips.csv` para materializar cinco preguntas: una columna calculada, dos filtros, una condición compuesta y un conteo por sexo.

## Idea central

Una fila se transforma o descarta localmente; una agregación requiere emitir una clave y combinar todos sus valores. El resultado no depende de una descarga durante la ejecución.

## Entregables

Cinco archivos `query_*.csv` en `submission/`, generados por `src/main.py`, y un notebook de celdas exclusivamente de código cuya primera celda inicia con `# Problema:`.

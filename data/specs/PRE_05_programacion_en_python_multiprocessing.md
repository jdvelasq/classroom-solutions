# PRE_05 — Programación en Python con multiprocessing

## Problema

Ejecutar el mismo conteo de palabras clave--valor de PRE_02 sobre varias particiones de texto, primero de forma secuencial y luego con procesos locales.

## Idea central

Cada partición puede producir conteos parciales sin estado compartido. El proceso principal combina esos resultados por palabra. La preparación de los datos no se cronometra: se compara exclusivamente el mismo cómputo secuencial y paralelo.

## Resultado observable

`benchmark.csv` reporta procesos, tiempos y aceleración; `word_counts.csv` prueba que ambos modos produjeron el mismo resultado. El tamaño repetido del trabajo permite una aceleración visible en equipos con varios núcleos, sin afirmar una cifra fija como requisito de prueba.

## Frontera

No cubre bloqueos, memoria compartida, colas, programación asíncrona ni administración de procesos. Es un puente desde las particiones de MapReduce hacia la idea de cómputo paralelo local.

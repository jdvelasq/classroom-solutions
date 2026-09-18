# PRE_01 — Verificación del entorno de trabajo

## Resultado de la auditoría

Este PRE abre el trabajo práctico del curso verificando que cada estudiante
puede ejecutar de manera reproducible los materiales que se utilizarán en la
familia inicial de Word Count. No introduce análisis descriptivo ni se
convierte en una clase de instalación de herramientas.

Su duración definitiva es de **1 bloque de 50 minutos**.

## Propósito pedagógico

Instalar una condición de trabajo común: ejecutar un caso mínimo desde el
repositorio del curso, identificar las versiones del entorno y producir una
evidencia verificable de que el resultado se puede repetir.

Esta actividad introduce la reproducibilidad como práctica transversal. Los
PRE posteriores reutilizan el entorno; no deben repetir esta verificación
salvo que su propio material añada una dependencia específica.

## Punto de partida

El estudiante ya debe contar con los fundamentos de programación y uso del
entorno de desarrollo que exige el curso. El instructor proporciona antes de
la sesión el repositorio, las instrucciones de preparación y las versiones
compatibles de las dependencias requeridas.

## Actividad y tiempo estimado

| Minutos | Actividad |
|---:|---|
| 0–5 | Explicar el objetivo, el criterio de terminación y la evidencia que se debe conservar. |
| 5–15 | Abrir la copia del repositorio del curso y comprobar estructura, intérprete o entorno declarado y acceso a los archivos de entrada. |
| 15–30 | Ejecutar desde un entorno limpio el caso de comprobación provisto: lectura de un archivo pequeño, transformación mínima y salida verificable. |
| 30–40 | Registrar versiones relevantes, comando o procedimiento de ejecución y resultado obtenido. |
| 40–50 | Comparar resultados, resolver incidencias comunes que afecten al grupo y clasificar las incidencias restantes para atención fuera del bloque. |

## Artefacto final

Una evidencia breve de entorno reproducible, entregada en el mecanismo que
defina la cohorte, con:

- identificación de la copia o versión del material usada;
- versiones relevantes del intérprete y dependencias;
- procedimiento o comando de ejecución;
- salida esperada del caso de comprobación;
- cualquier incidencia que todavía impida continuar.

## Criterio de terminación

El PRE está terminado cuando el caso de comprobación se ejecuta desde el
material del curso y su salida coincide con la esperada, o cuando la
incidencia queda registrada y el estudiante recibe una vía concreta de
resolución antes de `PRE_02`.

## Límites

Quedan fuera del PRE:

- instalación individual extensa o depuración de sistemas operativos;
- enseñanza de Python, Git, notebooks, SQL o paquetes específicos;
- configuración de credenciales o servicios que solo se requieran en PRE
  posteriores;
- análisis de los datos de comprobación.

El instructor debe trasladar los bloqueos individuales de instalación a una
guía previa, soporte fuera de clase o una ruta alternativa ya preparada. Así
se protege el bloque completo para la verificación común y la continuidad de
la secuencia.

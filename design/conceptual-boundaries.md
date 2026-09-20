# Identidad y fronteras conceptuales de los cursos

## Punto de partida: Analytics no es una colección de técnicas

La arquitectura del programa parte de una concepción profesional de Analytics como el proceso de transformar datos en conocimiento para tomar mejores decisiones. INFORMS no lo organiza como una lista de algoritmos: su marco recorre siete dominios —encuadre del problema de negocio, encuadre analítico, datos, selección de metodología, construcción del modelo, despliegue y gestión del ciclo de vida—. El modelo, por tanto, es un medio dentro de una cadena de creación de valor, no su final. [INFORMS Analytics Framework](https://www.informs.org/Professional-Development/INFORMS-Analytics-Framework) y [Job Task Analysis de CAP](https://info.informs.org/jta).

La clásica tríada descriptiva–predictiva–prescriptiva tampoco representa tres pilas tecnológicas. Es una diferencia de **pregunta, objeto producido y criterio de éxito**. INFORMS define lo descriptivo como comprensión de eventos pasados, lo predictivo como anticipación de lo futuro y lo prescriptivo como consejo accionable para decidir. [Operations Research & Analytics](https://www.informs.org/Explore/Operations-Research-Analytics). Cada curso debe conservar esa pregunta rectora; si se sustituye por el nombre de una herramienta o familia de algoritmos, pierde su identidad.

## Qué significa “producto de datos”

La expresión tiene dos usos legítimos que el curso debe enseñar de manera relacionada, pero sin confundirlos.

### 1. Datos como producto

Un **producto de datos** puede ser una unidad curada de datos analíticos, empaquetada para un consumidor concreto y un problema de negocio. No es un archivo ni una tabla aislada. Debe ser descubrible, comprensible, confiable, accesible, seguro, documentado y mantenido; incluye semántica, calidad, contrato de uso, metadatos, propiedad y compromiso de servicio. Esa es la acepción de *data as a product* empleada en data mesh. [Google Cloud: About data products](https://docs.cloud.google.com/dataplex/docs/data-products-overview) y [Dehghani: Data Mesh Principles](https://martinfowler.com/articles/data-mesh-principles.html).

En esa acepción, el producto puede ser un dataset curado, una vista, un flujo de eventos, un feature set o una API de datos. El consumidor puede ser una persona, un tablero, un modelo o otro producto de datos. Su valor reside en reducir la fricción para encontrar, entender, confiar y usar datos.

### 2. Producto analítico o habilitado por datos

Un **producto analítico** entrega a un usuario una capacidad para observar, predecir, decidir o actuar. Puede incorporar uno o varios productos de datos, un modelo, una regla de decisión, una simulación, una interfaz o una API. Ejemplos legítimos son un servicio que prioriza solicitudes, un recomendador, un sistema de alertas o una experiencia que entrega un pronóstico y permite actuar sobre él.

Aquí el producto no se define por “tener ML”. Se define por tener un usuario, una decisión o tarea, una propuesta de valor, límites de uso, una experiencia de consumo, propiedad responsable y una capacidad de evolucionar con evidencia. Un tablero puede ser un producto analítico si está empaquetado, tiene consumidores definidos, responde una necesidad y cumple un contrato de calidad; no lo es solo por existir como visualización. De forma equivalente, un modelo guardado no es un producto hasta que alguien puede usarlo de manera segura y confiable para un propósito definido.

### Consecuencia curricular

El curso **Productos de Datos** debe abarcar la relación entre ambas acepciones:

```text
producto de datos confiable
        ↓ alimenta
capacidad analítica o de decisión
        ↓ se entrega como
producto analítico utilizable y operable
```

Esto lo distingue tanto de Ingeniería de Datos —que diseña y produce datos confiables— como de un curso de desarrollo de software —que podría construir una aplicación sin pregunta analítica, evidencia ni contrato de datos—.

## Qué es MLOps/DataOps y qué no es

MLOps y DataOps son disciplinas de entrega y operación. Hacen reproducible, verificable, observable y gobernable una capacidad basada en datos: controlan versiones, automatizan pruebas, promueven cambios, observan calidad y desempeño, manejan incidentes y cierran el ciclo de aprendizaje. No definen por sí solos el producto ni sustituyen la validación de que el producto resuelve una necesidad de usuario.

Por ello, Productos de Datos no es:

- un curso de ingeniería de software general (arquitecturas de aplicación, patrones de código, complejidad algorítmica o certificación cloud);
- una formación de administración de infraestructura o certificación de una plataforma;
- un curso de ML que enseña a ajustar modelos nuevos;
- un curso de UX independiente;
- un curso de DataOps desligado de valor, consumidor y decisión.

Sí es el curso donde se conecta la capacidad analítica con su consumidor y con condiciones de operación sostenida. MLflow puede ilustrar registro de experimentos, artefactos, modelos y trazabilidad; no constituye el currículo ni se debe enseñar como fin en sí mismo.

## Fronteras no negociables

| Curso | Pregunta que responde | Entregable intelectual propio | Qué no es |
|---|---|---|---|
| **Fundamentos de Analítica** | ¿Qué problema vale la pena abordar con analítica, qué tipo de pregunta es y qué límites tiene la evidencia disponible? | Encuadre analítico y nivel mínimo común de vocabulario/práctica para el ingreso a los cursos de posgrado. | Una secuencia reducida de los cursos de posgrado: sus `PRE_*` nivelan y orientan; Descriptiva, Predictiva y Prescriptiva desarrollan las competencias con profundidad propia. |
| **Fundamentos de Datos para Analítica** | ¿Cómo se adquieren, representan, transforman, validan y sirven datos confiables para el consumo analítico? | Datos curados, documentados y verificables, con su contrato de calidad, linaje y arquitectura pertinente. | Administración de bases de datos, certificación cloud o producto analítico final: entrega insumos confiables para los demás cursos. |
| **Analítica Descriptiva y Visualización** | ¿Qué ocurrió, qué patrón existe y qué evidencia respalda esa lectura? | Evidencia explorada, contextualizada y comunicada con sus límites. | Estadística básica: emplea resúmenes y variabilidad para interpretar datos, pero su núcleo es exploración, representación, contexto y comunicación de evidencia. Tampoco es una colección de gráficos. |
| **Analítica Predictiva** | ¿Qué resultado o probabilidad puede anticiparse y con qué desempeño, incertidumbre y condiciones? | Predicción validada y documentada, o evidencia de que una relación no permite predecir útilmente. | Otro curso de ML: los algoritmos son instrumentos subordinados a encuadre, validación fuera de muestra, calibración, costo de error, sesgo y decisión de uso. Incluye el pivote que separa predicción de causalidad. |
| **Analítica Prescriptiva** | ¿Qué acción, política o asignación conviene dadas metas, restricciones, incertidumbre y efectos? | Recomendación o política defendible, con escenarios, sensibilidad y condiciones de validez. | Investigación de operaciones completa: usa optimización, simulación, reglas y análisis de decisión en problemas alimentados por datos, sin convertir el curso en teoría exhaustiva de métodos, demostraciones o administración de solvers. INFORMS sitúa precisamente la prescripción en la intersección de paradigma centrado en datos y paradigma centrado en problemas. [Defining analytics](https://pubsonline.informs.org/do/10.1287/orms.2016.03.12/full/). |
| **Productos de Datos** | ¿Cómo se empaqueta, entrega, gobierna y evoluciona una capacidad de datos/analítica para que un consumidor obtenga valor sostenido? | Producto de datos o producto analítico con consumidor, contrato, propiedad, evidencia de valor y plan operativo. | Ingeniería de software: usa prácticas de entrega solo donde preservan la utilidad, calidad, seguridad y evolución de la capacidad analítica. |

### Transiciones precisas

- **Descriptiva → Predictiva:** una asociación, segmentación o tendencia se convierte en un candidato a predicción solo cuando se define objetivo, horizonte, protocolo de evaluación y uso futuro. Mostrar que dos variables se mueven juntas no autoriza a afirmar que una anticipará la otra.
- **Predictiva → Prescriptiva:** una probabilidad o pronóstico no es una decisión. La transición requiere alternativas de acción, función de valor, restricciones y tolerancia al riesgo.
- **Prescriptiva → Productos:** una recomendación matemática no es un producto. La transición requiere consumidor, modo de interacción o consumo, contrato, responsabilidad y operación.
- **Datos → Productos:** Datos garantiza que la entrada sea disponible, confiable y gobernada; Productos garantiza que una capacidad construida con esa entrada sea utilizable, entregable y sostenible.

## Implicaciones para talleres `PRE_*`

Un caso pequeño y autocontenido puede realizar la función pedagógica de un producto sin convertirse en capstone. Puede tomar como punto de partida una organización real, Kaggle, un libro o un ejemplo de herramienta, pero debe adaptarse a una situación realista simplificada para el aula —no a un ejercicio artificial de comandos— y tener una unidad de valor completa:

```text
consumidor y necesidad
→ dato/modelo/regla disponible
→ contrato o condición de uso
→ entrega mínima verificable
→ evidencia de calidad, valor u operación
```

Un taller de Productos puede, por ejemplo, registrar un experimento y comparar versiones de un modelo; publicar una capacidad bajo un contrato; detectar una falla de calidad y detener una entrega; observar deriva y justificar una acción; o evaluar un flujo RAG con criterios de fundamentación y permisos. Cada ejemplo se cierra dentro de sí mismo. Ninguno depende de que el estudiante acumule partes de un sistema durante el semestre.

La escala del caso es deliberadamente flexible: una pregunta profesional acotada, como convertir de manera confiable un conjunto de archivos CSV en JSON, puede ser un microproyecto completo si exige especificar entrada y salida, tratar calidad o esquema, validar el resultado y explicar para qué consumidor analítico queda disponible.

## Criterio de calidad para la siguiente fase

Al programar sesiones y talleres, se deberá poder responder para cada tema: **¿a cuál pregunta rectora sirve?, ¿qué entrega propia permite producir?, ¿qué curso no debe repetirlo?** Si no hay una respuesta clara, el tema se reubica o se elimina. Esta prueba protege la identidad disciplinar de los cuatro cursos y evita que sus nombres se conviertan en etiquetas para herramientas.

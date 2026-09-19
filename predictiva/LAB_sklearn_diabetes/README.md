# Descripción

En este laboratorio debe construir un modelo predictivo de regresión para 
predecir el progreso de la diabetes en pacientes usando scikit-learn. La
base de datos contine un total de 442 pacientes y 10 variables de entrada
que pueden ser utilizadas para predecir el progreso de la diabetes 
(columna `target` en el dataset). Las variables de entrada son:

* `age` 

* `sex`

* `bmi`

* `bp`

* `s1`

* `s2`

* `s3`

* `s4`

* `s5`

* `s6`

El modelo debe ser estimado usando la información disponible en el archivo
`data/train_dataset.csv` y evaluado usando el archivo 
`data/test_dataset.csv`. El modelo obtenido debe ser salvado en el 
archivo `models/model.pkl`.  


# Configuración en MacOS y Linux

## Instalación del ambiante de desarrollo

Ejecute los siguientes comandos en el terminal:

```bash
python3 -m venv .venv
source .venv/bin/activate
source setup.sh
```

## Calificación del laboratorio

Ejecute los siguientes comandos en el terminal:

```bash
./tests/run.sh
```

# Configuración en Windows

## Instalación del ambiante de desarrollo

Ejecute los siguientes comandos en el terminal:

```bash
python3 -m venv .venv
.venv\Scripts\activate
setup
```

## Calificación del laboratorio

Ejecute los siguientes comandos en el terminal:

```bash
tests\run
```

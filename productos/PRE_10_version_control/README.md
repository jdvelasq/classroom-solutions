# PRE-10 — Control de versiones

Este taller practica un cambio pequeño y verificable en un repositorio Git aislado. No se modifica el repositorio del curso.

## Cambio solicitado

El producto analítico `factory_totals` necesita declarar con precisión su unidad de medida. En `product_card.md`, reemplace:

```text
- Unidad de medida: Pendiente de definir.
```

por:

```text
- Unidad de medida: unidades producidas por fábrica y día.
```

## Pasos

Abra una terminal en la carpeta de este PRE y ejecute los comandos en este orden:

```bash
cp -R data/repository_template temp/version_control_case
cd temp/version_control_case
git init
git config user.name "Estudiante"
git config user.email "estudiante@example.com"
git status
```

Abra `product_card.md` en su editor, aplique el cambio solicitado y guarde el archivo. Después ejecute:

```bash
git diff
git add product_card.md
git status
git commit -m "docs: define unit of measure"
git log --oneline -1
cd ../..
```

## Qué observar

- `git status` muestra qué archivos cambiaron y cuáles están listos para confirmar.
- `git diff` muestra el cambio antes de incorporarlo al historial.
- `git commit` crea una versión recuperable del producto.
- `git log` permite identificar esa versión después.

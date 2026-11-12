# Contrato entre el libro y la web

El libro (`02-libro`) y la web (`01-web`) son proyectos separados. Este contrato es lo único que comparten. Si uno de los dos necesita cambiarlo, se cambia en ambos a la vez y se sube la versión.

**Versión del contrato: 1**

## 1. Quién hace qué

- **El libro** escribe Markdown en `02-libro/contenido/`. No sabe nada de la tecnología de la web.
- **La web** lee `02-libro/contenido/` (como submódulo de git o copiándolo en el build) y nunca escribe en esa carpeta. Genera:
  - las páginas;
  - la búsqueda;
  - las descargas en `.md` de cada capítulo, cada parte y el libro completo.

## 2. Carpetas y nombres

```
contenido/
├── 00-preliminares/          # prologo.md, metodo.md, convenciones.md
├── parte-01-base/
│   ├── _parte.md             # apertura de la parte
│   ├── cap-01-git-por-dentro.md
│   ├── ...
│   └── soluciones.md
├── ...
├── parte-09-go/
├── 99-apendices/
└── _img/                     # imágenes, si alguna vez hacen falta
```

- **Partes:** `parte-NN-<id>`, con el id de la parte del catálogo (`base`, `python`, `backend`, `ia`, `agentes`, `agentica`, `typescript`, `arquitectura`, `go`).
- **Capítulos:** `cap-NN-<slug>.md`, con el número global de 01 a 59. La ruta exacta de cada uno está en `docs/04-catalogo-capitulos.md`.
- **Orden:** el de los números. Las descargas por parte y del libro completo concatenan en ese orden: preliminares, partes y apéndices.

## 3. Cabecera YAML obligatoria

```yaml
---
id: python/py-async          # id del catálogo
parte: 2
capitulo: 10
titulo: Asincronía
estado: borrador             # borrador | revisado | publicado
actualizado: 2026-11-12
palabras: 7420
versiones:
  python: "3.13"
---
```

`_parte.md` y `soluciones.md` llevan `parte`, `titulo` y `estado`.

## 4. Markdown permitido

- **Sintaxis.** CommonMark más tablas al estilo GitHub. Sin HTML ni componentes de ningún framework; los comentarios HTML (`<!-- -->`) sí se permiten.
- **Código.** Bloques con el lenguaje en la valla (`python`, `bash`, `ts`, `go`, `text` para salidas).
- **Diagramas.** Bloques ` ```mermaid `.
- **Recuadros.** Citas con un título fijo en negrita al principio, y solo estos cuatro:

  ```markdown
  > **Bajo el capó.** ...
  > **Error típico.** ...
  > **En un proyecto real.** ...
  > **Ojo con la versión.** ...
  ```

  La web puede darles estilo detectando el título; el `.md` descargado se lee bien sin él.
- **Referencias.** `[n]` en el texto y, al final del capítulo, una sección `## Fuentes` con una línea por fuente:

  ```markdown
  [1] Pro Git 3.1, ¿Qué es una rama? https://git-scm.com/book/es/v2/... (consultada 2026-11-12)
  ```

- **Enlaces entre capítulos.** Con ruta relativa al archivo (`../parte-02-python/cap-10-asincronia.md#101-modelo-mental-el-bucle-de-eventos`). Funcionan en GitHub y en cualquier lector de Markdown, y la web los convierte en enlaces a sus páginas.
- **Marcas internas.** El libro nunca entrega a la web marcas sin resolver, como `<!-- ejemplo: ... -->` o ids `[h10-003]`. Si aparecen, es un error del libro.

## 5. Estado y publicación

- **En producción** la web solo muestra capítulos con `estado: publicado`.
- **En previsualización** puede mostrar todos, indicando el estado en la página.
- **Descargas:** solo incluyen capítulos publicados.

## 6. Validación

El libro incluye `scripts/validar_contrato.py`, que comprueba:

- nombres y rutas;
- la cabecera YAML;
- que no haya HTML;
- que los recuadros usen solo los cuatro títulos;
- que cada `[n]` tenga su línea en `## Fuentes`;
- que no queden marcas internas.

La web puede ejecutar el mismo script antes de su build.

# Libro devOC: «Programar entendiendo el código» (escritura)

Este proyecto escribe un libro técnico en español (9 partes, 59 capítulos) a partir de fuentes públicas verificadas. Produce Markdown en `contenido/`; la web es otro proyecto (`../01-web`) y solo lee ese Markdown según `docs/06-contrato-con-la-web.md`.

Antes de cualquier tarea nueva, lee `docs/00-proyecto.md` y `docs/05-metodo-sin-alucinaciones.md`.

## Documentos

- `docs/00-proyecto.md`: visión, reglas, plantilla de capítulo, flujo y plan por hitos.
- `docs/01-modelo-y-esfuerzo.md`: modelo y esfuerzo para cada fase y cada subagente.
- `docs/02-indice-general.md`: índice completo.
- `docs/03-indice-con-fuentes.md`: única lista de fuentes autorizadas.
- `docs/04-catalogo-capitulos.md`: ficha obligatoria de cada capítulo.
- `docs/05-metodo-sin-alucinaciones.md`: los cinco cortafuegos y la redacción cerrada.
- `docs/06-contrato-con-la-web.md`: formato que debe cumplir `contenido/`.
- `docs/estado.md`: tablero de progreso; actualízalo al cambiar el estado de un capítulo.

## Reglas que no se rompen

1. El modelo propone y los scripts verifican. Ninguna afirmación técnica sin un hecho de `investigacion/cap-XX/hechos.md` con evidencia literal validada por `scripts/verificar_evidencias.py`.
2. Nunca cites ni uses una URL que no esté en `docs/03-indice-con-fuentes.md` y que no hayas abierto. Una fuente nueva se verifica y se añade primero.
3. Nunca completes con memoria. Si falta un hecho, escribe `> PENDIENTE: ...` y sigue; un PENDIENTE es un resultado correcto.
4. No escribas código ni salidas a mano en el capítulo: usa `<!-- ejemplo: ruta -->` y deja que `scripts/insertar_ejemplos.py` ejecute el programa e inserte la salida real.
5. No copies: escribe con palabras propias. Las citas literales al lector tienen menos de 15 palabras y van entre comillas.
6. Los cursos de mouredev y midudev sirven para práctica y ejemplos, no como respaldo técnico; comprueba su licencia antes de reutilizar código.
7. Los libros de pago del catálogo no son fuente.
8. Investigación, redacción y revisión se hacen en sesiones o subagentes distintos, y siempre de una sección en una sección.
9. Ningún capítulo pasa a `publicado` sin la aprobación de devOC.

## Estilo

- Español de España, segunda persona y frases cortas; sin emojis ni relleno.
- Un término en inglés va en cursiva la primera vez, con su traducción.
- Recuadros solo con estos cuatro títulos: **Bajo el capó**, **Error típico**, **En un proyecto real** y **Ojo con la versión**.
- Mermaid cuando haya estructura que dibujar.

## Cuándo preguntar a devOC

- Al proponer el esquema de cada capítulo.
- Cuando una sección no tenga fuente fiable.
- Antes de ampliar el alcance o de reescribir un capítulo aprobado.

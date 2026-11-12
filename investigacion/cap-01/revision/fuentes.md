# Revisión de fuentes del capítulo 1

Revisor de fuentes (sesión limpia), 2026-11-12. Comparó cada párrafo con las copias locales (secuencias de 6 o más palabras compartidas y similitud frase a frase; scripts en el scratchpad del revisor).

## Resultado

| Tipo | Hallazgos |
| --- | --- |
| Autorización (URL fuera de docs/03 o ids inexistentes) | 0 |
| Cita literal de 15 palabras o más sin comillas | 1 (1.3-1) |
| Fragmento literal sin comillas, menos de 15 palabras | 5 (1.1-2, 1.2-2, 1.2-3, 1.2-6, 1.4-5) |
| Paráfrasis cercana (redacción de la fuente con palabras cambiadas) | 34 (1.1: 7; 1.2: 6; 1.3: 4; 1.4: 4; 1.5: 6; 1.6: 3; 1.7: 4) |
| Sección con el mismo orden y ejemplos que un capítulo de Pro Git | 7 (altas: 1.1, 1.4, 1.6, 1.7) |
| Fuentes no válidas | 0 |
| Licencias (ejemplos derivados y tabla sin atribución) | 2 |
| **Total** | **49** |

**Causa de fondo.** Los campos `hecho:` de `hechos.md` ya parafrasean la fuente muy de cerca, y el borrador los transcribe. Al corregir hay que reescribir desde la idea, no desde el texto del hecho.

## Hallazgos principales por sección

- **1.1 (estructura alta).** Recorre Pro Git 1.1 y 1.2 con sus mismos ejemplos (copiar a otro directorio, RCS, CVS/Subversion, servidor caído una hora, disco corrupto, restaurar desde un clon, Linux/BitKeeper/Torvalds y objetivos). Literal: «Los sistemas centralizados, como CVS o Subversion, tienen un único servidor con todos los archivos versionados y varios clientes que descargan de él los archivos» (l.47). Paráfrasis casi literal: «Si se cae durante una hora…» (l.86); el párrafo de la historia resume Pro Git 1.2 frase a frase (l.88). Propuesta: contar los tres modelos desde `facturas`, quitar «una hora», reducir la historia a una o dos frases propias.
- **1.2 (estructura media).** Esqueleto de Pro Git 1.3 y 2.2. Literales: «Conceptualmente, la mayoría de los demás sistemas… guardan la información como una lista de cambios en los archivos» (l.96); «una serie de instantáneas, copias puntuales de los archivos completos» (l.96, f01-07); el párrafo de las tres secciones calca f01-03 (12 palabras literales: «El directorio de trabajo es una copia de una versión del proyecto», l.138). Propuesta: abrir con el ejemplo 03 y que la teoría salga de lo que se ve.
- **1.3.** Cita literal de 17 palabras sin comillas: «es una de las pocas áreas en las que Git puede perder parte de tu trabajo si te equivocas» (l.302, f01-06). La parte de deshacer sigue Pro Git 2.4 paso a paso. Autor/confirmador calca f01-05 (l.300).
- **1.4 (estructura alta).** Reproduce el escenario de Pro Git 3.2 (rama de tema, «arreglo urgente» con `-c`, avance rápido, `-d`, fusión a tres bandas, conflicto, `status`, marcadores, `add`, commit, ventaja frente a CVS) y luego 3.3. Paráfrasis encadenadas en l.460, 512, 516, 590, 596, 600. HEAD desacoplado sigue f01-21 en su orden. Propuesta: quitar el planteamiento del «arreglo urgente» y explicar desde la salida de los ejemplos 08 y 09.
- **1.5.** Los cinco pasos del rebase con los mismos verbos y orden que f01-10 (l.670); el «Bajo el capó» de `patch-id` condensa f01-10 frase a frase (l.935); el «Error típico» sigue «Los peligros de reorganizar» (l.933).
- **1.6 (estructura alta, ejemplos cosméticos).** Orden y ejemplos de Pro Git 10.1-10.3; los ejemplos 16, 17 y 19 son los de 10.2 con cambios cosméticos («hola» por «test content», Python por Ruby). Propuesta: ir de arriba abajo desde `facturas` (`cat-file` de HEAD, árbol, blob) y calcular a mano el hash de un blob de `facturas`.
- **1.7 (estructura alta, ejemplos cosméticos).** Pro Git 7.7 completo y en orden; ejemplos 21 y 23 (`develop` frente a `main`) y 24 (misma secuencia que 10.7) con cambios cosméticos; el 13 copia los mensajes «WIP» y «oops». Paráfrasis encadenadas en l.1164-1168, 1170, 1202. Propuesta: ordenar la sección alrededor de «El problema» (abrir con `reset --soft HEAD~2` + `commit`), usar ramas de `facturas`, quitar «WIP»/«oops».

## Licencias

- **L-1.** Ningún identificador de Pro Git en `ejemplos/cap-01/` y `facturas` es propio, pero 05, 08, 09, 13, 16, 17, 19, 21, 23 y 24 reproducen secuencias de Pro Git con cambios cosméticos y sin atribución. Si se tratan como adaptaciones, CC BY-NC-SA exige atribución, uso no comercial y misma licencia. Preferible rehacerlos (regla 3); si no, atribuir y que devOC decida la licencia del libro.
- **L-2.** La tabla resumen de 1.7 tiene las mismas filas, orden y columnas que la de Pro Git 7.7. Rediseñarla con `switch` y `restore`, o atribuirla.

## Orden de corrección propuesto

Empezar por 1.3-1 y por las cuatro secciones de estructura alta (1.1, 1.4, 1.6, 1.7): rehacer su orden y sus ejemplos arregla de paso buena parte de las paráfrasis y las dos de licencia.

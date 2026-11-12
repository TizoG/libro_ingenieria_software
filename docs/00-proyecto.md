# Proyecto: «Programar entendiendo el código», el libro de devOC

Este documento explica la escritura del libro a Claude Code (y a Cowork, si interviene). Léelo entero antes de crear o tocar nada. La construcción de la web es un proyecto aparte, en la carpeta `01-web`; aquí solo importa el contrato entre ambos (`docs/06-contrato-con-la-web.md`). Cuando algo de este documento choque con una petición puntual de devOC, pregunta antes de actuar.

---

## 1. Qué vamos a construir

Un libro técnico completo, escrito en español de España, que lleva a un desarrollador desde bases sólidas hasta contribuir en proyectos open source de IA, en especial al ecosistema [gentle-shell](https://github.com/Gentleman-Programming/gentle-shell).

### La envergadura

- **9 partes, 59 capítulos y previsiblemente entre 250 y 300 secciones.** Cada capítulo equivale a un capítulo de un libro técnico impreso, de unas 15 a 30 páginas (entre 5.000 y 10.000 palabras orientativas).
- **Previsiblemente más de 300 fuentes externas.** Cada afirmación técnica del libro sale de una fuente pública, gratuita y verificada.
- **Ejemplos ejecutables.** Todo el código del libro se ejecuta de verdad y su salida se copia tal cual.
- **Publicado en una web de lectura** (proyecto aparte) donde está todo el libro, con descarga en Markdown de cada capítulo, de cada parte y del libro completo. Este proyecto produce el Markdown; la web lo consume.

### Las partes

Las partes van en orden de aprendizaje. Cada una tiene un proyecto hilo (la «misión») que crece capítulo a capítulo.

| Parte | Nombre | Capítulos | Fase |
| --- | --- | --- | --- |
| I | El oficio: Git, terminal, HTTP, leer código | 1 a 5 | 1, bases |
| II | Python profundo | 6 a 13 | 1, bases |
| III | Backend con FastAPI | 14 a 22 | 2, construir |
| IV | IA aplicada: LLMs, RAG y skills | 23 a 30 | 2, construir |
| V | Agentes de IA | 31 a 36 | 3, agentes y contribución |
| VI | Ingeniería de software agéntica | 37 a 41 | 3, agentes y contribución |
| VII | TypeScript y Node | 42 a 47 | 3, agentes y contribución |
| VIII | Arquitectura y diseño de sistemas | 48 a 53 | 4, profundidad |
| IX | Go | 54 a 59 | 4, profundidad |

El índice completo está en `docs/02-indice-general.md`, las fuentes de cada capítulo en `docs/03-indice-con-fuentes.md` y la ficha obligatoria de cada capítulo en `docs/04-catalogo-capitulos.md`.

---

## 2. Para quién y con qué filosofía

### El lector

devOC: desarrollador en Cádiz que trabaja con Python, FastAPI, Flutter y Next.js y está dando el salto a freelance. No es principiante, pero quiere bases sólidas.

### La idea central

Hoy la IA escribe mucho código; el lector tiene que **entenderlo, explicarlo y defenderlo**. Por eso el libro:

- explica siempre el **porqué** antes que el cómo;
- muestra qué pasa **por dentro**;
- enseña a desconfiar del código que no se entiende.

### El método de estudio

Este método condiciona cómo se escribe el libro. Cada capítulo se da por dominado solo cuando el lector supera tres pruebas:

1. **Explicar** sin mirar.
2. **Construir** el ejercicio sin IA.
3. **Defender** sus decisiones ante un examinador.

Por eso cada capítulo termina con esas tres cosas preparadas.

### Contexto que existe fuera del repo

Ya existe una web de roadmap interactiva (en claude.ai) donde devOC marca su progreso por nodos; cada capítulo corresponde a un nodo con el mismo `id`. Ya existe también un documento de referencia del roadmap. Claude Code no tiene acceso a ninguno de los dos y no los necesita: todo lo relevante está copiado en `docs/`.

---

## 3. Reglas innegociables

Estas reglas están por encima de cualquier otra consideración, incluida la velocidad. El sistema que las hace cumplir (copias locales, hechos con evidencia, scripts y revisión adversarial) está en `docs/05-metodo-sin-alucinaciones.md`.

1. **Nada inventado.** Toda afirmación técnica (cómo funciona algo, qué hace un comando, qué devuelve una función, un número, una fecha, una versión) lleva una referencia numerada a una fuente de `docs/03-indice-con-fuentes.md`. Si no hay fuente, no se escribe; se marca `> PENDIENTE: falta fuente para ...` y se avisa a devOC.
2. **Solo fuentes del mapa.** Una fuente nueva se añade primero a `docs/03-indice-con-fuentes.md`, tras abrirla y comprobar que existe y trata el tema. Nunca se cita una URL que no se haya abierto.
3. **No copiar.** El texto se escribe con palabras propias. Las citas literales van entre comillas, son cortas (menos de 15 palabras) y solo se usan cuando la redacción exacta importa: una definición de una especificación, un mensaje de error. No se reproduce la estructura de un capítulo ajeno, ni sus ejemplos con cambios cosméticos. Varias fuentes tienen licencias que exigen atribución (Pro Git es CC BY-NC-SA, MDN es CC BY-SA, Composing Programs es CC BY-SA); la página de créditos de la web las recoge.
4. **Código ejecutado.** Todo bloque de código del libro existe como archivo en `ejemplos/`, se ha ejecutado y su salida se pega sin retocar. Cada bloque indica la versión de la herramienta con la que se ejecutó. Si un ejemplo no se puede ejecutar en el entorno (por ejemplo, depende de un servicio de pago), se dice explícitamente en el texto.
5. **Los libros comprados no son fuente.** El catálogo menciona libros de pago del roadmap original como referencia orientativa. No se citan ni se usan como base del texto: el libro se construye solo con fuentes gratuitas y públicas.
6. **Vídeos solo con transcripción.** Un vídeo puede recomendarse como complemento, pero no es fuente citable salvo que se disponga de su transcripción y se haya leído.
7. **devOC aprueba.** Ningún capítulo pasa a «publicado» sin la aprobación explícita de devOC.

### Jerarquía de fuentes

Cuando haya que elegir fuente, de más a menos preferida:

1. Documentación oficial y especificaciones: docs.python.org, FastAPI, MDN, RFC, documentación de cada herramienta.
2. Libros técnicos gratuitos con licencia abierta: Pro Git, Composing Programs.
3. Cursos universitarios publicados: MIT Missing Semester, Berkeley.
4. Escritos de los propios mantenedores: blogs oficiales del proyecto, notas de versión, propuestas de diseño.
5. Código fuente y tests del propio proyecto, como evidencia de cómo funciona algo.
6. Cursos de la comunidad en español (mouredev, midudev): para ejercicios, ejemplos y vocabulario, nunca como respaldo de una afirmación técnica (ver `docs/05-metodo-sin-alucinaciones.md`, sección 6).

No se usan como fuente:

- blogs de agregadores o contenido SEO;
- respuestas de foros (salvo que las firme un mantenedor);
- contenido generado por IA;
- resúmenes de terceros cuando existe el original.

Se prefiere la versión en español de una fuente solo si está al día con la original; ante la duda, se usa la original.

---

## 4. Cómo es el libro por dentro

### Niveles

| Nivel del libro | Equivale a | Ejemplo |
| --- | --- | --- |
| Libro | El roadmap completo | Programar entendiendo el código |
| Parte | Una rama del roadmap | Parte I: El oficio |
| Capítulo | Un nodo del roadmap | Capítulo 1: Git por dentro |
| Sección | Un subtema (fila de `docs/03-indice-con-fuentes.md`) | 1.4 Las ramas son punteros |

### Preliminares y apéndices

- **Preliminares:**
  - un prólogo que explica cómo usar el libro y el método de las tres pruebas;
  - las convenciones tipográficas;
  - el índice.
- **Apéndices:**
  - preparar el entorno;
  - un glosario general (se alimenta de los glosarios de cada capítulo);
  - una chuleta por parte;
  - créditos y licencias de las fuentes.

### Apertura de cada parte

Archivo `_parte.md` de la carpeta de la parte:

1. Por qué importa la parte, en un párrafo.
2. El mapa de capítulos y qué depende de qué.
3. El proyecto hilo (la misión del catálogo) y qué pieza aporta cada capítulo.

### Plantilla obligatoria de cada capítulo

1. **Lo que podrás hacer al terminar.** Entre 3 y 5 objetivos comprobables («explicar por qué…», «construir…»).
2. **Lo que necesitas antes.** Capítulos previos, con número.
3. **El problema.** Una situación concreta que hace necesario el concepto. No se empieza por una definición.
4. **Las secciones.** Una por fila del mapa de fuentes, y todas con el mismo ritmo:
   1. la idea en dos frases;
   2. el modelo mental, con un diagrama Mermaid si hay estructura (flujos, grafos, estados);
   3. un ejemplo mínimo con su salida real;
   4. por qué funciona así, con su referencia;
   5. un caso límite.
5. **El proyecto avanza.** La pieza de la misión que permite construir este capítulo, como enunciado y guía. No se da la solución completa: el lector la construye.
6. **Resumen.** Cinco líneas como máximo.
7. **Ejercicios graduados.** De comprobación, de aplicación y un reto. Incluyen siempre el «ejercicio de construir» del catálogo. Las soluciones van en un archivo aparte (`soluciones.md` de la parte), nunca al lado del enunciado.
8. **Preguntas de examen.** La «pregunta de explicar» del catálogo, más 4 a 6 preguntas de defensa basadas en el «foco del examen», todas de tipo «por qué» o «qué pasaría si».
9. **Para profundizar y fuentes.** La lista numerada de fuentes [1], [2]… del capítulo, cada una con su enlace a la sección exacta y la fecha de consulta.

### Recuadros recurrentes

Siempre con el mismo nombre, escritos como cita Markdown con título en negrita para que se lean bien también en el `.md` descargado:

```markdown
> **Bajo el capó.** Qué pasa realmente por dentro...

> **Error típico.** El fallo que comete casi todo el mundo y cómo detectarlo...

> **En un proyecto real.** El concepto en el código de FastAPI, gentle-shell u otro repo, con enlace al archivo y al commit...

> **Ojo con la versión.** Qué cambia entre versiones...
```

### Convenciones de escritura

- **Tono.** Segunda persona, frases cortas, sin relleno ni frases motivacionales.
- **Términos en inglés.** En cursiva la primera vez, con su traducción: *staging area* (área de preparación). Después se usa el término que use la comunidad hispanohablante.
- **Citas.** Referencias numeradas entre corchetes [3] al final de la frase que apoyan.
- **Código.** Cada bloque lleva el lenguaje en la valla (`python`, `bash`…) y, en un comentario de la primera línea, la versión con la que se ejecutó.
- **Formato.** Nada de emojis. Negrita con moderación.

---

## 5. Estructura del repositorio

```
02-libro/
├── CLAUDE.md                     # Reglas cortas que se cargan en cada sesión
├── docs/
│   ├── 00-proyecto.md            # Este documento
│   ├── 01-modelo-y-esfuerzo.md   # Qué modelo y qué esfuerzo en cada fase
│   ├── 02-indice-general.md      # Índice completo del libro
│   ├── 03-indice-con-fuentes.md  # Fuentes autorizadas por capítulo y sección
│   ├── 04-catalogo-capitulos.md  # Ficha obligatoria de cada capítulo
│   ├── 05-metodo-sin-alucinaciones.md
│   ├── 06-contrato-con-la-web.md # Formato que la web espera
│   └── estado.md                 # Tablero de progreso (lo crea Claude Code)
├── contenido/                    # EL LIBRO: Markdown puro, fuente de verdad
│   ├── 00-preliminares/
│   ├── parte-01-base/
│   │   ├── _parte.md
│   │   ├── cap-01-git-por-dentro.md
│   │   └── soluciones.md
│   └── 99-apendices/
├── investigacion/                # Trabajo por capítulo (no se publica)
│   └── cap-01/
│       ├── fuentes.yaml          # Fuentes del capítulo: id fNN-MM, título y URL
│       ├── hechos.md             # Hechos atómicos con evidencia literal
│       ├── esquema.md            # Esquema que aprueba devOC
│       ├── borrador.md           # Borrador con ids [h01-003] y marcas de ejemplo
│       └── revision.md           # Informe del revisor (veredicto por frase)
├── fuentes-cache/                # Copias locales de las fuentes (en .gitignore)
├── ejemplos/                     # Código ejecutable de cada capítulo
├── scripts/                      # Verificación: evidencias, ejemplos, ids, enlaces, informe
├── tests/                        # Tests de los scripts (pytest)
└── .claude/agents/               # Subagentes del flujo (sección 7)
```

El borrador vive en `investigacion/cap-XX/borrador.md`, no en `contenido/`. `scripts/compilar_capitulo.py` lo convierte en el archivo publicable de `contenido/`: cambia los ids de hechos por referencias numeradas, genera `## Fuentes`, quita las marcas de ejemplo y valida el contrato. Así `contenido/` nunca contiene marcas internas.

### Scripts

| Script | Cortafuegos o fase | Qué hace |
| --- | --- | --- |
| `descargar_fuentes.py N` | 1 | Descarga las fuentes de `fuentes.yaml` a `fuentes-cache/` con fecha y huella; `--comprobar` avisa si una página cambió |
| `juntar_hechos.py N` | 2 | Junta `secciones/*.md` en `hechos.md` y detecta ids repetidos |
| `verificar_evidencias.py N` | 2 | Rechaza los hechos cuya evidencia no está literalmente en la copia local, o cuya fuente no está autorizada |
| `insertar_ejemplos.py borrador` | 3 | Ejecuta los ejemplos e inserta código y salida real; `--comprobar` falla si algo cambió |
| `comprobar_ids.py N` | Redacción cerrada | Cada id citado existe y pasa el cortafuegos 2 |
| `comprobar_enlaces.py rutas` | Revisión | Enlaces relativos y anclas existen; URLs externas autorizadas; `--red` las pide |
| `detectar_copia.py N` | Revisión | Busca en el borrador secuencias de 8 o más palabras copiadas de una fuente (y citas de 15 o más) |
| `informe_capitulo.py N` | Sección 8 | Métricas del capítulo; `--guardar` las escribe en `docs/estado.md` |
| `compilar_capitulo.py N` | 7 | Borrador → `contenido/` |
| `validar_contrato.py` | 7 | `contenido/` cumple `docs/06-contrato-con-la-web.md` |
| `validar_mermaid.js rutas` (Node) | Revisión | Renderiza cada bloque ```` ```mermaid ```` con Chromium y falla si alguno está roto; requiere `npm install` |

Dependencias en `requirements.txt` (Python 3.13) y `package.json` (solo Mermaid, para `validar_mermaid.js`). Tests: `python -m pytest -q`.

### Por qué esta separación

- **`contenido/` es Markdown puro, sin componentes de ningún framework.** Así el archivo que se descarga es exactamente el que se escribe, y el libro sobrevive a cualquier cambio de tecnología de la web.
- **`investigacion/` y `fuentes-cache/` son la trazabilidad.** Si devOC pregunta «¿de dónde sale esto?», la respuesta está ahí.
- **`ejemplos/` permite volver a ejecutar todo** cuando cambie una versión.

---

## 6. Relación con la web

La web vive en otro proyecto (`01-web`) y solo lee `contenido/`. El formato que espera (nombres de archivo, cabecera YAML, recuadros, enlaces) está en `docs/06-contrato-con-la-web.md`. Este proyecto no instala ni toca nada de la web.

---

## 7. Cómo se produce un capítulo

Cada capítulo pasa por estas fases, en este orden. (El 2026-11-12, con el capítulo piloto, devOC aprobó proponer el esquema antes de programar los ejemplos, porque los ejemplos dependen del esquema.) El estado se registra en `docs/estado.md`.

| Fase | Quién | Qué hace | Sale |
| --- | --- | --- | --- |
| 1. Fuentes | Claude Code | Comprueba que el capítulo tiene mapa en `docs/03-indice-con-fuentes.md`; si no, lo construye con las reglas de ese archivo | Mapa verificado |
| 2. Investigación | Cowork o Claude Code | Descarga cada fuente a `fuentes-cache/` y escribe `investigacion/cap-XX/hechos.md`: hechos atómicos, cada uno con su evidencia literal, que el script valida | Hechos verificados |
| 3. Esquema | Claude Code (redactor) | Propone en `investigacion/cap-XX/esquema.md` las secciones, el hilo narrativo, los hechos de cada sección y la lista de ejemplos que necesita; devOC lo aprueba | Esquema aprobado |
| 4. Ejemplos | Claude Code (programador) | Escribe y ejecuta en `ejemplos/cap-XX/` los ejemplos que pide el esquema y guarda la salida real y las versiones | Código que funciona |
| 5. Redacción | Claude Code (redactor) | Una sección por pasada, solo con hechos de `hechos.md` y marcas de ejemplo | Borrador |
| 6. Revisión | Claude Code, en otra pasada o con un subagente revisor | Aplica la lista de control de la sección 8 y corrige | Revisado |
| 7. Aprobación | devOC | Lee y aprueba o pide cambios | Aprobado |
| 8. Publicación | Claude Code | Convierte ids de hechos en referencias numeradas, comprueba enlaces, valida el contrato con la web y hace commit | Publicado |

### Reparto entre Claude Code y Cowork

- **Claude Code** es el responsable del repositorio. Se encarga del mapa de fuentes, los ejemplos, la redacción, la revisión y los scripts de verificación.
- **Cowork** es opcional. Su papel natural es la fase 2: leer fuentes y producir notas de investigación. Si interviene, escribe solo en `investigacion/` y sigue el mismo formato de notas, porque Claude Code redacta a partir de esos archivos.
- **devOC** interviene en tres momentos de cada capítulo: aprueba el esquema, aprueba el borrador revisado y hace el muestreo final.

### Subagentes recomendados en Claude Code

Si se definen subagentes (`.claude/agents/`), estos encajan con el flujo:

- **investigador:** fases 1 y 2.
- **redactor:** fases 3 (esquema) y 5 (redacción).
- **programador:** fase 4.
- **revisor-tecnico:** fase 6; comprueba código, salidas y exactitud contra las notas.
- **revisor-de-fuentes:** fase 6; comprueba que cada afirmación tiene referencia y que nada está copiado.

Separar redacción y revisión importa: quien acaba de escribir un texto tiende a darlo por bueno.

### Formato de los hechos

Está definido en `docs/05-metodo-sin-alucinaciones.md` (cortafuegos 2).

---

## 8. Lista de control de revisión

Un capítulo no pasa a «revisado» hasta que todo esto se cumple:

- [ ] Sigue la plantilla completa (sección 4), en orden.
- [ ] Las métricas de `docs/05-metodo-sin-alucinaciones.md` (sección 7) están en su objetivo.
- [ ] Cada afirmación técnica tiene su referencia [n], y cada [n] está en la lista de fuentes del capítulo.
- [ ] Cada fuente citada está en `docs/03-indice-con-fuentes.md` y su enlace responde.
- [ ] Ningún párrafo reproduce o sigue de cerca la redacción de una fuente. Las citas literales tienen menos de 15 palabras y van entre comillas.
- [ ] Todo el código está en `ejemplos/`, se ha ejecutado en esta revisión y su salida coincide con la del texto.
- [ ] El ejercicio de construir, la pregunta de explicar y el foco del examen del catálogo están presentes.
- [ ] Las soluciones están en `soluciones.md`, no en el capítulo.
- [ ] No hay marcas `PENDIENTE` sin resolver o, si las hay, devOC está avisado.
- [ ] La extensión está en el rango orientativo, o se justifica en `docs/estado.md` por qué no.
- [ ] El archivo cumple `docs/06-contrato-con-la-web.md` y se lee bien fuera de la web.

---

## 9. Plan por hitos

1. **Hito 0, cimientos.**
   - Estructura de la sección 5.
   - Scripts de los cortafuegos: `verificar_evidencias`, `insertar_ejemplos`, comprobación de ids, enlaces e `informe_capitulo`, con tests.
   - Subagentes con su modelo (`docs/01-modelo-y-esfuerzo.md`).
   - `docs/estado.md` creado.
2. **Hito 1, capítulo piloto.** El capítulo 1, «Git por dentro», de principio a fin con el flujo de la sección 7. devOC lo revisa a fondo; lo que se ajuste del método, la plantilla o el estilo se actualiza en este documento antes de seguir.
3. **Hito 2, Parte I completa,** con su apertura, sus soluciones y su misión.
4. **Hito 3, Parte II completa.**
5. **Hitos 4 a 10.** Partes III a IX. Cada una empieza por construir y verificar su mapa en `docs/03-indice-con-fuentes.md`, y solo después se investiga y redacta.
6. **Hito final.** Preliminares, apéndices, glosario general y créditos de las fuentes.

Ritmo: un capítulo por sesión de trabajo es lo razonable para mantener la calidad. No se trabaja en varios capítulos a la vez sin pedírselo devOC.

---

## 10. Qué no hacer

- Escribir de memoria o «completar» lo que una fuente no dice.
- Citar una URL sin abrirla, o construir una URL a ojo.
- Usar los libros de pago del catálogo como base del texto.
- Poner las soluciones junto a los ejercicios.
- Meter componentes del framework web dentro de `contenido/`.
- Dar por publicado un capítulo sin la aprobación de devOC.
- Reescribir capítulos ya aprobados sin que devOC lo pida. Si una fuente cambia, se anota en `docs/estado.md` y se propone el cambio.
- Ampliar el alcance (nuevas partes, nuevos capítulos) sin preguntar.

---

## 11. Archivos de este proyecto

- `CLAUDE.md`: reglas cortas que se cargan en cada sesión.
- `docs/00-proyecto.md`: este documento, la visión completa.
- `docs/01-modelo-y-esfuerzo.md`: modelo y esfuerzo por fase.
- `docs/02-indice-general.md`: índice completo (9 partes, 59 capítulos).
- `docs/03-indice-con-fuentes.md`: fuentes autorizadas; Partes I y II por sección y verificadas, III a IX por capítulo.
- `docs/04-catalogo-capitulos.md`: ficha obligatoria de cada capítulo.
- `docs/05-metodo-sin-alucinaciones.md`: el sistema de verificación.
- `docs/06-contrato-con-la-web.md`: lo que la web espera de `contenido/`.
- `docs/estado.md`: tablero de progreso, que Claude Code crea en el hito 0.

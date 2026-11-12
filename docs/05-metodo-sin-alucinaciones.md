# Cómo escribir el libro sin alucinaciones

Este es el documento más importante del proyecto. Explica por qué no se escribe el libro con un único prompt y cuál es el sistema que sustituye a ese prompt.

---

## 1. Por qué un prompt con todo no funciona

Si a un modelo le pides «escribe el capítulo 10 sobre asyncio con estas fuentes», pasan tres cosas:

1. **Mezcla lo que leyó con lo que «sabe».** El texto sale fluido, pero no hay forma de distinguir qué frase viene de la documentación y cuál es memoria del modelo, que puede estar desactualizada o ser simplemente falsa.
2. **Las citas se vuelven decorativas.** El modelo pone [3] al final de una frase porque «suena» a que viene de la fuente 3, no porque lo haya comprobado.
3. **El código y su salida se inventan juntos.** La salida que aparece debajo de un ejemplo es la que el modelo espera, no la que produce el programa.

La solución no es pedirle al modelo que tenga más cuidado. Es **cambiar el proceso** para que una invención no pueda llegar al texto sin que algo la detecte, y que ese algo sea, siempre que se pueda, un script y no otro modelo.

---

## 2. Los cinco cortafuegos

Cada capítulo pasa por cinco barreras. Las tres primeras son deterministas (scripts): no dependen de que el modelo acierte.

| # | Cortafuegos | Qué detiene | Quién lo aplica |
| --- | --- | --- | --- |
| 1 | Copia local de cada fuente | Citar páginas que no se han leído o que han cambiado | Script |
| 2 | Hechos con evidencia literal | Afirmaciones que la fuente no dice | Script |
| 3 | Código y salida insertados por script | Salidas inventadas | Script |
| 4 | Revisión adversarial frase a frase | Paráfrasis que deforman el hecho | Otro modelo, en sesión limpia |
| 5 | Muestreo humano | Lo que se haya escapado | devOC |

### Cortafuegos 1: copia local de cada fuente

Antes de usar una fuente, se descarga su texto a `fuentes-cache/<capitulo>/<id>.md` con la URL, la fecha y una huella (hash) en la cabecera.

Reglas:

- Esta carpeta va en `.gitignore`: es una herramienta de verificación privada, no se publica ni se redistribuye.
- Si la página ya no existe o su contenido cambió mucho, el capítulo se marca para revisar.

Sirve para dos cosas: el redactor y el revisor trabajan sobre el mismo texto exacto, y meses después se puede saber qué decía la fuente cuando se escribió el capítulo.

### Cortafuegos 2: hechos con evidencia literal

La investigación no produce resúmenes: produce **hechos atómicos**, uno por línea, en `investigacion/cap-XX/hechos.md`:

```markdown
## 10.1 Modelo mental: el bucle de eventos

- id: h10-003
  hecho: Llamar a una función async no ejecuta su cuerpo; devuelve un objeto corrutina.
  evidencia: "does not execute the print statement; instead, it creates a coroutine object"
  fuente: f10-01
  ancla: https://docs.python.org/es/3/howto/a-conceptual-overview-of-asyncio.html
  consultada: 2026-11-12
```

Un script (`scripts/verificar_evidencias.py`) comprueba que **cada `evidencia` aparece literalmente en la copia local** de su fuente:

- Normaliza espacios y comillas, nada más.
- Si la cadena no está, el hecho se rechaza.
- Un modelo no puede «colar» una evidencia inventada, porque el script no le cree: busca el texto.

Las evidencias son citas cortas internas de verificación. Nunca pasan al libro tal cual.

### Cortafuegos 3: código y salida insertados por script

En el borrador, el redactor no escribe código ni salidas a mano. Escribe una marca:

```markdown
<!-- ejemplo: ejemplos/cap-10/tareas_concurrentes.py -->
```

Un script (`scripts/insertar_ejemplos.py`) hace el resto:

1. Ejecuta el archivo con la versión fijada.
2. Captura la salida real.
3. Sustituye la marca por el bloque de código, la versión y la salida.

Si el programa falla, el build falla. Así es imposible que haya una salida inventada en el libro.

### Cortafuegos 4: revisión adversarial frase a frase

Una sesión distinta, sin el historial del redactor (o un subagente revisor), recibe cada frase técnica del capítulo junto con los hechos que cita y el fragmento de la copia local. Para cada frase responde una de tres cosas:

- **SOPORTADA**
- **PARCIAL**, explicando qué sobra
- **NO SOPORTADA**

Lo que no sale SOPORTADA se corrige o se elimina; no se discute.

El revisor tiene una instrucción explícita: **su trabajo es encontrar fallos**. Un informe sin ningún hallazgo en un capítulo largo es sospechoso y se repite con otro enfoque.

### Cortafuegos 5: muestreo humano

devOC elige al azar cinco afirmaciones del capítulo y las comprueba él mismo contra la fuente original. Si falla una, se revisa el capítulo entero.

Además lee el capítulo completo antes de aprobarlo; eso ya forma parte del flujo.

---

## 3. Redacción cerrada

El redactor trabaja con reglas que lo encierran dentro de las notas:

1. **Solo puede usar hechos de `hechos.md`.** En el borrador, cada frase técnica termina con los ids de los hechos que la sostienen: `[h10-003]`. Un script comprueba que todos los ids existen y han pasado el cortafuegos 2. Al publicar, los ids se convierten en referencias numeradas [1], [2]…
2. **Puede escribir sin hecho** las transiciones, las analogías, las preguntas al lector y la narración del problema. Lo que no puede es afirmar nada técnico sin id.
3. **Si necesita un hecho que no está,** no lo inventa: escribe `> PENDIENTE: falta hecho sobre ...` y sigue. Un PENDIENTE es un resultado correcto, no un fallo. Se resuelve volviendo a la fase de investigación.
4. **Nunca completa con memoria,** ni siquiera algo que «todo el mundo sabe». Si es tan sabido, estará en la documentación y se puede extraer como hecho.
5. **Si dos fuentes se contradicen,** no elige en silencio. Registra el conflicto en las notas, prefiere la fuente oficial más reciente y, si importa al lector, lo cuenta en un recuadro «Ojo con la versión».

---

## 3 bis. No copiar: la otra cara de la fidelidad

Lección del capítulo piloto (2026-11-12). Los cortafuegos anteriores impiden inventar, pero empujan a copiar: un hecho fiel se parece a su fuente, y un borrador que transcribe hechos acaba calcando la redacción, el orden y los ejemplos del capítulo de origen. El revisor de fuentes encontró 49 casos en el capítulo 1. Para evitarlo:

1. **Los hechos son respaldo, no texto.** El redactor escribe cada párrafo a partir de lo que muestra un ejemplo propio o de la idea que quiere explicar, con sus palabras, y después cita los hechos que lo sostienen. Nunca redacta retocando el texto de un hecho.
2. **El esquema no sigue el índice de una fuente.** Cada sección se organiza alrededor del problema y del repositorio de ejemplo del capítulo. Si una sección recorre los mismos pasos, en el mismo orden, que un capítulo ajeno, hay que reordenarla.
3. **Los ejemplos son propios.** No se adapta un ejemplo de una fuente cambiando nombres o lenguaje. Se parte de la misión y del repositorio del capítulo. Si una demostración ajena es insustituible, se dice en el texto de quién es y se consulta a devOC, porque varias fuentes tienen licencias que se heredan (Pro Git, MDN y Composing Programs son CC BY-SA o BY-NC-SA).
4. **Un script lo vigila.** `scripts/detectar_copia.py` busca en el borrador secuencias de 8 o más palabras que aparecen tal cual en una copia local (y citas entre comillas de 15 o más). Es una métrica bloqueante de `informe_capitulo.py`. No detecta la paráfrasis cercana ni el calco de estructura: eso sigue siendo trabajo del revisor de fuentes.
5. **La versión manda sobre la fuente.** Cuando una fuente antigua describe un comportamiento, se comprueba con la versión fijada del capítulo (un ejemplo ejecutado) y con la documentación actual antes de afirmarlo. En el piloto, tres afirmaciones fieles a Pro Git en español eran falsas con Git 2.43.

---

## 4. Trabajo en piezas pequeñas

Ningún paso trabaja con más de una sección a la vez. Un capítulo de 7 secciones son unas 25 o 30 pasadas pequeñas, no una grande:

- **Cada fase en una sesión limpia.** La investigación, la redacción y la revisión no comparten conversación: lo que pasa de una a otra son archivos (`hechos.md`, borrador, informe de revisión). Así ningún paso arrastra suposiciones del anterior.
- **Una sección por pasada de redacción.** Al terminar cada sección se ejecutan los scripts de los cortafuegos 2 y 3 antes de seguir.
- **Puntos de control con devOC:**
  1. Al aprobar el esquema del capítulo (secciones e hilo narrativo), antes de redactar.
  2. Al terminar el borrador revisado.
  3. Con el muestreo final.

  Tres intervenciones por capítulo bastan; no hace falta supervisar cada paso.

---

## 5. Versiones fijadas

Muchas fuentes de este libro cambian rápido. Durante la verificación ya han aparecido casos:

- **MCP:** la versión del protocolo 2026-07-28 cambia el descubrimiento y declara obsoleto *sampling*.
- **Agno:** tiene documentación separada para su versión 1.
- **OpenCode:** su configuración V2 de permisos usa otra sintaxis.
- **mouredev/hello-python:** el curso backend despliega en un servicio, Deta, que ya no existe.

Por eso cada capítulo declara en su cabecera las versiones exactas de lo que explica:

```yaml
versiones:
  python: "3.13"
  fastapi: "0.x.y"
  mcp_protocolo: "2026-07-28"
```

Los ejemplos se ejecutan con esas versiones. Cuando una fuente de comunidad o un libro usa una versión anterior, la diferencia se cuenta en «Ojo con la versión».

---

## 6. Fuentes de comunidad (mouredev, midudev)

Sus cursos son valiosos para practicar y para ver cómo se explica algo en español, pero cumplen otro papel que la documentación oficial:

- **Sirven para:** ejercicios extra, ideas de ejemplos, terminología en español y la sección «Para profundizar».
- **No sirven para:** respaldar una afirmación técnica. Si un curso dice algo sobre FastAPI, se cita la documentación de FastAPI que lo confirma; si no la hay, no se afirma.
- **Su código:** antes de reutilizarlo se comprueba la licencia del repositorio. Por defecto se enlaza, no se copia.

---

## 7. Métricas de cada capítulo

`scripts/informe_capitulo.py` genera estas cifras y se guardan en `docs/estado.md`. Un capítulo con cualquiera de las cinco primeras métricas fuera de su objetivo no puede pasar a «revisado».

| Métrica | Objetivo |
| --- | --- |
| Frases técnicas sin id de hecho | 0 |
| Evidencias que no aparecen en su fuente | 0 |
| Ejemplos que fallan al ejecutarse | 0 |
| Frases NO SOPORTADAS sin resolver | 0 |
| Fragmentos literales de una fuente (`detectar_copia.py`) | 0 |
| PENDIENTES abiertos | Los que haya, siempre visibles y comunicados a devOC |
| Afirmaciones del muestreo humano que fallan | 0 |

---

## 8. Resumen en una frase

**El modelo propone y los scripts verifican.** Ninguna afirmación llega al libro sin una cita literal localizada en una fuente descargada, ningún resultado de código sin haberse ejecutado, y ninguna frase sin que un revisor independiente haya intentado tumbarla.

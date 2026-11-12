# Índice por capítulos con fuentes

De aquí sale cada capítulo. Es la única lista de fuentes autorizadas; una fuente nueva se añade aquí, verificada, antes de usarse.

## Leyenda y nivel de detalle

- **✔ verificada**: la página se abrió o se vio en resultados de búsqueda el 11 o 12 de noviembre de 2026 y trata el tema.
- **◯ candidata**: fuente oficial probable, sin abrir todavía. Claude Code la verifica (y concreta la URL exacta) en la fase 1 del capítulo.
- **Comunidad en español**: cursos de mouredev y midudev. Sirven para practicar, para ejemplos y para vocabulario en español, pero **no respaldan afirmaciones técnicas**: esas se citan siempre de la fuente oficial. Antes de reutilizar código suyo se comprueba la licencia del repositorio; por defecto se enlaza, no se copia.
- **Partes I y II**: detalle por sección, ya verificado.
- **Partes III a IX**: detalle por capítulo. En la fase 1 de cada capítulo, Claude Code baja este mapa al nivel de sección con el formato de las Partes I y II.

## Fuentes de comunidad añadidas

| Fuente | Qué aporta | Dónde se usa |
| --- | --- | --- |
| [mouredev/hello-git](https://github.com/mouredev/hello-git) ✔ | Curso de Git y GitHub desde cero | Capítulos 1 y 2 |
| [mouredev/hello-python](https://github.com/mouredev/hello-python) ✔ | Python básico, intermedio, testing y backend con FastAPI | Capítulos 6 a 8, 11 a 13, 15 y 19 |
| [mouredev/roadmap-retos-programacion](https://github.com/mouredev/roadmap-retos-programacion) ✔ | Retos semanales para practicar lógica en cualquier lenguaje | Ejercicios extra de las Partes II y IX |
| [midudev/curso-node-js](https://github.com/midudev/curso-node-js) ✔ | Curso de Node.js desde cero | Capítulos 43 y 44 |
| [midudev/libros-programacion-gratis](https://github.com/midudev/libros-programacion-gratis) ✔ | Lista de libros de programación gratis en español | Buscar fuentes en español; cada libro se verifica aparte antes de entrar aquí |

No se han mapeado otros repositorios de ambos perfiles: GitHub no permite leer el listado completo de forma automática, así que solo figuran los que he podido comprobar. Si quieres alguno más (por ejemplo, el curso de React de midudev, que no encaja en el roadmap actual), dímelo y lo verifico.

---

## Parte I: El oficio

Fuentes base:

- [Pro Git en español](https://git-scm.com/book/es/v2), licencia CC BY-NC-SA 3.0.
- [The Missing Semester 2026](https://missing.csail.mit.edu/2026/), MIT.
- [MDN: HTTP](https://developer.mozilla.org/es/docs/Web/HTTP), licencia CC BY-SA.

### Capítulo 1: Git por dentro

| Sección | Principal | Profundizar |
| --- | --- | --- |
| 1.1 Qué es el control de versiones | [Pro Git 1.1](https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones) | [Pro Git 1.2](https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Una-breve-historia-de-Git) |
| 1.2 Fotos, no diferencias; los tres estados | [Pro Git 1.3](https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git) | [Pro Git 2.2](https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio) |
| 1.3 Leer y deshacer el historial | [Pro Git 2.3](https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones) | [Pro Git 2.4](https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas) |
| 1.4 Las ramas son punteros | [Pro Git 3.1](https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F) | [Pro Git 3.2](https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar), [3.3](https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Gesti%c3%b3n-de-Ramas) |
| 1.5 Rebase y reescribir historia | [Pro Git 3.6](https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado) | [Pro Git 7.6](https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia) |
| 1.6 Bajo el capó: objetos y referencias | [Pro Git 10.2](https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git), [10.3](https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git) | [Pro Git 10.1](https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Fontaner%c3%ada-y-porcelana) |
| 1.7 reset sin miedo | [Pro Git 7.7](https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado) | [Missing Semester: Version Control and Git](https://missing.csail.mit.edu/2026/version-control/) |

Comunidad: [mouredev, Hello Git: curso de Git y GitHub desde cero](https://github.com/mouredev/hello-git). Complemento en español para practicar comandos.

Fuentes añadidas el 2026-11-12 para cubrir lo que la edición en español de Pro Git no trata o trata con una versión antigua de Git (ver `investigacion/cap-01/huecos.md`). La documentación de referencia de git-scm.com describe la última versión de Git; los ejemplos del libro se ejecutan con la versión fijada en la cabecera del capítulo.

| Sección | Fuente | Estado |
| --- | --- | --- |
| 1.2, 1.4 | [Documentación de Git: git-init](https://git-scm.com/docs/git-init) (rama inicial, `init.defaultBranch`) | ✔ |
| 1.2 | [Documentación de Git: hash-function-transition](https://git-scm.com/docs/hash-function-transition) (SHA-1 y SHA-256) | ✔ |
| 1.3, 1.7 | [Documentación de Git: git-restore](https://git-scm.com/docs/git-restore) | ✔ |
| 1.4 | [Documentación de Git: git-switch](https://git-scm.com/docs/git-switch) | ✔ |
| 1.4, 1.7 | [Documentación de Git: git-checkout](https://git-scm.com/docs/git-checkout) (HEAD desacoplado) | ✔ |
| 1.4 | [Documentación de Git: git-merge](https://git-scm.com/docs/git-merge) (`--abort`) | ✔ |
| 1.5 | [Documentación de Git: git-rebase](https://git-scm.com/docs/git-rebase) (`--abort`, `--skip`, `drop`) | ✔ |
| 1.5 | [Documentación de Git: git-revert](https://git-scm.com/docs/git-revert) | ✔ |
| 1.7 | [Documentación de Git: git-reflog](https://git-scm.com/docs/git-reflog) | ✔ |
| 1.7 | [Pro Git 10.7, Mantenimiento y recuperación de datos](https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Mantenimiento-y-recuperaci%c3%b3n-de-datos) | ✔ |
| 1.4 | [Documentación de Git: merge-strategies](https://git-scm.com/docs/merge-strategies) (estrategia `ort`) | ✔ |
| 1.2, 1.3, 1.5, 1.7 | [Pro Git 7.1, Revisión por selección](https://git-scm.com/book/es/v2/Herramientas-de-Git-Revisi%C3%B3n-por-selecci%C3%B3n) (hash abreviado, `HEAD~N`, `^`) | ✔ |
| 1.2, 1.3, 1.6 | [Documentación de Git: gitrevisions](https://git-scm.com/docs/gitrevisions) (`~`, `^`, `^{tree}`, `@{n}`) | ✔ |
| 1.2, 1.3 | [Documentación de Git: git-log](https://git-scm.com/docs/git-log) (`--oneline`) | ✔ |
| Apertura | [Pro Git 1.6, Configurando Git por primera vez](https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Configurando-Git-por-primera-vez) | ✔ |
| 1.3, 1.4 | [Documentación de Git: git-commit](https://git-scm.com/docs/git-commit) (`--no-edit`, mensaje tras un conflicto) | ✔ |
| 1.5 | [Documentación de Git: git-diff](https://git-scm.com/docs/git-diff) (comparar dos commits o ramas) | ✔ |
| 1.5 | [Documentación de Git: git-pull](https://git-scm.com/docs/git-pull) (ramas divergentes, `pull.rebase`) | ✔ |
| 1.7 | [Documentación de Git: git-reset](https://git-scm.com/docs/git-reset) (modos, reset con ruta) | ✔ |

### Capítulo 2: Flujo de contribución

| Sección | Principal | Profundizar |
| --- | --- | --- |
| 2.1 Remotos y ramas remotas | [Pro Git 2.5](https://git-scm.com/book/es/v2/Fundamentos-de-Git-Trabajar-con-Remotos) | [Pro Git 3.5](https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Ramas-Remotas) |
| 2.2 Flujos de trabajo distribuidos | [Pro Git 5.1](https://git-scm.com/book/es/v2/Git-en-entornos-distribuidos-Flujos-de-trabajo-distribuidos) | [Pro Git 3.4](https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Flujos-de-Trabajo-Ramificados) |
| 2.3 Contribuir a un proyecto | [Pro Git 5.2](https://git-scm.com/book/es/v2/Git-en-entornos-distribuidos-Contribuyendo-a-un-Proyecto) | [Pro Git 5.3](https://git-scm.com/book/es/v2/Git-en-entornos-distribuidos-Manteniendo-un-proyecto) |
| 2.4 Fork y pull request en GitHub | [Pro Git 6.2](https://git-scm.com/book/es/v2/GitHub-Participando-en-Proyectos) | [GitHub: proponer cambios con pull requests](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests) |
| 2.5 Mantener el PR al día y responder revisiones | [GitHub: crear pull requests](https://docs.github.com/es/pull-requests/how-tos/create-pull-requests?tool=webui) | [Pro Git 7.2](https://git-scm.com/book/es/v2/Herramientas-de-Git-Organizaci%c3%b3n-interactiva) |
| 2.6 Contribuir sin escribir código | [GitHub: formas de colaborar](https://docs.github.com/es/github/getting-started-with-github/exploring-projects-on-github/finding-ways-to-contribute-to-open-source-on-github) | [freeCodeCamp: cómo contribuir (español)](https://github.com/freeCodeCamp/how-to-contribute-to-open-source/blob/master/README-ES.md) |

Comunidad: [mouredev, Hello Git: GitHub, ramas remotas y flujo de colaboración](https://github.com/mouredev/hello-git). Complemento en español.

### Capítulo 3: Terminal y procesos

| Sección | Principal | Profundizar |
| --- | --- | --- |
| 3.1 La shell: comandos, rutas y PATH | [Missing Semester: Introduction to the Shell](https://missing.csail.mit.edu/2026/course-shell/) | [Pro Git 1.4](https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-La-L%c3%adnea-de-Comandos) |
| 3.2 Procesos, señales, variables de entorno | [Missing Semester: Command-line Environment](https://missing.csail.mit.edu/2026/command-line-environment/) | [Pro Git 10.8](https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Variables-de-entorno) |
| 3.3 Tu entorno de desarrollo | [Missing Semester: Development Environment and Tools](https://missing.csail.mit.edu/2026/development-environment/) | |
| 3.4 Depurar y medir | [Missing Semester: Debugging and Profiling](https://missing.csail.mit.edu/2026/debugging-profiling/) | |

Vídeo complementario: [lista de Missing Semester 2026 en YouTube](https://www.youtube.com/playlist?list=PLyzOVJj3bHQunmnnTXrNbZnBaCA-ieK4L). No es fuente citable mientras no se disponga de la transcripción; las notas escritas de cada clase sí lo son.

### Capítulo 4: HTTP de verdad

| Sección | Principal | Profundizar |
| --- | --- | --- |
| 4.1 Cliente, servidor y sin estado | [MDN: generalidades de HTTP](https://developer.mozilla.org/es/docs/Web/HTTP/Guides/Overview) | [MDN: evolución de HTTP](https://developer.mozilla.org/es/docs/Web/HTTP/Guides/Evolution_of_HTTP) |
| 4.2 Anatomía de mensajes y sesión | [MDN: mensajes HTTP](https://developer.mozilla.org/es/docs/Web/HTTP/Guides/Messages) | [MDN: una sesión típica](https://developer.mozilla.org/es/docs/Web/HTTP/Guides/Session) |
| 4.3 Métodos e idempotencia | [MDN: métodos de petición](https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Methods) | [PUT](https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Methods/PUT), [PATCH](https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Methods/PATCH), [POST](https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Methods/POST) |
| 4.4 Códigos de estado | [MDN: códigos de estado](https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Status) | [401](https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Status/401), [403](https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Status/403), [422](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/422), [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/429) |
| 4.5 Cabeceras y tipos de contenido | [MDN: cabeceras](https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Headers) | [Content-Type](https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Headers/Content-Type), [tipos MIME](https://developer.mozilla.org/es/docs/Web/HTTP/Guides/MIME_types) |
| 4.6 Caché y peticiones condicionales | [MDN: caché HTTP](https://developer.mozilla.org/es/docs/Web/HTTP/Guides/Caching) | [MDN: peticiones condicionales](https://developer.mozilla.org/es/docs/Web/HTTP/Guides/Conditional_requests) |
| 4.7 Autenticación y CORS | [MDN: autenticación HTTP](https://developer.mozilla.org/es/docs/Web/HTTP/Guides/Authentication) | [MDN: CORS](https://developer.mozilla.org/es/docs/Web/HTTP/Guides/CORS) |
| 4.8 Conexiones | [MDN: gestión de la conexión en HTTP/1.x](https://developer.mozilla.org/es/docs/Web/HTTP/Guides/Connection_management_in_HTTP_1.x) | |

### Capítulo 5: Leer código ajeno

| Sección | Principal | Profundizar |
| --- | --- | --- |
| 5.1 Moverse por el historial | [Pro Git 7.1](https://git-scm.com/book/es/v2/Herramientas-de-Git-Revisi%c3%b3n-por-selecci%c3%b3n) | [Pro Git 2.3](https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones) |
| 5.2 Buscar en el código y en la historia | [Pro Git 7.5](https://git-scm.com/book/es/v2/Herramientas-de-Git-Buscando) | |
| 5.3 blame y bisect | [Pro Git 7.10](https://git-scm.com/book/es/v2/Herramientas-de-Git-Haciendo-debug-con-Git) | [Missing Semester: Debugging and Profiling](https://missing.csail.mit.edu/2026/debugging-profiling/) |
| 5.4 Calidad de código: qué buscar al leer | [Missing Semester: Code Quality](https://missing.csail.mit.edu/2026/code-quality/) | |
| 5.5 Práctica en un repo real | [Repositorio de FastAPI](https://github.com/fastapi/fastapi): código para leer, no fuente de texto | |

---

## Parte II: Python profundo

Fuentes base:

- [Tutorial oficial de Python en español](https://docs.python.org/es/3/tutorial/index.html), licencia PSF.
- HOWTO oficiales de Python.
- [Composing Programs](https://www.composingprograms.com) (Berkeley), licencia CC BY-SA 3.0.

### Capítulo 6: Modelo de objetos

| Sección | Principal | Profundizar |
| --- | --- | --- |
| 6.1 Nombres que apuntan a objetos | [Tutorial 9.1](https://docs.python.org/es/3/tutorial/classes.html#a-word-about-names-and-objects) | [Glosario](https://docs.python.org/es/3/glossary.html) |
| 6.2 Ámbitos y espacios de nombres | [Tutorial 9.2](https://docs.python.org/es/3/tutorial/classes.html#python-scopes-and-namespaces) | |
| 6.3 Estructuras mutables e inmutables | [Tutorial 5](https://docs.python.org/es/3/tutorial/datastructures.html) | [Tutorial 5.8](https://docs.python.org/es/3/tutorial/datastructures.html#comparing-sequences-and-other-types) |
| 6.4 Clases, instancias y variables de clase | [Tutorial 9.3](https://docs.python.org/es/3/tutorial/classes.html#a-first-look-at-classes) | [Tutorial 9.3.5](https://docs.python.org/es/3/tutorial/classes.html#class-and-instance-variables) |
| 6.5 Herencia | [Tutorial 9.5](https://docs.python.org/es/3/tutorial/classes.html#inheritance) | [Tutorial 9.6](https://docs.python.org/es/3/tutorial/classes.html#private-variables) |
| 6.6 Métodos especiales | [Referencia: modelo de datos](https://docs.python.org/es/3/reference/datamodel.html) (abrir antes de usar) | [Composing Programs, capítulo 2](https://www.composingprograms.com) |

Comunidad: [mouredev, Hello Python: fundamentos (clases)](https://github.com/mouredev/hello-python). Complemento en español.

### Capítulo 7: Funciones, closures y decoradores

| Sección | Principal | Profundizar |
| --- | --- | --- |
| 7.1 Definir funciones y valores por omisión | [Tutorial 4.8 y 4.9](https://docs.python.org/es/3/tutorial/controlflow.html#more-on-defining-functions) | [Tutorial 4.9.1](https://docs.python.org/es/3/tutorial/controlflow.html#default-argument-values) |
| 7.2 Parámetros especiales, *args y **kwargs | [Tutorial 4.9.3](https://docs.python.org/es/3/tutorial/controlflow.html#special-parameters) | [Tutorial 4.9.4](https://docs.python.org/es/3/tutorial/controlflow.html#arbitrary-argument-lists) |
| 7.3 Funciones de orden superior y closures | [Composing Programs 1.6](https://composingprograms.com/pages/16-higher-order-functions.html) | |
| 7.4 Decoradores | [Composing Programs 1.6](https://composingprograms.com/pages/16-higher-order-functions.html) | [HOWTO de programación funcional](https://docs.python.org/es/3/howto/functional.html) |
| 7.5 Anotaciones de función | [Tutorial 4.9.8](https://docs.python.org/es/3/tutorial/controlflow.html#function-annotations) | |

Comunidad: [mouredev, Hello Python: intermedio (lambdas, funciones de orden superior)](https://github.com/mouredev/hello-python). Complemento en español.

### Capítulo 8: Iteradores y generadores

| Sección | Principal | Profundizar |
| --- | --- | --- |
| 8.1 Técnicas de iteración y comprensiones | [Tutorial 5.6](https://docs.python.org/es/3/tutorial/datastructures.html#looping-techniques) | [Tutorial 5.1.3](https://docs.python.org/es/3/tutorial/datastructures.html#list-comprehensions) |
| 8.2 El protocolo de iteración | [Tutorial 9.8](https://docs.python.org/es/3/tutorial/classes.html#iterators) | [HOWTO funcional](https://docs.python.org/es/3/howto/functional.html) |
| 8.3 Generadores y expresiones generadoras | [Tutorial 9.9 y 9.10](https://docs.python.org/es/3/tutorial/classes.html#generators) | [HOWTO funcional](https://docs.python.org/es/3/howto/functional.html) |
| 8.4 itertools y functools | [HOWTO funcional](https://docs.python.org/es/3/howto/functional.html) | [Tutorial 11.7](https://docs.python.org/es/3/tutorial/stdlib2.html#tools-for-working-with-lists) |

Comunidad: [mouredev, Hello Python: intermedio (list comprehension)](https://github.com/mouredev/hello-python). Complemento en español.

### Capítulo 9: Tipos y validación

| Sección | Principal | Profundizar |
| --- | --- | --- |
| 9.1 Anotaciones y el módulo typing | [typing](https://docs.python.org/es/3/library/typing.html) (abrir antes de usar) | [Tutorial 4.9.8](https://docs.python.org/es/3/tutorial/controlflow.html#function-annotations) |
| 9.2 dataclasses | [dataclasses](https://docs.python.org/es/3/library/dataclasses.html) (abrir antes de usar) | |
| 9.3 Validar en tiempo de ejecución con Pydantic | [Pydantic: modelos](https://docs.pydantic.dev/usage/models) | |

### Capítulo 10: Asincronía

| Sección | Principal | Profundizar |
| --- | --- | --- |
| 10.1 Modelo mental: el bucle de eventos | [HOWTO: visión conceptual de asyncio](https://docs.python.org/es/3/howto/a-conceptual-overview-of-asyncio.html) | |
| 10.2 Corrutinas, tareas y gather | [Corrutinas y tareas](https://docs.python.org/es/3/library/asyncio-task.html) | |
| 10.3 Hilos frente a async | [Tutorial 11.4](https://docs.python.org/es/3/tutorial/stdlib2.html#multi-threading) | |

### Capítulo 11: Errores y gestores de contexto

| Sección | Principal | Profundizar |
| --- | --- | --- |
| 11.1 Capturar y lanzar excepciones | [Tutorial 8.3 y 8.4](https://docs.python.org/es/3/tutorial/errors.html#handling-exceptions) | |
| 11.2 Encadenar y definir excepciones propias | [Tutorial 8.5 y 8.6](https://docs.python.org/es/3/tutorial/errors.html#exception-chaining) | [Tutorial 8.9 y 8.10](https://docs.python.org/es/3/tutorial/errors.html#raising-and-handling-multiple-unrelated-exceptions) |
| 11.3 Limpieza y la sentencia with | [Tutorial 8.7 y 8.8](https://docs.python.org/es/3/tutorial/errors.html#defining-clean-up-actions) | |
| 11.4 Escribir gestores de contexto | [contextlib](https://docs.python.org/es/3/library/contextlib.html) (abrir antes de usar) | |

Comunidad: [mouredev, Hello Python: excepciones y tipos de error](https://github.com/mouredev/hello-python). Complemento en español.

### Capítulo 12: Testing con pytest

| Sección | Principal | Profundizar |
| --- | --- | --- |
| 12.1 Control de calidad en la biblioteca estándar | [Tutorial 10.11](https://docs.python.org/es/3/tutorial/stdlib.html#quality-control) | |
| 12.2 Estructura de un proyecto con tests | [pytest: buenas prácticas de integración](https://docs.pytest.org/goodpractices.html) | |
| 12.3 Fixtures, parametrize y dobles de prueba | **Pendiente:** buscar y verificar la página oficial de pytest | |

Comunidad: [mouredev, Hello Python: taller de introducción a testing](https://github.com/mouredev/hello-python). Complemento en español.

### Capítulo 13: Módulos, paquetes y entornos

| Sección | Principal | Profundizar |
| --- | --- | --- |
| 13.1 Módulos y ruta de búsqueda | [Tutorial 6.1](https://docs.python.org/es/3/tutorial/modules.html#the-module-search-path) | |
| 13.2 Paquetes | [Tutorial 6.4](https://docs.python.org/es/3/tutorial/modules.html#packages) | |
| 13.3 Entornos virtuales | [Tutorial 12](https://docs.python.org/es/3/tutorial/venv.html) | |
| 13.4 pyproject.toml y publicar | [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/) | [pytest: diseño src](https://docs.pytest.org/goodpractices.html) |

Comunidad: [mouredev, Hello Python: módulos](https://github.com/mouredev/hello-python). Complemento en español.

---


---

## Parte III: Backend con FastAPI

### Capítulo 14: Diseño de APIs REST

Secciones: 14.1 Recursos y URIs · 14.2 Verbos y su semántica · 14.3 Códigos de estado y formato de errores · 14.4 Paginación, filtros y versionado · 14.5 El contrato: OpenAPI

| Fuente | Estado |
| --- | --- |
| [MDN: métodos de petición](https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Methods) | ✔ |
| [MDN: códigos de estado](https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Status) | ✔ |
| [FastAPI: características (OpenAPI y validación)](https://fastapi.tiangolo.com/es/features/) | ✔ |
| Especificación OpenAPI | ◯ |

### Capítulo 15: Endpoints y routing

Secciones: 15.1 Primera aplicación y path operations · 15.2 Parámetros de ruta · 15.3 Parámetros de consulta · 15.4 Cuerpo de la petición · 15.5 response_model y status_code · 15.6 Routers y aplicaciones grandes

| Fuente | Estado |
| --- | --- |
| [FastAPI: características](https://fastapi.tiangolo.com/es/features/) | ✔ |
| [Tutorial de FastAPI en español: Primeros pasos, Parámetros de Path y de Query, Request Body, Código de estado, Aplicaciones más grandes](https://fastapi.tiangolo.com/es/) | ◯ |
| [mouredev, Hello Python: curso Backend (lecciones de path, query, POST/PUT/DELETE, status codes y routers)](https://github.com/mouredev/hello-python) (comunidad; usa MongoDB y despliegue en Deta; el propio curso avisa de que Deta ya no existe) | ✔ |

Ojo con la versión: El curso Backend de Hello Python despliega en Deta, servicio que ya no existe según el propio curso.

### Capítulo 16: Validación con Pydantic

Secciones: 16.1 Modelos de entrada y de salida · 16.2 Validadores propios · 16.3 Errores 422 y manejo de errores · 16.4 Un modelo por operación (crear, leer, actualizar)

| Fuente | Estado |
| --- | --- |
| [Pydantic: modelos](https://docs.pydantic.dev/usage/models) | ✔ |
| [MDN: 422](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/422) | ✔ |
| [Tutorial de FastAPI: Manejo de Errores, Body actualizaciones](https://fastapi.tiangolo.com/es/) | ◯ |

### Capítulo 17: Inyección de dependencias

Secciones: 17.1 Depends: qué problema resuelve · 17.2 Clases como dependencias y subdependencias · 17.3 Dependencias con yield · 17.4 Sustituir dependencias en tests

| Fuente | Estado |
| --- | --- |
| [FastAPI: obtener usuario actual (dependencias en cadena)](https://fastapi.tiangolo.com/es/tutorial/security/get-current-user/) | ✔ |
| [Tutorial de FastAPI: Dependencias, Clases como dependencias, Sub-dependencias, Dependencias con yield](https://fastapi.tiangolo.com/es/) | ◯ |
| [FastAPI avanzado: Probando dependencias con overrides](https://fastapi.tiangolo.com/es/) | ◯ |

### Capítulo 18: Persistencia con SQLAlchemy y PostgreSQL

Secciones: 18.1 SQL y PostgreSQL lo justo · 18.2 SQLAlchemy 2.0: engine y sesión · 18.3 Modelos ORM y relaciones · 18.4 Transacciones · 18.5 Migraciones con Alembic · 18.6 El problema N+1 y la carga de relaciones · 18.7 Integración con FastAPI

| Fuente | Estado |
| --- | --- |
| [SQLAlchemy 2.0: Unified Tutorial](https://docs.sqlalchemy.org) | ◯ |
| Alembic: tutorial | ◯ |
| PostgreSQL: tutorial oficial | ◯ |
| [Tutorial de FastAPI: Bases de Datos SQL](https://fastapi.tiangolo.com/es/) | ◯ |

### Capítulo 19: Autenticación y autorización

Secciones: 19.1 Autenticación frente a autorización · 19.2 Guardar contraseñas: hashing · 19.3 OAuth2 con flujo password · 19.4 JWT: qué contiene y qué garantiza · 19.5 Scopes y roles

| Fuente | Estado |
| --- | --- |
| [FastAPI: seguridad, primeros pasos](https://fastapi.tiangolo.com/es/tutorial/security/first-steps/) | ✔ |
| [FastAPI: obtener usuario actual](https://fastapi.tiangolo.com/es/tutorial/security/get-current-user/) | ✔ |
| [FastAPI: OAuth2 con password, hashing y JWT](https://fastapi.tiangolo.com/es/tutorial/security/oauth2-jwt/) | ✔ |
| [MDN: autenticación HTTP](https://developer.mozilla.org/es/docs/Web/HTTP/Guides/Authentication) | ✔ |
| [mouredev, Hello Python: lecciones OAuth2 y OAuth2 JWT](https://github.com/mouredev/hello-python) (comunidad; contrastar con la versión actual del tutorial oficial, que ha cambiado de librería JWT) | ✔ |

Ojo con la versión: El tutorial oficial de FastAPI avisa de que antes usaba otra librería (PyJWT): contrasta cualquier curso con la versión actual del tutorial.

### Capítulo 20: Async, streaming y tareas

Secciones: 20.1 def frente a async def · 20.2 Tareas en segundo plano · 20.3 Server-Sent Events · 20.4 Streaming de respuestas

| Fuente | Estado |
| --- | --- |
| [HOWTO: visión conceptual de asyncio](https://docs.python.org/es/3/howto/a-conceptual-overview-of-asyncio.html) | ✔ |
| [Tutorial de FastAPI: Server-Sent Events, Tareas en Segundo Plano](https://fastapi.tiangolo.com/es/) | ◯ |
| [FastAPI: Async y await (concurrencia)](https://fastapi.tiangolo.com/es/) | ◯ |

### Capítulo 21: Tests de API

Secciones: 21.1 El cliente de pruebas · 21.2 Base de datos de pruebas y fixtures · 21.3 Tests asíncronos · 21.4 Sustituir dependencias

| Fuente | Estado |
| --- | --- |
| [pytest: buenas prácticas de integración](https://docs.pytest.org/goodpractices.html) | ✔ |
| [Tutorial de FastAPI: Pruebas; avanzado: Tests Asíncronos](https://fastapi.tiangolo.com/es/) | ◯ |

### Capítulo 22: Docker y despliegue

Secciones: 22.1 Imágenes y contenedores · 22.2 Dockerfile y capas · 22.3 Builds multietapa · 22.4 Configuración por entorno y secretos · 22.5 Desplegar

| Fuente | Estado |
| --- | --- |
| [Missing Semester: Packaging and Shipping Code](https://missing.csail.mit.edu/2026/shipping-code/) | ✔ |
| Docker: guía de inicio oficial | ◯ |
| [FastAPI: despliegue con contenedores](https://fastapi.tiangolo.com/es/) | ◯ |

## Parte IV: IA aplicada: LLMs, RAG y skills

### Capítulo 23: Cómo funciona un LLM

Secciones: 23.1 Tokens y tokenización · 23.2 Transformers a vista de pájaro · 23.3 Ventana de contexto · 23.4 Muestreo y temperatura · 23.5 Por qué un modelo inventa

| Fuente | Estado |
| --- | --- |
| [Hugging Face: LLM Course](https://huggingface.co/learn/llm-course) | ✔ |
| [Hugging Face Agents Course, unidad 1 (LLMs y tokens especiales)](https://huggingface.co/learn/agents-course/unit1) | ✔ |
| Documentación de un proveedor de modelos: tokens y ventana de contexto | ◯ |

### Capítulo 24: Llamar a un modelo

Secciones: 24.1 Mensajes y roles · 24.2 Parámetros de la petición · 24.3 Streaming · 24.4 Salida estructurada · 24.5 Errores, límites y reintentos

| Fuente | Estado |
| --- | --- |
| [MDN: 429 Too Many Requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/429) | ✔ |
| [Documentación oficial de la API de un proveedor (mensajes, streaming, salida estructurada)](https://docs.claude.com) | ◯ |

### Capítulo 25: Instrucciones y prompts

Secciones: 25.1 Instrucciones claras · 25.2 Ejemplos · 25.3 Formato de salida · 25.4 Descomponer tareas

| Fuente | Estado |
| --- | --- |
| [Guía de prompt engineering de Anthropic](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview) | ◯ |

### Capítulo 26: Tool calling

Secciones: 26.1 Qué es el tool calling · 26.2 Describir herramientas con JSON Schema · 26.3 El bucle petición y resultado · 26.4 Validar argumentos y fallos

| Fuente | Estado |
| --- | --- |
| [Hugging Face Agents Course, unidad 1 (herramientas y acciones)](https://huggingface.co/learn/agents-course/unit1) | ✔ |
| [Documentación de tool use de un proveedor](https://docs.claude.com) | ◯ |

### Capítulo 27: Embeddings y RAG

Secciones: 27.1 Embeddings · 27.2 Troceado de documentos · 27.3 Almacenes vectoriales y búsqueda · 27.4 Recuperar y generar · 27.5 Reordenar y citar · 27.6 Por qué falla un RAG

| Fuente | Estado |
| --- | --- |
| [Agno: Knowledge (RAG) en las capacidades del SDK](https://docs.agno.com/features) | ✔ |
| [Hugging Face Agents Course, unidad 3 (RAG agéntico)](https://huggingface.co/learn/agents-course) | ◯ |
| [Hugging Face LLM Course: capítulos de embeddings y búsqueda semántica](https://huggingface.co/learn/llm-course) | ◯ |

### Capítulo 28: Evaluación

Secciones: 28.1 Por qué evaluar · 28.2 Conjuntos de prueba · 28.3 Métricas · 28.4 Un modelo como juez y sus límites · 28.5 Regresiones

| Fuente | Estado |
| --- | --- |
| [Agno: Evals en el SDK](https://docs.agno.com/sdk/introduction) | ✔ |
| [Hugging Face Agents Course, unidad extra 2 (observabilidad y evaluación)](https://huggingface.co/learn/agents-course/unit0/introduction) | ◯ |

### Capítulo 29: Skills

Secciones: 29.1 Qué es una skill · 29.2 Anatomía de una skill · 29.3 Skill, prompt o herramienta: cuándo cada una

| Fuente | Estado |
| --- | --- |
| [Agno: Skills en las capacidades del SDK](https://docs.agno.com/features) | ✔ |
| Documentación de Agent Skills de Anthropic | ◯ |

### Capítulo 30: Dónde aporta valor

Secciones: 30.1 Casos de uso reales · 30.2 Coste y latencia · 30.3 Cuándo no usar IA · 30.4 Flujos deterministas frente a agentes

| Fuente | Estado |
| --- | --- |
| [Missing Semester: Agentic Coding](https://missing.csail.mit.edu/2026/agentic-coding/) | ✔ |
| [Agno: Workflows deterministas](https://docs.agno.com/sdk/introduction) | ✔ |
| Anthropic: «Building effective agents» | ◯ |

## Parte V: Agentes de IA

### Capítulo 31: El bucle del agente

Secciones: 31.1 Qué es un agente · 31.2 Pensar, actuar, observar · 31.3 Condición de parada y presupuesto · 31.4 Trazas: ver qué hizo el agente

| Fuente | Estado |
| --- | --- |
| [Hugging Face Agents Course, unidad 1](https://huggingface.co/learn/agents-course/unit1/introduction) | ✔ |
| [Hugging Face Agents Course: portada y temario](https://huggingface.co/learn/agents-course) | ✔ |

### Capítulo 32: Agentes con Agno

Secciones: 32.1 Agent, Team y Workflow · 32.2 Herramientas en Agno · 32.3 Salida estructurada · 32.4 De tu bucle a mano a Agno

| Fuente | Estado |
| --- | --- |
| [Agno: introducción](https://docs.agno.com/introduction) | ✔ |
| [Agno SDK: Agent, Team, Workflow](https://docs.agno.com/sdk/introduction) | ✔ |
| [Agno: capacidades](https://docs.agno.com/features) | ✔ |

Ojo con la versión: Agno tiene documentación separada para la versión 1 (docs-v1.agno.com) y la actual; los libros y cursos anteriores pueden usar la 1.

### Capítulo 33: Memoria

Secciones: 33.1 Contexto frente a memoria · 33.2 Sesiones e historial · 33.3 Memoria persistente · 33.4 Resúmenes y compresión · 33.5 Privacidad

| Fuente | Estado |
| --- | --- |
| [Agno: capacidades (Storage, Sessions, State, Memory)](https://docs.agno.com/features) | ✔ |

### Capítulo 34: MCP

Secciones: 34.1 El problema que resuelve MCP · 34.2 Host, cliente y servidor · 34.3 Primitivas: tools, resources y prompts · 34.4 Transportes: stdio y Streamable HTTP · 34.5 Descubrimiento y versión del protocolo · 34.6 Construir un servidor

| Fuente | Estado |
| --- | --- |
| [MCP: arquitectura](https://modelcontextprotocol.io/docs/learn/architecture) | ✔ |
| [MCP: aprender](https://modelcontextprotocol.io/docs/learn) | ✔ |
| SDK oficial de MCP para Python | ◯ |
| Hugging Face: curso de MCP | ◯ |

Ojo con la versión: La versión del protocolo MCP 2026-07-28 introduce cambios (descubrimiento con server/discover, sampling obsoleto); fija la versión que explicas.

### Capítulo 35: Multiagente y A2A

Secciones: 35.1 Cuándo dividir en varios agentes · 35.2 Orquestador y subagentes · 35.3 Equipos en Agno · 35.4 El protocolo A2A · 35.5 MCP frente a A2A

| Fuente | Estado |
| --- | --- |
| [Agno SDK: Teams](https://docs.agno.com/sdk/introduction) | ✔ |
| [Repositorio del protocolo A2A](https://github.com/a2aproject/A2A) | ◯ |

### Capítulo 36: Seguridad y control

Secciones: 36.1 Inyección de prompts · 36.2 Mínimo privilegio y permisos · 36.3 Sandbox · 36.4 Aprobación humana

| Fuente | Estado |
| --- | --- |
| [OpenCode: permisos](https://opencode.ai/docs/permissions/) | ✔ |
| [Agno: guardrails y human-in-the-loop](https://docs.agno.com/introduction) | ✔ |
| OWASP Top 10 para aplicaciones LLM | ◯ |

Ojo con la versión: OpenCode tiene una configuración V2 de permisos con sintaxis distinta a la V1.

## Parte VI: Ingeniería de software agéntica

### Capítulo 37: Trabajar con un agente de código

Secciones: 37.1 Qué hace un agente de código · 37.2 Contexto y archivos de reglas · 37.3 Permisos · 37.4 Sesiones y límites

| Fuente | Estado |
| --- | --- |
| [Missing Semester: Agentic Coding](https://missing.csail.mit.edu/2026/agentic-coding/) | ✔ |
| [OpenCode: reglas](https://opencode.ai/docs/rules/) | ✔ |
| [OpenCode: permisos](https://opencode.ai/docs/permissions/) | ✔ |

Ojo con la versión: OpenCode tiene una configuración V2 con sintaxis distinta a la V1.

### Capítulo 38: Especificar antes de pedir

Secciones: 38.1 Tarea frente a especificación · 38.2 Criterios de aceptación verificables · 38.3 El flujo ODD de Gentle AI

| Fuente | Estado |
| --- | --- |
| [gentle-ai: repositorio](https://github.com/Gentleman-Programming/gentle-ai) | ✔ |
| [Missing Semester: Agentic Coding](https://missing.csail.mit.edu/2026/agentic-coding/) | ✔ |

### Capítulo 39: Revisar código de IA

Secciones: 39.1 Leer un diff de verdad · 39.2 Tests primero · 39.3 Señales de alarma · 39.4 Cuándo rechazar un cambio

| Fuente | Estado |
| --- | --- |
| [Missing Semester: Code Quality](https://missing.csail.mit.edu/2026/code-quality/) | ✔ |
| [Missing Semester: Agentic Coding](https://missing.csail.mit.edu/2026/agentic-coding/) | ✔ |
| GitHub: revisar cambios en pull requests | ◯ |

### Capítulo 40: Contexto del proyecto

Secciones: 40.1 AGENTS.md y CLAUDE.md · 40.2 Instrucciones externas · 40.3 Contexto que estorba

| Fuente | Estado |
| --- | --- |
| [OpenCode: reglas (AGENTS.md)](https://opencode.ai/docs/rules/) | ✔ |
| [Claude Code: memoria y CLAUDE.md](https://code.claude.com/docs/en/memory) | ✔ |

### Capítulo 41: Cómo trabaja gentle-shell

Secciones: 41.1 Qué es gentle-shell: Pi y Gentle AI · 41.2 Instalación aislada · 41.3 Recorrido de una tarea · 41.4 Versiones fijadas del runtime

| Fuente | Estado |
| --- | --- |
| [Wiki de gentle-shell](https://github.com/Gentleman-Programming/gentle-shell/wiki) | ✔ |
| [gentle-shell: repositorio](https://github.com/Gentleman-Programming/gentle-shell) | ✔ |
| [gentle-ai: repositorio](https://github.com/Gentleman-Programming/gentle-ai) | ✔ |

## Parte VII: TypeScript y Node

### Capítulo 42: Sistema de tipos

Secciones: 42.1 Tipos básicos · 42.2 Tipado estructural · 42.3 Uniones y narrowing · 42.4 Genéricos · 42.5 unknown, any y never

| Fuente | Estado |
| --- | --- |
| [TypeScript Handbook: introducción](https://typescriptlang.org/docs/handbook/intro) | ✔ |
| [TypeScript Handbook: The Basics](https://www.typescriptlang.org/docs/handbook/2/basic-types.html) | ✔ |
| [TypeScript Handbook: Narrowing, Generics, Object Types](https://www.typescriptlang.org/docs/handbook/intro) | ◯ |

### Capítulo 43: Módulos y paquetes

Secciones: 43.1 ESM frente a CommonJS · 43.2 package.json y exports · 43.3 Compilar con tsc · 43.4 tsconfig

| Fuente | Estado |
| --- | --- |
| TypeScript Handbook: Modules | ◯ |
| Node.js: documentación de paquetes y módulos | ◯ |
| [midudev, curso de Node.js desde cero](https://github.com/midudev/curso-node-js) (comunidad; complemento en español; comprobar versión de Node usada) | ✔ |

### Capítulo 44: Event loop de Node

Secciones: 44.1 El modelo del event loop · 44.2 Promesas y async/await · 44.3 Timers y nextTick · 44.4 Streams · 44.5 Procesos hijo

| Fuente | Estado |
| --- | --- |
| Node.js: guía oficial del event loop | ◯ |
| [midudev, curso de Node.js desde cero](https://github.com/midudev/curso-node-js) (comunidad; complemento en español) | ✔ |

### Capítulo 45: npm y versiones

Secciones: 45.1 Semver · 45.2 Lockfiles · 45.3 Binarios y CLIs · 45.4 Publicar · 45.5 Cadena de suministro

| Fuente | Estado |
| --- | --- |
| [Missing Semester: Packaging and Shipping Code](https://missing.csail.mit.edu/2026/shipping-code/) | ✔ |
| Documentación oficial de npm | ◯ |

### Capítulo 46: Tests en TypeScript

Secciones: 46.1 El runner de tests · 46.2 Tipos en los tests · 46.3 Integración continua con GitHub Actions

| Fuente | Estado |
| --- | --- |
| Node.js: test runner integrado | ◯ |
| GitHub Actions: documentación | ◯ |

### Capítulo 47: Leer gentle-shell

Secciones: 47.1 Estructura del repositorio · 47.2 Cómo se carga como paquete de Pi · 47.3 Publicación y verificación de versiones · 47.4 Encontrar un primer issue

| Fuente | Estado |
| --- | --- |
| [gentle-shell: repositorio](https://github.com/Gentleman-Programming/gentle-shell) | ✔ |
| [Wiki de gentle-shell](https://github.com/Gentleman-Programming/gentle-shell/wiki) | ✔ |

## Parte VIII: Arquitectura y diseño de sistemas

### Capítulo 48: Analizar compromisos

Secciones: 48.1 No hay mejores prácticas, solo compromisos · 48.2 ADRs · 48.3 Atributos de calidad

| Fuente | Estado |
| --- | --- |
| [System Design Primer](https://github.com/donnemartin/system-design-primer) | ✔ |
| ADR: plantillas y guía | ◯ |

### Capítulo 49: Acoplamiento y granularidad

Secciones: 49.1 Acoplamiento y cohesión · 49.2 Monolito frente a servicios · 49.3 Granularidad

| Fuente | Estado |
| --- | --- |
| [System Design Primer (microservicios y capa de aplicación)](https://github.com/donnemartin/system-design-primer) | ✔ |

### Capítulo 50: Datos distribuidos

Secciones: 50.1 Consistencia y disponibilidad · 50.2 Replicación · 50.3 Particionado · 50.4 Sagas

| Fuente | Estado |
| --- | --- |
| [System Design Primer: patrones de consistencia](https://github.com/donnemartin/system-design-primer#consistency-patterns) | ✔ |
| [System Design Primer: patrones de disponibilidad](https://github.com/donnemartin/system-design-primer#availability-patterns) | ✔ |
| Patrón saga en microservices.io | ◯ |

### Capítulo 51: Escalado

Secciones: 51.1 Escalado vertical y horizontal · 51.2 Balanceadores de carga · 51.3 Servicios sin estado · 51.4 Estimaciones rápidas

| Fuente | Estado |
| --- | --- |
| [System Design Primer: escalado horizontal](https://github.com/donnemartin/system-design-primer#horizontal-scaling) | ✔ |
| [System Design Primer: balanceador de carga](https://github.com/donnemartin/system-design-primer#load-balancer) | ✔ |

### Capítulo 52: Cachés y colas

Secciones: 52.1 Estrategias de caché · 52.2 Invalidación · 52.3 Asincronía y colas · 52.4 Entrega y reintentos

| Fuente | Estado |
| --- | --- |
| [System Design Primer: caché](https://github.com/donnemartin/system-design-primer#cache) | ✔ |
| [MDN: caché HTTP](https://developer.mozilla.org/es/docs/Web/HTTP/Guides/Caching) | ✔ |
| [System Design Primer (asincronía y colas)](https://github.com/donnemartin/system-design-primer) | ✔ |

### Capítulo 53: Casos de diseño

Secciones: 53.1 Limitador de peticiones · 53.2 Sistema de notificaciones · 53.3 Caso real: el almacenamiento de Git

| Fuente | Estado |
| --- | --- |
| [System Design Primer](https://github.com/donnemartin/system-design-primer) | ✔ |
| [Pro Git 10.4: archivos empaquetadores](https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Archivos-empaquetadores) | ✔ |
| [Pro Git 10.7: mantenimiento y recuperación de datos](https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Mantenimiento-y-recuperaci%c3%b3n-de-datos) | ✔ |

## Parte IX: Go

### Capítulo 54: Fundamentos de Go

Secciones: 54.1 Tipos, structs y métodos · 54.2 Interfaces implícitas · 54.3 Slices y mapas · 54.4 Paquetes

| Fuente | Estado |
| --- | --- |
| [A Tour of Go](https://go.dev/tour/) | ✔ |
| [Go by Example](https://gobyexample.com/) | ✔ |
| [Effective Go](https://go.dev/doc/effective_go) | ✔ |

### Capítulo 55: Errores como valores

Secciones: 55.1 error como valor · 55.2 Envolver errores · 55.3 errors.Is y errors.As · 55.4 panic frente a error

| Fuente | Estado |
| --- | --- |
| [Effective Go (errores)](https://go.dev/doc/effective_go) | ✔ |
| [Go by Example (errores)](https://gobyexample.com/) | ✔ |
| Blog de Go: «Errors are values» | ◯ |

### Capítulo 56: Módulos y versiones

Secciones: 56.1 go mod · 56.2 Versión mayor en la ruta del módulo · 56.3 go install

| Fuente | Estado |
| --- | --- |
| [Go Modules Reference](https://go.dev/ref/mod) | ◯ |
| [gentle-ai: repositorio (rutas de módulo por versión)](https://github.com/Gentleman-Programming/gentle-ai) | ✔ |

### Capítulo 57: Concurrencia

Secciones: 57.1 Goroutines · 57.2 Canales · 57.3 select · 57.4 context y cancelación · 57.5 sync

| Fuente | Estado |
| --- | --- |
| [A Tour of Go (concurrencia)](https://go.dev/tour/) | ✔ |
| [Effective Go (concurrencia)](https://go.dev/doc/effective_go) | ✔ |
| [Go by Example (goroutines, canales, select, context)](https://gobyexample.com/) | ✔ |

### Capítulo 58: CLIs en Go

Secciones: 58.1 Flags · 58.2 Subcomandos · 58.3 Binario único y distribución

| Fuente | Estado |
| --- | --- |
| [Go by Example (flags y subcomandos)](https://gobyexample.com/) | ✔ |
| [Go: Get Started](https://go.dev/learn/) | ✔ |

### Capítulo 59: Leer gentle-ai

Secciones: 59.1 Estructura del runtime · 59.2 Instalación y sincronización · 59.3 Publicación de versiones · 59.4 Primer issue en Go

| Fuente | Estado |
| --- | --- |
| [gentle-ai: repositorio](https://github.com/Gentleman-Programming/gentle-ai) | ✔ |

## Cómo completar el mapa de un capítulo (fase 1)

1. Para cada sección del capítulo, elige una fuente Principal y, si aporta, fuentes para Profundizar, siguiendo la jerarquía de `docs/PROYECTO.md`.
2. Abre cada página y guarda su copia local de verificación (ver `docs/06-metodo-sin-alucinaciones.md`). Una página no abierta no entra en el mapa.
3. Sustituye la tabla del capítulo por una tabla por secciones (formato de las Partes I y II) y cambia ◯ por ✔.
4. Si una sección no tiene fuente fiable, márcala PENDIENTE y avisa a devOC. Nunca se rellena con conocimiento propio.
5. Mantén cada parte por debajo de 50 páginas distintas, o divídela en dos grupos, para que quepa en un cuaderno de NotebookLM del plan gratuito.

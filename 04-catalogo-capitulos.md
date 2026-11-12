# Catálogo de capítulos

Ficha completa de cada uno de los 59 capítulos. Es el contrato de contenido: un capítulo no está terminado si no cumple su ficha. Las fuentes no están aquí sino en `03-indice-con-fuentes.md`.

## Campos de cada ficha

| Campo | Significado |
| --- | --- |
| id | Identificador estable; coincide con el nodo del roadmap y con el nombre del archivo |
| Archivo | Ruta en `contenido/` |
| Requisitos | Capítulos que el lector debe dominar antes |
| Al terminar podrás | Objetivos comprobables; van al principio del capítulo |
| Secciones | Orden obligatorio de las secciones |
| Explicar | Pregunta de la prueba de explicar; va en «Preguntas de examen» |
| Construir sin IA | Ejercicio de la prueba de construir; va en «Ejercicios» |
| Defender | Foco de las 4 a 6 preguntas de defensa |
| Ojo con la versión | Cambios detectados entre versiones de las fuentes, si los hay |
| Libro de referencia | Libro de pago del roadmap original: solo orientativo, nunca fuente |

---

## Parte I. Oficio: Git, terminal y leer código

- **Fase:** 1
- **Por qué:** Contribuir en open source es sobre todo leer código ajeno y colaborar con Git. Sin esto, todo lo demás se queda en proyectos que solo tú tocas.
- **Requisitos de la parte:** Ninguno
- **Proyecto de la parte (Arqueología de un PR):** Elige un PR ya integrado en gentle-shell. Vuelve al commit anterior, reimplementa el cambio sin mirar el diff y compáralo con el real. Escribe qué decidió el autor de forma distinta y por qué. Repite con un PR de FastAPI.

### Capítulo 1. Git por dentro

| Campo | Contenido |
| --- | --- |
| id | `base/git-modelo` |
| Archivo | `contenido/parte-01-base/cap-01-git-por-dentro.md` |
| Requisitos | Ninguno |
| Al terminar podrás | Explicar commits como fotos del proyecto, el historial como grafo, ramas y HEAD como punteros, el área de preparación. Construir sin ayuda: crea un repo, tres ramas, provoca un conflicto, resuélvelo y limpia el historial con rebase interactivo. Dibuja el grafo antes y después. Defender tus decisiones sobre: rebase frente a merge, cuándo no reescribir historia, qué hace realmente reset. |
| Secciones | 1.1 Qué es el control de versiones<br>1.2 Fotos, no diferencias; los tres estados<br>1.3 Leer y deshacer el historial<br>1.4 Las ramas son punteros<br>1.5 Rebase y reescribir historia<br>1.6 Bajo el capó: objetos y referencias<br>1.7 reset sin miedo |
| Explicar | ¿Qué es realmente una rama y qué cambia en el repositorio cuando haces un commit? |
| Construir sin IA | Crea un repo, tres ramas, provoca un conflicto, resuélvelo y limpia el historial con rebase interactivo. Dibuja el grafo antes y después. |
| Defender | Rebase frente a merge, cuándo no reescribir historia, qué hace realmente reset. |

### Capítulo 2. Flujo de contribución

| Campo | Contenido |
| --- | --- |
| id | `base/git-colab` |
| Archivo | `contenido/parte-01-base/cap-02-flujo-de-contribucion.md` |
| Requisitos | Capítulo 1 |
| Al terminar podrás | Explicar fork y upstream, ramas de trabajo, PR pequeños, mensajes de commit claros, responder a una revisión. Construir sin ayuda: simula una contribución: fork de un repo tuyo, PR desde una rama, «revisión» con dos cambios pedidos y actualización del PR sin abrir otro. Defender tus decisiones sobre: cómo mantener tu fork al día, qué hacer si upstream cambió mientras trabajabas. |
| Secciones | 2.1 Remotos y ramas remotas<br>2.2 Flujos de trabajo distribuidos<br>2.3 Contribuir a un proyecto<br>2.4 Fork y pull request en GitHub<br>2.5 Mantener el PR al día y responder revisiones<br>2.6 Contribuir sin escribir código |
| Explicar | ¿Por qué los proyectos piden PR pequeños y una rama por cambio? |
| Construir sin IA | Simula una contribución: fork de un repo tuyo, PR desde una rama, «revisión» con dos cambios pedidos y actualización del PR sin abrir otro. |
| Defender | Cómo mantener tu fork al día, qué hacer si upstream cambió mientras trabajabas. |

### Capítulo 3. Terminal y procesos

| Campo | Contenido |
| --- | --- |
| id | `base/terminal` |
| Archivo | `contenido/parte-01-base/cap-03-terminal-y-procesos.md` |
| Requisitos | Capítulo 2 |
| Al terminar podrás | Explicar shell, tuberías, redirecciones, variables de entorno, PATH, códigos de salida, procesos y señales. Construir sin ayuda: script que liste los TODO de un repo y cuente cuántos añadió cada autor usando git blame. Defender tus decisiones sobre: por qué importa el código de salida, diferencia entre variable de shell y de entorno. |
| Secciones | 3.1 La shell: comandos, rutas y PATH<br>3.2 Procesos, señales y variables de entorno<br>3.3 Tu entorno de desarrollo<br>3.4 Depurar y medir |
| Explicar | ¿Qué ocurre, paso a paso, desde que escribes un comando hasta que ves su salida? |
| Construir sin IA | Script que liste los TODO de un repo y cuente cuántos añadió cada autor usando git blame. |
| Defender | Por qué importa el código de salida, diferencia entre variable de shell y de entorno. |

### Capítulo 4. HTTP de verdad

| Campo | Contenido |
| --- | --- |
| id | `base/http` |
| Archivo | `contenido/parte-01-base/cap-04-http-de-verdad.md` |
| Requisitos | Capítulo 3 |
| Al terminar podrás | Explicar petición y respuesta, métodos, códigos de estado, cabeceras, idempotencia, cuerpo y tipos de contenido. Construir sin ayuda: habla HTTP a mano con curl -v contra una API pública y explica cada línea de la respuesta. Defender tus decisiones sobre: pUT frente a PATCH, 401 frente a 403, para qué sirve cada cabecera que viste. |
| Secciones | 4.1 Cliente, servidor y sin estado<br>4.2 Anatomía de mensajes y sesión<br>4.3 Métodos e idempotencia<br>4.4 Códigos de estado<br>4.5 Cabeceras y tipos de contenido<br>4.6 Caché y peticiones condicionales<br>4.7 Autenticación y CORS<br>4.8 Conexiones |
| Explicar | ¿Qué hace idempotente a un método y por qué le importa a un cliente que reintenta? |
| Construir sin IA | Habla HTTP a mano con curl -v contra una API pública y explica cada línea de la respuesta. |
| Defender | PUT frente a PATCH, 401 frente a 403, para qué sirve cada cabecera que viste. |

### Capítulo 5. Leer código ajeno

| Campo | Contenido |
| --- | --- |
| id | `base/leer-codigo` |
| Archivo | `contenido/parte-01-base/cap-05-leer-codigo-ajeno.md` |
| Requisitos | Capítulo 4 |
| Al terminar podrás | Explicar encontrar el punto de entrada, usar los tests como documentación, buscar con grep o ripgrep, git log -p, git blame y git bisect. Construir sin ayuda: en el repo de FastAPI, localiza dónde se convierte el valor que devuelve un endpoint en una respuesta JSON. Entrega las rutas de archivo y el recorrido. Defender tus decisiones sobre: por qué empezar por los tests, cuándo usar bisect. |
| Secciones | 5.1 Moverse por el historial<br>5.2 Buscar en el código y en la historia<br>5.3 blame y bisect<br>5.4 Calidad de código: qué buscar al leer<br>5.5 Práctica en un repo real |
| Explicar | ¿Cuál es tu método para entender un repo que nunca has visto en una hora? |
| Construir sin IA | En el repo de FastAPI, localiza dónde se convierte el valor que devuelve un endpoint en una respuesta JSON. Entrega las rutas de archivo y el recorrido. |
| Defender | Por qué empezar por los tests, cuándo usar bisect. |

---

## Parte II. Python profundo

- **Fase:** 1
- **Por qué:** Todo lo que viene (FastAPI, agentes, RAG) es Python. Si entiendes el modelo de objetos, async y los tipos, el código de la IA deja de ser magia.
- **Requisitos de la parte:** Parte I (capítulo 3 para entornos y terminal)
- **Proyecto de la parte (Pydantic de juguete):** Construye una mini librería de validación que lea las anotaciones de una clase y valide datos, con tests. Después lee cómo lo resuelve Pydantic y escribe la comparación. Si encuentras un ejemplo confuso en su documentación, propón la mejora: es tu primera contribución.
- **Nota:** Ninguno de tus libros cubre Python desde la base: aquí la fuente es la documentación oficial.

### Capítulo 6. Modelo de objetos

| Campo | Contenido |
| --- | --- |
| id | `python/py-objetos` |
| Archivo | `contenido/parte-02-python/cap-06-modelo-de-objetos.md` |
| Requisitos | Parte I (capítulo 3 para entornos y terminal) |
| Al terminar podrás | Explicar todo es un objeto, nombres que apuntan a objetos, mutabilidad, identidad frente a igualdad, métodos especiales. Construir sin ayuda: clase Dinero con suma, comparación, representación y hash correctos; tests que demuestren cada método especial. Defender tus decisiones sobre: por qué no usar listas como valor por defecto, cuándo un objeto debe ser hashable. |
| Secciones | 6.1 Nombres que apuntan a objetos<br>6.2 Ámbitos y espacios de nombres<br>6.3 Estructuras mutables e inmutables<br>6.4 Clases, instancias y variables de clase<br>6.5 Herencia<br>6.6 Métodos especiales |
| Explicar | ¿Por qué modificar una lista dentro de una función cambia la original y reasignarla no? |
| Construir sin IA | Clase Dinero con suma, comparación, representación y hash correctos; tests que demuestren cada método especial. |
| Defender | Por qué no usar listas como valor por defecto, cuándo un objeto debe ser hashable. |

### Capítulo 7. Funciones, closures y decoradores

| Campo | Contenido |
| --- | --- |
| id | `python/py-funciones` |
| Archivo | `contenido/parte-02-python/cap-07-funciones-closures-y-decoradores.md` |
| Requisitos | Capítulo 6 |
| Al terminar podrás | Explicar ámbitos, closures, funciones como valores, decoradores con y sin argumentos, functools.wraps. Construir sin ayuda: decorador de reintentos con espera exponencial y número de intentos configurable, con tests. Defender tus decisiones sobre: por qué FastAPI usa decoradores para las rutas, qué pierde una función decorada sin wraps. |
| Secciones | 7.1 Definir funciones y valores por omisión<br>7.2 Parámetros especiales, *args y **kwargs<br>7.3 Funciones de orden superior y closures<br>7.4 Decoradores<br>7.5 Anotaciones de función |
| Explicar | ¿Qué es exactamente un decorador y qué hace Python cuando ve @algo encima de una función? |
| Construir sin IA | Decorador de reintentos con espera exponencial y número de intentos configurable, con tests. |
| Defender | Por qué FastAPI usa decoradores para las rutas, qué pierde una función decorada sin wraps. |

### Capítulo 8. Iteradores y generadores

| Campo | Contenido |
| --- | --- |
| id | `python/py-iteracion` |
| Archivo | `contenido/parte-02-python/cap-08-iteradores-y-generadores.md` |
| Requisitos | Capítulo 7 |
| Al terminar podrás | Explicar protocolo de iteración, generadores, yield, expresiones generadoras, evaluación perezosa, itertools. Construir sin ayuda: lector de un log enorme que filtre y agrupe por línea sin cargarlo entero en memoria. Defender tus decisiones sobre: cuándo un generador se agota, por qué el streaming de respuestas de un LLM es un generador. |
| Secciones | 8.1 Técnicas de iteración y comprensiones<br>8.2 El protocolo de iteración<br>8.3 Generadores y expresiones generadoras<br>8.4 itertools y functools |
| Explicar | ¿Qué diferencia hay entre una lista y un generador en memoria y en tiempo? |
| Construir sin IA | Lector de un log enorme que filtre y agrupe por línea sin cargarlo entero en memoria. |
| Defender | Cuándo un generador se agota, por qué el streaming de respuestas de un LLM es un generador. |

### Capítulo 9. Tipos y validación

| Campo | Contenido |
| --- | --- |
| id | `python/py-tipos` |
| Archivo | `contenido/parte-02-python/cap-09-tipos-y-validacion.md` |
| Requisitos | Capítulo 8 |
| Al terminar podrás | Explicar anotaciones, genéricos, Protocol, dataclasses, Pydantic, comprobación estática con mypy o pyright. Construir sin ayuda: modela un pedido con dataclasses y luego con Pydantic; escribe qué errores atrapa cada uno. Defender tus decisiones sobre: protocol frente a herencia, por qué los type hints son la base de FastAPI y del tool calling. |
| Secciones | 9.1 Anotaciones y el módulo typing<br>9.2 dataclasses<br>9.3 Validar en tiempo de ejecución con Pydantic |
| Explicar | ¿Qué hace una anotación de tipo en tiempo de ejecución y qué añade Pydantic encima? |
| Construir sin IA | Modela un pedido con dataclasses y luego con Pydantic; escribe qué errores atrapa cada uno. |
| Defender | Protocol frente a herencia, por qué los type hints son la base de FastAPI y del tool calling. |

### Capítulo 10. Asincronía

| Campo | Contenido |
| --- | --- |
| id | `python/py-async` |
| Archivo | `contenido/parte-02-python/cap-10-asincronia.md` |
| Requisitos | Capítulo 9 |
| Al terminar podrás | Explicar event loop, corrutinas, await, tareas, gather, timeouts; concurrencia frente a paralelismo y el GIL. Construir sin ayuda: cliente que consulta 20 URLs a la vez con límite de 5 simultáneas y timeout por petición. Defender tus decisiones sobre: qué pasa si llamas a algo bloqueante dentro de async, tareas frente a hilos. |
| Secciones | 10.1 Modelo mental: el bucle de eventos<br>10.2 Corrutinas, tareas y gather<br>10.3 Hilos frente a async |
| Explicar | ¿Por qué async no hace tu código más rápido por sí solo y cuándo sí ayuda? |
| Construir sin IA | Cliente que consulta 20 URLs a la vez con límite de 5 simultáneas y timeout por petición. |
| Defender | Qué pasa si llamas a algo bloqueante dentro de async, tareas frente a hilos. |

### Capítulo 11. Errores y gestores de contexto

| Campo | Contenido |
| --- | --- |
| id | `python/py-errores` |
| Archivo | `contenido/parte-02-python/cap-11-errores-y-gestores-de-contexto.md` |
| Requisitos | Capítulo 10 |
| Al terminar podrás | Explicar excepciones propias, jerarquías, encadenamiento, with, contextlib. Construir sin ayuda: gestor de contexto que cronometra un bloque y registra si terminó con error. Defender tus decisiones sobre: cuándo capturar y cuándo dejar subir una excepción. |
| Secciones | 11.1 Capturar y lanzar excepciones<br>11.2 Encadenar y definir excepciones propias<br>11.3 Limpieza y la sentencia with<br>11.4 Escribir gestores de contexto |
| Explicar | ¿Qué garantiza un bloque with que no garantiza un try normal mal escrito? |
| Construir sin IA | Gestor de contexto que cronometra un bloque y registra si terminó con error. |
| Defender | Cuándo capturar y cuándo dejar subir una excepción. |

### Capítulo 12. Testing con pytest

| Campo | Contenido |
| --- | --- |
| id | `python/py-tests` |
| Archivo | `contenido/parte-02-python/cap-12-testing-con-pytest.md` |
| Requisitos | Capítulo 11 |
| Al terminar podrás | Explicar tests unitarios, fixtures, parametrize, dobles de prueba, cobertura, TDD. Construir sin ayuda: escribe primero los tests de una función de parseo de fechas en español y luego la implementación. Defender tus decisiones sobre: mock frente a fake, por qué los proyectos open source exigen tests en cada PR. |
| Secciones | 12.1 Control de calidad en la biblioteca estándar<br>12.2 Estructura de un proyecto con tests<br>12.3 Fixtures, parametrize y dobles de prueba |
| Explicar | ¿Qué hace que un test sea útil y no solo verde? |
| Construir sin IA | Escribe primero los tests de una función de parseo de fechas en español y luego la implementación. |
| Defender | Mock frente a fake, por qué los proyectos open source exigen tests en cada PR. |

### Capítulo 13. Módulos, paquetes y entornos

| Campo | Contenido |
| --- | --- |
| id | `python/py-paquetes` |
| Archivo | `contenido/parte-02-python/cap-13-modulos-paquetes-y-entornos.md` |
| Requisitos | Capítulo 12 |
| Al terminar podrás | Explicar imports, paquetes, pyproject.toml, entornos virtuales, uv, publicar un paquete. Construir sin ayuda: empaqueta una utilidad tuya con pyproject.toml e instálala en otro proyecto. Defender tus decisiones sobre: imports relativos y absolutos, para qué sirve un lockfile. |
| Secciones | 13.1 Módulos y ruta de búsqueda<br>13.2 Paquetes<br>13.3 Entornos virtuales<br>13.4 pyproject.toml y publicar |
| Explicar | ¿Cómo encuentra Python un módulo cuando haces import? |
| Construir sin IA | Empaqueta una utilidad tuya con pyproject.toml e instálala en otro proyecto. |
| Defender | Imports relativos y absolutos, para qué sirve un lockfile. |

---

## Parte III. Backend con FastAPI

- **Fase:** 2
- **Por qué:** Es tu stack y la base de las herramientas de IA: casi todo agente acaba hablando con una API que alguien tiene que diseñar bien.
- **Requisitos de la parte:** Partes I y II
- **Proyecto de la parte (Simulador de proveedor LLM):** Servidor FastAPI que imita la API de mensajes de un proveedor de LLM: respuestas guionizadas desde un archivo YAML, streaming por SSE e inyección de fallos (429, timeouts, respuestas cortadas). Sirve para probar agentes sin gastar tokens y será el banco de pruebas de las ramas de IA y agentes. Publícalo como open source con README y tests.

### Capítulo 14. Diseño de APIs REST

| Campo | Contenido |
| --- | --- |
| id | `backend/api-diseno` |
| Archivo | `contenido/parte-03-backend/cap-14-diseno-de-apis-rest.md` |
| Requisitos | Partes I y II |
| Al terminar podrás | Explicar recursos, verbos, códigos de estado, paginación, errores, versionado. Construir sin ayuda: diseña en papel la API de un sistema de préstamo de herramientas entre vecinos: rutas, códigos y errores. Defender tus decisiones sobre: errores coherentes, por qué no devolver 200 con un error dentro. |
| Secciones | 14.1 Recursos y URIs<br>14.2 Verbos y su semántica<br>14.3 Códigos de estado y formato de errores<br>14.4 Paginación, filtros y versionado<br>14.5 El contrato: OpenAPI |
| Explicar | ¿Cómo decides si algo es un recurso propio o un campo de otro? |
| Construir sin IA | Diseña en papel la API de un sistema de préstamo de herramientas entre vecinos: rutas, códigos y errores. |
| Defender | Errores coherentes, por qué no devolver 200 con un error dentro. |
| Libro de referencia | Alvero Velmora, *FastAPI en Acción* |

### Capítulo 15. Endpoints y routing

| Campo | Contenido |
| --- | --- |
| id | `backend/endpoints` |
| Archivo | `contenido/parte-03-backend/cap-15-endpoints-y-routing.md` |
| Requisitos | Capítulo 14 |
| Al terminar podrás | Explicar parámetros de ruta, consulta y cuerpo, routers, response_model, códigos de estado. Construir sin ayuda: cRUD completo de un recurso con routers separados, sin plantilla ni IA, en 60 minutos. Defender tus decisiones sobre: por qué el decorador, qué valida response_model a la salida. |
| Secciones | 15.1 Primera aplicación y path operations<br>15.2 Parámetros de ruta<br>15.3 Parámetros de consulta<br>15.4 Cuerpo de la petición<br>15.5 response_model y status_code<br>15.6 Routers y aplicaciones grandes |
| Explicar | ¿Qué hace FastAPI con la firma de tu función para saber de dónde sale cada parámetro? |
| Construir sin IA | CRUD completo de un recurso con routers separados, sin plantilla ni IA, en 60 minutos. |
| Defender | Por qué el decorador, qué valida response_model a la salida. |
| Ojo con la versión | El curso Backend de Hello Python despliega en Deta, servicio que ya no existe según el propio curso. |
| Libro de referencia | Alvero Velmora, *FastAPI en Acción* |

### Capítulo 16. Validación con Pydantic

| Campo | Contenido |
| --- | --- |
| id | `backend/validacion` |
| Archivo | `contenido/parte-03-backend/cap-16-validacion-con-pydantic.md` |
| Requisitos | Capítulo 15 |
| Al terminar podrás | Explicar modelos de entrada y salida, validadores, errores 422, modelos separados para crear, leer y actualizar. Construir sin ayuda: endpoint de alta con validaciones cruzadas entre campos y errores legibles. Defender tus decisiones sobre: qué devuelve un 422 y por qué, dónde poner reglas de negocio. |
| Secciones | 16.1 Modelos de entrada y de salida<br>16.2 Validadores propios<br>16.3 Errores 422 y manejo de errores<br>16.4 Un modelo por operación (crear, leer, actualizar) |
| Explicar | ¿Por qué separar el modelo de entrada del de salida aunque tengan casi los mismos campos? |
| Construir sin IA | Endpoint de alta con validaciones cruzadas entre campos y errores legibles. |
| Defender | Qué devuelve un 422 y por qué, dónde poner reglas de negocio. |
| Libro de referencia | Alvero Velmora, *FastAPI en Acción* |

### Capítulo 17. Inyección de dependencias

| Campo | Contenido |
| --- | --- |
| id | `backend/dependencias` |
| Archivo | `contenido/parte-03-backend/cap-17-inyeccion-de-dependencias.md` |
| Requisitos | Capítulo 16 |
| Al terminar podrás | Explicar depends, dependencias con yield, sub-dependencias, sustituirlas en tests. Construir sin ayuda: sesión de base de datos y usuario actual como dependencias, sustituidas por fakes en los tests. Defender tus decisiones sobre: ciclo de vida de una dependencia con yield, por qué facilita testear. |
| Secciones | 17.1 Depends: qué problema resuelve<br>17.2 Clases como dependencias y subdependencias<br>17.3 Dependencias con yield<br>17.4 Sustituir dependencias en tests |
| Explicar | ¿Qué problema resuelve Depends y cómo se relaciona con Clean Architecture? |
| Construir sin IA | Sesión de base de datos y usuario actual como dependencias, sustituidas por fakes en los tests. |
| Defender | Ciclo de vida de una dependencia con yield, por qué facilita testear. |
| Libro de referencia | Alvero Velmora, *FastAPI en Acción* |

### Capítulo 18. Persistencia con SQLAlchemy y PostgreSQL

| Campo | Contenido |
| --- | --- |
| id | `backend/persistencia` |
| Archivo | `contenido/parte-03-backend/cap-18-persistencia-con-sqlalchemy-y-postgresql.md` |
| Requisitos | Capítulo 17 |
| Al terminar podrás | Explicar modelos, sesiones, transacciones, relaciones, migraciones con Alembic, el problema N+1. Construir sin ayuda: dos tablas relacionadas, una migración y un endpoint que evite el N+1; demuestra la diferencia con el log de SQL. Defender tus decisiones sobre: carga perezosa frente a ansiosa, transacciones y rollback. |
| Secciones | 18.1 SQL y PostgreSQL lo justo<br>18.2 SQLAlchemy 2.0: engine y sesión<br>18.3 Modelos ORM y relaciones<br>18.4 Transacciones<br>18.5 Migraciones con Alembic<br>18.6 El problema N+1 y la carga de relaciones<br>18.7 Integración con FastAPI |
| Explicar | ¿Qué es una sesión y cuándo se ejecuta realmente la SQL? |
| Construir sin IA | Dos tablas relacionadas, una migración y un endpoint que evite el N+1; demuestra la diferencia con el log de SQL. |
| Defender | Carga perezosa frente a ansiosa, transacciones y rollback. |
| Libro de referencia | Alvero Velmora, *FastAPI en Acción* |

### Capítulo 19. Autenticación y autorización

| Campo | Contenido |
| --- | --- |
| id | `backend/auth` |
| Archivo | `contenido/parte-03-backend/cap-19-autenticacion-y-autorizacion.md` |
| Requisitos | Capítulo 18 |
| Al terminar podrás | Explicar hash de contraseñas, OAuth2 con password flow, JWT, scopes, expiración. Construir sin ayuda: login con JWT y un endpoint que solo pueda usar un rol concreto. Defender tus decisiones sobre: por qué no guardar datos sensibles en el token, cómo revocar. |
| Secciones | 19.1 Autenticación frente a autorización<br>19.2 Guardar contraseñas: hashing<br>19.3 OAuth2 con flujo password<br>19.4 JWT: qué contiene y qué garantiza<br>19.5 Scopes y roles |
| Explicar | ¿Qué contiene un JWT, quién puede leerlo y qué impide que lo falsifiquen? |
| Construir sin IA | Login con JWT y un endpoint que solo pueda usar un rol concreto. |
| Defender | Por qué no guardar datos sensibles en el token, cómo revocar. |
| Ojo con la versión | El tutorial oficial de FastAPI avisa de que antes usaba otra librería (PyJWT): contrasta cualquier curso con la versión actual del tutorial. |
| Libro de referencia | Alvero Velmora, *FastAPI en Acción* |

### Capítulo 20. Async, streaming y tareas

| Campo | Contenido |
| --- | --- |
| id | `backend/async-api` |
| Archivo | `contenido/parte-03-backend/cap-20-async-streaming-y-tareas.md` |
| Requisitos | Capítulo 19 |
| Al terminar podrás | Explicar endpoints async frente a sync, tareas en segundo plano, streaming y Server-Sent Events. Construir sin ayuda: endpoint que emita eventos SSE token a token, como hace un LLM. Defender tus decisiones sobre: qué bloquea el event loop, cuándo una cola externa en vez de background tasks. |
| Secciones | 20.1 def frente a async def<br>20.2 Tareas en segundo plano<br>20.3 Server-Sent Events<br>20.4 Streaming de respuestas |
| Explicar | ¿Qué hace FastAPI distinto con def y con async def? |
| Construir sin IA | Endpoint que emita eventos SSE token a token, como hace un LLM. |
| Defender | Qué bloquea el event loop, cuándo una cola externa en vez de background tasks. |
| Libro de referencia | Alvero Velmora, *FastAPI en Acción* |

### Capítulo 21. Tests de API

| Campo | Contenido |
| --- | --- |
| id | `backend/tests-api` |
| Archivo | `contenido/parte-03-backend/cap-21-tests-de-api.md` |
| Requisitos | Capítulo 20 |
| Al terminar podrás | Explicar cliente de pruebas, base de datos de test, fixtures, tests de contrato. Construir sin ayuda: suite que cubra éxito, validación, auth y error de base de datos de un recurso. Defender tus decisiones sobre: aislar la base de datos entre tests, qué no merece la pena testear. |
| Secciones | 21.1 El cliente de pruebas<br>21.2 Base de datos de pruebas y fixtures<br>21.3 Tests asíncronos<br>21.4 Sustituir dependencias |
| Explicar | ¿Qué pruebas en un test de API que no pruebas en uno unitario? |
| Construir sin IA | Suite que cubra éxito, validación, auth y error de base de datos de un recurso. |
| Defender | Aislar la base de datos entre tests, qué no merece la pena testear. |
| Libro de referencia | Alvero Velmora, *FastAPI en Acción* |

### Capítulo 22. Docker y despliegue

| Campo | Contenido |
| --- | --- |
| id | `backend/despliegue` |
| Archivo | `contenido/parte-03-backend/cap-22-docker-y-despliegue.md` |
| Requisitos | Capítulo 21 |
| Al terminar podrás | Explicar imágenes, capas, variables de entorno, configuración por entorno, despliegue en Railway. Construir sin ayuda: dockerfile multi-etapa de tu API y despliegue con la base de datos como servicio aparte. Defender tus decisiones sobre: secretos fuera de la imagen, imagen frente a contenedor. |
| Secciones | 22.1 Imágenes y contenedores<br>22.2 Dockerfile y capas<br>22.3 Builds multietapa<br>22.4 Configuración por entorno y secretos<br>22.5 Desplegar |
| Explicar | ¿Por qué el orden de las instrucciones de un Dockerfile cambia el tiempo de build? |
| Construir sin IA | Dockerfile multi-etapa de tu API y despliegue con la base de datos como servicio aparte. |
| Defender | Secretos fuera de la imagen, imagen frente a contenedor. |
| Libro de referencia | Alvero Velmora, *FastAPI en Acción* |

---

## Parte IV. IA aplicada: LLMs, RAG y skills

- **Fase:** 2
- **Por qué:** Entender qué hace un modelo por dentro (tokens, contexto, herramientas, recuperación) es lo que separa usar IA de construir con IA.
- **Requisitos de la parte:** Partes I y II; capítulos 14 a 16
- **Proyecto de la parte (¿Ya existe ese issue?):** RAG sobre los issues y la documentación de gentle-shell: dado el texto de un issue nuevo, encuentra posibles duplicados y la documentación relevante, con citas. Evalúalo con pares reales de duplicado y no duplicado sacados del historial del repo. Es útil para quien mantiene el proyecto.

### Capítulo 23. Cómo funciona un LLM

| Campo | Contenido |
| --- | --- |
| id | `ia/llm-base` |
| Archivo | `contenido/parte-04-ia/cap-23-como-funciona-un-llm.md` |
| Requisitos | Partes I y II; capítulos 14 a 16 |
| Al terminar podrás | Explicar tokens, ventana de contexto, temperatura, por qué inventa, coste y latencia. Construir sin ayuda: script que cuente tokens de un prompt y estime coste y si cabe en el contexto de un modelo. Defender tus decisiones sobre: contexto frente a memoria, qué cambia la temperatura. |
| Secciones | 23.1 Tokens y tokenización<br>23.2 Transformers a vista de pájaro<br>23.3 Ventana de contexto<br>23.4 Muestreo y temperatura<br>23.5 Por qué un modelo inventa |
| Explicar | ¿Por qué un modelo puede inventar una función que no existe con total seguridad? |
| Construir sin IA | Script que cuente tokens de un prompt y estime coste y si cabe en el contexto de un modelo. |
| Defender | Contexto frente a memoria, qué cambia la temperatura. |
| Libro de referencia | Basilio Fajardo Gálvez, *Desarrollo de Aplicaciones con IA: de principiante a experto en Skills, Agentes y RAG*; Miguel Ángel Núñez Sabin y otro autor, *Agentes IA. Despierte, comprenda, cree y visione el futuro* |

### Capítulo 24. Llamar a un modelo

| Campo | Contenido |
| --- | --- |
| id | `ia/api-llm` |
| Archivo | `contenido/parte-04-ia/cap-24-llamar-a-un-modelo.md` |
| Requisitos | Capítulo 23 |
| Al terminar podrás | Explicar mensajes y roles, parámetros, streaming, salida estructurada en JSON. Construir sin ayuda: cliente mínimo con streaming contra tu simulador LLM y luego contra un proveedor real. Defender tus decisiones sobre: cómo garantizar JSON válido, qué hacer cuando no lo es. |
| Secciones | 24.1 Mensajes y roles<br>24.2 Parámetros de la petición<br>24.3 Streaming<br>24.4 Salida estructurada<br>24.5 Errores, límites y reintentos |
| Explicar | ¿Qué viaja exactamente en una petición a un modelo y por qué hay que reenviar el historial? |
| Construir sin IA | Cliente mínimo con streaming contra tu simulador LLM y luego contra un proveedor real. |
| Defender | Cómo garantizar JSON válido, qué hacer cuando no lo es. |
| Libro de referencia | Basilio Fajardo Gálvez, *Desarrollo de Aplicaciones con IA: de principiante a experto en Skills, Agentes y RAG* |

### Capítulo 25. Instrucciones y prompts

| Campo | Contenido |
| --- | --- |
| id | `ia/prompting` |
| Archivo | `contenido/parte-04-ia/cap-25-instrucciones-y-prompts.md` |
| Requisitos | Capítulo 24 |
| Al terminar podrás | Explicar instrucciones claras, ejemplos, formato de salida, descomponer tareas. Construir sin ayuda: mismo problema con tres prompts distintos; mide cuál acierta más en 20 casos. Defender tus decisiones sobre: cuándo el problema no es el prompt sino el diseño. |
| Secciones | 25.1 Instrucciones claras<br>25.2 Ejemplos<br>25.3 Formato de salida<br>25.4 Descomponer tareas |
| Explicar | ¿Por qué un ejemplo bien elegido vale más que tres párrafos de instrucciones? |
| Construir sin IA | Mismo problema con tres prompts distintos; mide cuál acierta más en 20 casos. |
| Defender | Cuándo el problema no es el prompt sino el diseño. |
| Libro de referencia | Basilio Fajardo Gálvez, *Desarrollo de Aplicaciones con IA: de principiante a experto en Skills, Agentes y RAG* |

### Capítulo 26. Tool calling

| Campo | Contenido |
| --- | --- |
| id | `ia/tool-calling` |
| Archivo | `contenido/parte-04-ia/cap-26-tool-calling.md` |
| Requisitos | Capítulo 25 |
| Al terminar podrás | Explicar esquema JSON de herramientas, quién ejecuta la herramienta, bucle de petición y resultado. Construir sin ayuda: dos herramientas (calculadora y buscador de archivos locales) con el bucle completo escrito a mano. Defender tus decisiones sobre: validar argumentos, qué pasa si el modelo pide una herramienta que no existe. |
| Secciones | 26.1 Qué es el tool calling<br>26.2 Describir herramientas con JSON Schema<br>26.3 El bucle petición y resultado<br>26.4 Validar argumentos y fallos |
| Explicar | ¿El modelo ejecuta la herramienta? Explica quién hace qué en cada paso. |
| Construir sin IA | Dos herramientas (calculadora y buscador de archivos locales) con el bucle completo escrito a mano. |
| Defender | Validar argumentos, qué pasa si el modelo pide una herramienta que no existe. |
| Libro de referencia | Basilio Fajardo Gálvez, *Desarrollo de Aplicaciones con IA: de principiante a experto en Skills, Agentes y RAG*; Micheal Lanham, *Agentes de IA en acción (2.ª ed.): flujos de trabajo inteligentes con LLM, MCP, A2A* |

### Capítulo 27. Embeddings y RAG

| Campo | Contenido |
| --- | --- |
| id | `ia/rag` |
| Archivo | `contenido/parte-04-ia/cap-27-embeddings-y-rag.md` |
| Requisitos | Capítulo 26 |
| Al terminar podrás | Explicar embeddings, troceado, almacenes vectoriales, recuperación, reordenación, citas. Construir sin ayuda: rAG sobre la documentación de un proyecto open source que responda con la cita exacta. Defender tus decisiones sobre: tamaño de trozo, búsqueda híbrida, cuándo RAG no es la solución. |
| Secciones | 27.1 Embeddings<br>27.2 Troceado de documentos<br>27.3 Almacenes vectoriales y búsqueda<br>27.4 Recuperar y generar<br>27.5 Reordenar y citar<br>27.6 Por qué falla un RAG |
| Explicar | ¿Por qué un RAG responde mal aunque el documento correcto esté en la base? |
| Construir sin IA | RAG sobre la documentación de un proyecto open source que responda con la cita exacta. |
| Defender | Tamaño de trozo, búsqueda híbrida, cuándo RAG no es la solución. |
| Libro de referencia | Basilio Fajardo Gálvez, *Desarrollo de Aplicaciones con IA: de principiante a experto en Skills, Agentes y RAG* |

### Capítulo 28. Evaluación

| Campo | Contenido |
| --- | --- |
| id | `ia/evals` |
| Archivo | `contenido/parte-04-ia/cap-28-evaluacion.md` |
| Requisitos | Capítulo 27 |
| Al terminar podrás | Explicar conjuntos de prueba, métricas, regresiones, evaluar con otro modelo y sus límites. Construir sin ayuda: set de 30 casos con respuesta esperada y un script que puntúe tu RAG antes y después de un cambio. Defender tus decisiones sobre: sesgos de evaluar con LLM, por qué guardar los casos en el repo. |
| Secciones | 28.1 Por qué evaluar<br>28.2 Conjuntos de prueba<br>28.3 Métricas<br>28.4 Un modelo como juez y sus límites<br>28.5 Regresiones |
| Explicar | ¿Cómo sabes que un cambio de prompt mejoró y no solo te lo parece? |
| Construir sin IA | Set de 30 casos con respuesta esperada y un script que puntúe tu RAG antes y después de un cambio. |
| Defender | Sesgos de evaluar con LLM, por qué guardar los casos en el repo. |

### Capítulo 29. Skills

| Campo | Contenido |
| --- | --- |
| id | `ia/skills` |
| Archivo | `contenido/parte-04-ia/cap-29-skills.md` |
| Requisitos | Capítulo 28 |
| Al terminar podrás | Explicar empaquetar conocimiento procedimental para un agente: instrucciones, ejemplos y scripts. Construir sin ayuda: skill que enseñe a un agente a preparar un PR según el CONTRIBUTING de un repo concreto. Defender tus decisiones sobre: qué va en la skill y qué en el código. |
| Secciones | 29.1 Qué es una skill<br>29.2 Anatomía de una skill<br>29.3 Skill, prompt o herramienta: cuándo cada una |
| Explicar | ¿Qué diferencia una skill de un prompt largo? |
| Construir sin IA | Skill que enseñe a un agente a preparar un PR según el CONTRIBUTING de un repo concreto. |
| Defender | Qué va en la skill y qué en el código. |
| Libro de referencia | Basilio Fajardo Gálvez, *Desarrollo de Aplicaciones con IA: de principiante a experto en Skills, Agentes y RAG* |

### Capítulo 30. Dónde aporta valor

| Campo | Contenido |
| --- | --- |
| id | `ia/valor-negocio` |
| Archivo | `contenido/parte-04-ia/cap-30-donde-aporta-valor.md` |
| Requisitos | Capítulo 29 |
| Al terminar podrás | Explicar casos de uso reales, coste frente a beneficio, cuándo no usar IA. Construir sin ayuda: ficha de un caso real con coste por uso estimado y riesgos. Defender tus decisiones sobre: por qué un flujo determinista a veces gana a un agente. |
| Secciones | 30.1 Casos de uso reales<br>30.2 Coste y latencia<br>30.3 Cuándo no usar IA<br>30.4 Flujos deterministas frente a agentes |
| Explicar | Elige un proceso que conozcas: ¿qué parte automatizarías con IA y cuál nunca? |
| Construir sin IA | Ficha de un caso real con coste por uso estimado y riesgos. |
| Defender | Por qué un flujo determinista a veces gana a un agente. |
| Libro de referencia | Iván Rodríguez, *Asistentes y agentes empresariales con IA* |

---

## Parte V. Agentes de IA

- **Fase:** 3
- **Por qué:** Un agente es un bucle con herramientas, memoria y límites. Construirlo primero a mano hace que cualquier framework, y gentle-shell, se lea fácil.
- **Requisitos de la parte:** Partes III y IV
- **Proyecto de la parte (Servidor MCP de contexto de contribución):** Servidor MCP que da a cualquier agente el contexto para contribuir a un repo: leer CONTRIBUTING, buscar issues (con tu RAG), historial de un archivo y quién lo mantiene. Pruébalo desde gentle-shell u OpenCode y desde tu bucle a mano, con el simulador LLM en los tests.

### Capítulo 31. El bucle del agente

| Campo | Contenido |
| --- | --- |
| id | `agentes/bucle` |
| Archivo | `contenido/parte-05-agentes/cap-31-el-bucle-del-agente.md` |
| Requisitos | Partes III y IV |
| Al terminar podrás | Explicar observar, decidir, actuar; condición de parada, presupuesto de pasos y de coste. Construir sin ayuda: agente sin framework que resuelva una tarea de varios pasos sobre archivos locales, con límite de pasos. Defender tus decisiones sobre: dónde poner los límites, cómo registrar cada paso. |
| Secciones | 31.1 Qué es un agente<br>31.2 Pensar, actuar, observar<br>31.3 Condición de parada y presupuesto<br>31.4 Trazas: ver qué hizo el agente |
| Explicar | ¿Qué impide que un agente se quede en bucle infinito y cuánto cuesta cada vuelta? |
| Construir sin IA | Agente sin framework que resuelva una tarea de varios pasos sobre archivos locales, con límite de pasos. |
| Defender | Dónde poner los límites, cómo registrar cada paso. |
| Libro de referencia | Micheal Lanham, *Agentes de IA en acción (2.ª ed.): flujos de trabajo inteligentes con LLM, MCP, A2A*; Manuel Schneider, *Desarrollo de Agentes de IA con Python: paso a paso con Agno* |

### Capítulo 32. Agentes con Agno

| Campo | Contenido |
| --- | --- |
| id | `agentes/agno` |
| Archivo | `contenido/parte-05-agentes/cap-32-agentes-con-agno.md` |
| Requisitos | Capítulo 31 |
| Al terminar podrás | Explicar agentes, herramientas, memoria y equipos en un framework real. Construir sin ayuda: reimplementa tu agente a mano con Agno y compara líneas, control y trazas. Defender tus decisiones sobre: cuándo un framework sobra. |
| Secciones | 32.1 Agent, Team y Workflow<br>32.2 Herramientas en Agno<br>32.3 Salida estructurada<br>32.4 De tu bucle a mano a Agno |
| Explicar | ¿Qué te da Agno que no tenías en tu bucle a mano y qué te oculta? |
| Construir sin IA | Reimplementa tu agente a mano con Agno y compara líneas, control y trazas. |
| Defender | Cuándo un framework sobra. |
| Ojo con la versión | Agno tiene documentación separada para la versión 1 (docs-v1.agno.com) y la actual; los libros y cursos anteriores pueden usar la 1. |
| Libro de referencia | Manuel Schneider, *Desarrollo de Agentes de IA con Python: paso a paso con Agno* |

### Capítulo 33. Memoria

| Campo | Contenido |
| --- | --- |
| id | `agentes/memoria` |
| Archivo | `contenido/parte-05-agentes/cap-33-memoria.md` |
| Requisitos | Capítulo 32 |
| Al terminar podrás | Explicar memoria de corto y largo plazo, resúmenes, memoria persistente entre sesiones. Construir sin ayuda: memoria persistente en SQLite para tu agente, con búsqueda por tema. Defender tus decisiones sobre: coste de contexto, memoria obsoleta, privacidad. |
| Secciones | 33.1 Contexto frente a memoria<br>33.2 Sesiones e historial<br>33.3 Memoria persistente<br>33.4 Resúmenes y compresión<br>33.5 Privacidad |
| Explicar | ¿Qué guardarías en memoria persistente de un agente de código y qué nunca? |
| Construir sin IA | Memoria persistente en SQLite para tu agente, con búsqueda por tema. |
| Defender | Coste de contexto, memoria obsoleta, privacidad. |
| Libro de referencia | Micheal Lanham, *Agentes de IA en acción (2.ª ed.): flujos de trabajo inteligentes con LLM, MCP, A2A* |

### Capítulo 34. MCP

| Campo | Contenido |
| --- | --- |
| id | `agentes/mcp` |
| Archivo | `contenido/parte-05-agentes/cap-34-mcp.md` |
| Requisitos | Capítulo 33 |
| Al terminar podrás | Explicar cliente y servidor, herramientas, recursos y prompts, transportes. Construir sin ayuda: servidor MCP mínimo con una herramienta y un recurso, probado desde un cliente real. Defender tus decisiones sobre: seguridad de un servidor MCP, por qué es un estándar y no una librería. |
| Secciones | 34.1 El problema que resuelve MCP<br>34.2 Host, cliente y servidor<br>34.3 Primitivas: tools, resources y prompts<br>34.4 Transportes: stdio y Streamable HTTP<br>34.5 Descubrimiento y versión del protocolo<br>34.6 Construir un servidor |
| Explicar | ¿Qué problema resuelve MCP que no resolvía el tool calling por sí solo? |
| Construir sin IA | Servidor MCP mínimo con una herramienta y un recurso, probado desde un cliente real. |
| Defender | Seguridad de un servidor MCP, por qué es un estándar y no una librería. |
| Ojo con la versión | La versión del protocolo MCP 2026-07-28 introduce cambios (descubrimiento con server/discover, sampling obsoleto); fija la versión que explicas. |
| Libro de referencia | Micheal Lanham, *Agentes de IA en acción (2.ª ed.): flujos de trabajo inteligentes con LLM, MCP, A2A* |

### Capítulo 35. Multiagente y A2A

| Campo | Contenido |
| --- | --- |
| id | `agentes/multiagente` |
| Archivo | `contenido/parte-05-agentes/cap-35-multiagente-y-a2a.md` |
| Requisitos | Capítulo 34 |
| Al terminar podrás | Explicar orquestador y subagentes, reparto de tareas, protocolo A2A. Construir sin ayuda: orquestador que delegue revisión y tests en dos subagentes y combine resultados. Defender tus decisiones sobre: mCP frente a A2A, cómo se comparte contexto entre agentes. |
| Secciones | 35.1 Cuándo dividir en varios agentes<br>35.2 Orquestador y subagentes<br>35.3 Equipos en Agno<br>35.4 El protocolo A2A<br>35.5 MCP frente a A2A |
| Explicar | ¿Cuándo compensa dividir en varios agentes y cuándo es complejidad gratuita? |
| Construir sin IA | Orquestador que delegue revisión y tests en dos subagentes y combine resultados. |
| Defender | MCP frente a A2A, cómo se comparte contexto entre agentes. |
| Libro de referencia | Micheal Lanham, *Agentes de IA en acción (2.ª ed.): flujos de trabajo inteligentes con LLM, MCP, A2A* |

### Capítulo 36. Seguridad y control

| Campo | Contenido |
| --- | --- |
| id | `agentes/seguridad-agentes` |
| Archivo | `contenido/parte-05-agentes/cap-36-seguridad-y-control.md` |
| Requisitos | Capítulo 35 |
| Al terminar podrás | Explicar inyección de prompts, permisos, sandbox, aprobación humana. Construir sin ayuda: ataca tu propio agente con un archivo trampa y añade la defensa. Defender tus decisiones sobre: mínimo privilegio, qué acciones exigen confirmación. |
| Secciones | 36.1 Inyección de prompts<br>36.2 Mínimo privilegio y permisos<br>36.3 Sandbox<br>36.4 Aprobación humana |
| Explicar | ¿Cómo puede un README malicioso hacer que un agente haga algo que no pediste? |
| Construir sin IA | Ataca tu propio agente con un archivo trampa y añade la defensa. |
| Defender | Mínimo privilegio, qué acciones exigen confirmación. |
| Ojo con la versión | OpenCode tiene una configuración V2 de permisos con sintaxis distinta a la V1. |
| Libro de referencia | Micheal Lanham, *Agentes de IA en acción (2.ª ed.): flujos de trabajo inteligentes con LLM, MCP, A2A*; Iván Rodríguez, *Asistentes y agentes empresariales con IA* |

---

## Parte VI. Ingeniería de software agéntica

- **Fase:** 3
- **Por qué:** Es exactamente lo que hace gentle-shell. Aprender a dirigir y revisar agentes de código es la habilidad que pide el futuro inmediato, y la que te hace útil en ese ecosistema.
- **Requisitos de la parte:** Parte V; capítulos 1, 2 y 5
- **Proyecto de la parte (Duelo humano contra agente):** Elige tres issues pequeños reales. Resuelve cada uno primero tú sin IA y cronometrado, luego con gentle-shell u OpenCode. Compara diffs y anota los fallos de ambos. Si encuentras un fallo reproducible del agente, conviértelo en un issue bien escrito para el proyecto.

### Capítulo 37. Trabajar con un agente de código

| Campo | Contenido |
| --- | --- |
| id | `agentica/opencode` |
| Archivo | `contenido/parte-06-agentica/cap-37-trabajar-con-un-agente-de-codigo.md` |
| Requisitos | Parte V; capítulos 1, 2 y 5 |
| Al terminar podrás | Explicar contexto, comandos, permisos, sesiones y límites de un agente como OpenCode. Construir sin ayuda: configura OpenCode en un proyecto tuyo con reglas propias y documenta qué cambió en sus respuestas. Defender tus decisiones sobre: qué le das y qué le niegas al agente. |
| Secciones | 37.1 Qué hace un agente de código<br>37.2 Contexto y archivos de reglas<br>37.3 Permisos<br>37.4 Sesiones y límites |
| Explicar | ¿Qué información necesita un agente de código para no inventarse la arquitectura? |
| Construir sin IA | Configura OpenCode en un proyecto tuyo con reglas propias y documenta qué cambió en sus respuestas. |
| Defender | Qué le das y qué le niegas al agente. |
| Ojo con la versión | OpenCode tiene una configuración V2 con sintaxis distinta a la V1. |
| Libro de referencia | Enrique Barros Fernández, *Ingeniería de software agéntica con inteligencia artificial: versión OpenCode* |

### Capítulo 38. Especificar antes de pedir

| Campo | Contenido |
| --- | --- |
| id | `agentica/especificar` |
| Archivo | `contenido/parte-06-agentica/cap-38-especificar-antes-de-pedir.md` |
| Requisitos | Capítulo 37 |
| Al terminar podrás | Explicar tareas con criterio de aceptación, specs, flujo ODD de Gentle AI. Construir sin ayuda: spec de una funcionalidad con criterios de aceptación verificables por tests, antes de abrir el agente. Defender tus decisiones sobre: qué nivel de detalle es suficiente. |
| Secciones | 38.1 Tarea frente a especificación<br>38.2 Criterios de aceptación verificables<br>38.3 El flujo ODD de Gentle AI |
| Explicar | ¿Por qué una buena spec ahorra más tiempo que un buen prompt? |
| Construir sin IA | Spec de una funcionalidad con criterios de aceptación verificables por tests, antes de abrir el agente. |
| Defender | Qué nivel de detalle es suficiente. |
| Libro de referencia | Enrique Barros Fernández, *Ingeniería de software agéntica con inteligencia artificial: versión OpenCode* |

### Capítulo 39. Revisar código de IA

| Campo | Contenido |
| --- | --- |
| id | `agentica/revisar` |
| Archivo | `contenido/parte-06-agentica/cap-39-revisar-codigo-de-ia.md` |
| Requisitos | Capítulo 38 |
| Al terminar podrás | Explicar leer cada línea del diff, tests primero, señales de alarma típicas. Construir sin ayuda: revisa tres diffs generados por IA y documenta cada problema encontrado. Defender tus decisiones sobre: cuándo rechazar un cambio entero. |
| Secciones | 39.1 Leer un diff de verdad<br>39.2 Tests primero<br>39.3 Señales de alarma<br>39.4 Cuándo rechazar un cambio |
| Explicar | ¿Qué errores típicos introduce un agente que pasan los tests? |
| Construir sin IA | Revisa tres diffs generados por IA y documenta cada problema encontrado. |
| Defender | Cuándo rechazar un cambio entero. |
| Libro de referencia | Enrique Barros Fernández, *Ingeniería de software agéntica con inteligencia artificial: versión OpenCode* |

### Capítulo 40. Contexto del proyecto

| Campo | Contenido |
| --- | --- |
| id | `agentica/contexto` |
| Archivo | `contenido/parte-06-agentica/cap-40-contexto-del-proyecto.md` |
| Requisitos | Capítulo 39 |
| Al terminar podrás | Explicar archivos de reglas como AGENTS.md, memoria persistente, convenciones. Construir sin ayuda: archivo de reglas para tu proyecto FastAPI y prueba de que cambia el resultado. Defender tus decisiones sobre: contexto que ayuda frente a contexto que estorba. |
| Secciones | 40.1 AGENTS.md y CLAUDE.md<br>40.2 Instrucciones externas<br>40.3 Contexto que estorba |
| Explicar | ¿Qué pondrías en el archivo de reglas de tu proyecto y por qué? |
| Construir sin IA | Archivo de reglas para tu proyecto FastAPI y prueba de que cambia el resultado. |
| Defender | Contexto que ayuda frente a contexto que estorba. |
| Libro de referencia | Enrique Barros Fernández, *Ingeniería de software agéntica con inteligencia artificial: versión OpenCode* |

### Capítulo 41. Cómo trabaja gentle-shell

| Campo | Contenido |
| --- | --- |
| id | `agentica/gentle-flujo` |
| Archivo | `contenido/parte-06-agentica/cap-41-como-trabaja-gentle-shell.md` |
| Requisitos | Capítulo 40 |
| Al terminar podrás | Explicar agente, subagentes, revisión y flujo ODD dentro del ecosistema Gentle AI. Construir sin ayuda: instala gentle-shell en modo independiente, usa el flujo en una tarea real y documenta cada fase. Defender tus decisiones sobre: qué parte pone Pi y qué parte pone Gentle AI. |
| Secciones | 41.1 Qué es gentle-shell: Pi y Gentle AI<br>41.2 Instalación aislada<br>41.3 Recorrido de una tarea<br>41.4 Versiones fijadas del runtime |
| Explicar | Explica el recorrido de una tarea dentro de gentle-shell desde que la pides hasta el cambio. |
| Construir sin IA | Instala gentle-shell en modo independiente, usa el flujo en una tarea real y documenta cada fase. |
| Defender | Qué parte pone Pi y qué parte pone Gentle AI. |

---

## Parte VII. TypeScript y Node

- **Fase:** 3
- **Por qué:** gentle-shell es un paquete TypeScript para Pi (distribuido en npm como gentle-pi). Sin TypeScript, tu contribución se queda en documentación.
- **Requisitos de la parte:** Partes I y II; capítulo 41
- **Proyecto de la parte (Primer PR a gentle-shell):** Antes, construye un paquete mínimo propio imitando cómo se empaqueta gentle-shell para entender su ciclo de carga. Después, primer PR: documentación o tests; luego un bug pequeño. Cada PR pasa por la arqueología de la rama Oficio aplicada a tu propio cambio.
- **Nota:** No hay libro de TypeScript en tu lista: la fuente es el Handbook oficial.

### Capítulo 42. Sistema de tipos

| Campo | Contenido |
| --- | --- |
| id | `typescript/ts-tipos` |
| Archivo | `contenido/parte-07-typescript/cap-42-sistema-de-tipos.md` |
| Requisitos | Partes I y II; capítulo 41 |
| Al terminar podrás | Explicar tipado estructural, uniones, narrowing, genéricos, unknown frente a any. Construir sin ayuda: modela los estados de un nodo de este roadmap con uniones discriminadas y funciones exhaustivas. Defender tus decisiones sobre: por qué evitar any, qué queda de los tipos en tiempo de ejecución. |
| Secciones | 42.1 Tipos básicos<br>42.2 Tipado estructural<br>42.3 Uniones y narrowing<br>42.4 Genéricos<br>42.5 unknown, any y never |
| Explicar | ¿Qué significa que TypeScript sea estructural y en qué se diferencia de los type hints de Python? |
| Construir sin IA | Modela los estados de un nodo de este roadmap con uniones discriminadas y funciones exhaustivas. |
| Defender | Por qué evitar any, qué queda de los tipos en tiempo de ejecución. |

### Capítulo 43. Módulos y paquetes

| Campo | Contenido |
| --- | --- |
| id | `typescript/ts-modulos` |
| Archivo | `contenido/parte-07-typescript/cap-43-modulos-y-paquetes.md` |
| Requisitos | Capítulo 42 |
| Al terminar podrás | Explicar eSM frente a CommonJS, package.json, exports, compilación. Construir sin ayuda: librería TypeScript pequeña que funcione importada desde otro proyecto. Defender tus decisiones sobre: campo exports, por qué fallan los imports tras compilar. |
| Secciones | 43.1 ESM frente a CommonJS<br>43.2 package.json y exports<br>43.3 Compilar con tsc<br>43.4 tsconfig |
| Explicar | ¿Qué decide si Node trata un archivo como ESM o CommonJS? |
| Construir sin IA | Librería TypeScript pequeña que funcione importada desde otro proyecto. |
| Defender | Campo exports, por qué fallan los imports tras compilar. |

### Capítulo 44. Event loop de Node

| Campo | Contenido |
| --- | --- |
| id | `typescript/node-async` |
| Archivo | `contenido/parte-07-typescript/cap-44-event-loop-de-node.md` |
| Requisitos | Capítulo 43 |
| Al terminar podrás | Explicar promesas, async y await, streams, procesos hijo. Construir sin ayuda: cLI que lance un proceso hijo y vaya mostrando su salida en vivo. Defender tus decisiones sobre: promesas sin await, errores no capturados. |
| Secciones | 44.1 El modelo del event loop<br>44.2 Promesas y async/await<br>44.3 Timers y nextTick<br>44.4 Streams<br>44.5 Procesos hijo |
| Explicar | Compara el event loop de Node con el de asyncio: ¿qué se parece y qué no? |
| Construir sin IA | CLI que lance un proceso hijo y vaya mostrando su salida en vivo. |
| Defender | Promesas sin await, errores no capturados. |

### Capítulo 45. npm y versiones

| Campo | Contenido |
| --- | --- |
| id | `typescript/npm` |
| Archivo | `contenido/parte-07-typescript/cap-45-npm-y-versiones.md` |
| Requisitos | Capítulo 44 |
| Al terminar podrás | Explicar publicar, semver, lockfiles, binarios, versiones fijadas. Construir sin ayuda: publica un paquete de prueba con un binario y una versión de parche. Defender tus decisiones sobre: rangos de semver, riesgos de la cadena de suministro. |
| Secciones | 45.1 Semver<br>45.2 Lockfiles<br>45.3 Binarios y CLIs<br>45.4 Publicar<br>45.5 Cadena de suministro |
| Explicar | ¿Por qué gentle-shell fija la versión exacta de su runtime en vez de aceptar cualquiera? |
| Construir sin IA | Publica un paquete de prueba con un binario y una versión de parche. |
| Defender | Rangos de semver, riesgos de la cadena de suministro. |

### Capítulo 46. Tests en TypeScript

| Campo | Contenido |
| --- | --- |
| id | `typescript/ts-tests` |
| Archivo | `contenido/parte-07-typescript/cap-46-tests-en-typescript.md` |
| Requisitos | Capítulo 45 |
| Al terminar podrás | Explicar runner de tests, tipos en los tests, integración continua. Construir sin ayuda: tests de tu CLI y un workflow de GitHub Actions que los ejecute. Defender tus decisiones sobre: qué hace la CI de un proyecto antes de aceptar un PR. |
| Secciones | 46.1 El runner de tests<br>46.2 Tipos en los tests<br>46.3 Integración continua con GitHub Actions |
| Explicar | ¿Qué atrapa el compilador que no atrapan los tests, y al revés? |
| Construir sin IA | Tests de tu CLI y un workflow de GitHub Actions que los ejecute. |
| Defender | Qué hace la CI de un proyecto antes de aceptar un PR. |

### Capítulo 47. Leer gentle-shell

| Campo | Contenido |
| --- | --- |
| id | `typescript/leer-gentle` |
| Archivo | `contenido/parte-07-typescript/cap-47-leer-gentle-shell.md` |
| Requisitos | Capítulo 46 |
| Al terminar podrás | Explicar estructura del repo, cómo se carga como paquete de Pi, cómo se publica y verifica una versión. Construir sin ayuda: mapa escrito del repo: carpetas, responsabilidades y dónde tocarías para un cambio pequeño. Defender tus decisiones sobre: cómo encontrar un primer issue asumible. |
| Secciones | 47.1 Estructura del repositorio<br>47.2 Cómo se carga como paquete de Pi<br>47.3 Publicación y verificación de versiones<br>47.4 Encontrar un primer issue |
| Explicar | Explica la estructura del repo y el camino desde el comando gentle-shell hasta que Pi carga el paquete. |
| Construir sin IA | Mapa escrito del repo: carpetas, responsabilidades y dónde tocarías para un cambio pequeño. |
| Defender | Cómo encontrar un primer issue asumible. |

---

## Parte VIII. Arquitectura y diseño de sistemas

- **Fase:** 4
- **Por qué:** Para contribuir a decisiones y no solo a líneas de código hace falta entender los compromisos que hay detrás de cada diseño.
- **Requisitos de la parte:** Partes III y V
- **Proyecto de la parte (ADRs del ecosistema Gentle):** Lee la arquitectura de gentle-shell y gentle-ai (versión de runtime fijada, home aislada, lanzador) y reconstruye tres ADRs: decisión, alternativas y compromisos. Contrasta tus hipótesis con los mantenedores en Discussions antes de darlas por buenas.

### Capítulo 48. Analizar compromisos

| Campo | Contenido |
| --- | --- |
| id | `arquitectura/compromisos` |
| Archivo | `contenido/parte-08-arquitectura/cap-48-analizar-compromisos.md` |
| Requisitos | Partes III y V |
| Al terminar podrás | Explicar no hay mejores prácticas, solo compromisos; ADRs y funciones de aptitud. Construir sin ayuda: escribe tres ADRs de decisiones reales de tus proyectos. Defender tus decisiones sobre: cómo documentar una decisión para que se entienda en un año. |
| Secciones | 48.1 No hay mejores prácticas, solo compromisos<br>48.2 ADRs<br>48.3 Atributos de calidad |
| Explicar | Elige una decisión de un proyecto tuyo: ¿qué ganaste y qué pagaste? |
| Construir sin IA | Escribe tres ADRs de decisiones reales de tus proyectos. |
| Defender | Cómo documentar una decisión para que se entienda en un año. |
| Libro de referencia | Ford, Richards, Sadalage y Dehghani, *Arquitectura de software: las partes difíciles* |

### Capítulo 49. Acoplamiento y granularidad

| Campo | Contenido |
| --- | --- |
| id | `arquitectura/acoplamiento` |
| Archivo | `contenido/parte-08-arquitectura/cap-49-acoplamiento-y-granularidad.md` |
| Requisitos | Capítulo 48 |
| Al terminar podrás | Explicar acoplamiento estático y dinámico, cuándo partir un servicio y cuándo juntarlo. Construir sin ayuda: analiza tu proyecto de finanzas o de actividades: qué partirías y qué no, con argumentos. Defender tus decisiones sobre: microservicios por moda, coste operativo. |
| Secciones | 49.1 Acoplamiento y cohesión<br>49.2 Monolito frente a servicios<br>49.3 Granularidad |
| Explicar | ¿Qué fuerzas empujan a partir un servicio y cuáles a juntarlo? |
| Construir sin IA | Analiza tu proyecto de finanzas o de actividades: qué partirías y qué no, con argumentos. |
| Defender | Microservicios por moda, coste operativo. |
| Libro de referencia | Ford, Richards, Sadalage y Dehghani, *Arquitectura de software: las partes difíciles* |

### Capítulo 50. Datos distribuidos

| Campo | Contenido |
| --- | --- |
| id | `arquitectura/datos-dist` |
| Archivo | `contenido/parte-08-arquitectura/cap-50-datos-distribuidos.md` |
| Requisitos | Capítulo 49 |
| Al terminar podrás | Explicar propiedad de los datos, consistencia eventual, sagas, transacciones distribuidas. Construir sin ayuda: diseña una saga con compensaciones para un flujo de tres pasos. Defender tus decisiones sobre: orquestación frente a coreografía. |
| Secciones | 50.1 Consistencia y disponibilidad<br>50.2 Replicación<br>50.3 Particionado<br>50.4 Sagas |
| Explicar | ¿Qué pierdes al pasar de una transacción en una base de datos a varias? |
| Construir sin IA | Diseña una saga con compensaciones para un flujo de tres pasos. |
| Defender | Orquestación frente a coreografía. |
| Libro de referencia | Ford, Richards, Sadalage y Dehghani, *Arquitectura de software: las partes difíciles* |

### Capítulo 51. Escalado

| Campo | Contenido |
| --- | --- |
| id | `arquitectura/escalado` |
| Archivo | `contenido/parte-08-arquitectura/cap-51-escalado.md` |
| Requisitos | Capítulo 50 |
| Al terminar podrás | Explicar vertical y horizontal, balanceo, servicios sin estado, estimaciones rápidas. Construir sin ayuda: estimación de capacidad para tu app de actividades con 100.000 usuarios. Defender tus decisiones sobre: dónde está el cuello de botella real. |
| Secciones | 51.1 Escalado vertical y horizontal<br>51.2 Balanceadores de carga<br>51.3 Servicios sin estado<br>51.4 Estimaciones rápidas |
| Explicar | ¿Por qué un servicio sin estado escala mejor? |
| Construir sin IA | Estimación de capacidad para tu app de actividades con 100.000 usuarios. |
| Defender | Dónde está el cuello de botella real. |
| Libro de referencia | Alex Xu, *Diseño de sistemas: una guía de información privilegiada (2.ª ed.)* |

### Capítulo 52. Cachés y colas

| Campo | Contenido |
| --- | --- |
| id | `arquitectura/cache-colas` |
| Archivo | `contenido/parte-08-arquitectura/cap-52-caches-y-colas.md` |
| Requisitos | Capítulo 51 |
| Al terminar podrás | Explicar estrategias de caché, invalidación, colas, mensajería, reintentos. Construir sin ayuda: añade caché y una cola de trabajos a tu simulador LLM y mide el efecto. Defender tus decisiones sobre: invalidación, entrega al menos una vez frente a exactamente una vez. |
| Secciones | 52.1 Estrategias de caché<br>52.2 Invalidación<br>52.3 Asincronía y colas<br>52.4 Entrega y reintentos |
| Explicar | ¿Cuándo una caché crea más problemas de los que resuelve? |
| Construir sin IA | Añade caché y una cola de trabajos a tu simulador LLM y mide el efecto. |
| Defender | Invalidación, entrega al menos una vez frente a exactamente una vez. |
| Libro de referencia | Alex Xu, *Diseño de sistemas: una guía de información privilegiada (2.ª ed.)* |

### Capítulo 53. Casos de diseño

| Campo | Contenido |
| --- | --- |
| id | `arquitectura/casos-diseno` |
| Archivo | `contenido/parte-08-arquitectura/cap-53-casos-de-diseno.md` |
| Requisitos | Capítulo 52 |
| Al terminar podrás | Explicar limitador de peticiones, notificaciones, colas de trabajo, almacenamiento. Construir sin ayuda: implementa un limitador de peticiones para el simulador y documenta su diseño. Defender tus decisiones sobre: alternativas de algoritmo y sus fallos. |
| Secciones | 53.1 Limitador de peticiones<br>53.2 Sistema de notificaciones<br>53.3 Caso real: el almacenamiento de Git |
| Explicar | Explica un limitador de peticiones de ventana deslizante a alguien que no programa. |
| Construir sin IA | Implementa un limitador de peticiones para el simulador y documenta su diseño. |
| Defender | Alternativas de algoritmo y sus fallos. |
| Libro de referencia | Alex Xu, *Diseño de sistemas: una guía de información privilegiada (2.ª ed.)* |

---

## Parte IX. Go

- **Fase:** 4
- **Por qué:** El runtime de Gentle AI está escrito en Go. Es la puerta a contribuir en el núcleo del ecosistema, no solo en su capa TypeScript.
- **Requisitos de la parte:** Parte VIII recomendada; capítulos 10 y 44 para comparar modelos de concurrencia
- **Proyecto de la parte (Tu simulador LLM, en Go):** Reescribe el núcleo del simulador (respuestas guionizadas y SSE) en Go y compáralo con la versión FastAPI: concurrencia, manejo de errores y distribución como binario. Luego, primer issue o PR en gentle-ai.
- **Nota:** No hay libro de Go en tu lista: la fuente es el Tour oficial y Effective Go.

### Capítulo 54. Fundamentos de Go

| Campo | Contenido |
| --- | --- |
| id | `go/go-base` |
| Archivo | `contenido/parte-09-go/cap-54-fundamentos-de-go.md` |
| Requisitos | Parte VIII recomendada; capítulos 10 y 44 para comparar modelos de concurrencia |
| Al terminar podrás | Explicar tipos, structs, métodos, interfaces implícitas, slices y mapas. Construir sin ayuda: port a Go de tu clase Dinero de la rama Python, con tests. Defender tus decisiones sobre: valor frente a puntero en receptores. |
| Secciones | 54.1 Tipos, structs y métodos<br>54.2 Interfaces implícitas<br>54.3 Slices y mapas<br>54.4 Paquetes |
| Explicar | ¿Qué significa que las interfaces de Go sean implícitas y qué recuerda de TypeScript? |
| Construir sin IA | Port a Go de tu clase Dinero de la rama Python, con tests. |
| Defender | Valor frente a puntero en receptores. |

### Capítulo 55. Errores como valores

| Campo | Contenido |
| --- | --- |
| id | `go/go-errores` |
| Archivo | `contenido/parte-09-go/cap-55-errores-como-valores.md` |
| Requisitos | Capítulo 54 |
| Al terminar podrás | Explicar error, wrapping, errors.Is y errors.As, panic frente a error. Construir sin ayuda: parser de configuración con errores envueltos y contexto útil. Defender tus decisiones sobre: cuándo un panic es aceptable. |
| Secciones | 55.1 error como valor<br>55.2 Envolver errores<br>55.3 errors.Is y errors.As<br>55.4 panic frente a error |
| Explicar | ¿Por qué Go no tiene excepciones y qué ganas con ello? |
| Construir sin IA | Parser de configuración con errores envueltos y contexto útil. |
| Defender | Cuándo un panic es aceptable. |

### Capítulo 56. Módulos y versiones

| Campo | Contenido |
| --- | --- |
| id | `go/go-modulos` |
| Archivo | `contenido/parte-09-go/cap-56-modulos-y-versiones.md` |
| Requisitos | Capítulo 55 |
| Al terminar podrás | Explicar go mod, versión mayor en la ruta del módulo, go install. Construir sin ayuda: módulo con dos versiones mayores instalables a la vez. Defender tus decisiones sobre: compatibilidad hacia atrás. |
| Secciones | 56.1 go mod<br>56.2 Versión mayor en la ruta del módulo<br>56.3 go install |
| Explicar | ¿Por qué gentle-ai cambia la ruta de su módulo al subir de versión mayor? |
| Construir sin IA | Módulo con dos versiones mayores instalables a la vez. |
| Defender | Compatibilidad hacia atrás. |

### Capítulo 57. Concurrencia

| Campo | Contenido |
| --- | --- |
| id | `go/go-concurrencia` |
| Archivo | `contenido/parte-09-go/cap-57-concurrencia.md` |
| Requisitos | Capítulo 56 |
| Al terminar podrás | Explicar goroutines, canales, select, context, sync. Construir sin ayuda: descargador concurrente con límite y cancelación por context. Defender tus decisiones sobre: fugas de goroutines, canales con y sin buffer. |
| Secciones | 57.1 Goroutines<br>57.2 Canales<br>57.3 select<br>57.4 context y cancelación<br>57.5 sync |
| Explicar | Compara goroutines con async de Python: ¿qué modelo es cada uno? |
| Construir sin IA | Descargador concurrente con límite y cancelación por context. |
| Defender | Fugas de goroutines, canales con y sin buffer. |

### Capítulo 58. CLIs en Go

| Campo | Contenido |
| --- | --- |
| id | `go/go-cli` |
| Archivo | `contenido/parte-09-go/cap-58-clis-en-go.md` |
| Requisitos | Capítulo 57 |
| Al terminar podrás | Explicar flags, subcomandos, binario único, distribución. Construir sin ayuda: cLI con subcomandos que lea y valide un archivo de configuración. Defender tus decisiones sobre: compilación cruzada, tamaño del binario. |
| Secciones | 58.1 Flags<br>58.2 Subcomandos<br>58.3 Binario único y distribución |
| Explicar | ¿Por qué tantas herramientas de desarrollo se escriben en Go? |
| Construir sin IA | CLI con subcomandos que lea y valide un archivo de configuración. |
| Defender | Compilación cruzada, tamaño del binario. |

### Capítulo 59. Leer gentle-ai

| Campo | Contenido |
| --- | --- |
| id | `go/leer-gentle-ai` |
| Archivo | `contenido/parte-09-go/cap-59-leer-gentle-ai.md` |
| Requisitos | Capítulo 58 |
| Al terminar podrás | Explicar estructura del runtime, cómo se instala y sincroniza, cómo se publica una versión. Construir sin ayuda: mapa del repo y localización de dónde vive un comando concreto. Defender tus decisiones sobre: primer issue asumible en Go. |
| Secciones | 59.1 Estructura del runtime<br>59.2 Instalación y sincronización<br>59.3 Publicación de versiones<br>59.4 Primer issue en Go |
| Explicar | Explica qué hace gentle-ai sync y por qué hay que ejecutarlo tras actualizar. |
| Construir sin IA | Mapa del repo y localización de dónde vive un comando concreto. |
| Defender | Primer issue asumible en Go. |

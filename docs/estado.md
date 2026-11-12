# Estado del libro

Tablero de progreso. Claude Code lo actualiza cada vez que un capítulo cambia de fase. Las métricas de cada capítulo las escribe `scripts/informe_capitulo.py N --guardar` al final de este archivo.

## Hitos

| Hito | Qué | Estado |
| --- | --- | --- |
| 0 | Cimientos: estructura, scripts con tests, subagentes y este tablero | hecho (2026-11-12) |
| 1 | Capítulo piloto: 1, «Git por dentro» | pendiente |
| 2 | Parte I completa | pendiente |
| 3 | Parte II completa | pendiente |
| 4 a 10 | Partes III a IX | pendiente |
| Final | Preliminares, apéndices, glosario y créditos | pendiente |

## Fases de un capítulo

`pendiente` → `1-fuentes` → `2-investigación` → `3-ejemplos` → `4-esquema` (lo aprueba devOC) → `4-redacción` → `5-revisión` → `6-aprobación` (devOC) → `7-publicado`.

## Capítulos

### Parte I. El oficio

| Cap. | Título | id | Fase | PENDIENTES | Notas |
| --- | --- | --- | --- | --- | --- |
| 1 | Git por dentro | `base/git-modelo` | pendiente | | |
| 2 | Flujo de contribución | `base/git-colab` | pendiente | | |
| 3 | Terminal y procesos | `base/terminal` | pendiente | | |
| 4 | HTTP de verdad | `base/http` | pendiente | | |
| 5 | Leer código ajeno | `base/leer-codigo` | pendiente | | |

### Parte II. Python profundo

| Cap. | Título | id | Fase | PENDIENTES | Notas |
| --- | --- | --- | --- | --- | --- |
| 6 | Modelo de objetos | `python/py-objetos` | pendiente | | |
| 7 | Funciones, closures y decoradores | `python/py-funciones` | pendiente | | |
| 8 | Iteradores y generadores | `python/py-iteracion` | pendiente | | |
| 9 | Tipos y validación | `python/py-tipos` | pendiente | | |
| 10 | Asincronía | `python/py-async` | pendiente | | |
| 11 | Errores y gestores de contexto | `python/py-errores` | pendiente | | |
| 12 | Testing con pytest | `python/py-tests` | pendiente | | |
| 13 | Módulos, paquetes y entornos | `python/py-paquetes` | pendiente | | |

### Parte III. Backend con FastAPI

| Cap. | Título | id | Fase | PENDIENTES | Notas |
| --- | --- | --- | --- | --- | --- |
| 14 | Diseño de APIs REST | `backend/api-diseno` | pendiente | | |
| 15 | Endpoints y routing | `backend/endpoints` | pendiente | | |
| 16 | Validación con Pydantic | `backend/validacion` | pendiente | | |
| 17 | Inyección de dependencias | `backend/dependencias` | pendiente | | |
| 18 | Persistencia con SQLAlchemy y PostgreSQL | `backend/persistencia` | pendiente | | |
| 19 | Autenticación y autorización | `backend/auth` | pendiente | | |
| 20 | Async, streaming y tareas | `backend/async-api` | pendiente | | |
| 21 | Tests de API | `backend/tests-api` | pendiente | | |
| 22 | Docker y despliegue | `backend/despliegue` | pendiente | | |

### Parte IV. IA aplicada

| Cap. | Título | id | Fase | PENDIENTES | Notas |
| --- | --- | --- | --- | --- | --- |
| 23 | Cómo funciona un LLM | `ia/llm-base` | pendiente | | |
| 24 | Llamar a un modelo | `ia/api-llm` | pendiente | | |
| 25 | Instrucciones y prompts | `ia/prompting` | pendiente | | |
| 26 | Tool calling | `ia/tool-calling` | pendiente | | |
| 27 | Embeddings y RAG | `ia/rag` | pendiente | | |
| 28 | Evaluación | `ia/evals` | pendiente | | |
| 29 | Skills | `ia/skills` | pendiente | | |
| 30 | Dónde aporta valor | `ia/valor-negocio` | pendiente | | |

### Parte V. Agentes de IA

| Cap. | Título | id | Fase | PENDIENTES | Notas |
| --- | --- | --- | --- | --- | --- |
| 31 | El bucle del agente | `agentes/bucle` | pendiente | | |
| 32 | Agentes con Agno | `agentes/agno` | pendiente | | |
| 33 | Memoria | `agentes/memoria` | pendiente | | |
| 34 | MCP | `agentes/mcp` | pendiente | | |
| 35 | Multiagente y A2A | `agentes/multiagente` | pendiente | | |
| 36 | Seguridad y control | `agentes/seguridad-agentes` | pendiente | | |

### Parte VI. Ingeniería de software agéntica

| Cap. | Título | id | Fase | PENDIENTES | Notas |
| --- | --- | --- | --- | --- | --- |
| 37 | Trabajar con un agente de código | `agentica/opencode` | pendiente | | |
| 38 | Especificar antes de pedir | `agentica/especificar` | pendiente | | |
| 39 | Revisar código de IA | `agentica/revisar` | pendiente | | |
| 40 | Contexto del proyecto | `agentica/contexto` | pendiente | | |
| 41 | Cómo trabaja gentle-shell | `agentica/gentle-flujo` | pendiente | | |

### Parte VII. TypeScript y Node

| Cap. | Título | id | Fase | PENDIENTES | Notas |
| --- | --- | --- | --- | --- | --- |
| 42 | Sistema de tipos | `typescript/ts-tipos` | pendiente | | |
| 43 | Módulos y paquetes | `typescript/ts-modulos` | pendiente | | |
| 44 | Event loop de Node | `typescript/node-async` | pendiente | | |
| 45 | npm y versiones | `typescript/npm` | pendiente | | |
| 46 | Tests en TypeScript | `typescript/ts-tests` | pendiente | | |
| 47 | Leer gentle-shell | `typescript/leer-gentle` | pendiente | | |

### Parte VIII. Arquitectura y diseño de sistemas

| Cap. | Título | id | Fase | PENDIENTES | Notas |
| --- | --- | --- | --- | --- | --- |
| 48 | Analizar compromisos | `arquitectura/compromisos` | pendiente | | |
| 49 | Acoplamiento y granularidad | `arquitectura/acoplamiento` | pendiente | | |
| 50 | Datos distribuidos | `arquitectura/datos-dist` | pendiente | | |
| 51 | Escalado | `arquitectura/escalado` | pendiente | | |
| 52 | Cachés y colas | `arquitectura/cache-colas` | pendiente | | |
| 53 | Casos de diseño | `arquitectura/casos-diseno` | pendiente | | |

### Parte IX. Go

| Cap. | Título | id | Fase | PENDIENTES | Notas |
| --- | --- | --- | --- | --- | --- |
| 54 | Fundamentos de Go | `go/go-base` | pendiente | | |
| 55 | Errores como valores | `go/go-errores` | pendiente | | |
| 56 | Módulos y versiones | `go/go-modulos` | pendiente | | |
| 57 | Concurrencia | `go/go-concurrencia` | pendiente | | |
| 58 | CLIs en Go | `go/go-cli` | pendiente | | |
| 59 | Leer gentle-ai | `go/leer-gentle-ai` | pendiente | | |

## Incidencias

- 2026-11-12: la red de la sesión en la nube bloquea git-scm.com, missing.csail.mit.edu y developer.mozilla.org. Hay que permitir esos dominios antes de la fase 2 del capítulo 1.

## Informes de métricas


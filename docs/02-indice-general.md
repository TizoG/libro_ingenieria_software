# Índice general del libro

**Programar entendiendo el código** · 9 partes · 59 capítulos · 258 secciones

## Preliminares

- Prólogo: cómo usar este libro
- El método: explicar, construir y defender
- Convenciones tipográficas

## Parte I. Oficio: Git, terminal y leer código

*Fase 1. Proyecto de la parte: Arqueología de un PR.*

**Capítulo 1. Git por dentro**

- 1.1 Qué es el control de versiones
- 1.2 Fotos, no diferencias; los tres estados
- 1.3 Leer y deshacer el historial
- 1.4 Las ramas son punteros
- 1.5 Rebase y reescribir historia
- 1.6 Bajo el capó: objetos y referencias
- 1.7 reset sin miedo
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 2. Flujo de contribución**

- 2.1 Remotos y ramas remotas
- 2.2 Flujos de trabajo distribuidos
- 2.3 Contribuir a un proyecto
- 2.4 Fork y pull request en GitHub
- 2.5 Mantener el PR al día y responder revisiones
- 2.6 Contribuir sin escribir código
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 3. Terminal y procesos**

- 3.1 La shell: comandos, rutas y PATH
- 3.2 Procesos, señales y variables de entorno
- 3.3 Tu entorno de desarrollo
- 3.4 Depurar y medir
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 4. HTTP de verdad**

- 4.1 Cliente, servidor y sin estado
- 4.2 Anatomía de mensajes y sesión
- 4.3 Métodos e idempotencia
- 4.4 Códigos de estado
- 4.5 Cabeceras y tipos de contenido
- 4.6 Caché y peticiones condicionales
- 4.7 Autenticación y CORS
- 4.8 Conexiones
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 5. Leer código ajeno**

- 5.1 Moverse por el historial
- 5.2 Buscar en el código y en la historia
- 5.3 blame y bisect
- 5.4 Calidad de código: qué buscar al leer
- 5.5 Práctica en un repo real
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Soluciones de la Parte I**

## Parte II. Python profundo

*Fase 1. Proyecto de la parte: Pydantic de juguete.*

**Capítulo 6. Modelo de objetos**

- 6.1 Nombres que apuntan a objetos
- 6.2 Ámbitos y espacios de nombres
- 6.3 Estructuras mutables e inmutables
- 6.4 Clases, instancias y variables de clase
- 6.5 Herencia
- 6.6 Métodos especiales
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 7. Funciones, closures y decoradores**

- 7.1 Definir funciones y valores por omisión
- 7.2 Parámetros especiales, *args y **kwargs
- 7.3 Funciones de orden superior y closures
- 7.4 Decoradores
- 7.5 Anotaciones de función
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 8. Iteradores y generadores**

- 8.1 Técnicas de iteración y comprensiones
- 8.2 El protocolo de iteración
- 8.3 Generadores y expresiones generadoras
- 8.4 itertools y functools
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 9. Tipos y validación**

- 9.1 Anotaciones y el módulo typing
- 9.2 dataclasses
- 9.3 Validar en tiempo de ejecución con Pydantic
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 10. Asincronía**

- 10.1 Modelo mental: el bucle de eventos
- 10.2 Corrutinas, tareas y gather
- 10.3 Hilos frente a async
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 11. Errores y gestores de contexto**

- 11.1 Capturar y lanzar excepciones
- 11.2 Encadenar y definir excepciones propias
- 11.3 Limpieza y la sentencia with
- 11.4 Escribir gestores de contexto
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 12. Testing con pytest**

- 12.1 Control de calidad en la biblioteca estándar
- 12.2 Estructura de un proyecto con tests
- 12.3 Fixtures, parametrize y dobles de prueba
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 13. Módulos, paquetes y entornos**

- 13.1 Módulos y ruta de búsqueda
- 13.2 Paquetes
- 13.3 Entornos virtuales
- 13.4 pyproject.toml y publicar
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Soluciones de la Parte II**

## Parte III. Backend con FastAPI

*Fase 2. Proyecto de la parte: Simulador de proveedor LLM.*

**Capítulo 14. Diseño de APIs REST**

- 14.1 Recursos y URIs
- 14.2 Verbos y su semántica
- 14.3 Códigos de estado y formato de errores
- 14.4 Paginación, filtros y versionado
- 14.5 El contrato: OpenAPI
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 15. Endpoints y routing**

- 15.1 Primera aplicación y path operations
- 15.2 Parámetros de ruta
- 15.3 Parámetros de consulta
- 15.4 Cuerpo de la petición
- 15.5 response_model y status_code
- 15.6 Routers y aplicaciones grandes
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 16. Validación con Pydantic**

- 16.1 Modelos de entrada y de salida
- 16.2 Validadores propios
- 16.3 Errores 422 y manejo de errores
- 16.4 Un modelo por operación (crear, leer, actualizar)
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 17. Inyección de dependencias**

- 17.1 Depends: qué problema resuelve
- 17.2 Clases como dependencias y subdependencias
- 17.3 Dependencias con yield
- 17.4 Sustituir dependencias en tests
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 18. Persistencia con SQLAlchemy y PostgreSQL**

- 18.1 SQL y PostgreSQL lo justo
- 18.2 SQLAlchemy 2.0: engine y sesión
- 18.3 Modelos ORM y relaciones
- 18.4 Transacciones
- 18.5 Migraciones con Alembic
- 18.6 El problema N+1 y la carga de relaciones
- 18.7 Integración con FastAPI
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 19. Autenticación y autorización**

- 19.1 Autenticación frente a autorización
- 19.2 Guardar contraseñas: hashing
- 19.3 OAuth2 con flujo password
- 19.4 JWT: qué contiene y qué garantiza
- 19.5 Scopes y roles
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 20. Async, streaming y tareas**

- 20.1 def frente a async def
- 20.2 Tareas en segundo plano
- 20.3 Server-Sent Events
- 20.4 Streaming de respuestas
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 21. Tests de API**

- 21.1 El cliente de pruebas
- 21.2 Base de datos de pruebas y fixtures
- 21.3 Tests asíncronos
- 21.4 Sustituir dependencias
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 22. Docker y despliegue**

- 22.1 Imágenes y contenedores
- 22.2 Dockerfile y capas
- 22.3 Builds multietapa
- 22.4 Configuración por entorno y secretos
- 22.5 Desplegar
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Soluciones de la Parte III**

## Parte IV. IA aplicada: LLMs, RAG y skills

*Fase 2. Proyecto de la parte: ¿Ya existe ese issue?.*

**Capítulo 23. Cómo funciona un LLM**

- 23.1 Tokens y tokenización
- 23.2 Transformers a vista de pájaro
- 23.3 Ventana de contexto
- 23.4 Muestreo y temperatura
- 23.5 Por qué un modelo inventa
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 24. Llamar a un modelo**

- 24.1 Mensajes y roles
- 24.2 Parámetros de la petición
- 24.3 Streaming
- 24.4 Salida estructurada
- 24.5 Errores, límites y reintentos
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 25. Instrucciones y prompts**

- 25.1 Instrucciones claras
- 25.2 Ejemplos
- 25.3 Formato de salida
- 25.4 Descomponer tareas
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 26. Tool calling**

- 26.1 Qué es el tool calling
- 26.2 Describir herramientas con JSON Schema
- 26.3 El bucle petición y resultado
- 26.4 Validar argumentos y fallos
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 27. Embeddings y RAG**

- 27.1 Embeddings
- 27.2 Troceado de documentos
- 27.3 Almacenes vectoriales y búsqueda
- 27.4 Recuperar y generar
- 27.5 Reordenar y citar
- 27.6 Por qué falla un RAG
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 28. Evaluación**

- 28.1 Por qué evaluar
- 28.2 Conjuntos de prueba
- 28.3 Métricas
- 28.4 Un modelo como juez y sus límites
- 28.5 Regresiones
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 29. Skills**

- 29.1 Qué es una skill
- 29.2 Anatomía de una skill
- 29.3 Skill, prompt o herramienta: cuándo cada una
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 30. Dónde aporta valor**

- 30.1 Casos de uso reales
- 30.2 Coste y latencia
- 30.3 Cuándo no usar IA
- 30.4 Flujos deterministas frente a agentes
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Soluciones de la Parte IV**

## Parte V. Agentes de IA

*Fase 3. Proyecto de la parte: Servidor MCP de contexto de contribución.*

**Capítulo 31. El bucle del agente**

- 31.1 Qué es un agente
- 31.2 Pensar, actuar, observar
- 31.3 Condición de parada y presupuesto
- 31.4 Trazas: ver qué hizo el agente
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 32. Agentes con Agno**

- 32.1 Agent, Team y Workflow
- 32.2 Herramientas en Agno
- 32.3 Salida estructurada
- 32.4 De tu bucle a mano a Agno
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 33. Memoria**

- 33.1 Contexto frente a memoria
- 33.2 Sesiones e historial
- 33.3 Memoria persistente
- 33.4 Resúmenes y compresión
- 33.5 Privacidad
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 34. MCP**

- 34.1 El problema que resuelve MCP
- 34.2 Host, cliente y servidor
- 34.3 Primitivas: tools, resources y prompts
- 34.4 Transportes: stdio y Streamable HTTP
- 34.5 Descubrimiento y versión del protocolo
- 34.6 Construir un servidor
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 35. Multiagente y A2A**

- 35.1 Cuándo dividir en varios agentes
- 35.2 Orquestador y subagentes
- 35.3 Equipos en Agno
- 35.4 El protocolo A2A
- 35.5 MCP frente a A2A
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 36. Seguridad y control**

- 36.1 Inyección de prompts
- 36.2 Mínimo privilegio y permisos
- 36.3 Sandbox
- 36.4 Aprobación humana
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Soluciones de la Parte V**

## Parte VI. Ingeniería de software agéntica

*Fase 3. Proyecto de la parte: Duelo humano contra agente.*

**Capítulo 37. Trabajar con un agente de código**

- 37.1 Qué hace un agente de código
- 37.2 Contexto y archivos de reglas
- 37.3 Permisos
- 37.4 Sesiones y límites
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 38. Especificar antes de pedir**

- 38.1 Tarea frente a especificación
- 38.2 Criterios de aceptación verificables
- 38.3 El flujo ODD de Gentle AI
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 39. Revisar código de IA**

- 39.1 Leer un diff de verdad
- 39.2 Tests primero
- 39.3 Señales de alarma
- 39.4 Cuándo rechazar un cambio
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 40. Contexto del proyecto**

- 40.1 AGENTS.md y CLAUDE.md
- 40.2 Instrucciones externas
- 40.3 Contexto que estorba
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 41. Cómo trabaja gentle-shell**

- 41.1 Qué es gentle-shell: Pi y Gentle AI
- 41.2 Instalación aislada
- 41.3 Recorrido de una tarea
- 41.4 Versiones fijadas del runtime
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Soluciones de la Parte VI**

## Parte VII. TypeScript y Node

*Fase 3. Proyecto de la parte: Primer PR a gentle-shell.*

**Capítulo 42. Sistema de tipos**

- 42.1 Tipos básicos
- 42.2 Tipado estructural
- 42.3 Uniones y narrowing
- 42.4 Genéricos
- 42.5 unknown, any y never
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 43. Módulos y paquetes**

- 43.1 ESM frente a CommonJS
- 43.2 package.json y exports
- 43.3 Compilar con tsc
- 43.4 tsconfig
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 44. Event loop de Node**

- 44.1 El modelo del event loop
- 44.2 Promesas y async/await
- 44.3 Timers y nextTick
- 44.4 Streams
- 44.5 Procesos hijo
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 45. npm y versiones**

- 45.1 Semver
- 45.2 Lockfiles
- 45.3 Binarios y CLIs
- 45.4 Publicar
- 45.5 Cadena de suministro
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 46. Tests en TypeScript**

- 46.1 El runner de tests
- 46.2 Tipos en los tests
- 46.3 Integración continua con GitHub Actions
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 47. Leer gentle-shell**

- 47.1 Estructura del repositorio
- 47.2 Cómo se carga como paquete de Pi
- 47.3 Publicación y verificación de versiones
- 47.4 Encontrar un primer issue
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Soluciones de la Parte VII**

## Parte VIII. Arquitectura y diseño de sistemas

*Fase 4. Proyecto de la parte: ADRs del ecosistema Gentle.*

**Capítulo 48. Analizar compromisos**

- 48.1 No hay mejores prácticas, solo compromisos
- 48.2 ADRs
- 48.3 Atributos de calidad
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 49. Acoplamiento y granularidad**

- 49.1 Acoplamiento y cohesión
- 49.2 Monolito frente a servicios
- 49.3 Granularidad
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 50. Datos distribuidos**

- 50.1 Consistencia y disponibilidad
- 50.2 Replicación
- 50.3 Particionado
- 50.4 Sagas
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 51. Escalado**

- 51.1 Escalado vertical y horizontal
- 51.2 Balanceadores de carga
- 51.3 Servicios sin estado
- 51.4 Estimaciones rápidas
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 52. Cachés y colas**

- 52.1 Estrategias de caché
- 52.2 Invalidación
- 52.3 Asincronía y colas
- 52.4 Entrega y reintentos
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 53. Casos de diseño**

- 53.1 Limitador de peticiones
- 53.2 Sistema de notificaciones
- 53.3 Caso real: el almacenamiento de Git
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Soluciones de la Parte VIII**

## Parte IX. Go

*Fase 4. Proyecto de la parte: Tu simulador LLM, en Go.*

**Capítulo 54. Fundamentos de Go**

- 54.1 Tipos, structs y métodos
- 54.2 Interfaces implícitas
- 54.3 Slices y mapas
- 54.4 Paquetes
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 55. Errores como valores**

- 55.1 error como valor
- 55.2 Envolver errores
- 55.3 errors.Is y errors.As
- 55.4 panic frente a error
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 56. Módulos y versiones**

- 56.1 go mod
- 56.2 Versión mayor en la ruta del módulo
- 56.3 go install
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 57. Concurrencia**

- 57.1 Goroutines
- 57.2 Canales
- 57.3 select
- 57.4 context y cancelación
- 57.5 sync
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 58. CLIs en Go**

- 58.1 Flags
- 58.2 Subcomandos
- 58.3 Binario único y distribución
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Capítulo 59. Leer gentle-ai**

- 59.1 Estructura del runtime
- 59.2 Instalación y sincronización
- 59.3 Publicación de versiones
- 59.4 Primer issue en Go
- *Cierre: el proyecto avanza, resumen, ejercicios, preguntas de examen y fuentes*

**Soluciones de la Parte IX**

## Apéndices

- A. Preparar el entorno
- B. Glosario general
- C. Chuletas por parte
- D. Créditos y licencias de las fuentes

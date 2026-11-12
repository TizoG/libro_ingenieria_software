# Modelo y nivel de esfuerzo

No se usa un único modelo para todo. Cada fase del capítulo tiene necesidades distintas: unas piden criterio y redacción fina, otras volumen y rapidez, y las mecánicas no necesitan pensar. Elegir bien ahorra uso del plan sin perder calidad donde importa.

## Lo que ofrece Claude Code (comprobado el 12 de noviembre de 2026)

- **El modelo y el esfuerzo son dos controles separados.** El modelo se cambia con `/model`. El esfuerzo se cambia con `/effort`, que acepta `low`, `medium`, `high` y `xhigh` y guarda el nivel elegido para el modelo activo ([referencia de configuración](https://code.claude.com/docs/es/settings-reference)).
- **`max` solo vale para la sesión.** No se guarda en la configuración, y la variable de entorno `CLAUDE_CODE_EFFORT_LEVEL` tiene prioridad sobre todo lo demás ([guía de esfuerzo por modelo](https://wmedia.es/en/tips/claude-code-effort-per-model)).
- **Existe el alias `opusplan`.** Planifica con Opus en el modo plan y ejecuta con Sonnet al aprobar el plan ([resumen de la configuración de modelos](https://dev.to/nixonperinchery/claude-code-model-config-aliases-opusplan-and-effort-mlc)).
- **Cada subagente puede tener su propio modelo.** Por eso conviene definir los subagentes del flujo (investigador, redactor, revisor) en `.claude/agents/`.

Modelos disponibles hoy: Haiku 5.5, Sonnet 5.5, Opus 5.5 y, según el plan, Fable 5.2. Comprueba en `/model` cuáles tienes antes de empezar. Ten en cuenta que los modelos mayores y el esfuerzo alto consumen más uso del plan.

## Recomendación por fase

| Fase | Modelo | Esfuerzo | Por qué |
| --- | --- | --- | --- |
| 1. Mapa de fuentes (buscar, abrir, verificar URLs) | Sonnet 5.5 | medium | Mucho volumen y poco razonamiento; los scripts comprueban el resultado |
| 2. Investigación (extraer hechos con evidencia) | Sonnet 5.5 | high | Lectura atenta; el script de evidencias rechaza lo que no esté en la fuente |
| 3. Esquema del capítulo (secciones, hilo, ejemplos) | Opus 5.5, o `opusplan` | high | Decisiones de estructura que condicionan todo el capítulo |
| 4. Ejemplos de código | Sonnet 5.5 | high | La ejecución real verifica el resultado |
| 5. Redacción por secciones | Opus 5.5 | high (xhigh en los capítulos densos) | Explicar el porqué con claridad es lo más difícil del libro |
| 6. Revisión adversarial | El modelo más capaz que tengas (Fable 5.2 u Opus 5.5) | xhigh | Encontrar fallos sutiles exige más que escribir; en una sesión distinta a la del redactor |
| Tareas mecánicas (formato, frontmatter, recuentos, enlaces) | Haiku 5.5 | low | Son deterministas; pensar más no aporta |

**Capítulos densos, con xhigh en la redacción:**

- 1 y 6, por los modelos internos de Git y de los objetos de Python;
- 10 y 44, por los bucles de eventos;
- 18, por las sesiones y transacciones;
- 34, por MCP;
- 50, por la consistencia;
- 57, por la concurrencia en Go.

## Configuración sugerida

Para no tener que acordarte de cambiar el modelo, fija uno distinto en cada subagente:

- **investigador:** Sonnet, esfuerzo high.
- **redactor:** Opus, esfuerzo high.
- **revisor:** el modelo más capaz, esfuerzo xhigh y sin acceso de escritura a `contenido/`.
- **mecánico:** Haiku, esfuerzo low.

El modelo y el esfuerzo de cada uno se definen en su archivo de `.claude/agents/`. Claude Code debe consultar la documentación actual de subagentes al crearlos, porque la sintaxis puede cambiar.

## Regla práctica

Si un paso lo puede comprobar un script, usa el modelo barato y deja que el script decida. Si un paso exige criterio (estructurar, explicar, encontrar fallos), usa el modelo caro. Lo que no se hace nunca es bajar el modelo de la revisión adversarial para ahorrar: es la barrera que protege la calidad del libro.

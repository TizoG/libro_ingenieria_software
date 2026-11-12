# Programar entendiendo el código

Libro técnico en español de devOC: lleva a un desarrollador desde bases sólidas hasta contribuir en proyectos open source de IA. Tiene 9 partes y 59 capítulos: Git y terminal, Python, FastAPI, IA aplicada, agentes, ingeniería agéntica, TypeScript, arquitectura y Go.

Cada afirmación técnica sale de una fuente pública verificada y todo el código se ejecuta de verdad. El método está en [`docs/05-metodo-sin-alucinaciones.md`](docs/05-metodo-sin-alucinaciones.md): el modelo propone y los scripts verifican.

## Estructura

| Carpeta | Qué contiene |
| --- | --- |
| `docs/` | Visión del proyecto, índice, fuentes autorizadas, catálogo de capítulos, método, contrato con la web y [tablero de estado](docs/estado.md) |
| `contenido/` | El libro en Markdown, listo para la web |
| `investigacion/` | Fuentes, hechos con evidencia, borradores e informes de revisión de cada capítulo |
| `ejemplos/` | Código ejecutable de cada capítulo |
| `scripts/` | Verificación: evidencias, ejemplos, ids, enlaces, métricas, compilación y contrato |
| `tests/` | Tests de los scripts |

## Uso

```bash
pip install -r requirements.txt
```

```bash
python -m pytest -q
```

```bash
python scripts/informe_capitulo.py 1
```

Empieza por [`docs/00-proyecto.md`](docs/00-proyecto.md).

# Hechos que faltan, detectados durante la redacción

Se extraen en `secciones/9-adicionales.md` (ids desde h01-809) y después el redactor resuelve los PENDIENTES.

**2026-11-12:** extraídos h01-809 a h01-830 (los cinco puntos de la tabla). `init.defaultBranch` sigue respaldado solo por f01-17 (h01-279).

| Detectado en | Qué falta | Fuente |
| --- | --- | --- |
| 1.1 | Que la herramienta creada en 2005 es Git | f01-02 («Desde su nacimiento en el 2005, Git…») |
| Apertura | Configurar `user.name` y `user.email` con `git config` | f01-31 |
| 1.2 | Hash abreviado: Git muestra solo los primeros caracteres; `--oneline` lo usa | f01-05 (`--abbrev-commit`), f01-28, f01-30 |
| 1.2 | `HEAD~N`, `HEAD^`: padre, abuelo... | f01-28, f01-29 |
| 1.2 | `<rev>^{tree}` en general | f01-29 |
| 1.3 | `git commit --no-edit` (usa el mensaje sin abrir el editor) | Documentación de `git commit` (no está en el mapa) |
| 1.3 | `--format=<estilo>` equivale a `--pretty=<estilo>` y admite `fuller` | f01-30 (git-log), hacia la línea 762 |
| 1.4 | Orden de las líneas `parent` de un merge: el primer padre es la rama en la que estabas (`^1`), el segundo la fusionada (`^2`) | f01-30 (`--first-parent`), documentación de `git merge` (f01-22) |
| 1.4 | Por qué el mensaje del merge conserva el bloque `# Conflicts:` | Documentación de `git commit` (no está en el mapa) |
| 1.5 | `git rebase -q` / `--quiet` | f01-23, líneas 285-286 («--quiet / Be quiet. Implies --no-stat.») |
| 1.5 | `git diff <rama> <rama>` (diff vacío entre dos ramas) | Documentación de `git diff` (no está en el mapa) |
| 1.6 | Modo `040000` de una entrada de árbol que es carpeta | Solo en salidas de ejemplo de f01-12; haría falta otra fuente |
| 1.6 | *Packfiles* (por qué un clon no muestra objetos sueltos) | Pro Git 10.4 (no está en el mapa; tema fuera de alcance según la decisión 7) |
| 1.6 | `git hash-object --stdin` | f01-12, justo antes de la evidencia de h01-619 |
| 1.7 | Por qué `git fsck --full` lista solo uno de los commits perdidos | Documentación de `git fsck` (no está en el mapa) |

**Pasada final (2026-11-12):** todos resueltos con h01-809 a h01-845, salvo el modo `040000` y `# Conflicts:` (el texto ya no los comenta), *packfiles* (fuera de alcance), `git fsck` (una frase sin explicar el porqué) y `git push` (capítulo 2).

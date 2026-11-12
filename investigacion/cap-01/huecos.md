# Huecos detectados en la investigación del capítulo 1

Lo que el capítulo podría necesitar y las fuentes actuales (Pro Git en español, Missing Semester) no dicen. Ninguno se ha rellenado con memoria. Cada uno se resuelve con una fuente nueva verificada o con un `> PENDIENTE` / recuadro «Ojo con la versión» en el borrador.

## Versión de Git (la edición en español de Pro Git es antigua)

1. `git switch` y `git restore`: no aparecen (f01-16 solo nombra `git restore` en una línea). Pro Git enseña `git checkout` y `git reset HEAD <archivo>` / `git checkout -- <archivo>`. Candidata: documentación oficial `git-scm.com/docs/git-switch` y `git-scm.com/docs/git-restore`.
2. Rama por defecto: las fuentes dicen `master`; Git actual permite `init.defaultBranch` y muchos entornos usan `main`. Candidata: `git-scm.com/docs/git-init` y `git-scm.com/docs/git-config`.
3. SHA-256: las fuentes solo hablan de SHA-1. Candidata: `git-scm.com/docs/hash-function-transition`.
4. Las salidas de ejemplo de las fuentes (mensajes de `git status`, «recursive strategy») son de versiones antiguas: los ejemplos del libro las generan con `insertar_ejemplos.py` (Git 2.43 en este entorno).

## Temas sin cubrir

5. Recuperar commits con `git reflog` (solo se menciona de pasada). Candidata: Pro Git 10.7 «Mantenimiento y recuperación de datos».
6. `git merge --abort`, `git rebase --abort` y `--skip`, y la acción `drop` del rebase interactivo. Candidata: `git-scm.com/docs/git-merge`, `git-scm.com/docs/git-rebase`.
7. HEAD desacoplado (*detached HEAD*). Candidata: `git-scm.com/docs/git-checkout` (sección DETACHED HEAD).
8. `git revert` como alternativa a reescribir historia publicada. Candidata: `git-scm.com/docs/git-revert`.
9. `git filter-repo` como alternativa moderna a `filter-branch` (Pro Git 7.6 solo trata `filter-branch`). Probablemente fuera del alcance del capítulo.

## Erratas de la traducción que el redactor no debe heredar

- 10.3: «en dicho sitio remoto» para `refs/remotes` (que es local); 10.2: un árbol «tiene una o más entradas de tipo árbol»; 7.6: «cambios del SHA-1», «alijos», «área de ensayo»; 7.7: «que como reset, no mueva HEAD»; 2.2: «el comando mv» por `git mv`.

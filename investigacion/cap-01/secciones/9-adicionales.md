## Adicionales (hechos añadidos tras aprobar el esquema; ids desde h01-801)

- id: h01-801
  hecho: La estrategia de fusión ort es la estrategia por defecto al hacer pull o al fusionar una sola rama.
  evidencia: "ort This is the default merge strategy when pulling or merging one branch."
  fuente: f01-27
  ancla: https://git-scm.com/docs/merge-strategies
  consultada: 2026-11-12

- id: h01-802
  hecho: El nombre de este algoritmo es un acrónimo de "Ostensibly Recursive's Twin".
  evidencia: 'The name for this algorithm is an acronym ("Ostensibly Recursive’s Twin")'
  fuente: f01-27
  ancla: https://git-scm.com/docs/merge-strategies
  consultada: 2026-11-12

- id: h01-803
  hecho: Este algoritmo se escribió como reemplazo del algoritmo predeterminado anterior, recursive.
  evidencia: 'it was written as a replacement for the previous default algorithm, recursive.'
  fuente: f01-27
  ancla: https://git-scm.com/docs/merge-strategies
  consultada: 2026-11-12

- id: h01-804
  hecho: La estrategia recursive es ahora un sinónimo de ort.
  evidencia: "recursive This is now a synonym for ort."
  fuente: f01-27
  ancla: https://git-scm.com/docs/merge-strategies
  consultada: 2026-11-12

- id: h01-805
  hecho: La estrategia recursive fue una implementación alternativa hasta la versión 2.49.0 de Git y pasó a significar ort en la 2.50.0.
  evidencia: "recursive This is now a synonym for ort. It was an alternative implementation until v2.49.0, but was redirected to mean ort in v2.50.0."
  fuente: f01-27
  ancla: https://git-scm.com/docs/merge-strategies
  consultada: 2026-11-12

- id: h01-806
  hecho: La antigua estrategia recursive fue la predeterminada para resolver dos cabezas desde Git v0.99.9k hasta v2.33.0.
  evidencia: "The previous recursive strategy was the default strategy for resolving two heads from Git v0.99.9k until v2.33.0."
  fuente: f01-27
  ancla: https://git-scm.com/docs/merge-strategies
  consultada: 2026-11-12

- id: h01-807
  hecho: La opción de configuración sequence.editor define el editor de texto que usa git rebase -i para editar el archivo de instrucciones del rebase.
  evidencia: "sequence.editor Text editor used by git rebase -i for editing the rebase instruction file."
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-808
  hecho: La variable de entorno GIT_SEQUENCE_EDITOR puede anular el valor configurado en sequence.editor.
  evidencia: "sequence.editor Text editor used by git rebase -i for editing the rebase instruction file. The value is meant to be interpreted by the shell when it is used. It can be overridden by the GIT_SEQUENCE_EDITOR environment variable."
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

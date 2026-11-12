# Revisión técnica, tramo 4: 1.7 y cierre

Revisor técnico (sesión limpia), 2026-11-12. 77 frases: 57 SOPORTADA, 14 PARCIAL, 2 NO SOPORTADA, 4 SIN HECHO. El revisor probó con Git 2.43 `reset` con ruta, `--hard`/`--soft` con ruta y `git log --stat` sobre un merge. Aquí van los bloques que no salieron SOPORTADA.

## 1.7 reset sin miedo

- frase: "Solo `--hard` es peligroso, porque sobrescribe tus archivos, y aun así lo confirmado se recupera, normalmente con el *reflog* (registro de referencias)."
  hechos: h01-730, h01-731, h01-345, h01-784, h01-774
  veredicto: PARCIAL
  nota: «se recupera» sin plazo; las entradas inalcanzables del reflog caducan a los 30 días (f01-25 l.87-92). Propuesta: «se puede recuperar durante un tiempo, y la vía más rápida suele ser el reflog».
  resuelto: no

- frase: "Has deshecho el último commit y nada más"
  hechos: h01-721
  veredicto: PARCIAL
  nota: «y nada más» sale de h01-722; citarlo o quitarlo.
  resuelto: no

- frase: "Con una ruta, `reset` se salta el primer paso y aplica el resto solo a esos archivos."
  hechos: h01-734
  veredicto: PARCIAL
  nota: «el resto» insinúa un paso 3 que no existe: Git 2.43 rechaza `--hard` y `--soft` con ruta (h01-752, h01-759). Propuesta: «se salta el primer paso y solo actualiza el índice para esos archivos».
  resuelto: no

- frase: "`git reset factura.py` abrevia `git reset --mixed HEAD factura.py`: copia el archivo de `HEAD` al índice, lo que en la práctica lo saca del área de preparación."
  hechos: h01-736, h01-737, h01-738
  veredicto: PARCIAL
  nota: con Git 2.43 la forma larga avisa: «--mixed with paths is deprecated». Necesita «Ojo con la versión» o presentarla como explicación de Pro Git. La página de git-reset no está en docs/03.
  resuelto: no

- frase: "Es la alternativa al `fixup` de la sección 1.5."
  hechos: —
  veredicto: SIN HECHO
  nota: sin id y no son equivalentes (fixup conserva el mensaje del primero). f01-15 l.143 dice «otra forma de hacerlo»: extraer y escribir «otra forma de hacer lo que hiciste con rebase interactivo».
  resuelto: no

- frase: "`checkout` comprueba que no pisa archivos con cambios, igual que `git switch`, y `reset --hard` lo reemplaza todo sin mirar."
  hechos: h01-745, h01-476, h01-746
  veredicto: PARCIAL
  nota: la seguridad vale solo sin ruta: escribir «`git checkout <rama>` comprueba…».
  resuelto: no

- frase: "| `git checkout [<commit>] <archivo>` | nada | sí | sí | no |"
  hechos: h01-760
  veredicto: PARCIAL
  nota: sin commit, checkout toma el archivo del índice y no lo actualiza (f01-21 l.62-65): «Índice: sí» solo vale con commit. Además el esquema aprobado pedía una tabla propia con switch/restore.
  resuelto: no

- frase: "Con ruta, `checkout` tampoco mueve `HEAD`, pero copia el archivo al índice y también al directorio de trabajo, sin proteger tus cambios."
  hechos: h01-750, h01-751, h01-752
  veredicto: PARCIAL
  nota: solo con commit.
  resuelto: no

- frase: "La sección 1.4 rescató con el reflog un experimento; ahora toca el caso típico que cita Pro Git, un `reset --hard` que abandona commits."
  hechos: h01-781
  veredicto: PARCIAL
  nota: «uno de los casos típicos» (la fuente da dos causas).
  resuelto: no

- frase: "¿Y si el reflog ya no lo tiene? Sus entradas caducan, por defecto a los 90 días."
  hechos: h01-779, h01-780
  veredicto: NO SOPORTADA
  nota: los 90 días valen para entradas alcanzables; las inalcanzables (el caso del reset --hard) caducan a los 30 (f01-25 l.54-56 y 87-92). El error viene del esquema. Extraer hecho.
  resuelto: no

- frase: "El final del ejemplo borra la rama y el reflog, que vive en `.git/logs/`, y aún queda `git fsck --full`: el commit perdido aparece tras `dangling commit` y se recupera igual, con una rama."
  hechos: h01-790, h01-791, h01-792, h01-793
  veredicto: PARCIAL
  nota: se perdieron dos commits y fsck solo lista el último (el otro es alcanzable desde él). «aparece el último de los commits perdidos, y una rama en él recupera los dos».
  resuelto: no

- frase: "En el ejemplo 21 el redondeo estaba confirmado y el reflog lo recuerda"
  hechos: h01-786, h01-732
  veredicto: PARCIAL
  nota: cierto, pero la salida no lo enseña. Añadir `git reflog -2` al ejemplo o reformular sin h01-732.
  resuelto: no

- frase: "Su última fila es lo que hoy escribes como `git restore --source <commit> --staged --worktree <archivo>`."
  hechos: h01-358, h01-355, h01-362
  veredicto: PARCIAL
  nota: solo vale con commit.
  resuelto: no

- frase: "`git rebase -i HEAD~4` creó commits nuevos (sección 1.5)."
  hechos: —
  veredicto: SIN HECHO
  nota: citar h01-764 (y ajustar al hallazgo del tramo 3: solo desde el primer commit cambiado).
  resuelto: no

- frase: "Ningún commit se borró: los que quedaron sin rama siguen localizables en tu reflog."
  hechos: h01-768, h01-774, h01-783, h01-784
  veredicto: PARCIAL
  nota: sin plazo y sin distinguir tu repositorio del servidor. «ningún commit se borró en tu repositorio: los que quedaron sin rama siguen en tu reflog durante un tiempo».
  resuelto: no

## El proyecto avanza

- frase: "Averigua cómo se integró: con un commit de fusión, con un solo commit que lo aplasta o con sus commits reaplicados en línea."
  hechos: —
  veredicto: SIN HECHO
  nota: da por hechas tres formas de integrar un PR; con lo que enseña el capítulo solo se distingue el commit de fusión. Admitir «no concluyente».
  resuelto: no

- frase: "Anota qué archivos tocó y cuántas líneas, solo con la vista resumida de `git log --stat`."
  hechos: h01-308, h01-309
  veredicto: PARCIAL
  nota: sobre un commit de fusión `git log --stat` no muestra estadística (f01-30 l.1375-1380). Indicar que se mire en los commits del PR o usar `--first-parent` con hecho.
  resuelto: no

## Resumen

- frase: "`reset` mueve la rama y, según el modo, copia al índice y al directorio de trabajo; solo `--hard` destruye datos, y solo los que no confirmaste."
  hechos: h01-718, h01-720, h01-725, h01-728, h01-730, h01-733, h01-345
  veredicto: PARCIAL
  nota: «`reset` sin ruta mueve la rama»; y la recuperación de lo confirmado tiene plazo.
  resuelto: no

## Ejercicios

- frase: "Recupera el `factura.py` anterior a ese commit sin mover la rama y confírmalo como commit nuevo. Explica por qué no usas `reset`."
  hechos: — (en contra: h01-740, h01-759)
  veredicto: NO SOPORTADA
  nota: premisa falsa: `git reset <commit> <archivo>` + `git commit` hace justo eso sin mover la rama (f01-15 l.133-136; ejemplo 22). Reformular (comparar `restore --source` con `reset <commit> <archivo>`, o preguntar por `reset <commit>` sin ruta).
  resuelto: no

## Preguntas de examen

- frase: "Has subido un commit defectuoso a `main`, que comparte todo el equipo. ¿Por qué lo deshaces con `revert` y no con `reset`?"
  hechos: —
  veredicto: SIN HECHO
  nota: reponer h01-594, h01-535, h01-764.
  resuelto: no

## Otros puntos

- «Para deshacer algo publicado, la próxima vez, `git revert`» no encaja con «El problema» (se quería limpiar antes del PR): la lección es reorganizar solo lo no compartido (h01-535).
- Ejercicio 5: `git rebase -i` descarta por defecto los commits de fusión (f01-23 l.394) y el capítulo no lo cuenta.
- Ejercicio 3: el lector no tiene receta para montar `facturas`; hay dos commits del IVA distintos (d382532 y c87074a).
- Proyecto: clonar desde URL es del capítulo 2; `git switch -c` para el paso 3.

# Revisión técnica, tramo 3: 1.5 y 1.6

Revisor técnico (sesión limpia), 2026-11-12. 109 frases (55 en 1.5, 54 en 1.6): 90 SOPORTADA, 17 PARCIAL, 1 NO SOPORTADA, 1 SIN HECHO. El revisor reprodujo los ejemplos 13, 18 y 20 y un escenario de `git pull` con Git 2.43. Aquí van los bloques que no salieron SOPORTADA.

## 1.5 Rebase y reescribir historia

- frase: "La instantánea final es la misma que daría un merge y solo cambia el historial; por eso es inofensivo con commits que nunca has compartido y dañino con los que otros ya tienen, y para deshacer algo publicado tienes `git revert`."
  hechos: h01-510, h01-529, h01-591, h01-594
  veredicto: PARCIAL
  nota: «por eso» es una causalidad que ninguna fuente hace (el daño viene de abandonar commits y crear otros, h01-520). Ninguna fuente presenta `git revert` como la herramienta para deshacer lo publicado; reformular («revert no reescribe: añade un commit») o añadir hecho.
  resuelto: no

- frase: "Rebase es la otra forma: Git va al ancestro común, saca las diferencias que introduce cada commit de tu rama, las guarda en archivos temporales, lleva tu rama al commit de la otra y aplica de nuevo esas diferencias, en el mismo orden."
  hechos: h01-503, h01-504, h01-505, h01-506, h01-507, h01-508, h01-514
  veredicto: PARCIAL
  nota: es la mecánica antigua de Pro Git. La documentación actual (f01-23 l.51-61 y 510-514) describe la reaplicación tipo cherry-pick con el backend merge, usado también en rebases no interactivos; por eso el ejemplo 14 dice «interactive rebase in progress» sin `-i`. Añadir hecho nuevo y «Ojo con la versión» o reescribir.
  resuelto: no

- frase: "Es lo que viste con `--amend` en la sección 1.3, aplicado a una fila entera."
  hechos: ninguno
  veredicto: PARCIAL
  nota: en 1.3 el hash cambió por el contenido, con el mismo padre; aquí por el padre. La analogía vale para «no se edita, se sustituye» (h01-763, h01-764): reformular y citarlos.
  resuelto: no

- frase: "Por eso se suele hacer rebase antes de proponer tu trabajo: a quien mantiene el proyecto le basta con avanzar."
  hechos: h01-512, h01-513
  veredicto: PARCIAL
  nota: leve; la fuente dice «un avance rápido o una incorporación limpia».
  resuelto: no

- frase: "Es la primera orden del asistente de «El problema»: `git rebase -i HEAD~4` reescribe todos los commits del rango `HEAD~4..HEAD`, cambies algo en ellos o no."
  hechos: h01-543
  veredicto: NO SOPORTADA
  nota: f01-23 l.307-312 dice lo contrario (por defecto rebase avanza sobre los commits que no cambian) y Git 2.43 lo confirma: con la lista intacta los cuatro hashes no cambian. La frase de Pro Git en español (f01-11 l.35) es una errata o desfase: añadir a huecos.md. Reescribir: se reescriben el primer commit que cambias y los que lo siguen. Hecho nuevo de f01-23.
  resuelto: no

- frase: "El ejemplo la usa dos veces: con un comando que solo imprime la lista y con otro que pone `fixup` en las líneas 2 y 3 y `drop` en la 4."
  hechos: ninguno
  veredicto: PARCIAL
  nota: el ejemplo 13 usa `GIT_SEQUENCE_EDITOR` tres veces (la tercera con `--autosquash`).
  resuelto: no

- frase: "Para deshacer algo ya publicado no reescribes: `git revert` registra commits nuevos que deshacen el efecto de otros anteriores, y exige un árbol de trabajo limpio."
  hechos: h01-535, h01-594, h01-595
  veredicto: PARCIAL
  nota: «para deshacer algo ya publicado» no lo dice ninguna fuente (mismo problema en objetivos y en 1.7).
  resuelto: no

- frase: "Al traer tus cambios, `git pull` creó una fusión con las dos líneas del historial, la vieja y la reescrita, y su `git log` enseña dos commits con el mismo autor, fecha y mensaje: tus commits repetidos."
  hechos: h01-523, h01-524
  veredicto: PARCIAL
  nota: con Git 2.43 sin configurar, `git pull` se niega («fatal: Need to specify how to reconcile divergent branches»); la fusión solo aparece con `pull.rebase=false` o `--no-rebase`. Falta «Ojo con la versión» y fuente (página de `git pull`, no está en el índice). Afecta a «El problema».
  resuelto: no

- frase: "Con él, si tu compañera hace rebase de su trabajo sobre tus commits nuevos, Git puede reconocer qué parte era suya y aplicar solo esa, siempre que los parches viejos y nuevos sean muy parecidos."
  hechos: h01-526, h01-527
  veredicto: PARCIAL
  nota: leve; la fuente dice «es posible que» y «solo funciona si» (condición necesaria, no suficiente).
  resuelto: no

## 1.6 Bajo el capó: objetos y referencias

- frase: "Ahí guarda cuatro tipos de objeto que no cambian, y encima pone referencias que sí cambian; cada comando de Git añade objetos y añade o mueve referencias."
  hechos: h01-673, h01-766, h01-768
  veredicto: PARCIAL
  nota: falso para `git log`, `status`, `diff`, `cat-file`. Propuesta: «todo lo que cambia un comando se reduce a añadir objetos y añadir o mover referencias».
  resuelto: no

- frase: "[diagrama] HEAD, main, commits 7971f23..ce4f8a1, árboles y etiquetas v0.1 y v1.0"
  hechos: ninguno
  veredicto: PARCIAL
  nota: correcto, pero el lector no puede comprobarlo con ninguna salida insertada (el 18 no imprime el hash de HEAD ni el árbol de c87074a; las etiquetas solo existen en el ejemplo 20, no insertado). Insertar el 20 o quitar las etiquetas.
  resuelto: no

- frase: "De lo que lista `ls .git`, cuatro entradas importan: los archivos `HEAD` e `index` y las carpetas `objects` y `refs`."
  hechos: h01-610
  veredicto: PARCIAL
  nota: `index` no está en lo que lista `ls .git`. «De lo que hay en `.git`…».
  resuelto: no

- frase: "El segundo `find` enseña dónde ha ido: un archivo por objeto, en una subcarpeta con los dos primeros caracteres del hash, `5c`, y los 38 restantes como nombre."
  hechos: h01-621, h01-622
  veredicto: PARCIAL
  nota: pierde el «en principio» de la fuente (packfiles).
  resuelto: no

- frase: "`symbolic-ref` confirma que `HEAD` ya apuntaba allí."
  hechos: h01-670
  veredicto: PARCIAL
  nota: leve; el «ya» es una inferencia.
  resuelto: no

- frase: "Marca un commit como una rama que nunca se mueve."
  hechos: h01-675
  veredicto: PARCIAL
  nota: la fuente dice «generalmente»; se puede etiquetar cualquier objeto (h01-682).
  resuelto: no

- frase: "La ligera es solo una referencia; la anotada, que se crea con `git tag -a`, es una referencia a un objeto etiqueta con quien la creó, la fecha, el mensaje y un enlace al commit."
  hechos: h01-677, h01-680, h01-679, h01-674
  veredicto: PARCIAL
  nota: «quien la creó» no está en h01-674 («marcador», probable errata de *tagger*: añadir a huecos.md).
  resuelto: no

- frase: "Caso límite: dos archivos con nombres distintos e idéntico contenido. Son un solo blob, porque Git guarda un archivo por pieza de contenido, nombrado por su hash, y el nombre va en el árbol."
  hechos: h01-621, h01-626, h01-630
  veredicto: PARCIAL
  nota: pierde el «en principio»; ningún ejemplo lo demuestra.
  resuelto: no

- frase: "El árbol tendrá dos entradas con el mismo hash."
  hechos: ninguno
  veredicto: SIN HECHO
  nota: solo si están en la misma carpeta; sin id ni ejemplo.
  resuelto: no

- frase: "Aun así, `git init` sigue usando SHA-1 por defecto y los dos formatos no interoperan por ahora: el cálculo del ejemplo 17 es el de tus repositorios."
  hechos: h01-280, h01-283, h01-294
  veredicto: PARCIAL
  nota: leve; «salvo que crees el repositorio con SHA-256».
  resuelto: no

## Otros puntos

- Erratas para huecos.md: f01-11 l.35 («será reescrita, aún si cambias el mensaje o no») y f01-13 l.64 («marcador» por *tagger*).
- La lista de acciones de Pro Git en español también trae `exec`; decir «entre otras».
- `--autosquash` reordena la lista y cambia `pick` por `fixup` (h01-589): es lo más visible de la salida y no se comenta.

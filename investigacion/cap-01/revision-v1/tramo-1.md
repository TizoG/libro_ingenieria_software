# Revisión técnica, tramo 1: apertura, 1.1 y 1.2

Revisor técnico (sesión limpia), 2026-11-12. 98 frases técnicas revisadas: 81 SOPORTADA, 12 PARCIAL, 0 NO SOPORTADA, 5 SIN HECHO. Aquí se guardan los bloques que no salieron SOPORTADA; las SOPORTADAS están en el informe del revisor (sin observaciones que requieran cambios).

## Lo que podrás hacer al terminar

- frase: "Construir sin ayuda un repositorio con tres ramas, provocar y resolver un conflicto y limpiar el historial con rebase interactivo, dibujando el grafo antes y después."
  hechos: ninguno
  veredicto: SIN HECHO
  nota: menor; único objetivo sin ids. Citar algún hecho de 1.5 (rebase interactivo) y 1.4 (conflicto).
  resuelto: no

## Lo que necesitas antes

- frase: "La rama inicial llamada `main`, fijada con la variable de configuración `init.defaultBranch`, para que tus salidas coincidan con las del libro."
  hechos: h01-279
  veredicto: PARCIAL
  nota: con `main` solo coinciden los nombres de rama; los hashes del lector serán otros porque dependen de nombre, correo y hora (h01-639; insertar_ejemplos.py fija autor y fecha). El capítulo cita decenas de hashes y no avisa. Propuesta: «para que los nombres de rama coincidan; los hashes serán otros, porque dependen de tu nombre, tu correo y la hora (h01-639)». El apéndice «Preparar el entorno» aún no existe.
  resuelto: no

## El problema

- frase: "Al traer tus cambios ve tus commits repetidos en su historial, y su PR ya no se puede fusionar."
  hechos: ninguno
  veredicto: SIN HECHO
  nota: «commits repetidos» tiene hechos en 1.5 (h01-523, h01-524): citarlos. «Su PR ya no se puede fusionar» no tiene hecho en todo el capítulo ni se explica después (y los PR son del capítulo 2). Propuesta: sustituir por algo con hecho, p. ej. «ahora tiene que arreglar su historial a mano» (h01-591).
  resuelto: no

## 1.1 Qué es el control de versiones

- frase: "Para ordenar las ideas, fíjate en dónde vive el historial: solo en tu máquina, en un servidor central o en todas las máquinas a la vez."
  hechos: ninguno
  veredicto: SIN HECHO
  nota: menor; clasificación técnica sin id. Citar h01-108, h01-110, h01-120.
  resuelto: no

- frase: "La forma más simple de la primera opción ya la conoces: copiar los archivos a otro directorio."
  hechos: h01-105
  veredicto: PARCIAL
  nota: el superlativo no está en la fuente («muy común porque es muy sencillo»). Propuesta: «Una forma muy sencilla…».
  resuelto: no

- frase: "Las herramientas locales, como RCS, llevan el registro de los cambios en una base de datos sencilla y los guardan como conjuntos de parches, es decir, como diferencias entre archivos."
  hechos: h01-108, h01-109, h01-134
  veredicto: PARCIAL
  nota: la fuente atribuye los parches solo a RCS, no a todas las herramientas locales; h01-108 está en pasado; h01-134 no corresponde a la frase. Propuesta: «Las herramientas locales llevaban el registro en una base de datos sencilla; RCS, por ejemplo, guarda conjuntos de parches…».
  resuelto: no

- frase: "De 1991 a 2002, el *kernel* (núcleo) de Linux se mantuvo casi todo el tiempo intercambiando parches y archivos."
  hechos: h01-125
  veredicto: PARCIAL
  nota: la fuente identifica 1991-2002 con «la mayor parte» de la vida del kernel; «casi todo el tiempo» dentro de ese periodo es otra salvedad. Propuesta: «De 1991 a 2002, la mayor parte de la vida del kernel, los cambios circularon como parches y archivos».
  resuelto: no

- frase: "Esa red cubre lo que llegó a confirmarse."
  hechos: h01-345
  veredicto: PARCIAL
  nota: h01-345 viene de «Deshacer cosas» (recuperar en tu propio repositorio), no de restaurar un servidor desde un clon; y restaurar desde un clon solo cubre lo que había en ese clon. Separar las ideas o limitarlo a «lo que estaba en ese clon».
  resuelto: no

## 1.2 Fotos, no diferencias; los tres estados

- frase: "Piensa en un álbum. Cada vez que confirmas, Git fotografía todos tus archivos y guarda una referencia a esa foto."
  hechos: h01-203
  veredicto: PARCIAL
  nota: quita el «básicamente» de la fuente y contradice h01-263 (el commit guarda el área de preparación). Propuesta: «fotografía lo que tienes preparado».
  resuelto: no

- frase: "`git cat-file -p` muestra un objeto de forma legible según su tipo, y `^{tree}` detrás de una revisión designa su árbol."
  hechos: h01-623, h01-624, h01-829, h01-631
  veredicto: PARCIAL
  nota: h01-829 exige que <rev> sea un tree-ish. Propuesta: «detrás de un commit».
  resuelto: no

- frase: "Esos nombres de 40 caracteres son hashes."
  hechos: ninguno
  veredicto: SIN HECHO
  nota: menor; citar h01-630 o h01-212.
  resuelto: no

- frase: "Es la red de seguridad de la sección 1.1."
  hechos: ninguno
  veredicto: PARCIAL
  nota: la «red» de 1.1 era restaurar el servidor desde un clon; aquí es una base de datos que solo crece. Mismo nombre para dos mecanismos.
  resuelto: no

- frase: "[diagrama mermaid de los tres lugares] Directorio de Git (.git) -- «cambiar de rama» --> Directorio de trabajo; «La flecha de vuelta, cambiar de rama, la verás en la sección 1.4.»"
  hechos: ninguno
  veredicto: SIN HECHO
  nota: sin id y modelo incompleto: al cambiar de rama Git rellena el índice y luego el directorio de trabajo (h01-716, h01-472). Rotular «sacar una versión» (h01-225) o pasar por el índice citando h01-716.
  resuelto: no

- frase: "Para lo que no quieres que Git añada, ni que aparezca como sin rastrear, crea un `.gitignore` con patrones al empezar el proyecto, y no confirmarás nada por accidente."
  hechos: h01-272, h01-251, h01-252
  veredicto: PARCIAL
  nota: garantía absoluta; la fuente dice «generalmente una buena idea» y que así evitas confirmar por accidente lo que no quieres incluir. Propuesta: «y evitarás confirmar por accidente lo que no quieres incluir».
  resuelto: no

- frase: "Usa patrones *glob* (patrones de nombres de archivo) estándar, que se aplican de forma recursiva a todo el repositorio; un `!` delante niega un patrón."
  hechos: h01-253, h01-254
  veredicto: PARCIAL
  nota: omite la excepción de la barra inicial (f01-04, línea 130) y la glosa de glob no es la de la fuente. Propuesta: «por defecto se aplican de forma recursiva» o añadir la barra con hecho nuevo.
  resuelto: no

- frase: "`master` no tiene nada de especial: está en casi todos los repositorios solo porque `git init` la crea por defecto y casi nadie la renombra."
  hechos: h01-412, h01-413
  veredicto: PARCIAL
  nota: afirmación fechada de la edición española de Pro Git presentada en presente y sin atribución, en el mismo recuadro que la da por desfasada. Propuesta: «Pro Git explica que master está en casi todos los repositorios solo porque…».
  resuelto: no

- frase: "Con el hash, algo parecido: `git init` usa SHA-1 salvo que pidas `--object-format=sha256`, si está habilitado."
  hechos: h01-280
  veredicto: PARCIAL
  nota: presenta la opción como única excepción (también hay `init.defaultObjectFormat` y GIT_DEFAULT_HASH, sin hecho). Propuesta: «por defecto usa SHA-1; con `--object-format=sha256`, si está habilitado, usa SHA-256».
  resuelto: no

## Observaciones sin veredicto

- El ejemplo 03 hace el commit del IVA en grupos de preparación ocultos: el lector no ve el cambio de 20 % a 21 % que describen texto y diagrama. Decir «parte de un `facturas` en el que ya se ha confirmado…».
- El ejemplo 01, con un solo commit, no demuestra que el clon trae todo el historial (el esquema pedía mostrarlo; `facturas_historial 2` o más lo vería mejor).
- Líneas 94 y 96 repiten «no se vuelve a guardar: se enlaza».
- h01-245 (alcance «en el ejemplo de la fuente») se aplica a otro archivo; mejor citar h01-250 y h01-246.
- h01-128 sobra en la frase de los objetivos del nuevo sistema.

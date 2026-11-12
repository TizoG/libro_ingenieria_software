# Esquema revisado (v2) del capítulo 1: Git por dentro

Propuesta del redactor para que devOC la apruebe **antes** de reescribir el borrador. Parte del esquema aprobado (`esquema.md`, sección 12), de los informes de `revision/` (fuentes y tramos 1 a 4) y de la regla «3 bis» de `docs/05-metodo-sin-alucinaciones.md`. No es texto del libro: son guías para el redactor y el programador. Los ids remiten a `hechos.md`. La tanda h01-846 a h01-903 ya está extraída y se cita con sus ids; «hecho nuevo» se reserva para los tres que aún faltan (sección 9).

Lo que se ha comprobado con Git 2.43.0 en un repositorio de prueba del scratchpad (no es texto del libro; solo asegura que el plan es viable): `rebase -i` con la lista intacta no cambia ningún hash; con `fixup` en la línea 3 y `drop` en la 4, el primer commit conserva su hash; tras `reset --soft HEAD~2` queda `A  exportar.py`, tras `reset HEAD~2` queda `?? exportar.py` y tras `reset --hard HEAD~2` el archivo desaparece del disco; `git reflog exportar-csv` y `exportar-csv@{3}` localizan la punta anterior al rebase; un commit que cambia un archivo de `tests/` añade exactamente cuatro objetos; `git commit -m` en una fusión con conflicto no guarda las líneas `# Conflicts:`; `git reset --mixed HEAD <ruta>` avisa de que está obsoleto; y `git pull` en un clon local cuyo original se ha reescrito se niega con «You have divergent branches».

---

## 0. Reglas de la reescritura

1. **Se escribe desde cero, sección a sección, a partir de este esquema y de las salidas de los ejemplos.** No se retocan párrafos del borrador actual: así no se heredan sus 34 paráfrasis cercanas. Los hechos se citan después, como respaldo.
2. **Cada ejemplo se presenta diciendo de qué estado de `facturas` parte** (cuántos commits, qué ramas), porque cada script arranca en una carpeta limpia. Era un hallazgo del tramo 2.
3. **Todo síntoma de «El problema» se explica después con ids.** Lo que no se pueda explicar no entra en «El problema».
4. **La versión manda.** Cada comportamiento que el libro afirma se ve en un ejemplo ejecutado con Git 2.43 o se atribuye a la documentación actual («la documentación actual de `git pull` dice…»). Lo que solo dice Pro Git en español se atribuye a Pro Git.
5. **Al cerrar cada sección**, además de `comprobar_ids.py` e `insertar_ejemplos.py`, se ejecuta `detectar_copia.py 1`, y el revisor de fuentes mira el orden de la sección frente al capítulo de Pro Git correspondiente.

---

## 1. Qué se conserva y qué se rehace

### Se conserva (con los ajustes de la sección 6)

- **El hilo `facturas`** y `_facturas.sh` (con los cambios de la sección 2).
- **Ejemplos propios que los revisores valoran:** 03 (comparar los árboles de dos commits), 10 (HEAD desacoplado y rescate), 12 (misma foto, otro historial), 18 (bajar del commit al blob), y también 02, 04, 11, 14 y 15.
- **El recuadro del hash reproducible** (1.6), reanclado en `ce4f8a1`, que sale igual en todos los ejemplos, en lugar de en el ejemplo 19.
- **Los diagramas**, con la convención `flowchart` del esquema aprobado: antes y después de un commit, avance rápido frente a tres bandas, HEAD desacoplado, rebase antes y después, misma foto, pasos de `reset`, `amend`, `HEAD~n` y copias de `restore`. Se regeneran los hashes y se corrigen los dos señalados (flecha de vuelta en 1.2; diagrama de 1.6 limitado a lo que imprimen los ejemplos).
- **Recuadros** que no venían calcados: «Bajo el capó» de `diff3`/`zdiff3` (1.4); «Ojo con la versión» de `master`/`main`, de `checkout` frente a `switch`/`restore`, de `ort` (se mueve a 1.5) y de SHA-256; «Error típico» de editar `.git/refs` a mano.
- **Las decisiones del esquema aprobado** que no se mencionan aquí: terminología, rama `main`, grupos `# preparación`, fecha fija, orden del catálogo, lo que queda fuera, PENDIENTE de «En un proyecto real», etc.
- **El cierre:** estructura de «El proyecto avanza», reto del `git log --oneline` en Python, pregunta de «Explicar» y ejercicio de construir del catálogo.

### Se rehace

- **La prosa de todas las secciones**, por la regla 1 de la sección 0.
- **El orden de las siete secciones** (sección 4). Las de estructura alta según el revisor de fuentes (1.1, 1.4, 1.6 y 1.7) cambian por completo; 1.2, 1.3 y 1.5 se reordenan.
- **La premisa de «El problema»** (sin «su PR ya no se puede fusionar» y, según la decisión (a), ajustada a Git 2.43).
- **Nueve ejemplos derivados de Pro Git** (05, 08, 09, 13, 16, 17, 21, 23 y 24); el 19 se quita y se añade el 25 (sección 5).
- **La tabla de 1.7**, que se diseña de nuevo con `switch` y `restore` (hallazgo L-2).
- **Los ejercicios 3 y 4**, las preguntas de defensa 2, 3, 5 y 6, y los pasos 2 y 5 del proyecto.

---

## 2. Cambios comunes

### Cabecera YAML

La del esquema aprobado, sin cambios (`git: "2.43"`, `python: "3.13"`, `estado: borrador`).

### `_facturas.sh`

1. **Marta Ruiz es siempre la autora del commit «Añade tests de total»** (decisión (e)). Desaparece el párrafo que explicaba por qué ese commit tenía dos hashes (`795693a` y `7971f23`), y Marta pasa a ser también la compañera de «El problema». Cambian los hashes desde el cuarto commit; los blobs y árboles no.
2. **Los commits de la rama `exportar-csv` pasan a ser los de «El problema»**, con mensajes propios y sin «WIP» ni «oops»:
   - A: «Añade exportación a CSV».
   - B: «Añade la cabecera al CSV» (con un separador equivocado).
   - C: «Corrige el separador de la cabecera» (corrige B).
   - D: «Prueba el formato con punto y coma» (experimento que sobra).
   Tras el `fixup` de C y el `drop` de D, B' debe tener el mismo contenido que la cabecera que usa `facturas_divergentes`, para que los ejemplos 11 y 12 continúen la historia sin saltos.
3. **Nueva función `facturas_asistente`**: reproduce, en preparación oculta, la secuencia completa del asistente (rebase interactivo, `reset --soft HEAD~2` y `commit`), para los ejemplos 23 y 24.
4. **Nota para el programador sobre la fecha fija.** Con autor, confirmador y fecha fijos, un commit reaplicado sin cambios tendría el mismo hash aunque Git lo reescribiera. En el ejemplo 13, un grupo `# preparación` exporta otra `GIT_COMMITTER_DATE` antes de los rebases. Así, que el primer commit conserve su hash prueba de verdad que Git no lo reescribió.

### Aviso al lector sobre los hashes

En «Lo que necesitas antes»: con `main`, los nombres de rama coinciden con los del libro, pero los hashes de los commits serán otros, porque dependen de tu nombre, tu correo y la hora [h01-639, h01-647]. El recuadro «Bajo el capó» de 1.6 lo retoma y añade el matiz: los blobs y árboles sí coinciden si el contenido es idéntico [h01-294, h01-630].

### Hilo de `facturas` en la v2

| Sección | Estado de `facturas` | Ramas | Ejemplos (orden de aparición) |
| --- | --- | --- | --- |
| 1.1 | Tres commits; clon local en `copia/` | `main` | 01 |
| 1.2 | Dos commits (IVA del 20 % al 21 %); después, el repositorio desde cero | `main` | 03, 02 |
| 1.3 | Tres a cinco commits; Marta, autora de los tests | `main` | 05, 04, 06 |
| 1.4 | Tres commits; `descuentos` y un experimento desacoplado; fusión con conflicto | `main`, `descuentos`, `experimento` | 07, 10, 08, 09 |
| 1.5 | `exportar-csv` con A, B, C y D sobre el tercer commit; `main` con los tests de Marta | `main`, `exportar-csv`, `con-merge`, `con-rebase` | 13, 11, 12, 14, 15 |
| 1.6 | Cuatro commits con `tests/`; un quinto commit para contar objetos | `main` | 18, 17, 16 |
| 1.7 | `exportar-csv` tras el rebase del asistente (A y B'); después, tras toda la secuencia | `main`, `exportar-csv`, rama de rescate | 21, 25, 23, 22, 24 |

---

## 3. Apertura

### Lo que podrás hacer al terminar

Se mantienen los cinco objetivos del borrador, con tres ajustes:

- **3.** «Elegir entre merge y rebase, y decidir cuándo no reescribir, según si otros ya tienen esos commits; y deshacer un commit sin reescribir nada con `git revert`» [h01-510, h01-535, h01-591, h01-594].
- **4.** Se añade «y saber cuánto tiempo lo guarda el reflog» [h01-783, h01-784, h01-870, h01-872].
- **5.** Lleva ids [h01-542, h01-580, h01-448, h01-456] (era SIN HECHO).

### Lo que necesitas antes

- Capítulos previos: ninguno.
- Git 2.43 o posterior y una terminal.
- Nombre y correo con `git config --global` [h01-811, h01-812, h01-639].
- Rama inicial `main` con `init.defaultBranch` [h01-279], «para que coincidan los nombres de rama».
- Aviso de los hashes (sección 2).
- El apéndice «Preparar el entorno» aún no existe (llega en el hito final). Hasta entonces, las dos configuraciones se explican aquí mismo, en una frase cada una, y la remisión al apéndice se añade cuando exista.

### El problema

Las partes que siguen son guía para el redactor, no texto final (unas 170 palabras). Abarca la versión (a2) de la decisión (a).

1. Tu rama `exportar-csv` de `facturas` tiene cuatro commits: dos de la exportación, uno que corrige al anterior y uno de prueba que sobra. Antes de abrir el PR, le pides a un asistente de IA que la deje limpia.
2. Te da cuatro órdenes: un `git rebase -i HEAD~4` con una lista que funde la corrección con su commit y quita la prueba; `git reset --soft HEAD~2`; `git commit -m "Añade la exportación a CSV"`; y `git push --force`. Las ejecutas, nada protesta y queda un solo commit.
3. Al día siguiente te escribe Marta, que había empezado su rama a partir de la tuya. Cuando intenta traer tus cambios, Git le dice que su copia y la del servidor han divergido y se niega a seguir. Cuando le obliga a fusionar, su historial enseña tus commits viejos junto al nuevo, con los mismos cambios dos veces. Ahora tiene que arreglar su rama a mano.
4. Las tres preguntas se mantienen: qué hizo exactamente cada orden, dónde están los commits que «desaparecieron» de tu rama y cómo lo defiendes en la revisión.

Dónde se explica cada síntoma (regla 3):

| Síntoma | Dónde | Respaldo |
| --- | --- | --- |
| Qué hizo el rebase interactivo | 1.5, ejemplo 13 | h01-859, h01-860, h01-764 |
| Qué hicieron `reset --soft` y `commit` | 1.7, ejemplo 21 | h01-718, h01-891, h01-892 |
| `push --force` sobrescribe el servidor | 1.5, una frase (los remotos son del capítulo 2) | h01-522 |
| «Se niega a seguir» | 1.5, «Ojo con la versión» | h01-880, h01-881 |
| «Commits viejos y nuevo, cambios dos veces» | 1.5 | h01-520, h01-523, h01-524, h01-883 |
| «Arreglar su rama a mano» | 1.5 | h01-591, h01-593 |
| Dónde están los commits | 1.6 (siguen en `objects`) y 1.7, ejemplo 24 (reflog de la rama) | h01-766, h01-774, h01-783, h01-872, hecho nuevo `<ref>@{n}` |

Se quita «su PR ya no se puede fusionar»: no tiene hecho y los PR son del capítulo 2.

---

## 4. Las secciones

Cada sección conserva el ritmo de la plantilla (idea, modelo, ejemplo, porqué, caso límite), pero el hilo sale de `facturas` y de «El problema». Para cada una se indica el orden de la fuente de la que se calcó y en qué se diferencia el nuevo.

### 1.1 Qué es el control de versiones (450 palabras)

**Orden de la fuente (Pro Git 1.1 y 1.2).** Definición, sistemas locales (copiar directorios, RCS y parches), centralizados (CVS y Subversion, punto único de fallo, caída de una hora, disco corrupto), distribuidos (clon completo, restaurar desde un clon) e historia (kernel 1991-2002, BitKeeper en 2002, ruptura en 2005, objetivos de diseño).

**En qué se diferencia el nuevo orden.** Arranca con `facturas` y con un clon ejecutado. La taxonomía local/centralizado/distribuido se reduce a la pregunta «¿dónde vive el historial?» y se dibuja después de ver la salida. RCS desaparece. No hay «caída de una hora». La historia baja de un párrafo a una o dos frases, al final.

**Idea en dos frases.** Un control de versiones guarda la historia de tus archivos para volver a cualquier versión. En Git cada clon trae esa historia entera, y por eso casi todo ocurre en tu disco.

**Hilo propio.**

1. `facturas` antes de Git: una carpeta llena de copias (`facturas_v2_final_DEFINITIVO`). Qué falla al copiar carpetas, en dos frases propias [h01-105, h01-106, h01-107], y qué le pides a un control de versiones: volver a cualquier versión de un archivo o del proyecto [h01-101, h01-102, h01-103].
2. Ejemplo 01 (ajustado): `facturas` con tres commits, `git log --oneline`, clon en `copia` y el mismo `git log` dentro del clon.
3. Lectura de la salida: los tres commits, con los mismos nombres, están en la copia. Un clon copia el repositorio entero, no solo los archivos [h01-120, h01-121, h01-223].
4. Modelo: «¿dónde vive el historial?». Se conserva el diagrama centralizado/distribuido, con ids en la frase que lo presenta [h01-110, h01-112, h01-120] (era SIN HECHO).
5. Consecuencia que el lector puede comprobar: `git log` en `copia` no ha necesitado nada más que tu disco [h01-206, h01-207, h01-208].
6. Caso límite: el servidor pierde el disco. En un sistema centralizado se pierde el historial [h01-118]. Con Git, cualquier clon sirve para restaurarlo [h01-122], pero solo con lo que tuviera ese clon, y lo que nadie confirmó no está en ninguno [h01-347]. No se usa h01-345 aquí.
7. Cierre histórico, una o dos frases: Git nació en 2005 en la comunidad del kernel de Linux, cuando BitKeeper dejó de ser gratuito [h01-126, h01-127, h01-128, h01-809]. Dos de sus objetivos, la velocidad y las miles de ramas en paralelo, reaparecen en 1.4 [h01-129, h01-130].

**Recuadros.** Ninguno.

---

### 1.2 Fotos, no diferencias; los tres estados (1.200 palabras)

**Orden de la fuente (Pro Git 1.3 y 2.2).** Diagramas conceptuales de diferencias frente a instantáneas, operaciones locales, integridad con SHA-1, «solo añade», tres estados y tres secciones; después, rastrear, preparar, estado corto, ignorar, diff, confirmar, saltar la preparación, borrar y mover.

**En qué se diferencia el nuevo orden.** Abre con un experimento (ejemplo 03) y la teoría sale de lo que se ve. El hash se explica a partir de los nombres que aparecen en la salida. Las tres secciones llegan como respuesta a «¿de dónde sale la foto?». No hay párrafo de «operaciones locales» (ya está en 1.1), ni de borrar o mover archivos.

**Idea en dos frases.** Cada commit guarda una foto completa del proyecto en la que lo que no cambió se reutiliza, nombrada por el hash de su contenido. La foto se toma de una zona intermedia, el área de preparación, y no de tu disco.

**Hilo propio.**

1. Ejemplo 03 (ajustado): dos commits de `facturas`; `git diff HEAD~1 HEAD` enseña que solo cambia una línea de `factura.py`; después, los árboles de los dos commits. La pregunta: si el cambio es una línea, ¿qué ha guardado Git?
2. Lectura: cada commit tiene un árbol completo, y los archivos que no cambiaron tienen el mismo hash en los dos [h01-203, h01-204, h01-214, h01-630]. `git diff` te enseña la diferencia entre dos commits [h01-843]; lo que se guarda son fotos [h01-401, h01-205]. Se presentan `cat-file -p` y `^{tree}` «detrás de un commit» [h01-623, h01-624, h01-829, h01-631], como adelanto de 1.6.
3. El álbum, como analogía corregida: Git fotografía lo que tienes preparado [h01-203, h01-263].
4. Los nombres: 40 caracteres hexadecimales calculados del contenido [h01-209, h01-211, h01-212, h01-213]. `ce4f8a1` es un prefijo [h01-820, h01-821]. Cambiar un bit cambia el nombre [h01-210, h01-287]. Casi todo solo añade, así que lo confirmado es difícil de perder [h01-215, h01-216]. Ya no se llama «la red de seguridad de 1.1».
5. ¿De dónde sale la foto? Tres lugares: directorio de trabajo, área de preparación (índice) y `.git` [h01-221, h01-222, h01-224, h01-226, h01-706]. Diagrama de los tres lugares, corregido: la flecha de vuelta se rotula «sacar una versión» [h01-225]; el detalle de que pasa por el índice llega en 1.7 [h01-716].
6. Ejemplo 02 (se conserva): el recorrido `??`, `A `, ` M` y `MM`; las dos columnas de `git status -s` [h01-248, h01-249, h01-250]; el diagrama de estados conservado [h01-217, h01-233, h01-235, h01-241, h01-242].
7. `git diff` frente a `git diff --staged`, leídos sobre el `MM` [h01-255, h01-256, h01-257, h01-259, h01-260].
8. Por qué: `git add` copia el contenido de ese momento [h01-405, h01-246], y `git status` compara por parejas [h01-703, h01-714, h01-715].
9. Caso límite: confirmar con el `MM` se lleva la versión preparada y deja fuera la otra [h01-247, h01-262, h01-263]. Se cita h01-246 y h01-250, no h01-245.

**Recuadros.**

- **Error típico** (`.gitignore`), con las dos correcciones del tramo 1: «evitarás confirmar por accidente lo que no quieres» [h01-252] y «por defecto se aplican de forma recursiva» [h01-253].
- **Ojo con la versión** (`master`/`main` y SHA-1), corregido: «Pro Git explica que `master` está en casi todos los repositorios porque…» [h01-412, h01-413]; y «por defecto usa SHA-1; con `--object-format=sha256`, si está habilitado, SHA-256» [h01-280].

---

### 1.3 Leer y deshacer el historial (1.150 palabras)

**Orden de la fuente (Pro Git 2.3 y 2.4).** `git log`, `-p`, `--stat`, `--pretty` y su tabla de formatos, autor frente a confirmador, `--graph`, límites (`-n`, `--since`, `--author`, `--grep`, `-S`, ruta); después, `--amend` para un archivo olvidado, deshacer lo preparado con `reset HEAD` y lo modificado con `checkout --`.

**En qué se diferencia el nuevo orden.** Abre con la idea de que deshacer casi nunca borra, y con un `--amend` visto por dentro, no con la receta del archivo olvidado. Leer el historial llega como la herramienta para encontrar qué deshacer, y `git log` se cuenta por preguntas sobre `facturas`, no por opciones. Deshacer archivos se explica como copias entre los tres lugares de 1.2, no como dos recetas.

**Idea en dos frases.** Deshacer en Git casi siempre crea algo nuevo o copia contenido de un sitio a otro, y solo pierdes lo que nunca confirmaste. Para elegir qué deshacer necesitas leer el historial, y `git log` es una consulta sobre él.

**Hilo propio.**

1. La idea, con ids [h01-215, h01-764, h01-345, h01-347]. Aquí sí hay una forma de perder trabajo, y se dice con palabras propias [h01-327, h01-347]. Se elimina la cita literal de 17 palabras (hallazgo 1.3-1).
2. Ejemplo 05 (rehecho): confirmas el redondeo con un mensaje que no dice lo que hace y lo corriges con `git commit --amend -m`. Después, `git cat-file -p HEAD` y `git cat-file -p HEAD@{1}`: mismo `parent`, mismo `tree`, otro mensaje y otro hash.
3. Lectura: `--amend` sustituye la punta de la rama por un commit nuevo con los mismos padres y el mismo autor [h01-846, h01-847, h01-848, h01-763, h01-764]. El hash cambia porque el mensaje forma parte del commit [h01-640, h01-647]. Si hubieras preparado algo, entraría en la foto nueva [h01-331, h01-332]. Diagrama del `amend` conservado, con hashes nuevos.
4. Para deshacer hay que encontrar. El historial es un grafo que se recorre hacia atrás siguiendo los padres [h01-302, h01-570, h01-761] («cadena», no). `HEAD~n` y `^`, con su diagrama [h01-822, h01-825, h01-826, h01-828]. El `HEAD@{1}` del ejemplo 05 es otra cosa: dónde estaba `HEAD` un movimiento antes [h01-775].
5. Ejemplo 04 (se conserva), contado por preguntas. ¿Cuándo cambió el IVA? `-S` [h01-324]. ¿Qué commits tocaron el README? La ruta [h01-325, h01-326]. ¿Quién escribió los tests? `--format=fuller`: Marta es la autora y tú, el confirmador [h01-838, h01-839, h01-316, h01-317]. La explicación de autor y confirmador sale de la salida, sin calcar f01-05. El formato estable para scripts va en una frase [h01-312, h01-313].
6. Ejemplo 06 (ajustado): `git restore --staged` copia de `HEAD` al índice y solo toca el índice [h01-354, h01-356, h01-849]; `git restore` copia del índice al directorio de trabajo [h01-357, h01-850]. Ahora `git status -s` enseña `M `, ` M` y nada. Se conserva el diagrama de las copias y `--source` [h01-358, h01-359].
7. Error típico: `git restore <archivo>` sobre trabajo sin confirmar; el archivo se sobrescribe y lo que no confirmaste no vuelve [h01-342, h01-352, h01-347]. «La forma que enseña Pro Git, `git checkout -- <archivo>`», no «el antiguo» [h01-341, h01-479].
8. Caso límite: ¿dónde está el commit sustituido? `git reflog` lo lista [h01-774, h01-777, h01-786], y es recuperable [h01-346]. Cuánto tiempo y cómo, en 1.7.

**Recuadros.**

- **Ojo con la versión**, reescrito con las equivalencias correctas. Pro Git usa `git reset HEAD <archivo>` y `git checkout -- <archivo>` [h01-336, h01-340]. Hoy, `git restore --staged <archivo>` equivale a `git reset <archivo>` [h01-361, h01-901]. `git checkout -- <archivo>` copia desde el índice [h01-852], igual que `git restore <archivo>` [h01-357]. Con un commit, `git checkout <commit> -- <archivo>` pone esa versión en el archivo y en el índice [h01-853], que es lo que hace `restore` con `--staged --worktree` [h01-362, h01-851]. El `git status` de Git 2.43 ya sugiere la forma nueva [h01-350].

---

### 1.4 Las ramas son punteros (1.500 palabras)

**Orden de la fuente (Pro Git 3.1, 3.2 y 3.3).** Qué contiene un commit (blobs, árbol, commit), la rama como apuntador, `master` no es especial, `git branch`, HEAD, `checkout`, el commit que avanza la rama y la divergencia. Después, el escenario `iss53`: arreglo urgente con `hotfix`, avance rápido, borrar la rama, fusión a tres bandas y conflicto (estado, marcadores, `add`, `commit`). Y la gestión de ramas (`--merged`, `--no-merged`, `-d`/`-D`).

**En qué se diferencia el nuevo orden.** Empieza en el disco, con los archivos de las ramas y de `HEAD`. El HEAD desacoplado se adelanta y cierra la primera mitad («todo son punteros»), antes de las fusiones. Las fusiones se explican por qué puntero se mueve, desde las salidas, sin «arreglo urgente» ni borrado de ramas. No hay gestión de ramas: `-d`/`-D` queda en un recuadro.

**Idea en dos frases.** Una rama es un archivo con el hash de un commit, y `HEAD` es otro archivo que dice en qué rama estás (o en qué commit). Confirmar adelanta una rama; fusionar adelanta un puntero o crea un commit con dos padres, y hay conflicto cuando los dos lados cambian de forma distinta la misma zona.

**Hilo propio.**

1. Ejemplo 07 (ajustado): `git branch descuentos`, los dos archivos de rama con el mismo hash, `HEAD` con `ref:`, cambio de rama y commit. Al final se repiten los dos `cat` de las ramas: solo ha cambiado el de `descuentos`. Es la pregunta de «Explicar» del catálogo, respondida con la salida [h01-415, h01-417, h01-424, h01-655, h01-664, h01-665, h01-420, h01-643].
2. Modelo: commits que no se mueven y nombres que sí. Se conserva el diagrama antes y después del commit [h01-570, h01-763, h01-766, h01-416].
3. Lo que cuesta una rama: escribir 41 bytes [h01-425, h01-426]; es el objetivo de 1.1 [h01-130].
4. `HEAD` también puede señalar un commit. Ejemplo 10 (se conserva): HEAD desacoplado, el aviso al irte y el rescate con el reflog [h01-474, h01-482, h01-483, h01-484, h01-486, h01-487, h01-775, h01-788]. Se corrige h01-485: «la documentación de `git checkout` lo cuenta con su ejemplo: un commit al que nada referencia acabará eliminado por la recolección de basura; hasta entonces, el reflog lo guarda» [h01-485, h01-779, h01-872]. Diagrama conservado.
5. Juntar dos líneas: ¿qué puntero se mueve? Ejemplo 08 (rehecho): sigue donde acaba el 07; desde `main`, `cat .git/refs/heads/main`, `git merge descuentos` y otra vez el `cat`. El avance rápido consiste en reescribir el archivo de `main` con el hash de `descuentos` [h01-433, h01-434, h01-435, h01-497]. `--no-ff`, en una frase [h01-498].
6. Si las dos han avanzado, hace falta un commit con dos padres a partir del ancestro común [h01-440, h01-441, h01-442, h01-443, h01-445, h01-427]. Se conserva el diagrama de avance rápido frente a tres bandas, y «lo que haga Git depende de la forma del grafo» lleva ids [h01-434, h01-440].
7. Ejemplo 09 (rehecho), explicado desde la salida:
   - la divergencia en el grafo;
   - el merge que falla, con un `git status` que lista la ruta sin fusionar y ofrece `--abort` [h01-449, h01-450, h01-451, h01-452, h01-489, h01-490, h01-491];
   - `cat factura.py`, donde la línea `def`, que solo cambió `descuentos`, ya está fusionada y los marcadores encierran solo `return` [h01-855, h01-448 con «de forma distinta», h01-453, h01-454, h01-492, h01-493, h01-494]; si los dos lados hubieran hecho el mismo cambio, no habría conflicto [h01-856];
   - la resolución, que combina los dos cambios (es lo que muestra la salida; Git no decide por ti [h01-492]);
   - `git add` y `git commit -m` [h01-456, h01-457, h01-460];
   - las dos líneas `parent`, en orden [h01-404, h01-841];
   - `git log --oneline -1 HEAD^2`, porque `^2` solo tiene sentido en un commit de fusión [h01-823, h01-824].
8. Caso límite, como «Error típico»: `-d` se niega si hay trabajo sin fusionar y `-D` fuerza el borrado [h01-467, h01-468, h01-469], salvo que lo rescates del reflog [h01-346]. Cambiar de rama con cambios sin confirmar: Git aborta si fuera a perderlos [h01-476].

**Recuadros.** «Bajo el capó» de `diff3`/`zdiff3` (se conserva, con h01-857 y h01-858 para decir qué falta en los marcadores normales) y «Ojo con la versión» de `checkout` frente a `switch` (se conserva). El párrafo de `ort` se mueve a 1.5, junto a la primera salida que lo enseña (ejemplo 12). Se quita la comparación con CVS/Subversion (h01-446, h01-447): viene de una traducción antigua y habla en presente.

---

### 1.5 Rebase y reescribir historia (1.400 palabras)

**Orden de la fuente (Pro Git 3.6 y 7.6).** Rebase básico (C3/C4, archivos temporales, avance rápido), rebases interesantes (`--onto`), peligros (`push --force`, `pull` que duplica), reorganizar una reorganización (`patch-id`, `pull --rebase`) y rebase frente a merge (dos visiones del historial). En 7.6: `--amend`, `rebase -i HEAD~3` («reescribe todo el rango»), reordenar, aplastar, dividir y `filter-branch`.

**En qué se diferencia el nuevo orden.** Abre con la primera orden del asistente, el rebase interactivo, y deja el rebase básico como generalización. La mecánica es la de la documentación actual (reaplicar uno a uno y saltar los que no cambian), y se ve en la salida con Git 2.43. Los peligros se cuentan con Marta. `patch-id` y `git pull` van en recuadros con la versión actual. No hay `--onto`, ni la escena del servidor y el cliente, ni dividir commits, ni `filter-branch`.

**Idea en dos frases.** Rebase reaplica commits uno a uno sobre una base, y desde el primero que cambia crea commits nuevos con hashes nuevos; los antiguos se quedan sin rama. La foto final puede ser la misma que con un merge, pero el historial es otro, y eso daña a quien ya tenía los commits antiguos.

**Hilo propio.**

1. Ejemplo 13 (rehecho): los cuatro commits de `exportar-csv`.
   - El lector ve la lista de tareas.
   - Rebase con la lista intacta: ningún hash cambia.
   - Rebase con la lista del asistente (`fixup` en la 3, `drop` en la 4): A conserva su hash y B' es nuevo.
   La lista se edita con el comando de `GIT_SEQUENCE_EDITOR` [h01-807, h01-808].
2. Lectura: la lista se ejecuta de arriba abajo, en orden inverso al de `git log` [h01-547, h01-589]. Cada línea reaplica un commit, uno a uno [h01-859]. Por defecto Git avanza sin reescribir sobre los commits que no cambian; solo `--no-ff` los reaplicaría todos [h01-860, h01-861]. Desde el primero que cambia todos son nuevos, porque cada commit guarda el hash de su padre [h01-764, h01-570]. Las acciones se presentan «entre otras» [h01-548, h01-549, h01-550, h01-551, h01-552, h01-580]. Se sustituye la frase NO SOPORTADA sobre h01-543.
3. Diagrama nuevo: la fila de cuatro commits antes y después, con A compartido, B' nuevo, y B, C y D en discontinuo, sin rama.
4. Generalización: `git rebase main` es la misma reaplicación sobre otra base: lista los commits que `main` no tiene, se coloca en `main` y los reaplica [h01-859]. Ejemplo 11 (se conserva). Como todos cambian de padre, todos cambian de hash [h01-503, h01-514, h01-570], y el merge final es un avance rápido [h01-509, h01-434]. «Un avance rápido o una incorporación limpia» [h01-513]. Diagrama de antes y después conservado. La analogía con `--amend` se limita a «no se edita: se sustituye» [h01-763, h01-764].
5. ¿Qué has ganado frente al merge? Ejemplo 12 (se conserva): misma foto, otro grafo [h01-510, h01-511, h01-515, h01-843]. Aquí va el «Ojo con la versión» de `ort`, que aparece en su salida [h01-801, h01-803, h01-804, h01-805, h01-806].
6. Caso límite: conflicto a mitad del rebase. Ejemplo 14 (se conserva), con tres salidas posibles [h01-574, h01-575, h01-576]. Que diga «interactive rebase in progress» sin `-i` se explica con el *backend* `merge`, que es el de por defecto [h01-862, h01-863] y que antes se llamaba «interactive» [hecho nuevo, sección 9]. Si ese hecho no llega, la frase se limita a h01-863 y no explica el texto de la salida.
7. Vuelta a Marta. El asistente abandonó commits que eran la base de los de Marta y creó otros parecidos [h01-520, h01-521]. `push --force` sobrescribió el registro del servidor (una frase; los remotos son del capítulo 2) [h01-522]. Ahora Marta debe arreglar su historial a mano [h01-591, h01-593]. La regla: reorganiza lo que nadie más tiene y nunca lo que ya compartiste [h01-535, h01-519, h01-529]. El daño viene de abandonar commits y crear otros, no de que la foto sea igual (corrige el «por eso» del tramo 3).
8. Deshacer sin reescribir. Ejemplo 15 (se conserva): `git revert` añade un commit que deshace a otro y no toca los anteriores [h01-594, h01-595]; una fusión necesita `-m` [h01-598]. La conexión con el punto 7 se hace como razonamiento explícito del texto («si el commit ya está en una rama compartida, la regla te impide reescribirlo; revert no lo necesita»), no como algo que diga la fuente.
9. Opcional, una frase: las dos visiones del historial, atribuidas a Pro Git [h01-531, h01-533]. Se quita si falta espacio.

**Recuadros.**

- **Ojo con la versión** (`git pull`). Pro Git cuenta que, tras un rebase publicado, `git pull` crea una fusión con las dos líneas y `git log` enseña commits repetidos [h01-523, h01-524]. La documentación actual de `git pull` dice que, si no eliges cómo reconciliar ramas divergentes, solo hace avances rápidos y falla si tu rama ha divergido [h01-880, h01-881]; con `--no-rebase` fusiona y con `--rebase` reorganiza [h01-882, h01-883], y se puede fijar con `pull.rebase` [h01-885]. Es lo que le pasó a Marta. Sin ejemplo en este capítulo (decisión (a)).
- **Bajo el capó** (`patch-id`), escrito de nuevo con las salvedades: «es posible que Git reconozca…» y «solo funciona si los parches son muy parecidos» [h01-525, h01-526, h01-527, h01-528, h01-530].
- **Ojo con la versión** (acciones del rebase interactivo): se conserva, con «entre otras». Pro Git ya lista `exec`. `--autosquash` con `git commit --fixup` va en una frase opcional [h01-587, h01-588, h01-590]; sale del ejemplo.
- **Ojo con la versión** (mecánica): Pro Git describe el rebase guardando las diferencias en archivos temporales [h01-504 a h01-508]; la documentación actual describe cuatro pasos (listar, colocarse en la base, reaplicar uno a uno y mover la rama) y dos *backends*, con `merge` por defecto [h01-859, h01-862, h01-863]. Se puede fundir con el anterior si falta espacio.
- PENDIENTE de «En un proyecto real» (decisión 8 del esquema aprobado).

---

### 1.6 Bajo el capó: objetos y referencias (1.150 palabras)

**Orden de la fuente (Pro Git 10.1, 10.2 y 10.3).** Fontanería y porcelana, contenido de `.git`, almacén vacío y `hash-object -w --stdin` con un texto de prueba, versiones de un archivo, `cat-file -t`, árboles con `update-index`/`write-tree`/`read-tree`, commits con `commit-tree`, almacenamiento (cálculo en Ruby: cabecera, SHA-1, zlib), referencias con `update-ref`, HEAD con `symbolic-ref`, etiquetas y remotas. Va de abajo arriba y construye los objetos a mano.

**En qué se diferencia el nuevo orden.** Va de arriba abajo en un repositorio real: `HEAD`, rama, commit, árbol, subárbol y blob. Calcula el hash de un archivo de `facturas`, no de un texto de prueba, y lo compara con la entrada del árbol. No construye objetos a mano: observa qué escribe un commit normal. La fontanería se nombra en una frase al usar `cat-file`, no abre la sección.

**Idea en dos frases.** En `.git` hay objetos que no cambian, nombrados por el hash de su contenido (blobs, árboles, commits y etiquetas anotadas), y referencias que sí cambian. Todo lo que cambia un comando se reduce a añadir objetos y añadir o mover referencias.

**Hilo propio.**

1. Apertura con la segunda pregunta de «El problema» y la promesa de 1.2: para saber dónde están tus commits, mira qué es un commit en disco. Dos clases de piezas [h01-766, h01-768], con la frase corregida del tramo 3 («todo lo que cambia…»).
2. Ejemplo 18 (ajustado), de arriba abajo: `cat .git/HEAD`, `cat .git/refs/heads/main`, `git cat-file -t` y `-p` de ese hash, `HEAD^{tree}`, el subárbol `tests`, el blob y un `ls` de la subcarpeta de su objeto. Lectura nivel a nivel:
   - referencia simbólica y rama [h01-664, h01-652];
   - fontanería en una frase [h01-603, h01-604];
   - campos del commit [h01-638, h01-639, h01-640, h01-570];
   - entradas del árbol y subárbol [h01-628, h01-629, h01-630, h01-632, h01-635];
   - objeto en una subcarpeta de dos caracteres y un nombre de 38, «en principio» [h01-621, h01-622, h01-644].
3. Diagrama conservado y recortado a lo que imprime el 18: `HEAD`, rama, commit, padre, árbol, blobs y subárbol. Sin el árbol del padre. Etiquetas, según la decisión (c).
4. Ejemplo 17 (rehecho): en `facturas`, un bloque de Python lee `factura.py`, calcula el SHA-1 de la cabecera más el contenido y lo compara con el hash que da el árbol (y con `git hash-object factura.py`, sin `-w`). Después descomprime con zlib el archivo del objeto y enseña la cabecera [h01-294, h01-645, h01-646, h01-647, h01-648, h01-617, h01-618].
5. Árboles y commits se guardan igual, con otra cabecera [h01-649, h01-650, h01-651]. Por tanto, el hash de un commit depende de su árbol, sus padres, el autor y la fecha, y el mensaje, y cambiar un commit cambia los de todos los que lo siguen [h01-638, h01-640, h01-647, h01-570, h01-571]. Es la respuesta de fondo al objetivo 1.
6. **Bajo el capó** (hash reproducible), reanclado: `ce4f8a1` sale igual en todos los ejemplos, aunque cada uno se ejecute en una carpeta nueva, porque el entorno fija autor y fecha. En tu máquina los commits tendrán otros hashes; los blobs y los árboles, no, si el contenido es el mismo [h01-639, h01-647, h01-294, h01-630]. Hace a la vez de caso límite y sustituye al de «dos archivos con el mismo contenido» (SIN HECHO y sin ejemplo).
7. Ejemplo 16 (rehecho): qué escribe un commit. Se cuentan los archivos de `.git/objects` y se lee el de la rama antes y después de un commit que cambia un archivo de `tests/`. Salen cuatro objetos nuevos (blob, árbol `tests`, árbol raíz y commit) y una referencia movida [h01-643, h01-204, h01-768]. Es la pregunta de «Explicar», vista por dentro.
8. Referencias. Ramas y `HEAD` ya vistas. Etiquetas, según la decisión (c), con «generalmente» [h01-675]; «quien la creó» se apoya ahora en h01-875 (línea `tagger`) y no en h01-674, cuyo «marcador» es una errata. Remotas, en una frase y remitidas al capítulo 2 [h01-683, h01-687].
9. Cierre: tus commits abandonados siguen en `objects`, pero ninguna referencia los alcanza. La sección 1.7 los encuentra.

**Recuadros.** «Error típico» de editar referencias a mano (se conserva) [h01-655, h01-657, h01-658, h01-669, h01-672]. «Ojo con la versión» de SHA-1 y SHA-256 (se conserva), con «salvo que crees el repositorio con SHA-256» [h01-280, h01-283, h01-288, h01-289, h01-290, h01-292].

---

### 1.7 reset sin miedo (1.400 palabras)

**Orden de la fuente (Pro Git 7.7 y 10.7).** Los tres árboles, el flujo de trabajo, el papel de `reset` en tres pasos con `file.txt` v1/v2/v3 (`--soft`, `--mixed`, `--hard`), recapitulación, `reset` con ruta, aplastar con `reset --soft HEAD~2`, `checkout` sin rutas (`develop`/`master`) y con rutas, y la tabla resumen. En 10.7: `reset --hard` que pierde commits, reflog, `log -g`, rama de rescate, borrar el reflog y `fsck --full`.

**En qué se diferencia el nuevo orden.** Abre con lo que hizo el asistente (`reset --soft HEAD~2` y `commit`), que Pro Git trata casi al final (después del reset con ruta), y generaliza después. Los tres modos se comparan desde un mismo punto de partida, no en secuencia. La comparación con cambiar de rama usa `switch --detach` sobre el mismo `HEAD~2` del asistente, no `develop`/`master`. El rescate usa el reflog de la rama `exportar-csv`, sin la escena de borrar el reflog y `fsck`. La tabla es propia, con `switch` y `restore`.

**Idea en dos frases.** Sin ruta, `reset` mueve la rama a la que apunta `HEAD` y, según el modo, copia ese commit al índice y al directorio de trabajo. Lo confirmado sigue en el reflog durante un tiempo; lo que pisa `--hard` sin haberlo confirmado no vuelve.

**Hilo propio.**

1. Ejemplo 21 (rehecho): las órdenes 2 y 3 del asistente sobre `exportar-csv` (A y B' tras el rebase de 1.5): `git log`, `reset --soft HEAD~2`, `git status -s` con `A  exportar.py`, `git log`, `commit`, `git log` y `git reflog -3`. Lectura: solo se movió la rama, y el índice y el directorio no cambiaron [h01-718, h01-720, h01-891]; el `commit` confirmó de una vez lo que había en el índice. La documentación actual usa justo este par para unir varios commits en uno [h01-892]; Pro Git lo cuenta igual [h01-741, h01-742]. Diagrama nuevo del grafo antes y después.
2. ¿Y si hubiera escrito otro modo? Ejemplo 25 (nuevo): los tres modos desde el mismo punto, con `git status -s` y `ls`. `exportar.py` queda preparado con `--soft` [h01-891], sin rastrear con el modo mixto, que es el de por defecto [h01-888, h01-889, h01-890], y borrado del disco con `--hard`, que quita los archivos rastreados que no están en el commit [h01-893, h01-895, h01-896].
3. Modelo: los tres lugares de 1.2 con los nombres de Pro Git, «tres árboles», en una frase atribuida [h01-701, h01-702, h01-703, h01-704, h01-708]. Diagrama de los tres pasos conservado [h01-717, h01-724, h01-728]. «Has deshecho el último commit» lleva h01-721 y h01-722.
4. Qué mueve `reset` y qué mueve cambiar de sitio. Ejemplo 23 (rehecho): `reset --soft HEAD~2` frente a `switch --detach HEAD~2`, leyendo `.git/HEAD` y `.git/refs/heads/exportar-csv` tras cada uno. `reset` cambia el archivo de la rama y `switch`, el de `HEAD` [h01-718, h01-747, h01-474, h01-482]. Cambiar de rama comprueba que no pisa cambios; `reset --hard`, no [h01-745, h01-746, h01-476], escrito como «`git checkout <rama>` comprueba…».
5. Con ruta. Ejemplo 22 (ajustado): `git reset HEAD~2 factura.py` y `git restore --source=HEAD~2 --staged factura.py` dejan el mismo `MM` sin mover la rama. Con ruta, `reset` se salta el primer paso y solo actualiza el índice de esos archivos [h01-734, h01-735, h01-899, h01-902]; es lo contrario de `git add` [h01-900], y para tocar también el archivo hay que ir a `git restore` [h01-903, h01-358]. No se presenta la forma larga con `--mixed` como sintaxis actual.
6. Tabla propia (sección 4.1).
7. Recuperar lo que el asistente abandonó. Ejemplo 24 (rehecho): `git reflog exportar-csv` enseña cada movimiento de la rama (commits originales, fin del rebase, reset y commit); `git branch` en `exportar-csv@{n}` recupera los cuatro commits originales, y `git log --oneline` de la rama nueva los enseña [h01-774, h01-777, h01-783, h01-784, h01-788, hecho nuevo `<ref>@{n}`].
8. Caso límite: cuánto dura la red. Las entradas del reflog que siguen siendo alcanzables caducan por defecto a los 90 días, y las que ya no lo son (los commits que abandonó el asistente), a los 30 [h01-868, h01-870, h01-871, h01-872]; esa poda la lanza normalmente `git gc`, no el usuario [h01-873]. `git fsck --full`, en una frase, como último recurso [h01-791, h01-792, h01-793]. Lo no confirmado que pisa `--hard` no vuelve nunca [h01-733, h01-347].

**Recuadros.**

- **Error típico.** `reset --hard` con cambios sin confirmar [h01-730, h01-746, h01-733], sin el apoyo por analogía de h01-732.
- **Bajo el capó.** El reflog es local y vive en `.git/logs/` [h01-774, h01-790]; `HEAD@{n}` y `rama@{n}` [h01-775, hecho nuevo].
- **Ojo con la versión.** Pro Git explica el reset con ruta como `git reset --mixed HEAD <archivo>` y el checkout con ruta [h01-736, h01-751]. En la documentación actual, la forma con ruta solo toca el índice y equivale a `git restore --staged`, y para tocar también los archivos remite a `git restore` [h01-901, h01-902, h01-903, h01-597]. Que Git 2.43 avise de que `--mixed` con rutas está obsoleto no tiene hecho: o se pide (sección 9) o no se dice.

**Cierre de «El problema»** (unas 150 palabras), reescrito:

- Qué hizo cada orden: el rebase reescribió desde el primer commit que cambió (1.5), `reset --soft` movió la rama, `commit` unió lo preparado y `push --force` sobrescribió el servidor [h01-764, h01-718, h01-742, h01-522].
- Dónde están los commits: en tu repositorio, localizables desde el reflog de la rama durante 30 días, porque ninguna rama los alcanza [h01-774, h01-871, h01-872].
- Cómo se defiende: el problema fue reescribir commits sobre los que Marta ya trabajaba [h01-591]; la lección es reorganizar solo lo que nadie más tiene [h01-535].
- Qué puede hacer Marta: reorganizar su trabajo sobre tu commit nuevo, con la ayuda de `patch-id` si los parches se parecen [h01-526, h01-527, h01-528, h01-593].
- Se quita «para deshacer algo publicado, la próxima vez, `git revert`», que no encaja con «El problema».

#### 4.1 Tabla propia de 1.7

Columnas: «Qué cambia de sitio», «Índice», «Directorio de trabajo» y «¿Puede pisar cambios sin confirmar?». Las columnas no son las de Pro Git, y aquí la última fila pregunta por el riesgo, no por la protección.

| Orden | Qué cambia de sitio | Índice | Directorio | ¿Pisa cambios? | Respaldo |
| --- | --- | --- | --- | --- | --- |
| `git reset --soft <commit>` | la rama | no | no | no | h01-718, h01-891 |
| `git reset <commit>` | la rama | sí | no | no | h01-888, h01-889, h01-890 |
| `git reset --hard <commit>` | la rama | sí | sí | sí | h01-893, h01-894, h01-896, h01-746 |
| `git switch <rama>` o `--detach <commit>` | `HEAD` | sí | sí | no: se aborta | h01-471, h01-472, h01-476, h01-474 |
| `git reset [<commit>] <archivo>` | nada | sí | no | no | h01-899, h01-902 |
| `git restore --staged [--source=<commit>] <archivo>` | nada | sí | no | no | h01-354, h01-356, h01-358, h01-849 |
| `git restore [--source=<commit>] <archivo>` | nada | no | sí | sí | h01-352, h01-850, h01-772, hecho nuevo de f01-24 |

---

## 5. Lista de ejemplos v2

Categorías: **se conserva** (mismo script; solo se regenera la salida si cambia `_facturas.sh`), **se ajusta** (mismo planteamiento con cambios concretos), **se rehace** (planteamiento nuevo y propio, que no adapta una demostración de Pro Git ni usa «WIP», «oops», `develop`/`master` ni el «arreglo urgente»), **se quita** y **nuevo**.

| Nº | Archivo actual | Sección v2 | Categoría | Qué cambia |
| --- | --- | --- | --- | --- |
| 01 | `01-clon-completo.sh` | 1.1 | se ajusta | `facturas_historial 3`: el clon enseña tres commits, no uno |
| 02 | `02-tres-estados.sh` | 1.2 | se conserva | — |
| 03 | `03-fotos-no-diferencias.sh` | 1.2 (abre) | se ajusta | El cambio del IVA se ve: `git diff HEAD~1 HEAD` antes de los árboles |
| 04 | `04-leer-historial.sh` | 1.3 | se conserva | Solo la preparación, si Marta pasa a ser siempre la autora (decisión (e)) |
| 05 | `05-amend.sh` | 1.3 (abre) | se rehace | `--amend -m` corrige un mensaje; `cat-file -p HEAD` y `HEAD@{1}` muestran el mismo padre y árbol con otro hash; `git reflog -2`. Sin el «archivo olvidado» |
| 06 | `06-restore.sh` | 1.3 | se ajusta | `git status -s` antes del primer `restore` (`M `), además del `git status` largo con la pista |
| 07 | `07-rama-es-un-archivo.sh` | 1.4 (abre) | se ajusta | Repite al final los dos `cat` de las ramas: solo cambió `descuentos` |
| 08 | `08-avance-rapido.sh` | 1.4 | se rehace | Sigue al 07: `cat` del archivo de `main`, `git merge descuentos` y otra vez el `cat`. Sin `redondeo` urgente ni `branch -d` |
| 09 | `09-conflicto.sh` | 1.4 | se rehace | Mismo choque de `facturas`, nuevo guion: `def` se fusiona solo y `return` choca; `git status` largo; resolución; `git commit -m` (sin `# Conflicts:`); `cat-file -p HEAD`; `git log --oneline -1 HEAD^2`. Sin abortar y repetir |
| 10 | `10-head-desacoplado.sh` | 1.4 | se conserva | — |
| 11 | `11-rebase.sh` | 1.5 | se conserva | La preparación usa B' (cabecera ya corregida) |
| 12 | `12-misma-foto.sh` | 1.5 | se conserva | — |
| 13 | `13-rebase-interactivo.sh` | 1.5 (abre) | se rehace | Los cuatro commits de «El problema»: lista visible; lista intacta sin cambios de hash; lista del asistente (`fixup` 3, `drop` 4) con A intacto y B' nuevo. Sin «WIP» ni «oops», sin `--autosquash`. Otra `GIT_COMMITTER_DATE` en preparación |
| 14 | `14-rebase-conflicto.sh` | 1.5 | se conserva | — |
| 15 | `15-revert.sh` | 1.5 | se conserva | — |
| 16 | `16-dentro-de-git.sh` | 1.6 | se rehace | Qué escribe un commit: archivos de `.git/objects` y archivo de `main` antes y después de un commit en `tests/` (cuatro objetos nuevos). Sin almacén vacío ni `hash-object -w --stdin` con un texto de prueba |
| 17 | `17-hash-a-mano.py` | 1.6 | se rehace | Hash del blob de `factura.py` de `facturas`, comparado con la entrada del árbol y con `git hash-object factura.py`; zlib sobre su objeto. Puede pasar a `.sh` con preparación oculta y un bloque de Python, para no enseñar el montaje |
| 18 | `18-arbol-y-commit.sh` | 1.6 (abre) | se ajusta | Empieza con `cat .git/HEAD` y `cat .git/refs/heads/main`; acaba con `ls` de la subcarpeta del blob |
| 19 | `19-commit-a-mano.sh` | — | se quita | Es la secuencia de Pro Git 10.2/10.3 (`write-tree`, `commit-tree`, `update-ref`) con cambios cosméticos. Su papel pasa al 16 (objetos y referencia) y al recuadro de `ce4f8a1` (hash reproducible) |
| 20 | `20-etiquetas.sh` | 1.6 | según la decisión (c) | Recomendación: no se inserta. Si devOC lo quiere, se rehace: etiquetas de versiones de `facturas`, centrado en `cat-file -t` de cada una, sin la secuencia de Pro Git 10.3 |
| 21 | `21-reset-tres-modos.sh` | 1.7 (abre) | se rehace | Pasa a ser «lo que hizo el asistente»: `reset --soft HEAD~2` y `commit` sobre `exportar-csv`, con `git status -s` y `git reflog -3`. Sin v1/v2/v3 en secuencia |
| 22 | `22-reset-con-ruta.sh` | 1.7 | se ajusta | Compara `git reset HEAD~2 factura.py` con `git restore --source=HEAD~2 --staged factura.py`; se quita la pareja repetida si sobra |
| 23 | `23-reset-frente-a-switch.sh` | 1.7 | se rehace | `reset --soft HEAD~2` frente a `switch --detach HEAD~2` en `exportar-csv`, leyendo `.git/HEAD` y el archivo de la rama. Sin `develop`/`main` |
| 24 | `24-recuperar-con-reflog.sh` | 1.7 | se rehace | `git reflog exportar-csv` tras la secuencia completa del asistente; rama de rescate en `exportar-csv@{n}` con los cuatro commits originales. Sin `reset --hard HEAD~2`, `rm -rf .git/logs` ni `fsck` |
| 25 | (nuevo) `25-tres-modos-mismo-punto.sh` | 1.7 | nuevo | Los tres modos desde el mismo punto de `exportar-csv`: `exportar.py` preparado, sin rastrear y borrado (`git status -s` y `ls`), con preparación oculta que vuelve al punto de partida |
| 26 | (opcional) `26-pull-divergente.sh` | 1.5 | solo si devOC elige (a3) | Dos clones locales: se reescribe el original y `git pull` en el clon se niega (falla); `git pull --no-rebase` enseña los commits viejos y el nuevo |

**Recuento.** 7 se conservan (02, 04, 10, 11, 12, 14 y 15), 6 se ajustan (01, 03, 06, 07, 18 y 22), 9 se rehacen (05, 08, 09, 13, 16, 17, 21, 23 y 24), 1 se quita (19), 1 queda a la decisión (c) con recomendación de no insertarlo (20) y 1 es nuevo (25), más el 26 opcional. Con la recomendación, el capítulo inserta 23 ejemplos. Los diez ejemplos derivados del hallazgo L-1 quedan rehechos o quitados, así que no hace falta atribuir ningún ejemplo a Pro Git.

**Renumeración.** Cuando estén escritos, el agente mecánico los renumera en orden de aparición (01 a 23) y actualiza las marcas del borrador. Hasta entonces se usan los números de esta tabla.

---

## 6. Correcciones de contenido obligatorias

Cada hallazgo NO SOPORTADA, SIN HECHO o PARCIAL importante de los cuatro tramos, con cómo se resuelve. Los PARCIAL leves que desaparecen solos al reescribir la sección van marcados «desaparece».

### Apertura

| Hallazgo | Resolución |
| --- | --- |
| Objetivo 5 sin ids (SIN HECHO) | Citar h01-542, h01-580, h01-448 y h01-456 |
| `main` «para que tus salidas coincidan» (PARCIAL) | «Para que coincidan los nombres de rama» y aviso de hashes [h01-639, h01-647] |
| El apéndice «Preparar el entorno» no existe | Configuración en línea; remisión al apéndice cuando exista |
| «Su PR ya no se puede fusionar» (SIN HECHO) | Se quita; nueva premisa (decisión (a)) |
| «Commits repetidos» sin ids en «El problema» | Se explican en 1.5 [h01-520, h01-523, h01-524] |

### 1.1

| Hallazgo | Resolución |
| --- | --- |
| «Dónde vive el historial» sin id | h01-110, h01-112, h01-120 |
| «La forma más simple» (superlativo) | Desaparece (no se clasifica lo local); si se usa, «una forma muy sencilla» [h01-105] |
| RCS y parches atribuidos a todas las herramientas locales | Se quita RCS |
| 1991-2002 «casi todo el tiempo» | Desaparece al reducir la historia a una o dos frases |
| «Esa red cubre lo que llegó a confirmarse» [h01-345] | «Solo con lo que tuviera ese clon» [h01-122] más h01-347; h01-345 fuera de 1.1 |
| Literal y paráfrasis de Pro Git 1.1/1.2 (l.47, 86, 88) | Desaparecen con el nuevo orden; se comprueba con `detectar_copia.py` |

### 1.2

| Hallazgo | Resolución |
| --- | --- |
| «Fotografía todos tus archivos» frente a h01-263 | «Fotografía lo que tienes preparado» [h01-203, h01-263] |
| `^{tree}` «detrás de una revisión» | «Detrás de un commit» [h01-829] |
| «Esos nombres de 40 caracteres son hashes» (SIN HECHO) | h01-212, h01-630 |
| «Red de seguridad de la sección 1.1» (dos mecanismos con un nombre) | Se quita el enlace |
| Diagrama de los tres lugares: flecha «cambiar de rama» (SIN HECHO) | «Sacar una versión» [h01-225]; el paso por el índice, en 1.7 [h01-716] |
| `.gitignore`: «no confirmarás nada por accidente» | «Evitarás confirmar por accidente…» [h01-252] |
| Glob «recursivos a todo el repositorio» | «Por defecto, de forma recursiva» [h01-253] |
| `master` en presente y sin atribuir | «Pro Git explica que…» [h01-412, h01-413] |
| `--object-format` como única excepción | «Por defecto SHA-1; con `--object-format=sha256`, si está habilitado, SHA-256» [h01-280] |
| Ejemplo 03 esconde el cambio del IVA | Ejemplo 03 ajustado (`git diff HEAD~1 HEAD`) |
| h01-245 aplicado a otro archivo | h01-246 y h01-250 |
| Literales de f01-03/f01-07 (l.96, l.138) | Desaparecen; el párrafo de las tres secciones se escribe desde el diagrama |

### 1.3

| Hallazgo | Resolución |
| --- | --- |
| Cita literal de 17 palabras sin comillas (1.3-1, h01-328) | Frase propia [h01-327, h01-347] |
| «Cadena que se recorre hacia atrás» | «Grafo que se recorre hacia atrás siguiendo los padres» [h01-302, h01-570, h01-761] |
| Los ejemplos 05 y 06 parten de tres commits sin avisar | Regla 2 de la sección 0 |
| `--amend` conserva el padre (sin hecho) | h01-846, h01-847, h01-848 |
| `M ` → ` M` sin `git status -s` en la salida | Ejemplo 06 ajustado |
| «Exige añadir `--worktree`» | «`--staged` solo restaura el índice» [h01-849] |
| «El antiguo `git checkout --`» | «La forma que enseña Pro Git» [h01-341, h01-479] |
| Equivalencias de `restore` mal emparejadas (error del esquema aprobado) | «Ojo con la versión» reescrito con h01-852 (`checkout -- <archivo>` copia desde el índice), h01-853 y h01-901 |
| Autor/confirmador calca f01-05 (l.300) | Se escribe desde la salida del ejemplo 04 |

### 1.4

| Hallazgo | Resolución |
| --- | --- |
| Conflicto sin «de forma distinta» | Añadirlo [h01-448], con lo que no se solapa [h01-855] y el mismo cambio en los dos lados [h01-856] |
| «Tarde o temprano, el trabajo vuelve a `main`» (SIN HECHO) | Se quita |
| «Depende de la forma del grafo» (SIN HECHO) | h01-434, h01-440 |
| «Pro Git plantea elegir un lado o el otro» (deforma la fuente) | Se describe lo que hace el ejemplo (combina los dos) y que Git no decide por ti [h01-492] |
| `--no-edit` guarda `# Conflicts:` | Ejemplo 09 rehecho con `git commit -m` |
| «La sintaxis solo sirve en commits de fusión» | «`^2` solo tiene sentido en un commit de fusión» y `git log --oneline -1 HEAD^2` |
| «Las demás líneas las verás en 1.6» | Se quita |
| h01-485 generalizado y sin el reflog | Atribuido a su ejemplo y con el reflog [h01-485, h01-779, h01-872] |
| CVS/Subversion en presente (h01-446, h01-447) | Se quita |
| `ort` antes de su primera salida | Se mueve a 1.5 (ejemplo 12) |
| `-D` «aunque pierdas ese trabajo» frente a h01-346 | «Salvo que lo rescates del reflog» |
| `.git/refs/heads` con h01-652 | h01-655 |
| Escenario «arreglo urgente» y orden de Pro Git 3.2 (estructura alta) | Nuevo orden de la sección 4 |

### 1.5

| Hallazgo | Resolución |
| --- | --- |
| **NO SOPORTADA:** «`rebase -i HEAD~4` reescribe todos los commits del rango, cambies algo o no» (h01-543, errata de f01-11) | h01-860 y h01-861 (por defecto avanza sobre los que no cambian) y ejemplo 13 rehecho; h01-543 no se cita. Errata ya anotada en `huecos.md` |
| Mecánica de los archivos temporales (antigua) | Mecánica actual [h01-859, h01-862, h01-863]; la de Pro Git, en «Ojo con la versión» |
| «Por eso» entre misma foto y daño; revert «para deshacer lo publicado» | El daño se atribuye a abandonar commits [h01-520]; revert como «no reescribe», con el razonamiento explícito |
| «Lo que viste con `--amend`, aplicado a una fila» | «No se edita: se sustituye» [h01-763, h01-764] |
| «A quien mantiene le basta con avanzar» | «Un avance rápido o una incorporación limpia» [h01-513] |
| `GIT_SEQUENCE_EDITOR` «dos veces» (eran tres) | Desaparece: el texto describe el ejemplo 13 nuevo |
| `git pull` crea una fusión (falso con Git 2.43 sin configurar) | «Ojo con la versión» con h01-880 a h01-885 |
| `patch-id`: «puede reconocer… siempre que» | «Es posible que…» y «solo si…» [h01-526, h01-527] |
| `exec` también en Pro Git | «Entre otras» |
| `--autosquash` cambia la lista sin comentarlo | Sale del ejemplo; una frase opcional |
| Los cinco pasos con los verbos de f01-10 (l.670); `patch-id` frase a frase (l.935); «Error típico» que sigue «Los peligros de reorganizar» (l.933) | Desaparecen con el nuevo orden: Marta sustituye al «Error típico» calcado |

### 1.6

| Hallazgo | Resolución |
| --- | --- |
| «Cada comando añade objetos…» (falso para `log` o `status`) | «Todo lo que cambia un comando se reduce a…» [h01-768] |
| Diagrama no verificable (hash de HEAD, árbol del padre, etiquetas) | Diagrama limitado a la salida del 18; etiquetas, según (c) |
| `index` «en lo que lista `ls .git`» | Desaparece (no hay `ls .git`); si se nombra, «de lo que hay en `.git`» |
| Dos más 38 sin «en principio» | «En principio» o «cada objeto suelto» |
| `symbolic-ref` «ya» | Desaparece con el 19 |
| Etiqueta «nunca se mueve» | «Generalmente» [h01-675] |
| «Quien la creó» (errata «marcador» en h01-674) | Se apoya en h01-875 (línea `tagger`); la errata ya está en `huecos.md` |
| Dos archivos con el mismo contenido (PARCIAL y SIN HECHO) | Se sustituye por el caso límite del hash reproducible (blobs iguales y commits distintos) |
| SHA-256 «el cálculo es el de tus repositorios» | «Salvo que crees el repositorio con SHA-256» |
| Orden y ejemplos de Pro Git 10.1-10.3 (estructura alta) | Nuevo orden y ejemplos 16, 17 y 18 |

### 1.7

| Hallazgo | Resolución |
| --- | --- |
| **NO SOPORTADA:** «Las entradas del reflog caducan a los 90 días» | 90 días las alcanzables y 30 las inalcanzables [h01-870, h01-871, h01-872] |
| `--hard` «y aun así se recupera» sin plazo | «Se puede recuperar durante un tiempo; la vía más rápida suele ser el reflog» |
| «Y nada más» con h01-721 | h01-722 |
| Con ruta, «aplica el resto» | «Se salta el primer paso y solo actualiza el índice» [h01-734, h01-902] |
| `git reset --mixed HEAD <archivo>` como forma actual (Git 2.43 avisa de que está obsoleta) | Solo en «Ojo con la versión», atribuida a Pro Git |
| «Alternativa al `fixup`» (SIN HECHO) | «Otra forma de aplastar commits» [h01-874], con el ejemplo de la documentación (`--soft HEAD~5; git commit`) [h01-892] |
| `checkout` comprueba… (solo sin ruta) | «`git checkout <rama>` comprueba…» |
| Fila `checkout [<commit>] <archivo>` y frase de `checkout` con ruta (solo con commit) | Tabla nueva sin `checkout` |
| «El caso típico» | Desaparece (el rescate es el del asistente) |
| `fsck` lista solo el último commit perdido | Sale del ejemplo; una frase sin ese detalle |
| «En el ejemplo 21 el redondeo… el reflog lo recuerda» (salida que no lo enseña) | Ejemplo 21 rehecho con `git reflog -3` |
| La última fila de la tabla «hoy es `restore --source --staged --worktree`» | Desaparece con la tabla nueva |
| «`rebase -i HEAD~4` creó commits nuevos» (SIN HECHO) | h01-764 y h01-860 («desde el primero que cambia») |
| «Ningún commit se borró» | «En tu repositorio…, durante 30 días» |
| Tabla con filas y columnas de Pro Git 7.7 (L-2) | Tabla propia (sección 4.1) |

### Cierre

| Hallazgo | Resolución |
| --- | --- |
| Proyecto, paso 2: «tres formas de integrar» (SIN HECHO) | Con las herramientas del capítulo solo se reconoce el commit de fusión (dos `parent`); si no lo hay, se anota «no concluyente» y se resuelve en el capítulo 2 |
| Proyecto, paso 5: `--stat` sobre el merge no da estadística | «En los commits del PR», no en el de fusión [h01-308, h01-309, h01-877] |
| Proyecto: clonar desde una URL es del capítulo 2 | «El mismo `git clone` de 1.1, con la URL; los remotos se explican en el capítulo 2» |
| Proyecto, paso 3 | `git switch -c arqueologia/pr-NNN <base>` [h01-473] |
| Resumen: «`reset` mueve la rama» y «solo los que no confirmaste» | «Sin ruta, `reset` mueve la rama»; lo confirmado se recupera durante un tiempo |
| **NO SOPORTADA:** ejercicio 3, «sin mover la rama… explica por qué no usas `reset`» (premisa falsa) | Nuevo enunciado: recupera el `factura.py` anterior de dos formas, con `git restore --source` y con `git reset <commit> <archivo>`; confírmalo y explica qué toca cada camino y por qué ninguno mueve la rama. Las soluciones dicen cómo montar `facturas` (o admiten cualquier repositorio) |
| Ejercicio 4: tres commits «WIP»; volver al punto de partida | «Tres commits pequeños»; crear antes una rama de respaldo |
| Ejercicio 5: `rebase -i` descarta por defecto los commits de fusión | Pista en el enunciado: limpia la rama antes de fusionarla [h01-866] |
| Defensa 2: «¿qué verá al traer los cambios?» | «¿Qué le dirá Git al intentar traerla y qué verá si fuerza la fusión?» [h01-591, h01-881, h01-883, h01-523, h01-524] |
| Defensa 3: «cambian los hashes de todos los posteriores» | «¿Qué hashes cambian y cuáles no?» [h01-860, h01-570, h01-571] |
| Defensa 5 | Se añade «durante cuánto tiempo» |
| Defensa 6 (SIN HECHO) | Ids h01-594, h01-535, h01-764, h01-591, y enunciado «un commit defectuoso ya está en una rama que usa todo el equipo» |

---

## 7. El proyecto avanza, resumen, ejercicios y preguntas

Se mantiene la estructura del borrador con las correcciones de la sección 6. Resumen de cinco líneas: instantáneas nombradas por su contenido; grafo de commits inmutables; ramas y `HEAD` como referencias que se mueven; reescribir crea commits desde el primero que cambia, y no se hace con lo que otros tienen; sin ruta, `reset` mueve la rama y solo `--hard` destruye lo no confirmado, mientras que lo confirmado dura un tiempo en el reflog.

---

## 8. Extensión

Recuento de `informe_capitulo.py` (sin ids, sin código ni diagramas). Techo: 9.600.

| Parte | Borrador actual (aprox.) | v2 |
| --- | --- | --- |
| Objetivos, «Lo que necesitas antes» y «El problema» | 440 | 450 |
| 1.1 | 610 | 450 |
| 1.2 | 1.350 | 1.200 |
| 1.3 | 1.320 | 1.150 |
| 1.4 | 1.930 | 1.500 |
| 1.5 | 1.230 | 1.400 |
| 1.6 | 1.120 | 1.150 |
| 1.7 (con el cierre de «El problema») | 1.220 | 1.400 |
| Proyecto, resumen, ejercicios y preguntas | 710 | 700 |
| **Total** | **9.930 (9.563 según el informe)** | **9.400** |

El margen es de unas 200 palabras. Si se pasa, se recorta por este orden: la frase de las dos visiones del historial (1.5), la de `--autosquash` (1.5), el «Ojo con la versión» de la mecánica del rebase fundido con el de `pull` (1.5) y `--no-ff` (1.4). Insertar el ejemplo 20 (decisión (c)) costaría unas 200 palabras, que saldrían de esa lista.

---

## 9. Hechos nuevos que necesita este esquema

**Tanda h01-846 a h01-903 (ya en `hechos.md`).** Cubre los ocho temas previstos y casi todo lo que este esquema necesitaba. Por tema:

| Tema | Ids |
| --- | --- |
| `--amend` | h01-846 a h01-848 |
| `restore --staged` | h01-849 a h01-851 |
| `checkout -- <archivo>` | h01-852 a h01-854 |
| Fusión sin solape | h01-855 a h01-858 |
| Rebase actual | h01-859 a h01-867 |
| Reflog | h01-868 a h01-873 |
| `pull` | h01-880 a h01-887 |
| `reset` | h01-888 a h01-903 |
| Además | `tagger` (h01-875), «otra forma de aplastar» (h01-874) y los commits de fusión en `git log` (h01-876 a h01-879) |

**Lo que todavía falta** (fuentes ya autorizadas). Se piden al investigador antes de redactar 1.5 y 1.7:

| Hecho | Fuente | Para |
| --- | --- | --- |
| `<refname>@{<n>}` designa la posición n de esa referencia en su reflog (p. ej. `master@{1}`) | f01-29, hacia la l.104 | Ejemplo 24 y «Bajo el capó» de 1.7 |
| El *backend* `merge` se llamaba antes «interactive» y hoy se usa también en rebases no interactivos | f01-23, l.508-514 | Explicar «interactive rebase in progress» del ejemplo 14 |
| `git reset --hard` y `git restore --source` descartan los cambios sin confirmar del directorio de trabajo | f01-24, l.21-25 | Tabla de 1.7, columna «¿Pisa cambios?» de `restore` |

El aviso de Git 2.43 «--mixed with paths is deprecated» no aparece en f01-35; si se quiere contar, haría falta otra fuente o dejarlo fuera (es lo que propone este esquema).

**PENDIENTES previstos.** Solo el de «En un proyecto real» (decisión 8 del esquema aprobado). Si alguno de los tres hechos no se puede extraer, la frase se escribe como `> PENDIENTE` y no se afirma.

---

## 10. Decisiones para devOC

### Qué cambia respecto al esquema aprobado

- Nuevo orden interno de las siete secciones. Los títulos y el orden de las secciones del catálogo no cambian.
- Nueva premisa de «El problema».
- 9 ejemplos rehechos, el 19 fuera, el 25 nuevo y el 20 pendiente de (c).
- `_facturas.sh` con los commits de «El problema» y con Marta como autora fija.
- Tabla propia en 1.7.
- `ort` pasa de 1.4 a 1.5.
- `--autosquash` y `fsck` salen de los ejemplos.
- Extensión objetivo: 9.400.

### (a) «El problema» y `git pull`

Pro Git cuenta que, tras el push forzado, `git pull` de la compañera crea una fusión con commits repetidos. Con Git 2.43 sin configurar, `git pull` se niega («You have divergent branches»), y la fusión solo llega si la fuerza.

- **(a1)** Mantener la historia de Pro Git: «al traer tus cambios ve tus commits repetidos», con un «Ojo con la versión» que diga que hoy Git se niega. El síntoma central de «El problema» no lo vería el lector con su versión.
- **(a2)** Ajustarla a Git 2.43 (texto de la sección 3): «Git se niega a seguir; cuando le obliga a fusionar, ve tus commits viejos junto al nuevo». Sin ejemplo en este capítulo. Lo respaldan los hechos de f01-34 y Pro Git en 1.5, y la demostración ejecutada se pide para el capítulo 2 (2.5, «Mantener el PR al día…»), donde ya hay remotos.
- **(a3)** Como (a2), más el ejemplo opcional 26 con dos clones locales (sin `push`). Enseña el mensaje real, pero adelanta `origin/main` y el concepto de remoto del capítulo 2.

**Recomiendo (a2).**

### (b) El hash calculado a mano en Python

La idea (SHA-1 de «tipo, tamaño, byte nulo y contenido») es estándar y está en la documentación oficial de Git (h01-294, f01-18), no solo en Pro Git 10.2. El ejemplo rehecho calcula el hash de un archivo real de `facturas`, lo compara con la entrada del árbol y no reproduce la demostración en Ruby con un texto de prueba.

**Recomiendo mantenerlo** con el respaldo principal en h01-294. Opcionalmente, una línea en «Para profundizar» puede decir que Pro Git 10.2 hace el mismo cálculo en Ruby.

### (c) Las etiquetas

- **Opción 1.** No se inserta el ejemplo 20. Las etiquetas van en dos frases (cuarto tipo de objeto, ligera frente a anotada) [h01-673, h01-675, h01-677, h01-679, h01-680] y salen del diagrama de 1.6.
- **Opción 2.** Se inserta un ejemplo 20 rehecho (unas 200 palabras más, que salen de la lista de recortes).

**Recomiendo la opción 1.** Las etiquetas no están en los objetivos del catálogo, y el capítulo 2 las necesitará menos que los remotos.

### (d) Quitar el ejemplo 19 (commit construido a mano)

Era la demostración de Pro Git 10.2/10.3 con cambios cosméticos. El ejemplo 16 rehecho (qué escribe un commit) y el recuadro de `ce4f8a1` cubren sus dos papeles con material propio.

**Recomiendo quitarlo.**

### (e) Marta, autora fija del commit de tests

Une la compañera de «El problema» con la autora de 1.3 y elimina el párrafo sobre los dos hashes del mismo commit. Cambian todos los hashes citados desde el cuarto commit, pero la prosa se reescribe de todos modos.

**Recomiendo aceptarlo.**

---

## Decisiones aplicadas (2026-11-12)

devOC pidió terminar la corrección sin más rondas de aprobación ni de revisión y recibir el capítulo para revisarlo él. Se aplican las recomendaciones de este esquema, que devOC puede cambiar al leer el capítulo:

- (a) **a2:** «El problema» se ajusta al comportamiento de Git 2.43, sin ejemplo con remotos y con «Ojo con la versión» en 1.5.
- (b) Se mantiene el hash calculado en Python, con un blob de `facturas`.
- (c) No se inserta el ejemplo 20; las etiquetas se cuentan en dos frases y no se dibujan.
- (d) Se quita el ejemplo 19.
- (e) Marta Ruiz es la autora fija del commit de tests.

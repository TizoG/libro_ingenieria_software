# Esquema del capítulo 1: Git por dentro

Propuesta de la fase 3 para que devOC la apruebe. No es texto del libro: las frases de este archivo son guías para el redactor y el programador. Los ids remiten a `investigacion/cap-01/hechos.md` (568 hechos verificados). Lo que no tiene hecho va marcado como PENDIENTE previsto.

---

## 1. Cabecera YAML propuesta para el borrador

```yaml
---
id: base/git-modelo
parte: 1
capitulo: 1
titulo: Git por dentro
estado: borrador
actualizado: 2026-11-12
palabras: 0
versiones:
  git: "2.43"
  python: "3.13"
---
```

`python` solo hace falta si se mantiene el ejemplo `17-hash-a-mano.py` (sección 1.6). `palabras` lo rellena `scripts/informe_capitulo.py`.

---

## 2. Lo que podrás hacer al terminar

1. Explicar qué guarda un commit (una instantánea completa, sus padres y sus metadatos) y por qué cambiar un commit antiguo cambia el hash de todos los que vienen después.
2. Dibujar el grafo de commits, ramas y HEAD antes y después de un commit, un merge (avance rápido y a tres bandas), un rebase y un reset, y comprobar el dibujo con `git log --graph` y con los archivos de `.git`.
3. Elegir entre merge, rebase y revert según si el historial ya está publicado, y justificar la elección.
4. Predecir qué hacen `git reset --soft`, `--mixed` y `--hard` sobre HEAD, el índice y el directorio de trabajo, y recuperar con el reflog un commit que parecía perdido.
5. Construir sin ayuda un repositorio con tres ramas, provocar y resolver un conflicto y limpiar el historial con rebase interactivo.

## 3. Lo que necesitas antes

- Capítulos previos: ninguno (ficha del catálogo).
- Git 2.43 o posterior instalado y una terminal en la que sepas moverte entre carpetas (el capítulo 3 profundiza en la terminal).
- Nombre y correo configurados, porque Git los escribe en cada commit [h01-639]. Y, para que tus ejemplos coincidan con los del libro, la rama inicial llamada `main` con `init.defaultBranch` [h01-279]. Se remite al apéndice «Preparar el entorno».

## 4. El problema

Le pides a un asistente de IA que deje bonito el historial de tu rama antes de abrir un PR. Te devuelve tres comandos: un `git rebase -i HEAD~4`, un `git reset --soft HEAD~2` y un `git push --force`. Los ejecutas y todo parece en orden. Al día siguiente, una compañera que había partido de tu rama te escribe: sus commits aparecen duplicados y el PR no se puede fusionar. ¿Qué hizo exactamente cada comando, dónde están ahora tus commits «antiguos» y cómo lo explicas en la revisión? Este capítulo construye el modelo que responde a esas tres preguntas.

---

## 5. Hilo narrativo: el repositorio `facturas`

Un repositorio pequeño, `facturas`, con un programa en Python que calcula el total de una factura con IVA (encaja con un desarrollador que empieza como freelance). Archivos: `README.md`, `factura.py`, `tests/test_factura.py` (para tener un subárbol en 1.6) y `.gitignore`. Contenido mínimo, para que las salidas sean cortas.

Cada ejemplo se ejecuta en una carpeta temporal limpia (así funciona `scripts/insertar_ejemplos.py`), de modo que cada script reconstruye el estado que necesita. La continuidad es narrativa: el lector sigue el mismo repositorio de sección en sección.

| Sección | Qué le pasa a `facturas` | Ramas y referencias al terminar | Ejemplos |
| --- | --- | --- | --- |
| 1.1 | Sustituye a una carpeta con copias `facturas_v2_final_DEFINITIVO`. Nace con un commit y se clona en `copia/` para ver que el clon trae todo el historial | `main` | 01 |
| 1.2 | Entran `factura.py`, `README.md` y `.gitignore`; se ven los tres estados y un archivo a la vez preparado y modificado. Un segundo commit toca solo `factura.py` | `main` | 02, 03 |
| 1.3 | Crece hasta cinco commits (cambio del tipo de IVA, tests). Se busca con `git log -S` cuándo cambió el IVA; un commit que olvidó un archivo se arregla con `--amend`; un cambio se descarta con `git restore` | `main` | 04, 05, 06 |
| 1.4 | Aparecen `redondeo` (arreglo urgente, avance rápido) y `descuentos` (funcionalidad que choca con `main` en la función `total()`). Conflicto, resolución y commit de fusión con dos padres. Un experimento en HEAD desacoplado se pierde y se rescata | `main`, `descuentos`, `experimento` | 07, 08, 09, 10 |
| 1.5 | La rama `exportar-csv` acumula commits «WIP» y «oops». Se compara merge con rebase, se reorganiza sobre `main`, se limpia con rebase interactivo y se deshace con `git revert` un commit ya publicado | `main`, `exportar-csv` | 11 a 15 |
| 1.6 | Se abre `.git`: los objetos del último commit, el árbol con el subárbol `tests/`, un commit construido a mano con comandos de fontanería y las etiquetas `v0.1` (ligera) y `v1.0` (anotada) | `main`, `v0.1`, `v1.0` | 16 a 20 |
| 1.7 | Se aplican los tres modos de reset, se compara reset con cambiar de rama, se «pierde» un commit con `--hard` y se recupera con el reflog | `main`, `recuperada` | 21 a 24 |

---

## 6. Las secciones

Convención para los diagramas: `flowchart` de Mermaid, con los commits como nodos redondos y las referencias (ramas, HEAD, etiquetas) como nodos rectangulares que apuntan a ellos. Se descarta `gitGraph` porque no puede dibujar HEAD apuntando a una rama, que es justo la idea del capítulo.

### 1.1 Qué es el control de versiones

**Idea en dos frases.** Un control de versiones registra los cambios de un conjunto de archivos para que puedas volver a cualquier versión anterior. Git es distribuido: cada clon es una copia completa del historial, y eso explica que casi todo funcione sin red.

**Modelo mental.** Tres generaciones: copiar carpetas, un servidor central del que todos dependen y repositorios completos en cada máquina.

- Diagrama `flowchart TB` con dos subgrafos. «Centralizado»: nodo `Servidor (historial)` y nodos `Cliente A`, `Cliente B` que solo tienen la copia de trabajo, con flechas hacia el servidor. «Distribuido»: `Servidor (repo completo)`, `A (repo completo)`, `B (repo completo)` con flechas en ambos sentidos.

**Ejemplos.**

- `ejemplos/cap-01/01-clon-completo.sh`: crea `facturas` con un commit, lo clona con una ruta local en `copia/` y ejecuta `git log --oneline` dentro del clon. La salida debe mostrar el mismo hash de commit en el original y en la copia.

**Por qué funciona así.**

- Qué resuelve un VCS: h01-101, h01-102, h01-103, h01-104.
- Copiar carpetas y sus fallos: h01-105, h01-106, h01-107.
- Local, centralizado y distribuido: h01-108, h01-109, h01-112, h01-116, h01-117, h01-118, h01-119, h01-120, h01-121.
- Origen de Git y sus objetivos de diseño (velocidad, ramas paralelas, distribuido, proyectos grandes, diseño sencillo), que reaparecen en el resto del capítulo: h01-126, h01-127, h01-128, h01-129, h01-130, h01-131, h01-132, h01-133.
- Consecuencia práctica: trabajo local e inmediato: h01-206, h01-207, h01-208, h01-223.

**Caso límite.** El servidor se corrompe sin copias de seguridad. En un sistema centralizado se pierde el historial [h01-118]; en Git, cualquier clon sirve para restaurarlo [h01-122]. Lo que nadie llegó a confirmar no está en ningún clon [h01-347].

**Recuadros.** Ninguno. La sección es corta y de contexto.

**PENDIENTES previstos.** Ninguno.

**Palabras estimadas.** 500.

---

### 1.2 Fotos, no diferencias; los tres estados

**Idea en dos frases.** Cada commit guarda una instantánea completa del proyecto, nombrada por un hash de su contenido; lo que no cambia no se vuelve a guardar, se enlaza. Entre tus archivos y esa instantánea hay una zona intermedia, el área de preparación, y cada archivo está en uno de tres estados respecto a ellas.

**Modelo mental.** Tres lugares (directorio de trabajo, área de preparación, directorio `.git`) y dos verbos que mueven contenido entre ellos (`add`, `commit`).

- Diagrama 1, `flowchart LR`: `Directorio de trabajo` →(git add)→ `Área de preparación (índice)` →(git commit)→ `Directorio .git`; y `Directorio .git` →(cambiar de rama)→ `Directorio de trabajo`.
- Diagrama 2, `stateDiagram-v2` del ciclo de un archivo: `SinRastrear` →(git add)→ `Preparado` →(git commit)→ `SinModificar` →(editar)→ `Modificado` →(git add)→ `Preparado`.
- Diagrama 3, `flowchart LR` de instantáneas: commits C1, C2 y C3; en cada uno, `factura.py` apunta a una versión distinta y `README.md` apunta siempre al mismo nodo (enlace, no copia).

**Ejemplos.**

- `ejemplos/cap-01/02-tres-estados.sh`: `git init`, crea `README.md` y `factura.py`, y alterna `git status -s`, `git add`, `git commit`, una edición, otro `git add` y otra edición; termina con `git diff` y `git diff --staged`. La salida debe mostrar `??`, `A`, ` M` y, al final, `MM` en `factura.py`, y dos diffs distintos.
- `ejemplos/cap-01/03-fotos-no-diferencias.sh`: dos commits en los que solo cambia `factura.py`; `git cat-file -p` sobre el árbol de cada commit (`HEAD^{tree}` y `HEAD~1^{tree}`). La salida debe mostrar el mismo hash de blob para `README.md` en los dos árboles y hashes distintos para `factura.py`. Adelanta la sección 1.6.

**Por qué funciona así.**

- Instantáneas frente a listas de cambios: h01-201, h01-202, h01-203, h01-204, h01-205, h01-401.
- Todo se nombra por su hash y se verifica: h01-209, h01-210, h01-211, h01-212, h01-213, h01-214, h01-284, h01-286.
- Casi todo añade datos; lo confirmado es difícil de perder: h01-215, h01-216.
- Tres estados y tres secciones: h01-217, h01-218, h01-219, h01-220, h01-221, h01-222, h01-224, h01-226, h01-227, h01-228, h01-229.
- Rastreados y sin rastrear; `git status`: h01-233, h01-234, h01-235, h01-238, h01-240, h01-241, h01-242.
- Las dos columnas de `git status -s`: h01-248, h01-249, h01-250.
- `git diff` frente a `git diff --staged`: h01-255, h01-256, h01-257, h01-259, h01-260.
- El commit guarda el área de preparación, no el disco: h01-262, h01-263, h01-265.
- `git init`: h01-275, h01-276.

**Caso límite.** Editas un archivo después de `git add`: queda a la vez preparado y modificado, porque `add` copió el contenido de ese momento; si confirmas sin volver a añadirlo, el commit lleva la versión vieja [h01-245, h01-246, h01-247, h01-263].

**Recuadros.**

- **Ojo con la versión.** Pro Git en español da `master` como rama por defecto [h01-410]; la documentación actual dice que hoy sigue siendo `master`, que pasará a `main` con Git 3.0 y que se cambia con `init.defaultBranch` o con `git init -b` [h01-277, h01-278, h01-279]. La rama principal no tiene nada especial [h01-412, h01-413]. Los ejemplos del libro usan `main`.
- **Error típico.** Confirmar archivos generados (trazas, compilados, cachés). Se evita con un `.gitignore` creado al empezar: patrones glob recursivos y negación con `!` [h01-251, h01-252, h01-253, h01-254].
- **Bajo el capó.** Git no guarda que renombraste un archivo: lo deduce comparando instantáneas, y por eso da igual cómo lo renombres [h01-269, h01-270, h01-274]. Es una consecuencia directa de guardar fotos y no cambios.

**PENDIENTES previstos.** Ninguno.

**Palabras estimadas.** 1.300.

---

### 1.3 Leer y deshacer el historial

**Idea en dos frases.** `git log` es una consulta sobre el grafo de commits: puedes filtrar por autor, por texto añadido o quitado y por archivo, y elegir un formato estable para scripts. Deshacer en Git casi siempre significa crear algo nuevo (un commit que sustituye a otro) o copiar contenido de un sitio a otro, y solo pierdes lo que nunca confirmaste.

**Modelo mental.** El historial es una cadena de commits que solo crece; `--amend` no edita el último commit, crea uno nuevo con el mismo padre y mueve la rama.

- Diagrama `flowchart RL`: C1 ← C2 ← C3 (nodo con borde discontinuo, «sustituido») y C2 ← C3' ; `main` → C3'.

**Ejemplos.**

- `ejemplos/cap-01/04-leer-historial.sh`: crea cinco commits pequeños (uno de ellos con otro autor, sobrescribiendo el nombre del autor solo para ese commit); ejecuta `git log --oneline`, `git log --stat -1`, `git log -S "0.21" --oneline`, `git log --oneline -- README.md` y `git log --format=fuller -1` sobre el commit del otro autor. La salida debe mostrar el commit que introdujo el tipo de IVA, solo los commits que tocaron `README.md`, y un autor distinto del confirmador.
- `ejemplos/cap-01/05-amend.sh`: confirma olvidando `tests/test_factura.py`, muestra el hash, prepara el archivo y ejecuta `git commit --amend --no-edit`; después `git log --oneline` y `git reflog`. La salida debe mostrar un hash nuevo, un único commit en `log` y el commit sustituido todavía visible en el reflog. (Nota para el programador: como la fecha es fija, el amend debe cambiar el contenido o el mensaje; si no, el hash sería el mismo.)
- `ejemplos/cap-01/06-restore.sh`: modifica y prepara `factura.py`; `git status` completo; `git restore --staged factura.py`; `git status -s`; `git restore factura.py`; `git status -s`. La salida debe mostrar la sugerencia que da Git 2.43 en `git status`, el paso de `M ` a ` M` y un directorio limpio al final.

**Por qué funciona así.**

- Qué muestra `git log`: h01-301, h01-302, h01-303, h01-306, h01-308, h01-309, h01-310, h01-314.
- Filtrar: h01-321, h01-322, h01-324, h01-325, h01-326.
- Autor frente a confirmador: h01-311, h01-316, h01-317, h01-318.
- Formato propio y estable para scripts: h01-312, h01-313.
- Deshacer puede perder trabajo: h01-327, h01-328.
- `--amend`: h01-329, h01-330, h01-331, h01-332, h01-334, h01-539.
- `git restore` y de dónde copia: h01-352, h01-354, h01-356, h01-357, h01-358, h01-360.
- Lo confirmado se recupera; lo no confirmado, no: h01-345, h01-346, h01-347.

**Caso límite.** ¿Dónde está el commit que sustituiste con `--amend`? No ha desaparecido: ninguna rama lo alcanza, pero sigue recuperable [h01-346, h01-539]. Se deja la pregunta abierta hasta el reflog de la sección 1.7.

**Recuadros.**

- **Ojo con la versión.** Pro Git en español usa `git reset HEAD <archivo>` para sacar del área de preparación y `git checkout -- <archivo>` para descartar cambios [h01-336, h01-340]; la documentación actual ofrece `git restore --staged` y `git restore`, y dice que equivalen a esos usos de `reset` y `checkout` [h01-354, h01-357, h01-361, h01-362]. El `git status` de Git 2.43 que se ve en el ejemplo 06 ya sugiere la forma nueva.
- **Error típico.** Descartar con `git restore <archivo>` (o con el antiguo `git checkout --`) cambios que querías: el archivo se sobrescribe y, si nunca se confirmó, no vuelve [h01-341, h01-342, h01-343, h01-347].

**PENDIENTES previstos.**

- Opcional: falta hecho sobre en qué versión de Git aparecieron `git restore` y `git switch` y cambió el mensaje de `git status`. Sin él, el recuadro no da números de versión: se limita a comparar Pro Git con la documentación actual y con la salida real.

**Palabras estimadas.** 1.100.

---

### 1.4 Las ramas son punteros

**Idea en dos frases.** Una rama es un archivo con el hash de un commit, y HEAD es otro archivo que dice en qué rama estás; hacer un commit crea un objeto nuevo y adelanta la rama a la que apunta HEAD. Fusionar es mover un puntero hacia delante (avance rápido) o crear un commit con dos padres a partir del ancestro común (fusión a tres bandas); el conflicto aparece cuando los dos lados tocan la misma zona.

**Modelo mental.** Commits inmóviles enlazados con sus padres; etiquetas móviles (ramas) pegadas a ellos; HEAD apuntando a una etiqueta.

- Diagrama 1, `flowchart RL`: C1 ← C2 ← C3; `main` → C3; `descuentos` → C3; `HEAD` → `main`. Variante tras un commit en `descuentos`: `descuentos` → C4, `HEAD` → `descuentos`, `main` sigue en C3.
- Diagrama 2, avance rápido: antes `main` → C3 y `redondeo` → C4 (hijo de C3); después `main` → C4.
- Diagrama 3, fusión a tres bandas: ancestro común C3, puntas C5 (`main`) y C6 (`descuentos`), commit de fusión C7 con dos flechas de padre.
- Diagrama 4, HEAD desacoplado: `HEAD` → C2 directamente (sin rama) y un commit E colgando de C2 que solo HEAD alcanza.

**Ejemplos.**

- `ejemplos/cap-01/07-rama-es-un-archivo.sh`: `git branch descuentos`; `cat .git/refs/heads/main` y `cat .git/refs/heads/descuentos`; `cat .git/HEAD`; `git switch descuentos`; `cat .git/HEAD`; un commit; `git log --oneline --decorate --graph --all`. La salida debe mostrar el mismo hash en los dos archivos de rama, `ref: refs/heads/main` y luego `ref: refs/heads/descuentos`, y `descuentos` un commit por delante de `main`.
- `ejemplos/cap-01/08-avance-rapido.sh`: crea `redondeo` con `git switch -c`, confirma, vuelve a `main` y ejecuta `git merge redondeo`, `git branch -d redondeo` y `git log --oneline --graph`. La salida debe mostrar «Fast-forward» y un historial lineal.
- `ejemplos/cap-01/09-conflicto.sh` (**falla** en dos grupos): `main` y `descuentos` cambian la misma línea de `total()`. `git merge descuentos` (falla), `git status`, `git merge --abort`, `git status -s` (limpio); de nuevo `git merge descuentos` (falla), `cat factura.py` con los marcadores, resolución escribiendo el archivo, `git add`, `git commit --no-edit`, `git log --oneline --graph` y `git cat-file -p HEAD`. La salida debe mostrar `CONFLICT (content)`, «Automatic merge failed», «You have unmerged paths», los marcadores `<<<<<<<`, `=======` y `>>>>>>>`, y un commit con dos líneas `parent`.
- `ejemplos/cap-01/10-head-desacoplado.sh`: `git switch --detach HEAD~1`; `cat .git/HEAD` (un hash, no una ref); un commit «experimento»; `git switch main`; `git log --oneline --all` (no aparece); `git reflog -4`; `git branch experimento HEAD@{1}`; `git log --oneline --all`. La salida debe mostrar que el experimento desaparece del log y vuelve tras crear la rama.

**Por qué funciona así.**

- Qué contiene un commit (adelanto de 1.6): h01-402, h01-403, h01-404, h01-405, h01-406, h01-407.
- La rama es un puntero móvil y barato: h01-409, h01-411, h01-412, h01-414, h01-415, h01-417, h01-424, h01-425, h01-426, h01-659.
- HEAD y cambiar de rama: h01-416, h01-470, h01-419, h01-420, h01-421, h01-422, h01-432, h01-664, h01-666, h01-471, h01-472, h01-473.
- Avance rápido: h01-433, h01-434, h01-435, h01-436, h01-437, h01-497, h01-498, h01-499.
- Fusión a tres bandas: h01-427, h01-440, h01-441, h01-442, h01-443, h01-445, h01-446.
- Conflictos: h01-448, h01-449, h01-450, h01-452, h01-453, h01-454, h01-492, h01-493, h01-494, h01-455, h01-456, h01-457, h01-460.
- Abortar una fusión: h01-488, h01-489, h01-490, h01-491.
- Borrar ramas: h01-465, h01-467, h01-468, h01-469.

**Caso límite.** HEAD desacoplado: apuntas HEAD a un commit y no a una rama; lo que confirmes ahí solo lo alcanza HEAD y, cuando te vas, nada lo referencia y la recolección de basura acabará borrándolo salvo que le pongas nombre [h01-474, h01-475, h01-480, h01-481, h01-482, h01-483, h01-484, h01-485, h01-486, h01-487].

**Recuadros.**

- **Ojo con la versión.** Pro Git en español cambia de rama con `git checkout` y crea y cambia con `git checkout -b` [h01-418, h01-428, h01-429]; la documentación actual tiene `git switch` y `git switch -c` [h01-471, h01-473], y explica que `checkout` mezcla dos trabajos: cambiar de rama y restaurar archivos [h01-479]. El libro usa `switch` y `restore`.
- **Error típico.** Cambiar de rama con cambios sin confirmar o borrar con `-D` una rama sin fusionar. Git protege lo primero y avisa de lo segundo, pero `-D` pasa por encima [h01-430, h01-431, h01-476, h01-468, h01-469].
- **Bajo el capó.** El estilo de conflicto `diff3` o `zdiff3` añade entre los marcadores el texto del ancestro común, que es justo la tercera banda de la fusión [h01-495, h01-496, h01-442].

**PENDIENTES previstos.**

- Falta hecho sobre la estrategia de fusión `ort`. La salida de Git 2.43 dirá «Merge made by the 'ort' strategy.» y Pro Git en español muestra otra estrategia. Si el redactor quiere comentarlo, PENDIENTE; si no, no se menciona.

**Palabras estimadas.** 1.500.

---

### 1.5 Rebase y reescribir historia

**Idea en dos frases.** Rebase no mueve commits: copia los cambios de cada uno encima de otra base y crea commits nuevos con hashes nuevos, de modo que la foto final coincide con la de un merge y lo que cambia es el historial. Por eso es seguro con trabajo que solo tú tienes y dañino con trabajo que otros ya han descargado; para deshacer algo publicado está `git revert`.

**Modelo mental.** Reescribir es crear commits nuevos y mover la rama hacia ellos; los antiguos siguen existiendo hasta que nadie los referencia.

- Diagrama 1, `flowchart RL` antes y después: antes C1 ← C2 ← C3 (`main`) y C2 ← C4 (`exportar-csv`); después C3 ← C4' (`exportar-csv`) y C4 con borde discontinuo, sin referencia.
- Diagrama 2, dos subgrafos lado a lado, «con merge» (C3 y C4 unidos en un commit de fusión) y «con rebase» (C1 ← C2 ← C3 ← C4'), con una nota común: «misma instantánea final».

**Ejemplos.**

- `ejemplos/cap-01/11-rebase.sh`: `exportar-csv` con dos commits y `main` con uno nuevo; `git log --oneline --graph --all`; `git rebase main`; de nuevo el log; `git switch main`; `git merge exportar-csv`. La salida debe mostrar que los dos commits de la rama tienen hashes nuevos, que el historial queda lineal y que el merge final es un avance rápido.
- `ejemplos/cap-01/12-misma-foto.sh`: desde el mismo punto divergente crea `con-merge` (merge) y `con-rebase` (rebase); `git diff con-merge con-rebase` y `git log --oneline --graph` de cada una. La salida debe mostrar un diff vacío y dos historiales distintos.
- `ejemplos/cap-01/13-rebase-interactivo.sh`: cuatro commits en `exportar-csv` («Añade exportación a CSV», «WIP», «oops, falta la cabecera», «Prueba descartada»), uno de ellos creado con `git commit --fixup`. Muestra la lista de tareas que genera `git rebase -i HEAD~4`, la ejecuta sin intervención (fundir con `fixup`, descartar con `drop`) y repite la limpieza con `--autosquash`. La salida debe mostrar la lista de tareas de Git 2.43 en orden inverso al de `git log`, y el log antes y después con un solo commit limpio.
- `ejemplos/cap-01/14-rebase-conflicto.sh` (**falla** en un grupo): `exportar-csv` y `main` tocan la misma línea; `git rebase main` (falla); `git status`; `git rebase --abort`; `git log --oneline --graph --all`. La salida debe mostrar el conflicto, el estado de rebase en curso y la rama con exactamente los mismos hashes que antes.
- `ejemplos/cap-01/15-revert.sh`: en `main`, `git revert --no-edit` de un commit anterior; `git log --oneline` y `git show --stat HEAD`. La salida debe mostrar un commit nuevo que deshace el anterior sin borrar ninguno.

**Por qué funciona así.**

- Dos formas de integrar: h01-501, h01-502, h01-503, h01-514, h01-515.
- La mecánica del rebase: h01-504, h01-505, h01-506, h01-507, h01-508, h01-509.
- Misma foto, otro historial: h01-510, h01-511.
- Reescribir crea commits nuevos y cambia todos los hashes posteriores: h01-520, h01-570, h01-571, h01-763, h01-764.
- Cuándo sí y cuándo no: h01-512, h01-513, h01-519, h01-529, h01-535, h01-591, h01-592.
- Dos maneras de ver el historial (registro fiel frente a relato para el lector): h01-531, h01-532, h01-533, h01-534.
- Rebase interactivo: h01-540, h01-542, h01-543, h01-546, h01-547, h01-548, h01-549, h01-550, h01-551, h01-552, h01-553, h01-559, h01-560, h01-580, h01-581, h01-582.
- `--autosquash` y `git commit --fixup`: h01-587, h01-588, h01-589, h01-590.
- Comprobar cada paso con `exec`: h01-583, h01-584, h01-586.
- Conflictos durante el rebase: h01-574, h01-575, h01-576.
- `git revert`: h01-594, h01-595.

**Caso límite.** Un conflicto a mitad de rebase. Puedes resolver y continuar, saltarte ese commit o abortar; `--abort` deja la rama como estaba [h01-574, h01-575, h01-576]. Segundo caso, en una frase: revertir un commit de fusión exige decir cuál de sus padres es la línea principal [h01-598].

**Recuadros.**

- **Error típico.** Hacer rebase de una rama que otros ya tienen y subirla con `git push --force`: los demás se quedan con commits que ya no existen en el servidor y, al traer los cambios, aparecen duplicados con el mismo autor, fecha y mensaje [h01-519, h01-521, h01-522, h01-523, h01-524, h01-591]. Es el final de «El problema».
- **Bajo el capó.** Además del hash, Git calcula un `patch-id` a partir del parche de cada commit; con él puede reconocer como tuyo un commit reescrito y por eso `git pull --rebase` alivia el desastre anterior, aunque solo si los parches son casi iguales [h01-525, h01-526, h01-527, h01-528].
- **Ojo con la versión.** Pro Git en español enseña `pick`, `reword`, `edit`, `squash` y `fixup`, y borrar una línea para descartar [h01-548, h01-549, h01-550, h01-551, h01-552, h01-554]; la documentación actual añade `drop`, `break`, `exec`, `fixup -c` y los prefijos `amend!` [h01-578, h01-580, h01-582, h01-585, h01-588]. La lista de tareas del ejemplo 13 muestra los comandos de Git 2.43.

**PENDIENTES previstos.**

- Falta hecho sobre cómo sustituir el editor del rebase interactivo por un comando (`GIT_SEQUENCE_EDITOR` o `sequence.editor`). El ejemplo 13 lo necesita para ejecutarse sin intervención; si el texto lo explica, hace falta el hecho (ver decisión 4).
- Opcional: «En un proyecto real» sobre la política de gentle-shell o FastAPI respecto a squash, rebase o merge de los PR. Ninguna fuente del capítulo lo cubre.

**Palabras estimadas.** 1.500.

---

### 1.6 Bajo el capó: objetos y referencias

**Idea en dos frases.** Git es un almacén de clave y valor: guardas contenido y te devuelve su hash, y con tres tipos de objeto (blob, árbol y commit, más la etiqueta anotada) representa cualquier instantánea y su historia. Encima, las referencias son archivos pequeños y mutables con un hash dentro, y HEAD es una referencia a otra referencia; todos los comandos de las secciones anteriores son operaciones que añaden objetos y mueven referencias.

**Modelo mental.** Objetos inmutables nombrados por su contenido; nombres mutables que apuntan a ellos.

- Diagrama `flowchart TB`: `HEAD` →(ref:)→ `refs/heads/main` → commit C2; C2 → `árbol raíz`; `árbol raíz` → `blob README.md`, `blob factura.py`, `árbol tests/`; `árbol tests/` → `blob test_factura.py`; C2 →(parent)→ C1; C1 → su árbol, que apunta al mismo `blob README.md`; `refs/tags/v1.0` → `objeto etiqueta` → C2; `refs/tags/v0.1` → C1.

**Ejemplos.**

- `ejemplos/cap-01/16-dentro-de-git.sh`: `git init`; `ls .git`; `find .git/objects -type f` (vacío); `echo 'hola' | git hash-object -w --stdin`; `find .git/objects -type f`; `git cat-file -t` y `git cat-file -p` con ese hash. La salida debe mostrar las entradas de `.git`, el archivo del objeto en una subcarpeta de dos caracteres con un nombre de 38, el tipo `blob` y el contenido.
- `ejemplos/cap-01/17-hash-a-mano.py`: calcula en Python el SHA-1 de `blob <tamaño>\0<contenido>` y lo compara con lo que devuelve `git hash-object`; después lee el archivo del objeto en `.git/objects`, lo descomprime con `zlib` y muestra la cabecera. La salida debe mostrar los dos hashes iguales y la cabecera `blob N` seguida del contenido.
- `ejemplos/cap-01/18-arbol-y-commit.sh`: en `facturas` con `tests/`, `git cat-file -p HEAD`, `git cat-file -p HEAD^{tree}`, `git cat-file -p` del subárbol `tests/` y de un blob. La salida debe mostrar las líneas `tree`, `parent`, `author` y `committer` y el mensaje; las entradas del árbol con modo `100644`, tipo, hash y nombre; y `tests` como `tree`.
- `ejemplos/cap-01/19-commit-a-mano.sh`: llena el índice con `git add`, `git write-tree`, `git commit-tree` sin padre y luego otro con padre, `git update-ref refs/heads/main`, `git symbolic-ref HEAD` y `git log --oneline`. La salida debe mostrar un historial de dos commits construido sin `git commit`.
- `ejemplos/cap-01/20-etiquetas.sh` (opcional): `git tag v0.1` y `git tag -a v1.0 -m ...`; `cat` de los dos archivos de `.git/refs/tags`; `git cat-file -t` de cada hash; `git cat-file -p v1.0`. La salida debe mostrar que `v0.1` apunta a un `commit` y `v1.0` a un objeto `tag` que a su vez apunta al commit.

**Por qué funciona así.**

- Fontanería y porcelana: h01-601, h01-602, h01-603, h01-604.
- La carpeta `.git`: h01-605, h01-606, h01-607, h01-610, h01-611, h01-612, h01-613, h01-614.
- Almacén de clave y valor: h01-615, h01-616, h01-617, h01-618, h01-619, h01-621, h01-622, h01-623, h01-624, h01-625.
- Formato de un objeto (cabecera, byte nulo, SHA-1, zlib): h01-620, h01-645, h01-646, h01-647, h01-648, h01-649, h01-650, h01-294.
- Blob y árbol: h01-626, h01-627, h01-628, h01-629, h01-630, h01-632, h01-635, h01-636.
- Del índice al árbol y al commit: h01-633, h01-634, h01-637, h01-638, h01-639, h01-640, h01-641, h01-643, h01-644.
- Referencias y HEAD: h01-652, h01-653, h01-655, h01-658, h01-659, h01-662, h01-663, h01-664, h01-665, h01-666, h01-668, h01-669, h01-670.
- Etiquetas: h01-673, h01-674, h01-675, h01-677, h01-679, h01-680, h01-682.
- Referencias remotas, solo para situarlas (se desarrollan en el capítulo 2): h01-683, h01-684, h01-685, h01-687.
- El modelo completo en una frase: h01-761, h01-762, h01-765, h01-766, h01-768.

**Caso límite.** Dos archivos con distinto nombre e idéntico contenido son un solo blob, porque el nombre vive en el árbol y el blob solo guarda contenido [h01-214, h01-626, h01-627, h01-630]. Con esto se cierra la promesa de 1.2 («lo que no cambia se enlaza»).

**Recuadros.**

- **Ojo con la versión.** Pro Git en español solo habla de SHA-1. La documentación actual cuenta el ataque SHAttered, la implementación reforzada desde Git 2.13.0, la elección de SHA-256 y la opción `--object-format` de `git init`, que por defecto sigue en `sha1` y sin interoperabilidad entre ambos formatos por ahora [h01-280, h01-283, h01-288, h01-289, h01-290, h01-292, h01-293].
- **Error típico.** Editar a mano `.git/HEAD` o los archivos de `.git/refs`. Para eso están `git update-ref` y `git symbolic-ref`, que son más seguros [h01-657, h01-658, h01-669, h01-672].
- **Bajo el capó.** Por qué los hashes de los commits del libro son reproducibles: el commit incluye autor, confirmador y marca de tiempo, y el hash se calcula sobre todo su contenido; con el mismo árbol, los mismos padres, la misma fecha y el mismo mensaje sale el mismo hash [h01-638, h01-639, h01-640, h01-647]. Los ejemplos fijan autor y fecha.

**PENDIENTES previstos.**

- Falta hecho sobre los *packfiles* (objetos empaquetados). Si el lector abre `.git/objects` en un repositorio real clonado (por ejemplo gentle-shell, en «El proyecto avanza») no encontrará los objetos sueltos que ve aquí. Pro Git 10.4 lo trata, pero no está en el mapa de fuentes.
- Opcional: falta hecho sobre `git ls-files --stage` para enseñar el contenido del índice. Sin él, el índice se explica solo con h01-614 y h01-707.

**Palabras estimadas.** 1.500.

---

### 1.7 reset sin miedo

**Idea en dos frases.** Git trabaja con tres árboles (HEAD, el índice y el directorio de trabajo), y `reset` hace hasta tres pasos sobre ellos: mover la rama a la que apunta HEAD, copiar ese commit al índice y copiar el índice al directorio de trabajo; `--soft`, `--mixed` y `--hard` dicen dónde se para. Solo el tercer paso destruye datos, y aun así lo que llegó a confirmarse se recupera con el reflog.

**Modelo mental.** Tres cajas en fila y un comando que avanza por ellas hasta donde le digas; frente a él, cambiar de rama mueve HEAD en lugar de la rama.

- Diagrama 1, `flowchart LR` de los tres árboles: `Directorio de trabajo` →(git add)→ `Índice` →(git commit)→ `HEAD`; y en sentido contrario, al cambiar de rama, `HEAD` → `Índice` → `Directorio de trabajo`.
- Diagrama 2, `flowchart TB` de los pasos de reset: `1. Mover la rama a la que apunta HEAD` (aquí se para `--soft`) → `2. Copiar el commit al índice` (aquí se para `--mixed`, por defecto) → `3. Copiar el índice al directorio de trabajo` (`--hard`).
- Tabla propia (no la de Pro Git): filas `reset --soft`, `reset` (mixed), `reset --hard`, `switch <rama>`, `reset <archivo>`, `restore --source <commit> <archivo>`; columnas «qué mueve», «toca el índice», «toca el directorio de trabajo» y «protege tus cambios». Respaldo: h01-755, h01-756, h01-757, h01-758, h01-759, h01-760, h01-361.

**Ejemplos.**

- `ejemplos/cap-01/21-reset-tres-modos.sh`: tres commits de `factura.py` (v1, v2, v3). `git reset --soft HEAD~` y `git status -s`; nuevo commit; `git reset HEAD~` y `git status -s`; nuevo commit; `git reset --hard HEAD~`, `git status -s` y `cat factura.py`. La salida debe mostrar `M ` tras `--soft`, ` M` tras el reset mixto y un directorio limpio con el contenido de v2 tras `--hard`.
- `ejemplos/cap-01/22-reset-con-ruta.sh`: prepara un cambio; `git reset factura.py` y `git status -s`; lo vuelve a preparar; `git restore --staged factura.py` y `git status -s`; después `git reset HEAD~2 factura.py` y `git status -s`. La salida debe mostrar que las dos primeras órdenes dejan el mismo estado y que la tercera mete la versión antigua solo en el índice (`MM`) sin mover la rama.
- `ejemplos/cap-01/23-reset-frente-a-switch.sh`: en `develop`, `cat .git/HEAD` y `git log --oneline --all --decorate`; `git reset main` y de nuevo los dos comandos; vuelve al estado inicial y ejecuta `git switch main` con los mismos dos comandos. La salida debe mostrar que `reset` mueve `develop` y deja HEAD en `develop`, y que `switch` deja `develop` donde estaba y mueve HEAD.
- `ejemplos/cap-01/24-recuperar-con-reflog.sh`: `git reset --hard HEAD~2`; `git log --oneline` (faltan dos commits); `git reflog`; `git branch recuperada HEAD@{1}`; `git log --oneline recuperada`. Cierre opcional: borra `.git/logs` y muestra `git fsck --full` con el «dangling commit». La salida debe mostrar los commits perdidos en el reflog y de vuelta en la rama nueva.

**Por qué funciona así.**

- Los tres árboles: h01-701, h01-702, h01-703, h01-704, h01-705, h01-706, h01-707, h01-708, h01-709.
- El flujo normal sobre ellos y lo que ve `git status`: h01-710, h01-711, h01-712, h01-713, h01-714, h01-715, h01-716.
- Paso 1 y `--soft`: h01-717, h01-718, h01-719, h01-720, h01-721, h01-722, h01-723.
- Paso 2 y `--mixed`: h01-724, h01-725, h01-726, h01-727.
- Paso 3 y `--hard`: h01-728, h01-729, h01-730, h01-731.
- Reset con ruta: h01-734, h01-735, h01-736, h01-737, h01-738, h01-739, h01-740.
- Reset frente a cambiar de rama: h01-744, h01-745, h01-746, h01-747, h01-748, h01-749, h01-750, h01-751.
- Aplastar commits con `reset --soft` (se menciona y se practica en los ejercicios): h01-741, h01-742, h01-743, h01-773.
- El reflog y la recuperación: h01-732, h01-774, h01-775, h01-778, h01-781, h01-782, h01-783, h01-784, h01-786, h01-788, h01-789.
- Lo que conecta con el modelo general (commits inmutables, referencias mutables): h01-763, h01-764, h01-766.

**Caso límite.** ¿Cuándo se pierde algo de verdad? Lo no confirmado que pisa `--hard` no vuelve [h01-733, h01-347]. Un commit sin rama sobrevive mientras el reflog lo recuerde (90 días por defecto) [h01-779, h01-780]; si el reflog no lo tiene, todavía queda `git fsck --full` [h01-790, h01-791, h01-792, h01-793], y al final la recolección de basura lo elimina [h01-485].

**Recuadros.**

- **Error típico.** `git reset --hard` con cambios sin confirmar en el directorio de trabajo: es la única forma peligrosa de reset, no comprueba nada y lo no confirmado es irrecuperable [h01-730, h01-731, h01-733, h01-746].
- **Bajo el capó.** El reflog es local: vive en `.git/logs/`, se actualiza en cada commit y en cada cambio de rama, y no viaja con el repositorio [h01-774, h01-785, h01-786, h01-790]. La sintaxis `HEAD@{2}` se lee «donde estaba HEAD hace dos movimientos» [h01-775].
- **Ojo con la versión.** Pro Git y Missing Semester explican el reset con ruta y el checkout con ruta [h01-736, h01-751, h01-769, h01-771]; la documentación actual propone `git restore` para esos usos y lo declara equivalente [h01-361, h01-362, h01-597].

**PENDIENTES previstos.** Ninguno.

**Palabras estimadas.** 1.400.

---

## 7. El proyecto avanza: Arqueología de un PR, pieza 1

**Preparar la excavación.** Clona gentle-shell y elige un PR ya integrado. Antes de mirar su diff:

1. Localiza en el historial el commit que lo integró y averigua, mirando sus padres y la forma del grafo, si se integró con un commit de fusión, con un commit aplastado o con rebase. Escribe en `arqueologia.md` qué te ha hecho decidirlo.
2. Identifica el commit anterior al cambio (la base sobre la que trabajó el autor) y crea en él una rama `arqueologia/pr-NNN`. Comprueba con `cat .git/HEAD` y con el log que estás donde crees.
3. Dibuja en Mermaid el grafo alrededor del PR: la base, los commits del PR y el punto de integración.
4. Anota, sin abrir el diff, qué archivos tocó el PR y cuántas líneas (solo la vista resumida del log). Será tu único plano para reimplementarlo en el capítulo 5.

No escribas todavía nada de código: esta pieza solo deja el terreno marcado. Repite los pasos 1 a 3 con un PR de FastAPI.

---

## 8. Resumen

Cinco líneas como máximo, en el borrador: instantáneas nombradas por su contenido; grafo de commits inmutables; ramas y HEAD como referencias mutables; reescribir es crear commits nuevos; reset recorre tres árboles y solo `--hard` destruye, y solo lo no confirmado.

---

## 9. Ejercicios

**Comprobación**

1. Te dan un grafo: `main` en C3, `descuentos` en C2 (padre de C3) y HEAD apuntando a `descuentos`. Haces un commit. Dibuja el grafo resultante e indica qué archivos de `.git` han cambiado y cuáles no.
2. Te dan cuatro líneas de `git status -s` (`??`, `A `, ` M` y `MM`). Explica qué significa cada columna en cada línea y escribe la secuencia de comandos que produce cada estado desde un directorio limpio.

**Aplicación**

3. En `facturas`, encuentra con `git log` el commit que cambió el tipo de IVA sin abrir ningún archivo. Recupera la versión de `factura.py` anterior a ese commit sin mover la rama y confírmala como un commit nuevo. Explica por qué no has usado `reset`.
4. Crea tres commits «WIP» seguidos. Aplástalos primero con `git reset --soft` y después, desde el mismo punto, con rebase interactivo y `fixup`. Compara la instantánea final y el hash de ambos resultados y explica las diferencias.

**Construir sin IA** (ficha del catálogo)

5. Crea un repo, tres ramas, provoca un conflicto, resuélvelo y limpia el historial con rebase interactivo. Dibuja el grafo antes y después.

**Reto**

6. Escribe un programa en Python que, sin llamar a `git`, lea `.git/HEAD`, siga la referencia hasta el commit, descomprima los objetos con `zlib` y muestre la cadena de commits hasta el primero (hash y mensaje de cada uno), como un `git log --oneline` mínimo. Trabaja en un repositorio recién creado con pocos commits y compara tu salida con la de `git log --oneline`.

---

## 10. Preguntas de examen

**Explicar** (ficha del catálogo): ¿Qué es realmente una rama y qué cambia en el repositorio cuando haces un commit?

**Defender**

1. Un merge y un rebase de las mismas ramas producen la misma instantánea final. ¿Por qué no son intercambiables y qué criterio usas para elegir? [h01-510, h01-511, h01-515, h01-535]
2. ¿Qué pasaría si haces rebase de una rama que tu compañera ya ha descargado y la subes con `--force`? ¿Qué verá ella al traer los cambios? [h01-519, h01-521, h01-523, h01-524, h01-591]
3. ¿Por qué cambiar el mensaje de un commit de hace diez commits cambia el hash de todos los posteriores? [h01-570, h01-571, h01-647]
4. ¿Qué hace exactamente `git reset HEAD~` en cada uno de los tres árboles y por qué no pierdes trabajo? [h01-724, h01-725, h01-726, h01-727]
5. ¿Qué pasaría si ejecutas `git reset --hard HEAD~2` con cambios sin confirmar? ¿Qué recuperas, cómo y qué no recuperas? [h01-730, h01-731, h01-733, h01-783, h01-784]
6. Has subido un commit defectuoso a `main`, que comparte todo el equipo. ¿Por qué lo deshaces con `revert` y no con `reset`? [h01-594, h01-535, h01-764]

---

## 11. Decisiones que devOC debe tomar

1. **Terminología.** Propuesta: *commit* (cursiva la primera vez, «confirmación») y después «commit», como dice la comunidad; «rama», «fusión» con *merge* la primera vez y luego «merge» o «fusión» según el contexto; *rebase* sin traducir (Pro Git dice «reorganizar», que casi nadie usa); «área de preparación» e «índice» como sinónimos declarados [h01-706]; «directorio de trabajo»; «instantánea» para *snapshot*, y «foto» solo en el título y en la analogía; «puntero» (el título del catálogo lo usa) y no «apuntador» (Pro Git). ¿De acuerdo?
2. **`main` frente a `master`.** El entorno de ejemplos ya fija `init.defaultBranch=main`, pero el lector que ejecute `git init` con Git 2.43 sin configurar obtendrá `master`. Propuesta: usar `main`, explicarlo en el recuadro de 1.2 y pedir la configuración en «Lo que necesitas antes». ¿Aceptas?
3. **Preparación visible en los ejemplos.** Cada ejemplo `.sh` arranca en una carpeta vacía y todos sus comandos se imprimen. Para llegar al estado de 1.5 o 1.7 hacen falta varios commits previos que el lector verá antes de lo importante. Opciones: (a) aceptarlo y compactar la preparación en un solo grupo al principio; (b) añadir a `scripts/insertar_ejemplos.py` una marca para grupos que se ejecutan pero no se muestran (por ejemplo, terminados en `# preparación`), con sus tests; (c) menos ejemplos y más largos. Recomiendo (b): el texto queda limpio y la preparación sigue ejecutándose de verdad.
4. **Rebase interactivo sin editor.** El ejemplo 13 necesita sustituir el editor por un comando. No hay hecho que lo respalde. Opciones: (a) que el investigador extraiga un hecho de la página de `git rebase` o de `git config` (esta última no está en el mapa); (b) que el texto no lo explique y una nota diga solo que el ejemplo automatiza la edición. Recomiendo (a), y si no se encuentra, (b) con su PENDIENTE.
5. **Fecha fija en todos los commits.** Todos los commits de los ejemplos tienen la misma fecha. Consecuencias: un `--amend` o un `reset --soft` seguido de commit que no cambien ni contenido ni mensaje producen el mismo hash, y no se pueden enseñar filtros por fecha (`--since`). Propuesta: diseñar los ejemplos para que siempre cambie algo y usar el efecto como recuadro «Bajo el capó» en 1.6. ¿Aceptas, o prefieres que el script avance la fecha en cada commit?
6. **Orden del catálogo.** Los objetos (1.6) llegan después del rebase (1.5). Propongo mantener el orden y adelantar lo justo en 1.2 (ejemplo 03) y 1.4 (contenido de un commit), para que 1.6 confirme lo que el lector ya intuye. La alternativa sería mover 1.6 a la posición 3, lo que cambia la ficha.
7. **Qué se queda fuera.** `filter-branch` y `filter-repo` (solo se usa la idea de que cambiar un commit cambia todos los hashes siguientes), `stash`, `cherry-pick` como comando, remotos y `push`/`pull` (capítulo 2, salvo lo imprescindible en el recuadro de 1.5), *packfiles* y `gc`, *hooks*, estrategias de fusión, `bisect` y `git mergetool`. ¿Algo de esto debe entrar?
8. **Recuadros «En un proyecto real».** Ningún hecho del capítulo trata código de FastAPI o gentle-shell, así que el esquema no prevé ninguno. Si quieres al menos uno (el candidato natural es la política de integración de PR de gentle-shell, en 1.5), hay que dar de alta y verificar una fuente nueva.
9. **Extensión.** Secciones: unas 8.800 palabras (500 + 1.300 + 1.100 + 1.500 + 1.500 + 1.500 + 1.400); marco (objetivos, problema, proyecto, resumen, ejercicios y preguntas): unas 1.000. Total estimado: 9.800, dentro del rango 5.000-10.000 pero pegado al techo (el recuento de `informe_capitulo.py` excluye código y diagramas). Propongo apuntar a unas 8.500 recortando por este orden: el ejemplo 20 y las etiquetas (unas 300 palabras), `--autosquash` y `exec` en 1.5 (unas 300), el cierre con `fsck` en 1.7 (unas 150) y el recuadro de renombres de 1.2 (unas 100). ¿Recorto ya o se decide al ver el borrador?
10. **Ejemplos opcionales.** Son 24 (23 `.sh` y 1 `.py`); dos tienen grupos que deben fallar (09 y 14) y dos partes son opcionales (el 20 entero y el cierre del 24). ¿Los mantenemos todos para la fase 4?

### Notas para las fases siguientes

- **Para el programador.** En el código visible, preferir comandos cuyo comportamiento tiene hecho (`cat .git/HEAD`, `cat .git/refs/heads/...`, `git cat-file`, `git log --oneline --graph --all`, `HEAD~N`, `HEAD@{N}`, `^{tree}`). Si se usa algo sin hecho (`git rev-parse`, `git ls-files`, `ORIG_HEAD`, `git update-index`), el texto no podrá explicarlo. `advice.detachedHead=false` está fijado en el entorno, así que el ejemplo 10 no mostrará el aviso de HEAD desacoplado.
- **Para el redactor.** No heredar las erratas de la traducción listadas en `investigacion/cap-01/huecos.md`: `refs/remotes` es local; «área de preparación», no «área de ensayo»; «stash», no «alijos»; `git mv`, no «el comando mv».

---

## 12. Aprobación de devOC (2026-11-12)

devOC aprobó el esquema con estas decisiones:

1. Terminología: la propuesta tal cual.
2. Rama `main` en los ejemplos, con el recuadro de 1.2 y la configuración en «Lo que necesitas antes».
3. Opción (b): `insertar_ejemplos.py` admite grupos de preparación que se ejecutan pero no se muestran (terminados en `# preparación`), y la variable `EJEMPLO_DIR` para cargar ayudas comunes de `ejemplos/cap-01/_*.sh`.
4. Opción (a): el investigador busca el hecho sobre el editor del rebase interactivo; si no lo hay, (b) con su PENDIENTE.
5. Fecha fija: los ejemplos se diseñan para que cada commit cambie algo; el efecto se aprovecha en un «Bajo el capó» de 1.6.
6. Se mantiene el orden del catálogo.
7. Lo que queda fuera: la lista propuesta.
8. «En un proyecto real»: PENDIENTE hasta que el capítulo 2 dé de alta las guías de contribución de gentle-shell y FastAPI.
9. Extensión: se escribe y se recorta sobre el borrador.
10. Se mantienen los 24 ejemplos; los opcionales se deciden al recortar.
11. Estrategia `ort`: se da de alta la página oficial de estrategias de fusión (f01-27).

Los hechos que se añadan desde ahora van en `secciones/9-adicionales.md`, con ids desde h01-801.

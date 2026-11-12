# Revisión técnica, tramo 2: 1.3 y 1.4

Revisor técnico (sesión limpia), 2026-11-12. 154 bloques (63 en 1.3, 91 en 1.4, con 6 diagramas): 140 SOPORTADA, 12 PARCIAL, 0 NO SOPORTADA, 2 SIN HECHO. Los 50 hashes de la prosa y los diagramas aparecen en alguna salida. Aquí van los bloques que no salieron SOPORTADA.

## 1.3 Leer y deshacer el historial

- frase: "El historial es una cadena que se recorre hacia atrás, y `git log` la enseña con lo más reciente arriba."
  hechos: h01-302
  veredicto: PARCIAL
  nota: «cadena» choca con los commits de varios padres de la frase anterior (es un grafo); «se recorre hacia atrás» sale de h01-570, no citado. Propuesta: «un grafo que se recorre hacia atrás siguiendo los padres».
  resuelto: no

- frase: "En el ejemplo redondeas el total, escribes su test y solo preparas `factura.py`."
  hechos: —
  veredicto: PARCIAL
  nota: los ejemplos 05 y 06 parten de tres commits (`facturas_historial 3`), no de los cinco recién vistos; el padre `c87074a` del amend aparece sin explicación. Avisar como en 1.4.
  resuelto: no

- frase: "`3ddacd5` es otro commit, con otra instantánea y el mismo padre, `c87074a`, y `main` apunta ahora a él."
  hechos: h01-331, h01-764
  veredicto: PARCIAL
  nota: ningún hecho dice que `--amend` conserve el padre. Extraer de f01-32: «The new commit has the same parents and author as the current one».
  resuelto: no

- frase: "Con `--staged`, el destino es el índice y la fuente, por defecto, `HEAD`: `factura.py` pasa de `M ` a ` M` y tu línea sigue en disco, porque tocar también el directorio de trabajo exige añadir `--worktree`."
  hechos: h01-354, h01-356, h01-250, h01-355
  veredicto: PARCIAL
  nota: la salida no muestra `M ` (el ejemplo usa el `git status` largo). Añadir `git status -s` al ejemplo o redactar «pasa de "Changes to be committed" a ` M`». Para «exige», extraer de f01-19: «Specifying --staged will only restore the index».
  resuelto: no

- frase: "Usar `git restore <archivo>`, o el antiguo `git checkout -- <archivo>`, para «limpiar» y descubrir después que querías ese cambio."
  hechos: —
  veredicto: PARCIAL
  nota: ningún hecho dice que `git checkout --` sea «antiguo» (la documentación actual lo mantiene, h01-479). Mejor «la forma de Pro Git».
  resuelto: no

- frase: "La documentación actual de `git restore` dice que devolver un archivo del índice a la versión de `HEAD` equivale a usar `git reset`, y que restaurar a la vez el índice y el directorio de trabajo equivale a usar `git checkout`."
  hechos: h01-361, h01-362
  veredicto: PARCIAL
  nota: junto a `git checkout -- <archivo>` lleva a emparejarlos mal. La equivalencia con checkout es la de `restore --source=HEAD --staged --worktree` = `checkout HEAD -- <archivo>`; `git checkout -- <archivo>` copia desde el índice (f01-21) y equivale a `git restore <archivo>`. El error viene del esquema. Extraer hecho de f01-21 y reescribir.
  resuelto: no

## 1.4 Las ramas son punteros

- frase: "Fusionar es adelantar un puntero, si tu commit es ancestro directo del que fusionas, o crear un commit con dos padres a partir del ancestro común; y el conflicto aparece cuando los dos lados han cambiado la misma zona de un archivo."
  hechos: h01-434, h01-440, h01-442, h01-445, h01-448
  veredicto: PARCIAL
  nota: falta «de forma distinta» (si ambos lados hacen el mismo cambio no hay conflicto).
  resuelto: no

- frase: "Tarde o temprano, el trabajo de una rama vuelve a `main`."
  hechos: —
  veredicto: SIN HECHO
  nota: generalización que desmiente el propio ejemplo 10. Propuesta: «Cuando el trabajo de una rama está listo, vuelve a `main`».
  resuelto: no

- frase: "Lo que haga Git depende de la forma del grafo."
  hechos: —
  veredicto: SIN HECHO
  nota: leve; citar h01-434 y h01-440.
  resuelto: no

- frase: "Pro Git plantea la resolución como elegir a mano el contenido de un lado o del otro."
  hechos: h01-455
  veredicto: PARCIAL
  nota: deforma la fuente: Pro Git resuelve su ejemplo mezclando («contiene un poco de ambas partes», f01-08 l.142). Propuesta: «Puedes quedarte con un lado, con el otro o con una mezcla, como hace Pro Git».
  resuelto: no

- frase: "`git commit` termina la fusión; con `--no-edit`, usa sin abrir el editor el mensaje que Git propone por defecto, «Merge branch 'descuentos'»."
  hechos: h01-460, h01-831, h01-461
  veredicto: PARCIAL
  nota: la salida de `cat-file -p HEAD` muestra que el commit guarda también «# Conflicts:» y «#<tab>factura.py». Explicarlo o cambiar el ejemplo a `git commit -m` (y actualizar la salida).
  resuelto: no

- frase: "Por eso `HEAD^2` nombra `a660e13`; la sintaxis de la sección 1.3 solo sirve en commits de fusión."
  hechos: h01-823, h01-824
  veredicto: PARCIAL
  nota: al pie de la letra es falso (`~` y `^` sirven en cualquier commit). Propuesta: «`^2` solo tiene sentido en un commit de fusión». Añadir `git log --oneline -1 HEAD^2` al ejemplo lo demostraría.
  resuelto: no

- frase: "Las demás líneas las verás en la sección 1.6."
  hechos: —
  veredicto: PARCIAL
  nota: la 1.6 no explica las líneas «# Conflicts:». Ligado al bloque anterior.
  resuelto: no

- frase: "Es el caso que describe la documentación de `git checkout`: cuando nada referencia el commit, la recolección de basura de Git acabará eliminándolo, salvo que antes crees una referencia."
  hechos: h01-485
  veredicto: PARCIAL
  nota: h01-485 se limita a su ejemplo y aquí se generaliza; además ignora que el reflog lo protege (h01-779, h01-780). Propuesta: «cuando ninguna rama ni etiqueta lo referencia, la recolección de basura acabará eliminándolo; mientras, el reflog te deja rescatarlo».
  resuelto: no

## Otros puntos para la corrección

- Evidencias sin extraer que darían respaldo directo: f01-32 («Replace the tip of the current branch by creating a new commit», «same parents and author»); f01-19 («Specifying --staged will only restore the index»); f01-22 («non-overlapping ones ... are incorporated in the final result verbatim»); f01-21 (`git checkout -- <archivo>` copia desde el índice).
- «Git elige él mismo el mejor ancestro común; en CVS o Subversion tiene que hacerlo el desarrollador»: viene de una traducción antigua y habla de Subversion en presente. Atribuir a Pro Git, pasar a pasado o quitar.
- El «Ojo con la versión» sobre `ort` está en 1.4, pero la primera salida con la línea de estrategia aparece en 1.5. Valorar moverlo.
- `-D` «aunque pierdas ese trabajo» choca con h01-346 y con el reflog: añadir «salvo que lo rescates del reflog».
- «Cada rama es un archivo de `.git/refs/heads`»: h01-652 habla de `.git/refs`; citar h01-655 o h01-685 para la carpeta concreta.
- No hay erratas heredadas de huecos.md en 1.3 ni en 1.4.

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

- id: h01-809
  hecho: Git nació en 2005 y desde entonces ha evolucionado y madurado para ser fácil de usar sin perder sus características iniciales.
  evidencia: "Desde su nacimiento en el 2005, Git ha evolucionado y madurado para ser fácil de usar y conservar sus características iniciales."
  fuente: f01-02
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Una-breve-historia-de-Git
  consultada: 2026-11-12

- id: h01-810
  hecho: Git es muy rápido, muy eficiente con grandes proyectos y tiene un sistema de ramificación para el desarrollo no lineal.
  evidencia: "Git ha evolucionado y madurado para ser fácil de usar y conservar sus características iniciales. Es tremendamente rápido, muy eficiente con grandes proyectos y tiene un increíble sistema de ramificación (branching) para desarrollo no lineal"
  fuente: f01-02
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Una-breve-historia-de-Git
  consultada: 2026-11-12

- id: h01-811
  hecho: El nombre y el correo se configuran con git config --global user.name y git config --global user.email.
  evidencia: '$ git config --global user.name "John Doe" $ git config --global user.email johndoe@example.com'
  fuente: f01-31
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Configurando-Git-por-primera-vez
  consultada: 2026-11-12

- id: h01-812
  hecho: Los commits de Git usan el nombre de usuario y la dirección de correo que se establecen al instalar Git.
  evidencia: 'Lo primero que deberás hacer cuando instales Git es establecer tu nombre de usuario y dirección de correo electrónico. Esto es importante porque los "commits" de Git usan esta información'
  fuente: f01-31
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Configurando-Git-por-primera-vez
  consultada: 2026-11-12

- id: h01-813
  hecho: Con la opción --global basta configurar el nombre y el correo una sola vez, porque Git siempre usará esa información en ese sistema.
  evidencia: "De nuevo, sólo necesitas hacer esto una vez si especificas la opción --global, ya que Git siempre usará esta información para todo lo que hagas en ese sistema."
  fuente: f01-31
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Configurando-Git-por-primera-vez
  consultada: 2026-11-12

- id: h01-814
  hecho: Para usar otro nombre o correo en un proyecto concreto se ejecuta el comando sin --global dentro de ese proyecto.
  evidencia: "Si quieres sobrescribir esta información con otro nombre o dirección de correo para proyectos específicos, puedes ejecutar el comando sin la opción --global cuando estés en ese proyecto."
  fuente: f01-31
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Configurando-Git-por-primera-vez
  consultada: 2026-11-12

- id: h01-815
  hecho: La opción --abbrev-commit de git log muestra solo los primeros caracteres de la suma SHA-1 en vez de los 40 que la componen.
  evidencia: "--abbrev-commit Muestra solamente los primeros caracteres de la suma SHA-1, en vez de los 40 caracteres de que se compone."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-816
  hecho: Git identifica un commit a partir de los primeros caracteres de su SHA-1 si son al menos 4 y no son ambiguos.
  evidencia: "Git es lo suficientemente inteligente como para descifrar el “commit” al que te refieres si le entregas los primeros caracteres, siempre y cuando la parte de SHA-1 sea de al menos 4 caracteres y no sea ambigua"
  fuente: f01-28
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Revisi%C3%B3n-por-selecci%C3%B3n
  consultada: 2026-11-12

- id: h01-817
  hecho: Un SHA-1 parcial es ambiguo cuando más de un objeto del repositorio actual empieza por él, y no lo es cuando solo uno comienza así.
  evidencia: "no sea ambigua - esto quiere decir, que solamente un objeto en el repositorio actual comience con ese SHA-1 parcial."
  fuente: f01-28
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Revisi%C3%B3n-por-selecci%C3%B3n
  consultada: 2026-11-12

- id: h01-818
  hecho: Con --abbrev-commit, git log usa por defecto siete caracteres y los alarga si es necesario para que el SHA-1 siga siendo único.
  evidencia: "Si añades --abbrev-commit al comando git log, el resultado utilizará los valores cortos pero manteniéndolos únicos; por default utiliza siete caracteres pero los hace más largos de ser necesario para mantener el SHA-1 sin ambigüedades"
  fuente: f01-28
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Revisi%C3%B3n-por-selecci%C3%B3n
  consultada: 2026-11-12

- id: h01-819
  hecho: Generalmente bastan entre ocho y diez caracteres del SHA-1 para ser únicos en un proyecto.
  evidencia: "Generalmente, de ocho a diez caracteres son más que suficientes para ser únicos en un proyecto."
  fuente: f01-28
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Revisi%C3%B3n-por-selecci%C3%B3n
  consultada: 2026-11-12

- id: h01-820
  hecho: La opción --oneline de git log es una abreviatura de --pretty=oneline y --abbrev-commit usados juntos.
  evidencia: "--oneline This is a shorthand for --pretty=oneline --abbrev-commit used together."
  fuente: f01-30
  ancla: https://git-scm.com/docs/git-log
  consultada: 2026-11-12

- id: h01-821
  hecho: En git log, --abbrev-commit muestra, en lugar del nombre completo de 40 bytes en hexadecimal, un prefijo que nombra el objeto de forma única.
  evidencia: "--abbrev-commit Instead of showing the full 40-byte hexadecimal commit object name, show a prefix that names the object uniquely."
  fuente: f01-30
  ancla: https://git-scm.com/docs/git-log
  consultada: 2026-11-12

- id: h01-822
  hecho: Un sufijo ^ en una revisión significa el primer padre de ese commit.
  evidencia: "A suffix ^ to a revision parameter means the first parent of that commit object."
  fuente: f01-29
  ancla: https://git-scm.com/docs/gitrevisions
  consultada: 2026-11-12

- id: h01-823
  hecho: ^<n> significa el n-ésimo padre del commit, de modo que <rev>^ equivale a <rev>^1.
  evidencia: "^<n> means the <n>th parent (i.e. <rev>^ is equivalent to <rev>^1)."
  fuente: f01-29
  ancla: https://git-scm.com/docs/gitrevisions
  consultada: 2026-11-12

- id: h01-824
  hecho: Añadir un número tras ^ elige ese padre; la sintaxis solo sirve para fusiones confirmadas, que tienen más de un padre.
  evidencia: "También se puede especificar un número despúes de ^ - por ejemplo, d921970^2 significa “el segundo padre de d921970.” Esta sintaxis es útil solamente para fusiones confirmadas, las cuales tienen más de un padre."
  fuente: f01-28
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Revisi%C3%B3n-por-selecci%C3%B3n
  consultada: 2026-11-12

- id: h01-825
  hecho: HEAD~ también se refiere al primer padre, así que HEAD~ y HEAD^ son equivalentes.
  evidencia: "Este también refiere al primer padre, asi que HEAD~ y HEAD^ son equivalentes."
  fuente: f01-28
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Revisi%C3%B3n-por-selecci%C3%B3n
  consultada: 2026-11-12

- id: h01-826
  hecho: Un sufijo ~<n> designa el commit que es el n-ésimo ancestro del indicado, siguiendo solo los primeros padres.
  evidencia: "A suffix ~<n> to a revision parameter means the commit object that is the <n>th generation ancestor of the named commit object, following only the first parents."
  fuente: f01-29
  ancla: https://git-scm.com/docs/gitrevisions
  consultada: 2026-11-12

- id: h01-827
  hecho: <rev>~3 equivale a <rev>^^^, que a su vez equivale a <rev>^1^1^1.
  evidencia: "I.e. <rev>~3 is equivalent to <rev>^^^ which is equivalent to <rev>^1^1^1."
  fuente: f01-29
  ancla: https://git-scm.com/docs/gitrevisions
  consultada: 2026-11-12

- id: h01-828
  hecho: La diferencia entre ~ y ^ se hace evidente cuando se especifica un número, y HEAD~2 recorre el primer padre las veces indicadas.
  evidencia: "La diferencia se vuelve aparente cuando se especifica un número. HEAD~2 significa “el primer padre del primer padre,” o “el abuelo” - este recorre el primer padre las veces que se especifiquen."
  fuente: f01-28
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Revisi%C3%B3n-por-selecci%C3%B3n
  consultada: 2026-11-12

- id: h01-829
  hecho: Si <rev> es un tree-ish, <rev>^{tree} describe el objeto árbol correspondiente.
  evidencia: "Similarly, if <rev> is a tree-ish, <rev>^{tree} describes the corresponding tree object."
  fuente: f01-29
  ancla: https://git-scm.com/docs/gitrevisions
  consultada: 2026-11-12

- id: h01-830
  hecho: Si <rev> es un commit-ish, <rev>^{commit} describe el objeto commit correspondiente.
  evidencia: "For example, if <rev> is a commit-ish, <rev>^{commit} describes the corresponding commit object."
  fuente: f01-29
  ancla: https://git-scm.com/docs/gitrevisions
  consultada: 2026-11-12

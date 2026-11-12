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

- id: h01-831
  hecho: La opción --no-edit de git commit usa el mensaje de commit elegido sin lanzar un editor.
  evidencia: "--no-edit Use the selected commit message without launching an editor."
  fuente: f01-32
  ancla: https://git-scm.com/docs/git-commit
  consultada: 2026-11-12

- id: h01-832
  hecho: git commit --amend --no-edit modifica un commit sin cambiar su mensaje.
  evidencia: "For example, git commit --amend --no-edit amends a commit without changing its commit message."
  fuente: f01-32
  ancla: https://git-scm.com/docs/git-commit
  consultada: 2026-11-12

- id: h01-833
  hecho: El modo strip de --cleanup elimina las líneas vacías al principio y al final, los espacios finales, los comentarios y colapsa las líneas vacías consecutivas.
  evidencia: "strip Strip leading and trailing empty lines, trailing whitespace, commentary and collapse consecutive empty lines."
  fuente: f01-32
  ancla: https://git-scm.com/docs/git-commit
  consultada: 2026-11-12

- id: h01-834
  hecho: El modo por defecto de --cleanup equivale a strip si el mensaje se va a editar y a whitespace en caso contrario.
  evidencia: "default Same as strip if the message is to be edited. Otherwise whitespace."
  fuente: f01-32
  ancla: https://git-scm.com/docs/git-commit
  consultada: 2026-11-12

- id: h01-835
  hecho: En git merge, la opción --no-edit sirve para aceptar el mensaje de fusión autogenerado, aunque en general se desaconseja.
  evidencia: "Invoke an editor before committing successful mechanical merge to further edit the auto-generated merge message, so that the user can explain and justify the merge. The --no-edit option can be used to accept the auto-generated message (this is generally discouraged)."
  fuente: f01-22
  ancla: https://git-scm.com/docs/git-merge
  consultada: 2026-11-12

- id: h01-836
  hecho: Con --cleanup=scissors y un conflicto de fusión, git merge añade la línea de tijeras a MERGE_MSG antes de pasarlo al mecanismo de commit.
  evidencia: "if the <mode> is given a value of scissors, scissors will be appended to MERGE_MSG before being passed on to the commit machinery in the case of a merge conflict."
  fuente: f01-22
  ancla: https://git-scm.com/docs/git-merge
  consultada: 2026-11-12

- id: h01-837
  hecho: La documentación de git log presenta --pretty[=<formato>] y --format=<formato> juntas, en una misma entrada que imprime el contenido de los logs de commits en un formato dado.
  evidencia: "--pretty[=<format>] --format=<format> Pretty-print the contents of the commit logs in a given format"
  fuente: f01-30
  ancla: https://git-scm.com/docs/git-log
  consultada: 2026-11-12

- id: h01-838
  hecho: fuller es uno de los valores que puede tomar el formato de --pretty y --format, junto con oneline, short, medium, full, reference, email y raw.
  evidencia: "where <format> can be one of oneline, short, medium, full, fuller, reference, email, raw, format:<string> and tformat:<string>."
  fuente: f01-30
  ancla: https://git-scm.com/docs/git-log
  consultada: 2026-11-12

- id: h01-839
  hecho: El formato fuller muestra el hash del commit, el autor con su fecha de autoría y el committer con su fecha de commit.
  evidencia: "fuller commit <hash> Author: <author> AuthorDate: <author-date> Commit: <committer> CommitDate: <committer-date>"
  fuente: f01-30
  ancla: https://git-scm.com/docs/git-log
  consultada: 2026-11-12

- id: h01-840
  hecho: Con --first-parent, al encontrar un commit de fusión git log sigue solo el primer padre para decidir qué commits incluir.
  evidencia: "When finding commits to include, follow only the first parent commit upon seeing a merge commit."
  fuente: f01-30
  ancla: https://git-scm.com/docs/git-log
  consultada: 2026-11-12

- id: h01-841
  hecho: En una fusión confirmada, el primer padre es la rama en la que se estaba al fusionar y el segundo es el commit de la rama que se fusionó.
  evidencia: "El primer padre es la rama en el que se estaba al momento de fusionar, y el segundo es el “commit” en la rama en la que se fusionó"
  fuente: f01-28
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Revisi%C3%B3n-por-selecci%C3%B3n
  consultada: 2026-11-12

- id: h01-842
  hecho: La opción --quiet de git rebase (-q) silencia la salida e implica --no-stat.
  evidencia: "--quiet Be quiet. Implies --no-stat."
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-843
  hecho: git diff <commit> <commit> sirve para ver los cambios entre dos commits cualesquiera.
  evidencia: "git diff [<options>] [--merge-base] <commit> <commit> [--] [<path>...] This is to view the changes between two arbitrary <commit>."
  fuente: f01-33
  ancla: https://git-scm.com/docs/git-diff
  consultada: 2026-11-12

- id: h01-844
  hecho: git diff <commit>..<commit> es sinónimo de la forma sin los dos puntos para ver los cambios entre dos commits cualesquiera.
  evidencia: "git diff [<options>] <commit>..<commit> [--] [<path>...] This is synonymous to the earlier form (without the ..) for viewing the changes between two arbitrary <commit>."
  fuente: f01-33
  ancla: https://git-scm.com/docs/git-diff
  consultada: 2026-11-12

- id: h01-845
  hecho: En el ejemplo de git hash-object -w --stdin, la opción --stdin indica al comando que lea desde la entrada estándar.
  evidencia: "echo 'test content' | git hash-object -w --stdin d670460b4b4aece5915caf5c68d12f560a9fe3e4 La opción -w indica a hash-object que ha de guardar el objeto; de otro modo, el comando solo te respondería cual sería su clave. La opción --stdin indica al comando de leer desde la entrada estándar stdin"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-846
  hecho: Con --amend, git commit sustituye la punta de la rama actual creando un commit nuevo.
  evidencia: "--amend Replace the tip of the current branch by creating a new commit"
  fuente: f01-32
  ancla: https://git-scm.com/docs/git-commit
  consultada: 2026-11-12

- id: h01-847
  hecho: Con --amend, el commit nuevo tiene los mismos padres que el commit actual.
  evidencia: "--amend Replace the tip of the current branch by creating a new commit. The recorded tree is prepared as usual (including the effect of the -i and -o options and explicit pathspec), and the message from the original commit is used as the starting point, instead of an empty message, when no other message is specified from the command line via options such as -m, -F, -c, etc. The new commit has the same parents and author as the current one"
  fuente: f01-32
  ancla: https://git-scm.com/docs/git-commit
  consultada: 2026-11-12

- id: h01-848
  hecho: Con --amend, el commit nuevo tiene el mismo autor que el commit actual.
  evidencia: "--amend Replace the tip of the current branch by creating a new commit. The recorded tree is prepared as usual (including the effect of the -i and -o options and explicit pathspec), and the message from the original commit is used as the starting point, instead of an empty message, when no other message is specified from the command line via options such as -m, -F, -c, etc. The new commit has the same parents and author as the current one"
  fuente: f01-32
  ancla: https://git-scm.com/docs/git-commit
  consultada: 2026-11-12

- id: h01-849
  hecho: En git restore, indicar --staged restaura solo el índice.
  evidencia: "Specify the restore location. If neither option is specified, by default the working tree is restored. Specifying --staged will only restore the index."
  fuente: f01-19
  ancla: https://git-scm.com/docs/git-restore
  consultada: 2026-11-12

- id: h01-850
  hecho: En git restore, si no se indica ni --staged ni --worktree, se restaura por defecto el directorio de trabajo.
  evidencia: "If neither option is specified, by default the working tree is restored."
  fuente: f01-19
  ancla: https://git-scm.com/docs/git-restore
  consultada: 2026-11-12

- id: h01-851
  hecho: git restore puede restaurar a la vez el directorio de trabajo y el índice combinando --staged --worktree.
  evidencia: "The command can also be used to restore the content in the index with --staged, or restore both the working tree and the index with --staged --worktree."
  fuente: f01-19
  ancla: https://git-scm.com/docs/git-restore
  consultada: 2026-11-12

- id: h01-852
  hecho: Sin indicar tree-ish, git checkout -- <pathspec> sustituye los archivos o directorios indicados por la versión del índice.
  evidencia: "git checkout [-f|--ours|--theirs|-m|--conflict=<style>] [--] <pathspec>... git checkout [-f|--ours|--theirs|-m|--conflict=<style>] --pathspec-from-file=<file> [--pathspec-file-nul] Replace the specified files and/or directories with the version from the index."
  fuente: f01-21
  ancla: https://git-scm.com/docs/git-checkout
  consultada: 2026-11-12

- id: h01-853
  hecho: Con un tree-ish, git checkout <tree-ish> -- <pathspec> sustituye los archivos o directorios indicados por la versión de ese commit o árbol y los añade al índice.
  evidencia: "git checkout <tree-ish> [--] <pathspec>... git checkout <tree-ish> --pathspec-from-file=<file> [--pathspec-file-nul] Replace the specified files and/or directories with the version from the given commit or tree and add them to the index"
  fuente: f01-21
  ancla: https://git-scm.com/docs/git-checkout
  consultada: 2026-11-12

- id: h01-854
  hecho: git checkout <archivo> descarta los cambios sin preparar de ese archivo, por ejemplo tras decidir que fueron un error.
  evidencia: "if you check out a commit, edit file.txt, and then decide those changes were a mistake, git checkout file.txt will discard any unstaged changes to file.txt."
  fuente: f01-21
  ancla: https://git-scm.com/docs/git-checkout
  consultada: 2026-11-12

- id: h01-855
  hecho: En una fusión, los cambios que no se solapan (un lado cambió una zona y el otro la dejó intacta) se incorporan tal cual al resultado final.
  evidencia: "Among the changes made to the common ancestor’s version, non-overlapping ones (that is, you changed an area of the file while the other side left that area intact, or vice versa) are incorporated in the final result verbatim."
  fuente: f01-22
  ancla: https://git-scm.com/docs/git-merge
  consultada: 2026-11-12

- id: h01-856
  hecho: En una fusión, las líneas que ambos lados cambiaron de la misma manera se resuelven limpiamente, sin conflicto.
  evidencia: "Here are lines that are either unchanged from the common ancestor, or cleanly resolved because only one side changed, or cleanly resolved because both sides changed the same way."
  fuente: f01-22
  ancla: https://git-scm.com/docs/git-merge
  consultada: 2026-11-12

- id: h01-857
  hecho: El formato por defecto de los marcadores de conflicto no muestra qué decía el original en la zona en conflicto.
  evidencia: "The default format does not show what the original said in the conflicting area."
  fuente: f01-22
  ancla: https://git-scm.com/docs/git-merge
  consultada: 2026-11-12

- id: h01-858
  hecho: El estilo de conflicto diff3 añade un marcador ||||||| y el texto original antes del marcador =======.
  evidencia: 'An alternate style, "diff3", adds a ||||||| marker and the original text before the ======= marker.'
  fuente: f01-22
  ancla: https://git-scm.com/docs/git-merge
  consultada: 2026-11-12

- id: h01-859
  hecho: La descripción simplificada de git rebase <upstream> tiene cuatro pasos, que son listar los commits de la rama que no tienen equivalente en upstream, hacer checkout de upstream en modo detached, reaplicar los commits uno a uno y actualizar la rama con checkout -B.
  evidencia: "Here is a simplified description of what git rebase <upstream> does: Make a list of all commits on your current branch since it branched off from <upstream> that do not have an equivalent commit in <upstream>. Check out <upstream> with the equivalent of git checkout --detach <upstream>. Replay the commits, one by one, in order. This is similar to running git cherry-pick <commit> for each commit. See REBASING MERGES for how merges are handled. Update your branch to point to the final commit with the equivalent of git checkout -B <branch>."
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-860
  hecho: Con --no-ff (también --force-rebase o -f), rebase reaplica uno por uno todos los commits rebasados en lugar de avanzar sobre los que no cambian.
  evidencia: "--no-ff --force-rebase -f Individually replay all rebased commits instead of fast-forwarding over the unchanged ones."
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-861
  hecho: Con --no-ff, la historia completa de la rama rebasada queda compuesta por commits nuevos.
  evidencia: "--no-ff --force-rebase -f Individually replay all rebased commits instead of fast-forwarding over the unchanged ones. This ensures that the entire history of the rebased branch is composed of new commits."
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-862
  hecho: git rebase tiene dos backends principales, apply y merge.
  evidencia: "git rebase has two primary backends: apply and merge."
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-863
  hecho: La opción --merge de git rebase usa estrategias de fusión para rebasar, y la página la marca como opción por defecto.
  evidencia: "-m --merge Using merging strategies to rebase (default)."
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-864
  hecho: La opción --apply de git rebase usa estrategias de aplicación de parches, llamando internamente a git am.
  evidencia: "--apply Use applying strategies to rebase (calling git-am internally)."
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-865
  hecho: La variable de configuración rebase.backend fija el backend por defecto de rebase, con las opciones apply o merge.
  evidencia: "rebase.backend Default backend to use for rebasing. Possible choices are apply or merge."
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-866
  hecho: Por defecto, rebase descarta los commits de fusión de la lista de tareas y deja los commits rebasados en una sola rama lineal.
  evidencia: "-r --rebase-merges[=(rebase-cousins|no-rebase-cousins)] --no-rebase-merges By default, a rebase will simply drop merge commits from the todo list, and put the rebased commits into a single, linear branch."
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-867
  hecho: Con --rebase-merges, rebase intenta conservar la estructura de ramas de los commits a rebasar recreando los commits de fusión.
  evidencia: "With --rebase-merges, the rebase will instead try to preserve the branching structure within the commits that are to be rebased, by recreating the merge commits."
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-868
  hecho: El subcomando expire de git reflog elimina las entradas antiguas del reflog, según el tiempo de expiración y el de expiración de las inalcanzables.
  evidencia: 'The "expire" subcommand prunes older reflog entries. Entries older than expire time, or entries older than expire-unreachable time and not reachable from the current tip, are removed from the reflog.'
  fuente: f01-25
  ancla: https://git-scm.com/docs/git-reflog
  consultada: 2026-11-12

- id: h01-869
  hecho: La opción --expire de git reflog poda las entradas más antiguas que el tiempo indicado.
  evidencia: "--expire=<time> Prune entries older than the specified time."
  fuente: f01-25
  ancla: https://git-scm.com/docs/git-reflog
  consultada: 2026-11-12

- id: h01-870
  hecho: Sin --expire, git reflog toma el tiempo de expiración de gc.reflogExpire, que por defecto es de 90 días.
  evidencia: "--expire=<time> Prune entries older than the specified time. If this option is not specified, the expiration time is taken from the configuration setting gc.reflogExpire, which in turn defaults to 90 days."
  fuente: f01-25
  ancla: https://git-scm.com/docs/git-reflog
  consultada: 2026-11-12

- id: h01-871
  hecho: La opción --expire-unreachable de git reflog poda las entradas más antiguas que el tiempo indicado que no son alcanzables desde la punta actual de la rama.
  evidencia: "--expire-unreachable=<time> Prune entries older than <time> that are not reachable from the current tip of the branch."
  fuente: f01-25
  ancla: https://git-scm.com/docs/git-reflog
  consultada: 2026-11-12

- id: h01-872
  hecho: Sin --expire-unreachable, git reflog toma el tiempo de gc.reflogExpireUnreachable, que por defecto es de 30 días.
  evidencia: "--expire-unreachable=<time> Prune entries older than <time> that are not reachable from the current tip of the branch. If this option is not specified, the expiration time is taken from the configuration setting gc.reflogExpireUnreachable, which in turn defaults to 30 days."
  fuente: f01-25
  ancla: https://git-scm.com/docs/git-reflog
  consultada: 2026-11-12

- id: h01-873
  hecho: La página de git reflog indica que el subcomando expire no suele usarse directamente por los usuarios y remite a git-gc.
  evidencia: 'The "expire" subcommand prunes older reflog entries. Entries older than expire time, or entries older than expire-unreachable time and not reachable from the current tip, are removed from the reflog. This is typically not used directly by end users — instead, see git-gc[1].'
  fuente: f01-25
  ancla: https://git-scm.com/docs/git-reflog
  consultada: 2026-11-12

- id: h01-874
  hecho: Pro Git indica que se pueden aplastar commits con reset y que existe otra forma de hacerlo, la que presenta bajo el título Aplastando, aunque en ese ejemplo reset es más simple.
  evidencia: "Puedes usar reset para aplastarlos rápida y fácilmente en una sola confirmación que lo hace ver realmente inteligente. (Aplastando muestra otra forma de hacerlo, pero en este ejemplo es más simple usar reset.)"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-875
  hecho: La salida de git cat-file -p sobre una etiqueta anotada incluye una línea tagger con el nombre, el correo y la fecha de quien la creó.
  evidencia: "(la opción -a indica que la etiqueta es anotativa) $ git tag -a v1.1 1a410efbd13591db07496601ebc7a059dd55cfe9 -m 'test tag' Este es el objeto SHA-1 creado: $ cat .git/refs/tags/v1.1 9585191f37f7b0fb9444f35a9bf50de191beadc2 Ahora, lanzando el comando cat-file para ese valor SHA-1: $ git cat-file -p 9585191f37f7b0fb9444f35a9bf50de191beadc2 object 1a410efbd13591db07496601ebc7a059dd55cfe9 type commit tag v1.1 tagger Scott Chacon <schacon@gmail.com> Sat May 23 16:48:58 2009 -0700"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-876
  hecho: Por defecto, git log no genera ninguna salida de diff.
  evidencia: "By default, git log does not generate any diff output."
  fuente: f01-30
  ancla: https://git-scm.com/docs/git-log
  consultada: 2026-11-12

- id: h01-877
  hecho: En git log, los commits de fusión no muestran diff aunque se elija un formato como --patch, salvo que se indique una variante de --diff-merges (incluidas -m, -c, --cc y --dd).
  evidencia: "Note that unless one of --diff-merges variants (including short -m, -c, --cc, and --dd options) is explicitly given, merge commits will not show a diff, even if a diff format like --patch is selected, nor will they match search options like -S."
  fuente: f01-30
  ancla: https://git-scm.com/docs/git-log
  consultada: 2026-11-12

- id: h01-878
  hecho: En git log, los commits de fusión tampoco coinciden con opciones de búsqueda como -S salvo que se indique una variante de --diff-merges.
  evidencia: "Note that unless one of --diff-merges variants (including short -m, -c, --cc, and --dd options) is explicitly given, merge commits will not show a diff, even if a diff format like --patch is selected, nor will they match search options like -S."
  fuente: f01-30
  ancla: https://git-scm.com/docs/git-log
  consultada: 2026-11-12

- id: h01-879
  hecho: Con --first-parent, el formato de diff por defecto de los commits de fusión en git log es first-parent.
  evidencia: "Note that unless one of --diff-merges variants (including short -m, -c, --cc, and --dd options) is explicitly given, merge commits will not show a diff, even if a diff format like --patch is selected, nor will they match search options like -S. The exception is when --first-parent is in use, in which case first-parent is the default format for merge commits."
  fuente: f01-30
  ancla: https://git-scm.com/docs/git-log
  consultada: 2026-11-12

- id: h01-880
  hecho: git pull --ff-only solo hace actualizaciones de avance rápido y falla si la rama local ha divergido de la remota.
  evidencia: 'git pull --ff-only will only do "fast-forward" updates: it fails if your local branch has diverged from the remote branch.'
  fuente: f01-34
  ancla: https://git-scm.com/docs/git-pull
  consultada: 2026-11-12

- id: h01-881
  hecho: La opción --ff-only de git pull solo actualiza si no hay historia local divergente, y es el comportamiento por defecto cuando no se indica ningún método para reconciliar historias divergentes.
  evidencia: "--ff-only Only update to the new history if there is no divergent local history. This is the default when no method for reconciling divergent histories is provided (via the --rebase flags)."
  fuente: f01-34
  ancla: https://git-scm.com/docs/git-pull
  consultada: 2026-11-12

- id: h01-882
  hecho: git pull --rebase ejecuta git rebase.
  evidencia: "git pull --rebase runs git rebase"
  fuente: f01-34
  ancla: https://git-scm.com/docs/git-pull
  consultada: 2026-11-12

- id: h01-883
  hecho: git pull --no-rebase ejecuta git merge.
  evidencia: "git pull --no-rebase runs git merge."
  fuente: f01-34
  ancla: https://git-scm.com/docs/git-pull
  consultada: 2026-11-12

- id: h01-884
  hecho: Con --rebase (valor true), git pull rebasa la rama actual sobre la rama upstream después de hacer fetch.
  evidencia: "--rebase[=(true|merges|false|interactive)] true rebase the current branch on top of the upstream branch after fetching."
  fuente: f01-34
  ancla: https://git-scm.com/docs/git-pull
  consultada: 2026-11-12

- id: h01-885
  hecho: Se pueden fijar pull.rebase, pull.squash o pull.ff para elegir el comportamiento preferido de git pull.
  evidencia: "You can also set the configuration options pull.rebase, pull.squash, or pull.ff with your preferred behaviour."
  fuente: f01-34
  ancla: https://git-scm.com/docs/git-pull
  consultada: 2026-11-12

- id: h01-886
  hecho: pull.rebase, branch.<name>.rebase y branch.autoSetupRebase sirven para hacer que git pull use siempre --rebase en lugar de fusionar.
  evidencia: "See pull.rebase, branch.<name>.rebase and branch.autoSetupRebase in git-config[1] if you want to make git pull always use --rebase instead of merging."
  fuente: f01-34
  ancla: https://git-scm.com/docs/git-pull
  consultada: 2026-11-12

- id: h01-887
  hecho: La página de git pull advierte de que --rebase es un modo potencialmente peligroso porque reescribe la historia.
  evidencia: "Note This is a potentially dangerous mode of operation. It rewrites history, which does not bode well when you published that history already."
  fuente: f01-34
  ancla: https://git-scm.com/docs/git-pull
  consultada: 2026-11-12

- id: h01-888
  hecho: Si no se indica modo, git reset usa --mixed por defecto.
  evidencia: "The <mode> must be one of the following (default --mixed):"
  fuente: f01-35
  ancla: https://git-scm.com/docs/git-reset
  consultada: 2026-11-12

- id: h01-889
  hecho: El modo --mixed de git reset deja sin cambios el directorio de trabajo.
  evidencia: "The <mode> must be one of the following (default --mixed): --mixed Leave your working directory unchanged."
  fuente: f01-35
  ancla: https://git-scm.com/docs/git-reset
  consultada: 2026-11-12

- id: h01-890
  hecho: El modo --mixed de git reset actualiza el índice para que coincida con el nuevo HEAD, de modo que no queda nada preparado.
  evidencia: "--mixed Leave your working directory unchanged. Update the index to match the new HEAD, so nothing will be staged."
  fuente: f01-35
  ancla: https://git-scm.com/docs/git-reset
  consultada: 2026-11-12

- id: h01-891
  hecho: El modo --soft de git reset deja sin cambios los archivos del árbol de trabajo y el índice.
  evidencia: "--soft Leave your working tree files and the index unchanged."
  fuente: f01-35
  ancla: https://git-scm.com/docs/git-reset
  consultada: 2026-11-12

- id: h01-892
  hecho: Sin cambios preparados, git reset --soft HEAD~5 seguido de git commit combina los últimos 5 commits en uno.
  evidencia: "--soft Leave your working tree files and the index unchanged. For example, if you have no staged changes, you can use git reset --soft HEAD~5; git commit to combine the last 5 commits into 1 commit."
  fuente: f01-35
  ancla: https://git-scm.com/docs/git-reset
  consultada: 2026-11-12

- id: h01-893
  hecho: El modo --hard de git reset sobrescribe todos los archivos y directorios con la versión de <commit>.
  evidencia: "--hard Overwrite all files and directories with the version from <commit>,"
  fuente: f01-35
  ancla: https://git-scm.com/docs/git-reset
  consultada: 2026-11-12

- id: h01-894
  hecho: El modo --hard de git reset puede sobrescribir archivos sin seguimiento.
  evidencia: "--hard Overwrite all files and directories with the version from <commit>, and may overwrite untracked files."
  fuente: f01-35
  ancla: https://git-scm.com/docs/git-reset
  consultada: 2026-11-12

- id: h01-895
  hecho: Con --hard, los archivos con seguimiento que no están en <commit> se eliminan para que el árbol de trabajo coincida con <commit>.
  evidencia: "--hard Overwrite all files and directories with the version from <commit>, and may overwrite untracked files. Tracked files not in <commit> are removed so that the working tree matches <commit>."
  fuente: f01-35
  ancla: https://git-scm.com/docs/git-reset
  consultada: 2026-11-12

- id: h01-896
  hecho: Con --hard, git reset actualiza el índice para que coincida con el nuevo HEAD, de modo que no queda nada preparado.
  evidencia: "--hard Overwrite all files and directories with the version from <commit>, and may overwrite untracked files. Tracked files not in <commit> are removed so that the working tree matches <commit>. Update the index to match the new HEAD, so nothing will be staged."
  fuente: f01-35
  ancla: https://git-scm.com/docs/git-reset
  consultada: 2026-11-12

- id: h01-897
  hecho: git reset <modo> <commit> cambia el commit al que apunta HEAD.
  evidencia: "git reset [<mode>] <commit> changes which commit HEAD points to."
  fuente: f01-35
  ancla: https://git-scm.com/docs/git-reset
  consultada: 2026-11-12

- id: h01-898
  hecho: Cambiar el commit al que apunta HEAD con git reset permite deshacer operaciones de Git como commit, merge, rebase y pull.
  evidencia: "git reset [<mode>] <commit> changes which commit HEAD points to. This makes it possible to undo various Git operations, for example commit, merge, rebase, and pull."
  fuente: f01-35
  ancla: https://git-scm.com/docs/git-reset
  consultada: 2026-11-12

- id: h01-899
  hecho: Con rutas, git reset fija la versión preparada de los archivos o directorios indicados a la del commit o árbol dado, que por defecto es HEAD.
  evidencia: "git reset [-q] [<tree-ish>] [--] <pathspec>... git reset [-q] [--pathspec-from-file=<file> [--pathspec-file-nul]] [<tree-ish>] For all specified files or directories, set the staged version to the version from the given commit or tree (which defaults to HEAD)."
  fuente: f01-35
  ancla: https://git-scm.com/docs/git-reset
  consultada: 2026-11-12

- id: h01-900
  hecho: git reset <pathspec> es lo opuesto de git add <pathspec>, pues deshace la preparación de los cambios de esos archivos o directorios.
  evidencia: "This means that git reset <pathspec> is the opposite of git add <pathspec>: it unstages all changes to the specified file(s) or directories."
  fuente: f01-35
  ancla: https://git-scm.com/docs/git-reset
  consultada: 2026-11-12

- id: h01-901
  hecho: git reset <pathspec> equivale a git restore --staged <pathspec>.
  evidencia: "This means that git reset <pathspec> is the opposite of git add <pathspec>: it unstages all changes to the specified file(s) or directories. This is equivalent to git restore --staged <pathspec>"
  fuente: f01-35
  ancla: https://git-scm.com/docs/git-reset
  consultada: 2026-11-12

- id: h01-902
  hecho: Con rutas, git reset actualiza solo el índice, sin tocar HEAD ni los archivos del árbol de trabajo.
  evidencia: "In this mode, git reset updates only the index (without updating the HEAD or working tree files)."
  fuente: f01-35
  ancla: https://git-scm.com/docs/git-reset
  consultada: 2026-11-12

- id: h01-903
  hecho: Para actualizar los archivos además de las entradas del índice, la página de git reset remite a git restore.
  evidencia: "In this mode, git reset updates only the index (without updating the HEAD or working tree files). If you want to update the files as well as the index entries, use git-restore[1]."
  fuente: f01-35
  ancla: https://git-scm.com/docs/git-reset
  consultada: 2026-11-12

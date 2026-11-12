# Hechos del capítulo 1: Git por dentro

Hechos atómicos con evidencia literal (cortafuegos 2). Se generan con `scripts/juntar_hechos.py` a partir de `secciones/`; edita la sección y vuelve a juntar.

## 1.1 Qué es el control de versiones

- id: h01-101
  hecho: Un sistema de control de versiones registra los cambios hechos en un archivo o conjunto de archivos a lo largo del tiempo.
  evidencia: "Un control de versiones es un sistema que registra los cambios realizados en un archivo o conjunto de archivos a lo largo del tiempo"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-102
  hecho: El registro de cambios permite recuperar versiones concretas más adelante.
  evidencia: "registra los cambios realizados en un archivo o conjunto de archivos a lo largo del tiempo, de modo que puedas recuperar versiones específicas más adelante"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-103
  hecho: Un VCS permite regresar a versiones anteriores de los archivos y también a una versión anterior del proyecto completo.
  evidencia: "un sistema de control de versiones (VCS por sus siglas en inglés) es una decisión muy acertada. Dicho sistema te permite regresar a versiones anteriores de tus archivos, regresar a una versión anterior del proyecto completo"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-104
  hecho: Con un VCS suele ser posible recuperar fácilmente archivos que se han estropeado o perdido.
  evidencia: "Usar un VCS también significa generalmente que si arruinas o pierdes archivos, será posible recuperarlos fácilmente"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-105
  hecho: Un método habitual de control de versiones es copiar los archivos a otro directorio.
  evidencia: "Un método de control de versiones, usado por muchas personas, es copiar los archivos a otro directorio"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-106
  hecho: Copiar los archivos a otro directorio como método de control de versiones es tremendamente propenso a errores.
  evidencia: "es copiar los archivos a otro directorio (quizás indicando la fecha y hora en que lo hicieron, si son ingeniosos). Este método es muy común porque es muy sencillo, pero también es tremendamente propenso a errores"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-107
  hecho: Es fácil olvidar en qué directorio te encuentras y guardar accidentalmente en el archivo equivocado o sobrescribir archivos que no querías.
  evidencia: "Es fácil olvidar en qué directorio te encuentras y guardar accidentalmente en el archivo equivocado o sobrescribir archivos que no querías."
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-108
  hecho: Los VCS locales llevaban el registro de los cambios en una base de datos sencilla.
  evidencia: "desarrollaron hace tiempo VCS locales que contenían una simple base de datos, en la que se llevaba el registro de todos los cambios realizados a los archivos"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-109
  hecho: RCS guarda conjuntos de parches (es decir, las diferencias entre archivos) en un formato especial en disco.
  evidencia: "RCS, que todavía podemos encontrar en muchas de las computadoras actuales. Incluso el famoso sistema operativo Mac OS X incluye el comando rcs cuando instalas las herramientas de desarrollo. Esta herramienta funciona guardando conjuntos de parches (es decir, las diferencias entre archivos) en un formato especial en disco"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-110
  hecho: Los sistemas de control de versiones centralizados (CVCS) se desarrollaron para resolver el problema de colaborar con desarrolladores en otros sistemas.
  evidencia: "El siguiente gran problema con el que se encuentran las personas es que necesitan colaborar con desarrolladores en otros sistemas. Los sistemas de Control de Versiones Centralizados (CVCS por sus siglas en inglés) fueron desarrollados para solucionar este problema."
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-111
  hecho: CVS, Subversion y Perforce son ejemplos de sistemas de control de versiones centralizados.
  evidencia: "Los sistemas de Control de Versiones Centralizados (CVCS por sus siglas en inglés) fueron desarrollados para solucionar este problema. Estos sistemas, como CVS, Subversion y Perforce, tienen un único servidor"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-112
  hecho: Un sistema centralizado tiene un único servidor con todos los archivos versionados y varios clientes que los descargan de ahí.
  evidencia: "Los sistemas de Control de Versiones Centralizados (CVCS por sus siglas en inglés) fueron desarrollados para solucionar este problema. Estos sistemas, como CVS, Subversion y Perforce, tienen un único servidor que contiene todos los archivos versionados y varios clientes que descargan los archivos desde ese lugar central"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-113
  hecho: En un sistema centralizado, todas las personas saben hasta cierto punto en qué trabajan las demás.
  evidencia: "Figura 2. Control de versiones centralizado. Esta configuración ofrece muchas ventajas, especialmente frente a VCS locales. Por ejemplo, todas las personas saben hasta cierto punto en qué están trabajando los otros colaboradores del proyecto"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-114
  hecho: En un sistema centralizado, los administradores controlan al detalle qué puede hacer cada usuario.
  evidencia: "Figura 2. Control de versiones centralizado. Esta configuración ofrece muchas ventajas, especialmente frente a VCS locales. Por ejemplo, todas las personas saben hasta cierto punto en qué están trabajando los otros colaboradores del proyecto. Los administradores tienen control detallado sobre qué puede hacer cada usuario"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-115
  hecho: Es mucho más fácil administrar un CVCS que tener que lidiar con bases de datos locales en cada cliente.
  evidencia: "es mucho más fácil administrar un CVCS que tener que lidiar con bases de datos locales en cada cliente"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-116
  hecho: La desventaja más obvia de un sistema centralizado es que el servidor es un punto único de fallo.
  evidencia: "Sin embargo, esta configuración también tiene serias desventajas. La más obvia es el punto único de fallo que representa el servidor centralizado."
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-117
  hecho: Si el servidor centralizado se cae durante una hora, durante esa hora nadie puede colaborar ni guardar cambios en los archivos en los que había estado trabajando.
  evidencia: "La más obvia es el punto único de fallo que representa el servidor centralizado. Si ese servidor se cae durante una hora, entonces durante esa hora nadie podrá colaborar o guardar cambios en archivos en los que hayan estado trabajando."
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-118
  hecho: Si se corrompe el disco duro con la base de datos central y no se han hecho copias de seguridad adecuadas, se pierde toda la información del proyecto, salvo las copias instantáneas que las personas tengan en sus máquinas locales.
  evidencia: "Si el disco duro en el que se encuentra la base de datos central se corrompe, y no se han realizado copias de seguridad adecuadamente, se perderá toda la información del proyecto, con excepción de las copias instantáneas que las personas tengan en sus máquinas locales"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-119
  hecho: Git, Mercurial, Bazaar y Darcs son ejemplos de sistemas de control de versiones distribuidos.
  evidencia: "Los sistemas de Control de Versiones Distribuidos (DVCS por sus siglas en inglés) ofrecen soluciones para los problemas que han sido mencionados. En un DVCS (como Git, Mercurial, Bazaar o Darcs)"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-120
  hecho: En un DVCS, los clientes no solo descargan la última copia instantánea de los archivos, sino que replican completamente el repositorio.
  evidencia: "En un DVCS (como Git, Mercurial, Bazaar o Darcs), los clientes no solo descargan la última copia instantánea de los archivos, sino que se replica completamente el repositorio"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-121
  hecho: Cada clon es realmente una copia completa de todos los datos.
  evidencia: "Cada clon es realmente una copia completa de todos los datos."
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-122
  hecho: Si un servidor deja de funcionar y los sistemas colaboraban a través de él, cualquiera de los repositorios disponibles en los clientes puede copiarse al servidor para restaurarlo.
  evidencia: "De esta manera, si un servidor deja de funcionar y estos sistemas estaban colaborando a través de él, cualquiera de los repositorios disponibles en los clientes puede ser copiado al servidor con el fin de restaurarlo"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-123
  hecho: Muchos sistemas distribuidos manejan numerosos repositorios remotos, de modo que puedes colaborar simultáneamente con diferentes grupos de personas dentro del mismo proyecto.
  evidencia: "Figura 3. Control de versiones distribuido. Además, muchos de estos sistemas se encargan de manejar numerosos repositorios remotos con los cuales pueden trabajar, de tal forma que puedes colaborar simultáneamente con diferentes grupos de personas en distintas maneras dentro del mismo proyecto"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-124
  hecho: Se pueden establecer varios flujos de trabajo que no son posibles en sistemas centralizados, como los modelos jerárquicos.
  evidencia: "Esto permite establecer varios flujos de trabajo que no son posibles en sistemas centralizados, como pueden ser los modelos jerárquicos."
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-125
  hecho: Durante la mayor parte del mantenimiento del kernel de Linux (1991-2002), los cambios en el software se realizaban a través de parches y archivos.
  evidencia: "Durante la mayor parte del mantenimiento del kernel de Linux (1991-2002), los cambios en el software se realizaban a través de parches y archivos"
  fuente: f01-02
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Una-breve-historia-de-Git
  consultada: 2026-11-12

- id: h01-126
  hecho: En 2002, el proyecto del kernel de Linux empezó a usar BitKeeper, un DVCS propietario.
  evidencia: "En el 2002, el proyecto del kernel de Linux empezó a usar un DVCS propietario llamado BitKeeper."
  fuente: f01-02
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Una-breve-historia-de-Git
  consultada: 2026-11-12

- id: h01-127
  hecho: En 2005, la relación entre la comunidad del kernel de Linux y la compañía de BitKeeper se vino abajo y la herramienta dejó de ofrecerse gratis.
  evidencia: "En el 2005, la relación entre la comunidad que desarrollaba el kernel de Linux y la compañía que desarrollaba BitKeeper se vino abajo y la herramienta dejó de ser ofrecida de manera gratuita."
  fuente: f01-02
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Una-breve-historia-de-Git
  consultada: 2026-11-12

- id: h01-128
  hecho: Que la herramienta dejara de ofrecerse gratis impulsó a la comunidad de desarrollo de Linux, y en particular a Linus Torvalds, a desarrollar su propia herramienta.
  evidencia: "la herramienta dejó de ser ofrecida de manera gratuita. Esto impulsó a la comunidad de desarrollo de Linux (y en particular a Linus Torvalds, el creador de Linux) a desarrollar su propia herramienta"
  fuente: f01-02
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Una-breve-historia-de-Git
  consultada: 2026-11-12

- id: h01-129
  hecho: Velocidad fue uno de los objetivos del nuevo sistema.
  evidencia: "Algunos de los objetivos del nuevo sistema fueron los siguientes: Velocidad"
  fuente: f01-02
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Una-breve-historia-de-Git
  consultada: 2026-11-12

- id: h01-130
  hecho: Un gran soporte para el desarrollo no lineal (miles de ramas paralelas) fue uno de los objetivos del nuevo sistema.
  evidencia: "Algunos de los objetivos del nuevo sistema fueron los siguientes: Velocidad Diseño sencillo Gran soporte para desarrollo no lineal (miles de ramas paralelas)"
  fuente: f01-02
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Una-breve-historia-de-Git
  consultada: 2026-11-12

- id: h01-131
  hecho: Ser completamente distribuido fue uno de los objetivos del nuevo sistema.
  evidencia: "Algunos de los objetivos del nuevo sistema fueron los siguientes: Velocidad Diseño sencillo Gran soporte para desarrollo no lineal (miles de ramas paralelas) Completamente distribuido"
  fuente: f01-02
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Una-breve-historia-de-Git
  consultada: 2026-11-12

- id: h01-132
  hecho: Ser capaz de manejar grandes proyectos, como el kernel de Linux, con eficiencia en velocidad y tamaño de los datos fue uno de los objetivos del nuevo sistema.
  evidencia: "Algunos de los objetivos del nuevo sistema fueron los siguientes: Velocidad Diseño sencillo Gran soporte para desarrollo no lineal (miles de ramas paralelas) Completamente distribuido Capaz de manejar grandes proyectos (como el kernel de Linux) eficientemente (velocidad y tamaño de los datos)"
  fuente: f01-02
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Una-breve-historia-de-Git
  consultada: 2026-11-12

- id: h01-133
  hecho: Un diseño sencillo fue otro de los objetivos del nuevo sistema.
  evidencia: "Algunos de los objetivos del nuevo sistema fueron los siguientes: Velocidad Diseño sencillo"
  fuente: f01-02
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Una-breve-historia-de-Git
  consultada: 2026-11-12

- id: h01-134
  hecho: RCS fue una de las herramientas de control de versiones más populares.
  evidencia: "Una de las herramientas de control de versiones más popular fue un sistema llamado RCS"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

## 1.2 Fotos, no diferencias; los tres estados

- id: h01-201
  hecho: Conceptualmente, la mayoría de los otros sistemas de control de versiones almacenan la información como una lista de cambios en los archivos.
  evidencia: "La principal diferencia entre Git y cualquier otro VCS (incluyendo Subversion y sus amigos) es la forma en la que manejan sus datos. Conceptualmente, la mayoría de los otros sistemas almacenan la información como una lista de cambios en los archivos"
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-202
  hecho: Git maneja sus datos como un conjunto de copias instantáneas de un sistema de archivos miniatura.
  evidencia: "Git maneja sus datos como un conjunto de copias instantáneas de un sistema de archivos miniatura"
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-203
  hecho: Cada vez que confirmas un cambio, Git toma una foto del aspecto de todos los archivos en ese momento y guarda una referencia a esa copia instantánea.
  evidencia: "Cada vez que confirmas un cambio, o guardas el estado de tu proyecto en Git, él básicamente toma una foto del aspecto de todos tus archivos en ese momento y guarda una referencia a esa copia instantánea"
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-204
  hecho: Si un archivo no se ha modificado, Git no lo almacena de nuevo, sino que guarda un enlace al archivo anterior idéntico.
  evidencia: "si los archivos no se han modificado Git no almacena el archivo de nuevo, sino un enlace al archivo anterior idéntico que ya tiene almacenado"
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-205
  hecho: Git maneja sus datos como una secuencia de copias instantáneas.
  evidencia: "Git maneja sus datos como una secuencia de copias instantáneas."
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-206
  hecho: La mayoría de las operaciones de Git solo necesitan archivos y recursos locales para funcionar.
  evidencia: "La mayoría de las operaciones en Git sólo necesitan archivos y recursos locales para funcionar."
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-207
  hecho: Debido a que tienes toda la historia del proyecto en tu disco local, la mayoría de las operaciones parecen prácticamente inmediatas.
  evidencia: "Debido a que tienes toda la historia del proyecto ahí mismo, en tu disco local, la mayoría de las operaciones parecen prácticamente inmediatas"
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-208
  hecho: Si estás en un avión o en un tren y quieres trabajar un poco, puedes confirmar tus cambios hasta que consigas una conexión de red para subirlos.
  evidencia: "Si te subes a un avión o a un tren y quieres trabajar un poco, puedes confirmar tus cambios felizmente hasta que consigas una conexión de red para subirlos"
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-209
  hecho: Todo en Git se verifica mediante una suma de comprobación antes de ser almacenado.
  evidencia: "Todo en Git es verificado mediante una suma de comprobación (checksum en inglés) antes de ser almacenado"
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-210
  hecho: Es imposible cambiar el contenido de un archivo o directorio sin que Git lo sepa.
  evidencia: "es imposible cambiar los contenidos de cualquier archivo o directorio sin que Git lo sepa"
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-211
  hecho: El mecanismo que usa Git para generar la suma de comprobación es el hash SHA-1.
  evidencia: "El mecanismo que usa Git para generar esta suma de comprobación se conoce como hash SHA-1."
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-212
  hecho: Un hash SHA-1 es una cadena de 40 caracteres hexadecimales.
  evidencia: "se conoce como hash SHA-1. Se trata de una cadena de 40 caracteres hexadecimales (0-9 y a-f)"
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-213
  hecho: El hash SHA-1 se calcula con base en los contenidos del archivo o la estructura del directorio en Git.
  evidencia: "se conoce como hash SHA-1. Se trata de una cadena de 40 caracteres hexadecimales (0-9 y a-f), y se calcula con base en los contenidos del archivo o estructura del directorio en Git"
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-214
  hecho: Git guarda todo por el valor hash de sus contenidos y no por el nombre de archivo.
  evidencia: "Git guarda todo no por nombre de archivo, sino por el valor hash de sus contenidos."
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-215
  hecho: Casi todas las acciones de Git solo añaden información a la base de datos de Git.
  evidencia: "Cuando realizas acciones en Git, casi todas ellas sólo añaden información a la base de datos de Git"
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-216
  hecho: Después de confirmar una copia instantánea en Git es muy difícil perderla.
  evidencia: "después de confirmar una copia instantánea en Git es muy difícil perderla"
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-217
  hecho: Git tiene tres estados principales para los archivos: confirmado, modificado y preparado.
  evidencia: "Git tiene tres estados principales en los que se pueden encontrar tus archivos: confirmado (committed), modificado (modified), y preparado (staged)."
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-218
  hecho: El estado confirmado significa que los datos están almacenados de manera segura en la base de datos local.
  evidencia: "Confirmado: significa que los datos están almacenados de manera segura en tu base de datos local."
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-219
  hecho: Un archivo modificado ha cambiado, pero todavía no se ha confirmado a la base de datos.
  evidencia: "Modificado: significa que has modificado el archivo pero todavía no lo has confirmado a tu base de datos."
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-220
  hecho: Un archivo preparado es un archivo modificado marcado, en su versión actual, para ir en la próxima confirmación.
  evidencia: "Preparado: significa que has marcado un archivo modificado en su versión actual para que vaya en tu próxima confirmación."
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-221
  hecho: Un proyecto de Git tiene tres secciones principales: el directorio de Git, el directorio de trabajo y el área de preparación.
  evidencia: "las tres secciones principales de un proyecto de Git: El directorio de Git (Git directory), el directorio de trabajo (working directory), y el área de preparación (staging area)."
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-222
  hecho: El directorio de Git almacena los metadatos y la base de datos de objetos del proyecto.
  evidencia: "El directorio de Git es donde se almacenan los metadatos y la base de datos de objetos para tu proyecto."
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-223
  hecho: El directorio de Git es lo que se copia al clonar un repositorio desde otra computadora.
  evidencia: "El directorio de Git es donde se almacenan los metadatos y la base de datos de objetos para tu proyecto. Es la parte más importante de Git, y es lo que se copia cuando clonas un repositorio desde otra computadora"
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-224
  hecho: El directorio de trabajo es una copia de una versión del proyecto.
  evidencia: "El directorio de trabajo es una copia de una versión del proyecto."
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-225
  hecho: Los archivos del directorio de trabajo se sacan de la base de datos comprimida del directorio de Git y se colocan en disco para usarlos o modificarlos.
  evidencia: "El directorio de trabajo es una copia de una versión del proyecto. Estos archivos se sacan de la base de datos comprimida en el directorio de Git, y se colocan en disco para que los puedas usar o modificar."
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-226
  hecho: El área de preparación es un archivo, generalmente dentro del directorio de Git, que almacena información sobre lo que irá en la próxima confirmación.
  evidencia: "El área de preparación es un archivo, generalmente contenido en tu directorio de Git, que almacena información acerca de lo que va a ir en tu próxima confirmación."
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-227
  hecho: El flujo de trabajo básico en Git empieza modificando una serie de archivos en el directorio de trabajo.
  evidencia: "El flujo de trabajo básico en Git es algo así: Modificas una serie de archivos en tu directorio de trabajo."
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-228
  hecho: En el flujo de trabajo básico de Git, después de modificar archivos en el directorio de trabajo, los preparas añadiéndolos al área de preparación.
  evidencia: "El flujo de trabajo básico en Git es algo así: Modificas una serie de archivos en tu directorio de trabajo. Preparas los archivos, añadiéndolos a tu área de preparación."
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-229
  hecho: Después de preparar los archivos, confirmas los cambios: se toman los archivos tal como están en el área de preparación y se almacena esa copia instantánea de forma permanente en el directorio de Git.
  evidencia: "Preparas los archivos, añadiéndolos a tu área de preparación. Confirmas los cambios, lo que toma los archivos tal y como están en el área de preparación y almacena esa copia instantánea de manera permanente en tu directorio de Git."
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-230
  hecho: Una versión de un archivo que está en el directorio de Git se considera confirmada.
  evidencia: "Si una versión concreta de un archivo está en el directorio de Git, se considera confirmada (committed)."
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-231
  hecho: Una versión de un archivo que ha sufrido cambios desde que se obtuvo del repositorio y ha sido añadida al área de preparación está preparada.
  evidencia: "Si una versión concreta de un archivo está en el directorio de Git, se considera confirmada (committed). Si ha sufrido cambios desde que se obtuvo del repositorio, pero ha sido añadida al área de preparación, está preparada (staged)."
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-232
  hecho: Una versión de un archivo que ha sufrido cambios desde que se obtuvo del repositorio y no se ha preparado está modificada.
  evidencia: "Si una versión concreta de un archivo está en el directorio de Git, se considera confirmada (committed). Si ha sufrido cambios desde que se obtuvo del repositorio, pero ha sido añadida al área de preparación, está preparada (staged). Y si ha sufrido cambios desde que se obtuvo del repositorio, pero no se ha preparado, está modificada (modified)."
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-233
  hecho: Los archivos rastreados son los que estaban en la última instantánea del proyecto.
  evidencia: "Los archivos rastreados (tracked files en inglés) son todos aquellos archivos que estaban en la última instantánea del proyecto"
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-234
  hecho: Un archivo rastreado puede estar sin modificar, modificado o preparado.
  evidencia: "Los archivos rastreados (tracked files en inglés) son todos aquellos archivos que estaban en la última instantánea del proyecto; pueden ser archivos sin modificar, modificados o preparados"
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-235
  hecho: Los archivos sin rastrear son los del directorio de trabajo que no estaban en la última instantánea ni están en el área de preparación.
  evidencia: "Los archivos sin rastrear son todos los demás - cualquier otro archivo en tu directorio de trabajo que no estaba en tu última instantánea y que no está en el área de preparación (staging area)"
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-236
  hecho: Al clonar un repositorio por primera vez, todos los archivos están rastreados y sin modificar.
  evidencia: "Cuando clonas por primera vez un repositorio, todos tus archivos estarán rastreados y sin modificar"
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-237
  hecho: El ciclo de los archivos consiste en preparar los modificados, confirmar los preparados y repetir.
  evidencia: "Luego preparas estos archivos modificados y finalmente confirmas todos los cambios preparados, y repites el ciclo."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-238
  hecho: El comando git status es la herramienta principal para saber qué archivos están en qué estado.
  evidencia: "La herramienta principal para determinar qué archivos están en qué estado es el comando git status."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-239
  hecho: Un directorio de trabajo limpio es aquel en el que no hay archivos rastreados y modificados.
  evidencia: "Esto significa que tienes un directorio de trabajo limpio - en otras palabras, que no hay archivos rastreados y modificados."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-240
  hecho: Un archivo sin rastrear es un archivo que Git ve y que no estaba en el commit anterior.
  evidencia: "Sin rastrear significa que Git ve archivos que no tenías en el commit anterior."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-241
  hecho: Git no incluye un archivo sin rastrear en el próximo commit a menos que se lo indiques explícitamente.
  evidencia: "Sin rastrear significa que Git ve archivos que no tenías en el commit anterior. Git no los incluirá en tu próximo commit a menos que se lo indiques explícitamente."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-242
  hecho: Para comenzar a rastrear un archivo se usa el comando git add.
  evidencia: "Para comenzar a rastrear un archivo debes usar el comando git add."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-243
  hecho: Tras ejecutar git add README para comenzar a rastrear el archivo README, este aparece rastreado y preparado para ser confirmado.
  evidencia: "Para comenzar a rastrear el archivo README, puedes ejecutar lo siguiente: $ git add README Ahora si vuelves a ver el estado del proyecto, verás que el archivo README está siendo rastreado y está preparado para ser confirmado"
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-244
  hecho: git add sirve para empezar a rastrear archivos nuevos, preparar archivos y marcar como resueltos los archivos en conflicto por combinación.
  evidencia: "git add es un comando que cumple varios propósitos - lo usas para empezar a rastrear archivos nuevos, preparar archivos, y hacer otras cosas como marcar archivos en conflicto por combinación como resueltos"
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-245
  hecho: En el ejemplo de la fuente, CONTRIBUTING.md aparece a la vez como preparado y como no preparado.
  evidencia: "Ahora CONTRIBUTING.md aparece como preparado y como no preparado."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-246
  hecho: Git prepara un archivo según el estado que tenía cuando ejecutaste git add.
  evidencia: "Resulta que Git prepara un archivo de acuerdo al estado que tenía cuando ejecutas el comando git add."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-247
  hecho: Si modificas un archivo después de git add, debes ejecutar git add de nuevo para preparar su última versión.
  evidencia: "Si modificas un archivo luego de ejecutar git add, deberás ejecutar git add de nuevo para preparar la última versión del archivo"
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-248
  hecho: git status -s y git status --short muestran una salida mucho más simplificada.
  evidencia: "Si ejecutas git status -s o git status --short, obtendrás una salida mucho más simplificada."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-249
  hecho: En la salida de git status -s, los archivos nuevos sin rastrear llevan ??, los preparados una A y los modificados una M.
  evidencia: "$ git status -s M README MM Rakefile A lib/git.rb M lib/simplegit.rb ?? LICENSE.txt Los archivos nuevos que no están rastreados tienen un ?? a su lado, los archivos que están preparados tienen una A y los modificados una M."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-250
  hecho: El estado aparece en dos columnas: la columna de la izquierda indica el estado preparado y la de la derecha el estado sin preparar.
  evidencia: "El estado aparece en dos columnas - la columna de la izquierda indica el estado preparado y la columna de la derecha indica el estado sin preparar."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-251
  hecho: Para archivos generados automáticamente, como trazas o archivos creados por el sistema de compilación, puedes crear un archivo llamado .gitignore que liste patrones a considerar.
  evidencia: "Este suele ser el caso de archivos generados automáticamente como trazas o archivos creados por tu sistema de compilación. En estos casos, puedes crear un archivo llamado .gitignore que liste patrones a considerar."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-252
  hecho: Crear un archivo .gitignore antes de empezar a trabajar suele ser buena idea para no confirmar archivos no deseados por accidente.
  evidencia: "Crear un archivo .gitignore antes de comenzar a trabajar es generalmente una buena idea, pues así evitas confirmar accidentalmente archivos que en realidad no quieres incluir en tu repositorio Git."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-253
  hecho: En .gitignore se usan patrones glob estándar que se aplican recursivamente a todo el directorio del repositorio local.
  evidencia: "Las reglas sobre los patrones que puedes incluir en el archivo .gitignore son las siguientes: Ignorar las líneas en blanco y aquellas que comiencen con #. Emplear patrones glob estándar que se aplicarán recursivamente a todo el directorio del repositorio local."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-254
  hecho: Los patrones pueden negarse si se añade al principio el signo de exclamación (!).
  evidencia: "Los patrones pueden negarse si se añade al principio el signo de exclamación (!)."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-255
  hecho: git diff muestra las líneas exactas que fueron añadidas y eliminadas, es decir, el parche.
  evidencia: "git diff te muestra las líneas exactas que fueron añadidas y eliminadas, es decir, el parche."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-256
  hecho: Comparar lo que hay en el directorio de trabajo con lo que está en el área de preparación indica los cambios hechos que aún no se han preparado.
  evidencia: "Este comando compara lo que tienes en tu directorio de trabajo con lo que está en el área de preparación. El resultado te indica los cambios que has hecho pero que aun no has preparado."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-257
  hecho: git diff --staged muestra lo que has preparado y se incluirá en la próxima confirmación.
  evidencia: "Si quieres ver lo que has preparado y será incluido en la próxima confirmación, puedes usar git diff --staged."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-258
  hecho: git diff --staged compara los cambios preparados con la última instantánea confirmada.
  evidencia: "Si quieres ver lo que has preparado y será incluido en la próxima confirmación, puedes usar git diff --staged. Este comando compara tus cambios preparados con la última instantánea confirmada."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-259
  hecho: git diff sin parámetros no muestra los cambios desde la última confirmación, solo los no preparados.
  evidencia: "al llamar a git diff sin parámetros no verás los cambios desde tu última confirmación - solo verás los cambios que aun no están preparados."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-260
  hecho: Las opciones --staged y --cached de git diff son sinónimos.
  evidencia: "y git diff --cached para ver que has preparado hasta ahora (--staged y --cached son sinónimos)"
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-261
  hecho: La forma más sencilla de confirmar es ejecutar git commit.
  evidencia: "La forma más sencilla de confirmar es escribiendo git commit:"
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-262
  hecho: Un archivo creado o modificado que no se ha agregado con git add desde su edición no será confirmado.
  evidencia: "cualquier archivo que hayas creado o modificado y que no hayas agregado con git add desde su edición - no será confirmado."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-263
  hecho: Una confirmación guarda una instantánea del área de preparación.
  evidencia: "Recuerda que la confirmación guarda una instantánea de tu área de preparación."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-264
  hecho: Cada commit guarda una instantánea del proyecto que se puede usar para comparar o volver a ella luego.
  evidencia: "Cada vez que realizas un commit, guardas una instantánea de tu proyecto la cual puedes usar para comparar o volver a ella luego."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-265
  hecho: La opción -a de git commit hace que Git prepare automáticamente todos los archivos rastreados antes de confirmar.
  evidencia: "Añadiendo la opción -a al comando git commit harás que Git prepare automáticamente todos los archivos rastreados antes de confirmarlos"
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-266
  hecho: Para eliminar un archivo de Git hay que quitarlo de los archivos rastreados, es decir, del área de preparación, y luego confirmar.
  evidencia: "Para eliminar archivos de Git, debes eliminarlos de tus archivos rastreados (o mejor dicho, eliminarlos del área de preparación) y luego confirmar"
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-267
  hecho: git rm, además de quitar el archivo del seguimiento, lo elimina del directorio de trabajo.
  evidencia: "Para eliminar archivos de Git, debes eliminarlos de tus archivos rastreados (o mejor dicho, eliminarlos del área de preparación) y luego confirmar. Para ello existe el comando git rm, que además elimina el archivo de tu directorio de trabajo"
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-268
  hecho: Si modificaste un archivo y ya lo habías añadido al índice, tendrás que forzar su eliminación con la opción -f.
  evidencia: "Si modificaste el archivo y ya lo habías añadido al índice, tendrás que forzar su eliminación con la opción -f."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-269
  hecho: Git no rastrea explícitamente los cambios de nombre de archivos.
  evidencia: "Git no rastrea explícitamente los cambios de nombre en archivos."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-270
  hecho: Si renombras un archivo en Git, no se guarda ningún metadato que indique el cambio de nombre.
  evidencia: "Si renombras un archivo en Git, no se guardará ningún metadato que indique que renombraste el archivo"
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-271
  hecho: La única diferencia real del comando mv es que es un solo comando en vez de tres, y existe por conveniencia.
  evidencia: "La única diferencia real es que mv es un solo comando en vez de tres - existe por conveniencia."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-272
  hecho: Puede haber archivos que no quieres que Git añada automáticamente o que ni siquiera aparezcan como no rastreados.
  evidencia: "A veces, tendrás algún tipo de archivo que no quieres que Git añada automáticamente o más aun, que ni siquiera quieras que aparezca como no rastreado."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-273
  hecho: Para ver qué has cambiado pero aún no has preparado, se escribe git diff sin más parámetros.
  evidencia: "Para ver qué has cambiado pero aun no has preparado, escribe git diff sin más parámetros"
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-274
  hecho: Da igual renombrar un archivo con mv, git rm y git add o con el comando mv: Git se da cuenta de que es un renombramiento implícito.
  evidencia: "$ mv README.md README $ git rm README.md $ git add README Git se da cuenta que es un renombramiento implícito, así que no importa si renombras el archivo de esa manera o a través del comando mv."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

## 1.2 Fotos, no diferencias; los tres estados (documentación de referencia de Git)

- id: h01-275
  hecho: El comando git init crea un repositorio vacío, que básicamente es un directorio .git con subdirectorios para objects, refs/heads y refs/tags, y archivos de plantilla.
  evidencia: "This command creates an empty Git repository - basically a .git directory with subdirectories for objects, refs/heads, refs/tags, and template files."
  fuente: f01-17
  ancla: https://git-scm.com/docs/git-init
  consultada: 2026-11-12

- id: h01-276
  hecho: Al ejecutar git init se crea también una rama inicial que no tiene ningún commit.
  evidencia: "An initial branch without any commits will be created"
  fuente: f01-17
  ancla: https://git-scm.com/docs/git-init
  consultada: 2026-11-12

- id: h01-277
  hecho: Las opciones -b y --initial-branch de git init permiten dar nombre a la rama inicial del repositorio recién creado.
  evidencia: "-b <branch-name> --initial-branch=<branch-name> Use <branch-name> for the initial branch in the newly created repository."
  fuente: f01-17
  ancla: https://git-scm.com/docs/git-init
  consultada: 2026-11-12

- id: h01-278
  hecho: Si no se indica nombre para la rama inicial, Git usa el nombre por defecto, que actualmente es master y cambiará a main cuando se publique Git 3.0.
  evidencia: "If not specified, fall back to the default name (currently master, but this will change to main when Git 3.0 is released)."
  fuente: f01-17
  ancla: https://git-scm.com/docs/git-init
  consultada: 2026-11-12

- id: h01-279
  hecho: El nombre por defecto de la rama inicial se puede personalizar con la variable de configuración init.defaultBranch.
  evidencia: "The default name can be customized via the init.defaultBranch configuration variable."
  fuente: f01-17
  ancla: https://git-scm.com/docs/git-init
  consultada: 2026-11-12

- id: h01-280
  hecho: La opción --object-format de git init fija el formato de objeto (el algoritmo hash) del repositorio; los valores válidos son sha1 y, si está habilitado, sha256, y sha1 es el valor por defecto.
  evidencia: "Specify the given object <format> (hash algorithm) for the repository. The valid values are sha1 and (if enabled) sha256. sha1 is the default."
  fuente: f01-17
  ancla: https://git-scm.com/docs/git-init
  consultada: 2026-11-12

- id: h01-281
  hecho: La opción --bare de git init crea un repositorio bare.
  evidencia: "Create a bare repository."
  fuente: f01-17
  ancla: https://git-scm.com/docs/git-init
  consultada: 2026-11-12

- id: h01-282
  hecho: Ejecutar git init en un repositorio que ya existe es seguro.
  evidencia: "Running git init in an existing repository is safe."
  fuente: f01-17
  ancla: https://git-scm.com/docs/git-init
  consultada: 2026-11-12

- id: h01-283
  hecho: Según la documentación de git init, por ahora no hay interoperabilidad entre repositorios SHA-256 y repositorios SHA-1.
  evidencia: "Note: At present, there is no interoperability between SHA-256 repositories and SHA-1 repositories."
  fuente: f01-17
  ancla: https://git-scm.com/docs/git-init
  consultada: 2026-11-12

- id: h01-284
  hecho: En su núcleo, el sistema de control de versiones Git es un sistema de archivos direccionable por contenido.
  evidencia: "At its core, the Git version control system is a content addressable filesystem."
  fuente: f01-18
  ancla: https://git-scm.com/docs/hash-function-transition
  consultada: 2026-11-12

- id: h01-285
  hecho: Git usa la función hash SHA-1 para nombrar el contenido.
  evidencia: "At its core, the Git version control system is a content addressable filesystem. It uses the SHA-1 hash function to name content."
  fuente: f01-18
  ancla: https://git-scm.com/docs/hash-function-transition
  consultada: 2026-11-12

- id: h01-286
  hecho: Los archivos, directorios y revisiones se refieren mediante valores hash, a diferencia de otros sistemas de control de versiones tradicionales, donde se refieren mediante números secuenciales.
  evidencia: "files, directories, and revisions are referred to by hash values unlike in other traditional version control systems where files or versions are referred to via sequential numbers."
  fuente: f01-18
  ancla: https://git-scm.com/docs/hash-function-transition
  consultada: 2026-11-12

- id: h01-287
  hecho: Comprobar la integridad es fácil con un hash: un cambio de bits se detecta porque el hash del contenido corrupto no coincide con su nombre.
  evidencia: "Integrity checking is easy. Bit flips, for example, are easily detected, as the hash of corrupted content does not match its name."
  fuente: f01-18
  ancla: https://git-scm.com/docs/hash-function-transition
  consultada: 2026-11-12

- id: h01-288
  hecho: El 23 de febrero de 2017 el ataque SHAttered demostró una colisión práctica de hash SHA-1.
  evidencia: "On 23 February 2017 the SHAttered attack (https://shattered.io) demonstrated a practical SHA-1 hash collision."
  fuente: f01-18
  ancla: https://git-scm.com/docs/hash-function-transition
  consultada: 2026-11-12

- id: h01-289
  hecho: Git v2.13.0 y posteriores pasaron por defecto a una implementación reforzada de SHA-1 que no es vulnerable al ataque SHAttered.
  evidencia: "Git v2.13.0 and later subsequently moved to a hardened SHA-1 implementation by default, which isn’t vulnerable to the SHAttered attack"
  fuente: f01-18
  ancla: https://git-scm.com/docs/hash-function-transition
  consultada: 2026-11-12

- id: h01-290
  hecho: Aun con la implementación reforzada, SHA-1 sigue siendo débil.
  evidencia: "which isn’t vulnerable to the SHAttered attack, but SHA-1 is still weak."
  fuente: f01-18
  ancla: https://git-scm.com/docs/hash-function-transition
  consultada: 2026-11-12

- id: h01-291
  hecho: Se considera prudente pasar a un nuevo hash y dejar atrás cualquier variante de SHA-1.
  evidencia: "Thus it’s considered prudent to move past any variant of SHA-1 to a new hash."
  fuente: f01-18
  ancla: https://git-scm.com/docs/hash-function-transition
  consultada: 2026-11-12

- id: h01-292
  hecho: A finales de 2018 el proyecto eligió SHA-256 como hash sucesor de SHA-1, entre varios candidatos.
  evidencia: "There were several contenders for a successor hash to SHA-1, including SHA-256, SHA-512/256, SHA-256x16, K12, and BLAKE2bp-256. In late 2018 the project picked SHA-256 as its successor hash."
  fuente: f01-18
  ancla: https://git-scm.com/docs/hash-function-transition
  consultada: 2026-11-12

- id: h01-293
  hecho: En el diseño de la transición, un objeto puede nombrarse con su nombre SHA-1 de 40 dígitos hexadecimales o con su nombre SHA-256 de 64 dígitos hexadecimales.
  evidencia: "Objects can be named by their 40 hexadecimal digit SHA-1 name or 64 hexadecimal digit SHA-256 name"
  fuente: f01-18
  ancla: https://git-scm.com/docs/hash-function-transition
  consultada: 2026-11-12

- id: h01-294
  hecho: El nombre SHA-1 de un objeto es el SHA-1 de la concatenación de su tipo, su longitud, un byte nulo y su contenido.
  evidencia: "The SHA-1 name of an object is the SHA-1 of the concatenation of its type, length, a nul byte, and the object’s SHA-1 content."
  fuente: f01-18
  ancla: https://git-scm.com/docs/hash-function-transition
  consultada: 2026-11-12

## 1.3 Leer y deshacer el historial

- id: h01-301
  hecho: git log es la herramienta más básica y potente para mirar atrás y ver qué modificaciones se han hecho.
  evidencia: "probablemente quieras mirar atrás para ver qué modificaciones se han llevado a cabo. La herramienta más básica y potente para hacer esto es el comando git log."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-302
  hecho: Sin parámetros, git log lista las confirmaciones en orden cronológico inverso.
  evidencia: "Por defecto, si no pasas ningún parámetro, git log lista las confirmaciones hechas sobre ese repositorio en orden cronológico inverso."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-303
  hecho: Cada entrada de git log muestra la suma de comprobación SHA-1, el autor con su correo, la fecha y el mensaje de la confirmación.
  evidencia: "git log lista las confirmaciones hechas sobre ese repositorio en orden cronológico inverso. Es decir, las confirmaciones más recientes se muestran al principio. Como puedes ver, este comando lista cada confirmación con su suma de comprobación SHA-1, el nombre y dirección de correo del autor, la fecha y el mensaje de confirmación."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-304
  hecho: La opción -p de git log muestra las diferencias introducidas en cada confirmación.
  evidencia: "El comando git log proporciona gran cantidad de opciones para mostrarte exactamente lo que buscas. Aquí veremos algunas de las más usadas. Una de las opciones más útiles es -p, que muestra las diferencias introducidas en cada confirmación."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-305
  hecho: Mostrar tras cada entrada las diferencias que le corresponden resulta muy útil para revisiones de código.
  evidencia: "añadiendo tras cada entrada las diferencias que le corresponden. Esto resulta muy útil para revisiones de código"
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-306
  hecho: git log acepta la opción -<n>, siendo n cualquier entero, para mostrar las últimas n confirmaciones.
  evidencia: "git log acepta una serie de opciones para limitar su salida —es decir, opciones que te permiten mostrar únicamente parte de las confirmaciones—. Ya has visto una de ellas, la opción -2, que muestra sólo las dos últimas confirmaciones. De hecho, puedes hacer -<n>, siendo n cualquier entero, para mostrar las últimas n confirmaciones."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-307
  hecho: Git pagina por defecto su salida, para que se vea cada página del historial por separado.
  evidencia: "ya que Git por defecto pagina su salida para que veas cada página del historial por separado."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-308
  hecho: La opción --stat imprime tras cada confirmación una lista de archivos modificados.
  evidencia: "la opción --stat imprime tras cada confirmación una lista de archivos modificados"
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-309
  hecho: Con --stat se indica, para cada archivo modificado, cuántas líneas han sido añadidas y eliminadas.
  evidencia: "la opción --stat imprime tras cada confirmación una lista de archivos modificados, indicando cuántos han sido modificados y cuántas líneas han sido añadidas y eliminadas para cada uno de ellos"
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-310
  hecho: Entre los estilos de la opción --pretty, oneline imprime cada confirmación en una única línea.
  evidencia: "Otra opción realmente útil es --pretty, que modifica el formato de la salida. Tienes unos cuantos estilos disponibles. La opción oneline imprime cada confirmación en una única línea"
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-311
  hecho: Las opciones short, full y fuller muestran la salida en un formato parecido, pero añadiendo menos o más información, respectivamente.
  evidencia: "Otras opciones son short, full y fuller, que muestran la salida en un formato parecido, pero añadiendo menos o más información, respectivamente"
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-312
  hecho: La opción format permite especificar un formato propio.
  evidencia: "La opción más interesante es format, que te permite especificar tu propio formato."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-313
  hecho: Si se especifica el formato explícitamente, no cambiará en futuras actualizaciones de Git, lo que resulta especialmente útil al generar una salida para que la analice otro programa.
  evidencia: "Esto resulta especialmente útil si estás generando una salida para que sea analizada por otro programa —como especificas el formato explícitamente, sabes que no cambiará en futuras actualizaciones de Git"
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-314
  hecho: La opción --graph añade un pequeño gráfico ASCII que muestra el historial de ramificaciones y uniones.
  evidencia: "Las opciones oneline y format son especialmente útiles combinadas con otra opción llamada --graph. Ésta añade un pequeño gráfico ASCII mostrando tu historial de ramificaciones y uniones"
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-315
  hecho: Las opciones oneline y format son especialmente útiles combinadas con --graph.
  evidencia: "Las opciones oneline y format son especialmente útiles combinadas con otra opción llamada --graph."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-316
  hecho: El autor es la persona que escribió originalmente el trabajo.
  evidencia: "El autor es la persona que escribió originalmente el trabajo, mientras que el confirmador es quien lo aplicó."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-317
  hecho: El confirmador es quien aplicó el trabajo.
  evidencia: "El autor es la persona que escribió originalmente el trabajo, mientras que el confirmador es quien lo aplicó."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-318
  hecho: Si mandas un parche a un proyecto y uno de sus miembros lo aplica, ambos recibís reconocimiento: tú como autor y el miembro del proyecto como confirmador.
  evidencia: "si mandas un parche a un proyecto, y uno de sus miembros lo aplica, ambos recibiréis reconocimiento —tú como autor, y el miembro del proyecto como confirmador"
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-319
  hecho: Las opciones temporales como --since (desde) y --until (hasta) resultan muy útiles.
  evidencia: "las opciones temporales como --since (desde) y --until (hasta) sí que resultan muy útiles."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-320
  hecho: git log --since=2.weeks lista las confirmaciones hechas durante las dos últimas semanas.
  evidencia: "Por ejemplo, este comando lista todas las confirmaciones hechas durante las dos últimas semanas: $ git log --since=2.weeks"
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-321
  hecho: La opción --author permite filtrar por autor.
  evidencia: "La opción --author te permite filtrar por autor"
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-322
  hecho: La opción --grep permite buscar palabras clave entre los mensajes de confirmación.
  evidencia: "--grep te permite buscar palabras clave entre los mensajes de confirmación."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-323
  hecho: Para aplicar a la vez --author y --grep hay que añadir --all-match; sin ella se muestran las confirmaciones que cumplan cualquiera de las dos.
  evidencia: "La opción --author te permite filtrar por autor, y --grep te permite buscar palabras clave entre los mensajes de confirmación. (Ten en cuenta que si quieres aplicar ambas opciones simultáneamente, tienes que añadir --all-match, o el comando mostrará las confirmaciones que cumplan cualquiera de las dos"
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-324
  hecho: La opción -S recibe una cadena y muestra solo las confirmaciones que cambiaron el código añadiendo o eliminando esa cadena.
  evidencia: "Otra opción útil es -S, la cual recibe una cadena y solo muestra las confirmaciones que cambiaron el código añadiendo o eliminando la cadena."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-325
  hecho: Indicar la ruta de un directorio o archivo limita la salida de git log a las confirmaciones que introdujeron un cambio en esos archivos.
  evidencia: "La última opción verdaderamente útil para filtrar la salida de git log es especificar una ruta. Si especificas la ruta de un directorio o archivo, puedes limitar la salida a aquellas confirmaciones que introdujeron un cambio en dichos archivos."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-326
  hecho: La ruta debe ser siempre la última opción y suele ir precedida de dos guiones (--) que la separan del resto de opciones.
  evidencia: "Si especificas la ruta de un directorio o archivo, puedes limitar la salida a aquellas confirmaciones que introdujeron un cambio en dichos archivos. Ésta debe ser siempre la última opción, y suele ir precedida de dos guiones (--) para separar la ruta del resto de opciones."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-327
  hecho: Al deshacer cambios, a veces no es posible recuperar lo deshecho.
  evidencia: "Ten cuidado, a veces no es posible recuperar algo luego que lo has deshecho."
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-328
  hecho: Deshacer cosas es una de las pocas áreas en las que Git puede perder parte de tu trabajo si cometes un error.
  evidencia: "Ten cuidado, a veces no es posible recuperar algo luego que lo has deshecho. Esta es una de las pocas áreas en las que Git puede perder parte de tu trabajo si cometes un error."
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-329
  hecho: Una acción común a deshacer es confirmar antes de tiempo y olvidar algún archivo, o equivocarse en el mensaje de confirmación.
  evidencia: "Uno de las acciones más comunes a deshacer es cuando confirmas un cambio antes de tiempo y olvidas agregar algún archivo, o te equivocas en el mensaje de confirmación."
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-330
  hecho: Para rehacer una confirmación se puede reconfirmar con git commit --amend.
  evidencia: "Si quieres rehacer la confirmación, puedes reconfirmar con la opción --amend: $ git commit --amend"
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-331
  hecho: git commit --amend utiliza el área de preparación para la confirmación.
  evidencia: "git commit --amend Este comando utiliza tu área de preparación para la confirmación."
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-332
  hecho: Si no hay cambios desde la última confirmación, git commit --amend solo cambia el mensaje de confirmación.
  evidencia: "git commit --amend Este comando utiliza tu área de preparación para la confirmación. Si no has hecho cambios desde tu última confirmación (por ejemplo, ejecutas este comando justo después de tu confirmación anterior), entonces la instantánea lucirá exactamente igual y lo único que cambiarás será el mensaje de confirmación."
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-333
  hecho: Se lanza el mismo editor de confirmación, que ya incluye el mensaje de la confirmación anterior.
  evidencia: "Se lanzará el mismo editor de confirmación, pero verás que ya incluye el mensaje de tu confirmación anterior."
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-334
  hecho: Tras confirmar, preparar un archivo olvidado y ejecutar git commit --amend, queda una sola confirmación: la segunda reemplaza el resultado de la primera.
  evidencia: "git commit -m 'initial commit' $ git add forgotten_file $ git commit --amend Al final terminarás con una sola confirmación - la segunda confirmación reemplaza el resultado de la primera."
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-335
  hecho: El comando que se usa para determinar el estado del área de preparación y del directorio de trabajo también recuerda cómo deshacer los cambios en ellas.
  evidencia: "Las siguientes dos secciones demuestran cómo lidiar con los cambios de tu área de preparación y tú directorio de trabajo. Afortunadamente, el comando que usas para determinar el estado de esas dos áreas también te recuerda cómo deshacer los cambios en ellas."
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-336
  hecho: Justo debajo del texto Changes to be committed se indica que se use git reset HEAD <file>... para deshacer la preparación.
  evidencia: "Justo debajo del texto "Changes to be committed" ("Cambios a ser confirmados", en inglés), verás que dice que uses git reset HEAD <file>... para deshacer la preparación."
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-337
  hecho: El archivo CONTRIBUTING.md queda modificado y, nuevamente, no preparado.
  evidencia: "El archivo CONTRIBUTING.md esta modificado y, nuevamente, no preparado."
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-338
  hecho: git reset puede ser un comando peligroso, especialmente con la opción --hard.
  evidencia: "git reset puede ser un comando peligroso, especialmente si lo llamas con la opción --hard."
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-339
  hecho: Aunque git reset puede ser peligroso, en el escenario descrito anteriormente el archivo del directorio de trabajo no se toca, por lo que es relativamente seguro.
  evidencia: "git reset puede ser un comando peligroso, especialmente si lo llamas con la opción --hard. Sin embargo, en el escenario descrito anteriormente, el archivo que está en tu directorio de trabajo no se toca, por lo que es relativamente seguro."
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-340
  hecho: Tras git checkout -- CONTRIBUTING.md, se puede ver que los cambios se han revertido.
  evidencia: "git checkout -- CONTRIBUTING.md $ git status On branch master Changes to be committed: (use "git reset HEAD <file>..." to unstage) renamed: README.md -> README Ahora puedes ver que los cambios se han revertido."
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-341
  hecho: git checkout -- [archivo] es un comando peligroso.
  evidencia: "Es importante entender que git checkout -- [archivo] es un comando peligroso."
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-342
  hecho: Con git checkout -- [archivo] desaparece cualquier cambio hecho al archivo, porque se sobrescribe con otro archivo.
  evidencia: "Es importante entender que git checkout -- [archivo] es un comando peligroso. Cualquier cambio que le hayas hecho a ese archivo desaparecerá - acabas de sobreescribirlo con otro archivo."
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-343
  hecho: Pro Git recomienda no usar git checkout -- [archivo] salvo que estés absolutamente seguro de que ya no quieres el archivo.
  evidencia: "Es importante entender que git checkout -- [archivo] es un comando peligroso. Cualquier cambio que le hayas hecho a ese archivo desaparecerá - acabas de sobreescribirlo con otro archivo. Nunca utilices este comando a menos que estés absolutamente seguro de que ya no quieres el archivo."
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-344
  hecho: Para conservar los cambios y apartar el archivo temporalmente, Pro Git remite a esconder archivos (stashing) y a las ramas.
  evidencia: "Para mantener los cambios que has hecho y a la vez deshacerte del archivo temporalmente, hablaremos sobre cómo esconder archivos (stashing, en inglés) y sobre ramas"
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-345
  hecho: Todo lo que esté confirmado en Git puede recuperarse.
  evidencia: "Recuerda, todo lo que esté confirmado en Git puede recuperarse."
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-346
  hecho: Pueden recuperarse commits de ramas eliminadas y commits sobrescritos con --amend.
  evidencia: "Incluso commits que estuvieron en ramas que han sido eliminadas o commits que fueron sobreescritos con --amend pueden recuperarse"
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-347
  hecho: Lo que se pierde y nunca fue confirmado puede no volver a verse jamás.
  evidencia: "Sin embargo, es posible que no vuelvas a ver jamás cualquier cosa que pierdas y que nunca haya sido confirmada."
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-348
  hecho: Las opciones --since y --after muestran aquellas confirmaciones hechas después de la fecha especificada.
  evidencia: "--since, --after Muestra aquellas confirmaciones hechas después de la fecha especificada."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-349
  hecho: Las opciones --until y --before muestran aquellas confirmaciones hechas antes de la fecha especificada.
  evidencia: "--until, --before Muestra aquellas confirmaciones hechas antes de la fecha especificada."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-350
  hecho: El comando git status te recuerda cómo sacar del área de preparación un archivo.
  evidencia: "¿Cómo puedes sacar del área de preparación uno de ellos? El comando git status te recuerda cómo:"
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-351
  hecho: La opción -(n) muestra solamente las últimas n confirmaciones.
  evidencia: "-(n) Muestra solamente las últimas n confirmaciones"
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

## 1.3 Leer y deshacer el historial (documentación de referencia de Git)

- id: h01-352
  hecho: git restore restaura las rutas indicadas del directorio de trabajo con contenido procedente de una fuente de restauración.
  evidencia: "Restore specified paths in the working tree with some contents from a restore source."
  fuente: f01-19
  ancla: https://git-scm.com/docs/git-restore
  consultada: 2026-11-12

- id: h01-353
  hecho: Si una ruta está rastreada pero no existe en la fuente de restauración, git restore la elimina para que coincida con la fuente.
  evidencia: "If a path is tracked but does not exist in the restore source, it will be removed to match the source."
  fuente: f01-19
  ancla: https://git-scm.com/docs/git-restore
  consultada: 2026-11-12

- id: h01-354
  hecho: Con la opción --staged, git restore puede restaurar también el contenido del índice.
  evidencia: "The command can also be used to restore the content in the index with --staged"
  fuente: f01-19
  ancla: https://git-scm.com/docs/git-restore
  consultada: 2026-11-12

- id: h01-355
  hecho: Con --staged --worktree, git restore restaura a la vez el directorio de trabajo y el índice.
  evidencia: "or restore both the working tree and the index with --staged --worktree."
  fuente: f01-19
  ancla: https://git-scm.com/docs/git-restore
  consultada: 2026-11-12

- id: h01-356
  hecho: Por defecto, si se da --staged, git restore restaura el contenido desde HEAD.
  evidencia: "By default, if --staged is given, the contents are restored from HEAD, otherwise from the index."
  fuente: f01-19
  ancla: https://git-scm.com/docs/git-restore
  consultada: 2026-11-12

- id: h01-357
  hecho: Por defecto, si no se da --staged, git restore restaura el contenido desde el índice.
  evidencia: "By default, if --staged is given, the contents are restored from HEAD, otherwise from the index."
  fuente: f01-19
  ancla: https://git-scm.com/docs/git-restore
  consultada: 2026-11-12

- id: h01-358
  hecho: La opción --source sirve para restaurar desde un commit distinto del de la fuente por defecto.
  evidencia: "Use --source to restore from a different commit."
  fuente: f01-19
  ancla: https://git-scm.com/docs/git-restore
  consultada: 2026-11-12

- id: h01-359
  hecho: Es habitual indicar el árbol de origen de --source nombrando un commit, una rama o una etiqueta asociados a él.
  evidencia: "It is common to specify the source tree by naming a commit, branch or tag associated with it."
  fuente: f01-19
  ancla: https://git-scm.com/docs/git-restore
  consultada: 2026-11-12

- id: h01-360
  hecho: Si no se especifica ni --staged ni --worktree, git restore restaura por defecto el directorio de trabajo.
  evidencia: "Specify the restore location. If neither option is specified, by default the working tree is restored."
  fuente: f01-19
  ancla: https://git-scm.com/docs/git-restore
  consultada: 2026-11-12

- id: h01-361
  hecho: La página de git restore indica que restaurar un archivo del índice para que coincida con la versión de HEAD es lo mismo que usar git reset.
  evidencia: "To restore a file in the index to match the version in HEAD (this is the same as using git-reset[1])"
  fuente: f01-19
  ancla: https://git-scm.com/docs/git-restore
  consultada: 2026-11-12

- id: h01-362
  hecho: La página de git restore indica que restaurar a la vez el índice y el directorio de trabajo es lo mismo que usar git checkout.
  evidencia: "or you can restore both the index and the working tree (this is the same as using git-checkout[1])"
  fuente: f01-19
  ancla: https://git-scm.com/docs/git-restore
  consultada: 2026-11-12

- id: h01-363
  hecho: La página de git restore remite a la sección «Reset, restore and revert» de la página de git para consultar las diferencias entre esos tres comandos.
  evidencia: "See "Reset, restore and revert" in git[1] for the differences between the three commands."
  fuente: f01-19
  ancla: https://git-scm.com/docs/git-restore
  consultada: 2026-11-12

> NOTA (huecos, f01-19): la copia local de git-restore no contiene ninguna advertencia de que el comando sea experimental, así que no se registra ningún hecho al respecto.

## 1.4 Las ramas son punteros

- id: h01-401
  hecho: Git no almacena sus datos de forma incremental (guardando solo diferencias), sino como una serie de instantáneas, que son copias puntuales de los archivos completos.
  evidencia: "la forma en que almacena sus datos. Recordando lo citado en [ch01-introduction], Git no los almacena de forma incremental (guardando solo diferencias), sino que los almacena como una serie de instantáneas (copias puntuales de los archivos completos, tal y como se encuentran en ese momento)"
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-402
  hecho: En cada confirmación Git almacena una instantánea del trabajo preparado.
  evidencia: "En cada confirmación de cambios (commit), Git almacena una instantánea de tu trabajo preparado."
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-403
  hecho: La instantánea de cada confirmación contiene además metadatos con el autor y el mensaje explicativo.
  evidencia: "En cada confirmación de cambios (commit), Git almacena una instantánea de tu trabajo preparado. Dicha instantánea contiene además unos metadatos con el autor y el mensaje explicativo"
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-404
  hecho: Una confirmación normal tiene un padre; la que registra una fusión tiene varios.
  evidencia: "un padre en los casos de confirmación normal, y múltiples padres en los casos de estar confirmando una fusión (merge) de dos o más ramas"
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-405
  hecho: Al preparar los archivos, Git guarda una copia de cada uno en el repositorio, y esas copias se llaman blobs.
  evidencia: "Al preparar los archivos, Git realiza una suma de control de cada uno de ellos (un resumen SHA-1, tal y como se mencionaba en [ch01-introduction]), almacena una copia de cada uno en el repositorio (estas copias se denominan "blobs")"
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-406
  hecho: Al confirmar con git commit, Git calcula sumas de control de cada subdirectorio y las guarda como objetos árbol en el repositorio.
  evidencia: "Cuando creas una confirmación con el comando git commit, Git realiza sumas de control de cada subdirectorio (en el ejemplo, solamente tenemos el directorio principal del proyecto), y las guarda como objetos árbol en el repositorio Git."
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-407
  hecho: Git crea un objeto de confirmación con los metadatos y un apuntador al objeto árbol raíz del proyecto.
  evidencia: "Git crea un objeto de confirmación con los metadatos pertinentes y un apuntador al objeto árbol raíz del proyecto."
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-408
  hecho: En ese momento del ejemplo, el repositorio de Git contendrá cinco objetos: un blob para cada uno de los tres archivos, un árbol con la lista de contenidos del directorio y una confirmación que apunta a la raíz de ese árbol.
  evidencia: "En este momento, el repositorio de Git contendrá cinco objetos: un "blob" para cada uno de los tres archivos, un árbol con la lista de contenidos del directorio (más sus respectivas relaciones con los "blobs"), y una confirmación de cambios (commit) apuntando a la raíz de ese árbol"
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-409
  hecho: Una rama de Git es un apuntador móvil a una confirmación.
  evidencia: "Una rama Git es simplemente un apuntador móvil apuntando a una de esas confirmaciones."
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-410
  hecho: La rama por defecto de Git es master.
  evidencia: "La rama por defecto de Git es la rama master."
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-411
  hecho: La rama principal master se crea apuntando a la primera confirmación, y en cada confirmación de cambios que se realice la rama avanza automáticamente.
  evidencia: "Con la primera confirmación de cambios que realicemos, se creará esta rama principal master apuntando a dicha confirmación. En cada confirmación de cambios que realicemos, la rama irá avanzando automáticamente."
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-412
  hecho: La rama master no es una rama especial; es como cualquier otra rama.
  evidencia: "La rama "master" en Git, no es una rama especial. Es como cualquier otra rama."
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-413
  hecho: La única razón por la que master aparece en casi todos los repositorios es que git init la crea por defecto y la gente no se molesta en cambiarle el nombre.
  evidencia: "La rama "master" en Git, no es una rama especial. Es como cualquier otra rama. La única razón por la cual aparece en casi todos los repositorios es porque es la que crea por defecto el comando git init y la gente no se molesta en cambiarle el nombre."
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-414
  hecho: Crear una rama nueva solo crea un apuntador nuevo que se puede mover libremente.
  evidencia: "¿Qué sucede cuando creas una nueva rama? Bueno…​, simplemente se crea un nuevo apuntador para que lo puedas mover libremente."
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-415
  hecho: git branch testing crea un apuntador nuevo a la misma confirmación en la que estás.
  evidencia: "Para ello, usarás el comando git branch: $ git branch testing Esto creará un nuevo apuntador apuntando a la misma confirmación donde estés actualmente."
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-416
  hecho: En Git, HEAD es el apuntador a la rama local en la que estás en ese momento.
  evidencia: "este HEAD es totalmente distinto al concepto de HEAD en otros sistemas de control de cambios como Subversion o CVS. En Git, es simplemente el apuntador a la rama local en la que tú estés en ese momento"
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-417
  hecho: git branch solo crea la rama nueva y no salta a ella.
  evidencia: "el comando git branch solamente crea una nueva rama, pero no salta a dicha rama"
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-418
  hecho: Para pasar de una rama a otra se usa git checkout.
  evidencia: "Para saltar de una rama a otra, tienes que utilizar el comando git checkout."
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-419
  hecho: git checkout testing mueve HEAD a la rama testing.
  evidencia: "git checkout testing Esto mueve el apuntador HEAD a la rama testing."
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-420
  hecho: Tras confirmar con git commit -a -m 'made a change', la rama testing avanza, mientras que master permanece en la confirmación donde estaba.
  evidencia: "git commit -a -m 'made a change' Figura 15. La rama apuntada por HEAD avanza con cada confirmación de cambios Observamos algo interesante: la rama testing avanza, mientras que la rama master permanece en la confirmación donde estaba"
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-421
  hecho: Volver a master con git checkout mueve HEAD de nuevo a master.
  evidencia: "git checkout master Figura 16. HEAD apunta a otra rama cuando hacemos un salto Este comando realiza dos acciones: Mueve el apuntador HEAD de nuevo a la rama master"
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-422
  hecho: Además de mover HEAD de nuevo a master, ese comando revierte los archivos del directorio de trabajo, dejándolos como estaban en la última instantánea confirmada en master.
  evidencia: "Este comando realiza dos acciones: Mueve el apuntador HEAD de nuevo a la rama master, y revierte los archivos de tu directorio de trabajo; dejándolos tal y como estaban en la última instantánea confirmada en dicha rama master."
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-423
  hecho: Con git log --oneline --decorate --graph --all se ve el historial con los apuntadores de las ramas y cómo ha divergido.
  evidencia: "Si ejecutas git log --oneline --decorate --graph --all te mostrará el historial de tus confirmaciones, indicando dónde están los apuntadores de tus ramas y como ha divergido tu historial."
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-424
  hecho: Una rama de Git es un archivo con los 40 caracteres de la suma de control SHA-1 de la confirmación a la que apunta.
  evidencia: "una rama Git es realmente un simple archivo que contiene los 40 caracteres de una suma de control SHA-1, (representando la confirmación de cambios a la que apunta)"
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-425
  hecho: Crear una rama equivale a escribir 41 bytes en un archivo: 40 caracteres y un retorno de carro.
  evidencia: "Crear una nueva rama es tan rápido y simple como escribir 41 bytes en un archivo, (40 caracteres y un retorno de carro)."
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-426
  hecho: En otros sistemas de control de versiones, crear una rama supone copiar todos los archivos del proyecto a un directorio nuevo y puede llevar segundos o minutos, mientras que en Git el proceso es siempre instantáneo.
  evidencia: "otros sistemas de control de versiones, en los que crear una rama nueva supone el copiar todos los archivos del proyecto a un directorio adicional nuevo. Esto puede llevar segundos o incluso minutos, dependiendo del tamaño del proyecto; mientras que en Git el proceso es siempre instantáneo"
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-427
  hecho: Como Git guarda los padres de cada confirmación, encontrar la base de una fusión es automático y generalmente sencillo.
  evidencia: "debido a que se almacenan también los nodos padre para cada confirmación, el encontrar las bases adecuadas para realizar una fusión entre ramas es un proceso automático y generalmente sencillo de realizar"
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-428
  hecho: git checkout con la opción -b crea una rama nueva y salta a ella en un solo paso.
  evidencia: "Para crear una nueva rama y saltar a ella, en un solo paso, puedes utilizar el comando git checkout con la opción -b"
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-429
  hecho: git checkout -b iss53 es un atajo de git branch iss53 seguido de git checkout iss53.
  evidencia: "git checkout -b iss53 Switched to a new branch "iss53" Esto es un atajo para: $ git branch iss53 $ git checkout iss53"
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-430
  hecho: Con cambios sin confirmar en el directorio de trabajo o en el área de preparación, Git puede impedir saltar a otra rama con la que habría conflictos.
  evidencia: "si tenemos cambios aún no confirmados en el directorio de trabajo o en el área de preparación, Git no nos permitirá saltar a otra rama con la que podríamos tener conflictos"
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-431
  hecho: Conviene tener un estado de trabajo limpio antes de saltar entre ramas.
  evidencia: "Lo mejor es tener siempre un estado de trabajo limpio y despejado antes de saltar entre ramas."
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-432
  hecho: Git añade, quita y modifica archivos automáticamente para asegurar que la copia de trabajo luce exactamente como lucía la rama en la última confirmación de cambios realizada sobre ella.
  evidencia: "Git añade, quita y modifica archivos automáticamente para asegurar que tu copia de trabajo luce exactamente como lucía la rama en la última confirmación de cambios realizada sobre ella."
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-433
  hecho: Para fusionar se activa la rama donde se quiere fusionar y se lanza git merge.
  evidencia: "activa (checkout) la rama donde deseas fusionar y lanza el comando git merge"
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-434
  hecho: En un avance rápido (Fast forward), Git mueve el apuntador hacia adelante porque la confirmación apuntada en la rama donde se fusiona estaba directamente arriba respecto a la confirmación actual.
  evidencia: "Notarás la frase "Fast forward" ("Avance rápido", en inglés) que aparece en la salida del comando. Git ha movido el apuntador hacia adelante, ya que la confirmación apuntada en la rama donde has fusionado estaba directamente arriba respecto a la confirmación actual."
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-435
  hecho: En lo que se denomina avance rápido, Git simplifica las cosas avanzando el puntero, ya que no hay ningún otro trabajo divergente a fusionar.
  evidencia: "Git simplifica las cosas avanzando el puntero, ya que no hay ningún otro trabajo divergente a fusionar. Esto es lo que se denomina "avance rápido" ("fast forward")."
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-436
  hecho: El avance rápido ocurre cuando se fusiona una confirmación con otra accesible siguiendo directamente el historial de la primera.
  evidencia: "Dicho de otro modo: cuando intentas fusionar una confirmación con otra confirmación accesible siguiendo directamente el historial de la primera; Git simplifica las cosas avanzando el puntero, ya que no hay ningún otro trabajo divergente a fusionar. Esto es lo que se denomina "avance rápido" ("fast forward")."
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-437
  hecho: Una rama que ya no se necesita porque apunta al mismo sitio que master puede borrarse con la opción -d del comando git branch.
  evidencia: "es importante borrar la rama hotfix, ya que no la vamos a necesitar más, puesto que apunta exactamente al mismo sitio que la rama master. Esto lo puedes hacer con la opción -d del comando git branch"
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-438
  hecho: Todo el trabajo realizado en la rama hotfix no está en los archivos de la rama iss53.
  evidencia: "todo el trabajo realizado en la rama hotfix no está en los archivos de la rama iss53"
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-439
  hecho: Si fuera necesario agregar a iss53 el trabajo de hotfix, se puede fusionar la rama master sobre iss53 con git merge master.
  evidencia: "todo el trabajo realizado en la rama hotfix no está en los archivos de la rama iss53. Si fuera necesario agregarlos, puedes fusionar (merge) la rama master sobre la rama iss53 utilizando el comando git merge master"
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-440
  hecho: Si la confirmación actual no es ancestro directo de la rama que se fusiona, Git tiene trabajo extra que hacer.
  evidencia: "Debido a que la confirmación en la rama actual no es ancestro directo de la rama que pretendes fusionar, Git tiene cierto trabajo extra que hacer."
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-441
  hecho: En ese caso Git hace una fusión a tres bandas.
  evidencia: "Debido a que la confirmación en la rama actual no es ancestro directo de la rama que pretendes fusionar, Git tiene cierto trabajo extra que hacer. Git realizará una fusión a tres bandas"
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-442
  hecho: La fusión a tres bandas usa las instantáneas de los extremos de ambas ramas y el ancestro común.
  evidencia: "Git realizará una fusión a tres bandas, utilizando las dos instantáneas apuntadas por el extremo de cada una de las ramas y por el ancestro común a ambas"
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-443
  hecho: Git crea una nueva instantánea resultante de la fusión a tres bandas.
  evidencia: "Git crea una nueva instantánea (snapshot) resultante de la fusión a tres bandas"
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-444
  hecho: Git crea automáticamente una nueva confirmación que apunta a esa instantánea.
  evidencia: "Git crea una nueva instantánea (snapshot) resultante de la fusión a tres bandas; y crea automáticamente una nueva confirmación de cambios (commit) que apunta a ella"
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-445
  hecho: Git crea una nueva instantánea y una confirmación que apunta a ella; a este proceso se le llama fusión confirmada y su particularidad es que tiene más de un padre.
  evidencia: "Git crea una nueva instantánea (snapshot) resultante de la fusión a tres bandas; y crea automáticamente una nueva confirmación de cambios (commit) que apunta a ella. Nos referimos a este proceso como "fusión confirmada" y su particularidad es que tiene más de un padre."
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-446
  hecho: Git determina automáticamente el mejor ancestro común para fusionar.
  evidencia: "es el propio Git quien determina automáticamente el mejor ancestro común para realizar la fusión"
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-447
  hecho: En CVS o Subversion es el desarrollador quien debe determinar el mejor ancestro común.
  evidencia: "a diferencia de otros sistemas tales como CVS o Subversion, donde es el desarrollador quien ha de determinar cuál puede ser dicho mejor ancestro común"
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-448
  hecho: Si hay modificaciones dispares en una misma porción de un mismo archivo en las dos ramas que se pretende fusionar, Git no es capaz de fusionarlas directamente.
  evidencia: "Si hay modificaciones dispares en una misma porción de un mismo archivo en las dos ramas distintas que pretendes fusionar, Git no será capaz de fusionarlas directamente."
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-449
  hecho: Ante un conflicto, git merge muestra CONFLICT (content) e informa de que la fusión automática ha fallado (Automatic merge failed).
  evidencia: "git merge iss53 Auto-merging index.html CONFLICT (content): Merge conflict in index.html Automatic merge failed; fix conflicts and then commit the result."
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-450
  hecho: Ante un conflicto, Git no crea automáticamente la confirmación de fusión, sino que hace una pausa en el proceso esperando a que se resuelva el conflicto.
  evidencia: "Git no crea automáticamente una nueva fusión confirmada (merge commit), sino que hace una pausa en el proceso, esperando a que tú resuelvas el conflicto."
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-451
  hecho: git status muestra qué archivos siguen sin fusionar durante un conflicto.
  evidencia: "Para ver qué archivos permanecen sin fusionar en un determinado momento conflictivo de una fusión, puedes usar el comando git status"
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-452
  hecho: En un momento conflictivo de una fusión, la salida de git status incluye el mensaje You have unmerged paths.
  evidencia: "Para ver qué archivos permanecen sin fusionar en un determinado momento conflictivo de una fusión, puedes usar el comando git status: $ git status On branch master You have unmerged paths."
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-453
  hecho: Git añade marcadores especiales de resolución de conflictos a los archivos conflictivos.
  evidencia: "Git añade a los archivos conflictivos unos marcadores especiales de resolución de conflictos"
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-454
  hecho: En el bloque conflictivo, lo que hay encima de ======= es la versión de HEAD, la rama activada antes de fusionar.
  evidencia: "la versión en HEAD (la rama master, la que habías activado antes de lanzar el comando de fusión) contiene lo indicado en la parte superior del bloque (todo lo que está encima de =======)"
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-455
  hecho: Para resolver un conflicto hay que elegir manualmente el contenido de uno u otro lado.
  evidencia: "Para resolver el conflicto, has de elegir manualmente el contenido de uno o de otro lado."
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-456
  hecho: Tras resolver los bloques conflictivos hay que lanzar git add sobre cada archivo modificado.
  evidencia: "Tras resolver todos los bloques conflictivos, has de lanzar comandos git add para marcar cada archivo modificado."
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-457
  hecho: Marcar un archivo como preparado indica a Git que sus conflictos están resueltos.
  evidencia: "Marcar archivos como preparados (staged) indica a Git que sus conflictos han sido resueltos."
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-458
  hecho: git mergetool arranca una herramienta de visualización para ir resolviendo los conflictos.
  evidencia: "puedes usar el comando git mergetool, el cual arrancará la correspondiente herramienta de visualización y te permitirá ir resolviendo conflictos con ella"
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-459
  hecho: git status sirve para ver si ya se han resuelto todos los conflictos, y en el ejemplo muestra All conflicts fixed but you are still merging.
  evidencia: "En cualquier momento, puedes lanzar el comando git status para ver si ya has resuelto todos los conflictos: $ git status On branch master All conflicts fixed but you are still merging."
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-460
  hecho: Con todos los archivos conflictivos preparados, git commit termina de confirmar la fusión.
  evidencia: "puedes lanzar el comando git commit para terminar de confirmar la fusión"
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-461
  hecho: Al terminar la fusión con git commit, el mensaje de confirmación por defecto será algo parecido a Merge branch 'iss53'.
  evidencia: "puedes lanzar el comando git commit para terminar de confirmar la fusión. El mensaje de confirmación por defecto será algo parecido a: Merge branch 'iss53'"
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-462
  hecho: git branch sin parámetros lista las ramas del proyecto.
  evidencia: "El comando git branch tiene más funciones que las de crear y borrar ramas. Si lo lanzas sin parámetros, obtienes una lista de las ramas presentes en tu proyecto"
  fuente: f01-09
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Gesti%c3%b3n-de-Ramas
  consultada: 2026-11-12

- id: h01-463
  hecho: En esa lista, el asterisco marca la rama activa, a la que apunta HEAD.
  evidencia: "Fijate en el carácter * delante de la rama master: nos indica la rama activa en este momento (la rama a la que apunta HEAD)"
  fuente: f01-09
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Gesti%c3%b3n-de-Ramas
  consultada: 2026-11-12

- id: h01-464
  hecho: git branch -v muestra la última confirmación de cada rama.
  evidencia: "Para ver la última confirmación de cambios en cada rama, puedes usar el comando git branch -v"
  fuente: f01-09
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Gesti%c3%b3n-de-Ramas
  consultada: 2026-11-12

- id: h01-465
  hecho: git branch --merged lista las ramas ya fusionadas con la rama activa.
  evidencia: "Si deseas ver las ramas que han sido fusionadas con la rama activa, puedes lanzar el comando git branch --merged"
  fuente: f01-09
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Gesti%c3%b3n-de-Ramas
  consultada: 2026-11-12

- id: h01-466
  hecho: Las ramas que no llevan por delante el asterisco pueden eliminarse sin problemas, porque todo su contenido ya ha sido incorporado a otras ramas.
  evidencia: "Las ramas que no llevan por delante el carácter * pueden ser eliminadas sin problemas, porque todo su contenido ya ha sido incorporado a otras ramas."
  fuente: f01-09
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Gesti%c3%b3n-de-Ramas
  consultada: 2026-11-12

- id: h01-467
  hecho: git branch --no-merged lista las ramas con trabajo sin fusionar.
  evidencia: "Para mostrar todas las ramas que contienen trabajos sin fusionar, puedes utilizar el comando git branch --no-merged"
  fuente: f01-09
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Gesti%c3%b3n-de-Ramas
  consultada: 2026-11-12

- id: h01-468
  hecho: Borrar con git branch -d una rama con trabajo sin fusionar da un error.
  evidencia: "Debido a que contiene trabajos sin fusionar, al intentar borrarla con git branch -d, el comando nos dará un error"
  fuente: f01-09
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Gesti%c3%b3n-de-Ramas
  consultada: 2026-11-12

- id: h01-469
  hecho: La opción -D fuerza el borrado de la rama aunque se pierda el trabajo que contiene.
  evidencia: "Si realmente deseas borrar la rama y perder el trabajo contenido en ella, puedes forzar el borrado con la opción -D"
  fuente: f01-09
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Gesti%c3%b3n-de-Ramas
  consultada: 2026-11-12

- id: h01-470
  hecho: Git sabe en qué rama estás mediante un apuntador especial denominado HEAD.
  evidencia: "¿cómo sabe Git en qué rama estás en este momento? Pues…​, mediante un apuntador especial denominado HEAD."
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

## 1.4 Las ramas son punteros (documentación de referencia de Git)

- id: h01-471
  hecho: git switch sirve para cambiar de rama.
  evidencia: "git-switch - Switch branches"
  fuente: f01-20
  ancla: https://git-scm.com/docs/git-switch
  consultada: 2026-11-12

- id: h01-472
  hecho: Al cambiar de rama con git switch, el directorio de trabajo y el índice se actualizan para coincidir con la rama.
  evidencia: "Switch to a specified branch. The working tree and the index are updated to match the branch."
  fuente: f01-20
  ancla: https://git-scm.com/docs/git-switch
  consultada: 2026-11-12

- id: h01-473
  hecho: La opción -c de git switch crea una rama nueva a partir de un punto de partida antes de cambiar a ella.
  evidencia: "-c <new-branch> --create <new-branch> Create a new branch named <new-branch> starting at <start-point> before switching to the branch."
  fuente: f01-20
  ancla: https://git-scm.com/docs/git-switch
  consultada: 2026-11-12

- id: h01-474
  hecho: La opción --detach de git switch sirve para cambiar a un commit para inspeccionarlo o hacer experimentos descartables.
  evidencia: "-d --detach Switch to a commit for inspection and discardable experiments."
  fuente: f01-20
  ancla: https://git-scm.com/docs/git-switch
  consultada: 2026-11-12

- id: h01-475
  hecho: Si lo hecho tras git switch --detach merece conservarse, se puede crear un nombre nuevo para ello, sin cambiar de sitio, con git switch -c.
  evidencia: "If it turns out whatever you have done is worth keeping, you can always create a new name for it (without switching away): $ git switch -c good-surprises"
  fuente: f01-20
  ancla: https://git-scm.com/docs/git-switch
  consultada: 2026-11-12

- id: h01-476
  hecho: Cambiar de rama no exige índice ni directorio de trabajo limpios, pero la operación se aborta si llevase a perder cambios locales, salvo que se indique lo contrario con --discard-changes o --merge.
  evidencia: "Switching branches does not require a clean index and working tree (i.e. no differences compared to HEAD). The operation is aborted however if the operation leads to loss of local changes, unless told otherwise with --discard-changes or --merge."
  fuente: f01-20
  ancla: https://git-scm.com/docs/git-switch
  consultada: 2026-11-12

- id: h01-477
  hecho: La opción -m de git switch lleva tus cambios locales a la nueva rama.
  evidencia: "You can give the -m flag to the command, which will carry your local changes to the new branch:"
  fuente: f01-20
  ancla: https://git-scm.com/docs/git-switch
  consultada: 2026-11-12

- id: h01-478
  hecho: La documentación de git switch menciona git checkout junto a git switch al explicar que la sintaxis @{-<N>} se refiere a la N-ésima última rama o commit a la que se cambió con cualquiera de los dos.
  evidencia: "You can use the @{-<N>} syntax to refer to the <N>-th last branch/commit switched to using git switch or git checkout operation."
  fuente: f01-20
  ancla: https://git-scm.com/docs/git-switch
  consultada: 2026-11-12

- id: h01-479
  hecho: git checkout tiene dos modos principales: cambiar de rama y restaurar otra versión de un archivo.
  evidencia: "git checkout has two main modes: Switch branches, with git checkout <branch> Restore a different version of a file, for example with git checkout <commit> <filename> or git checkout <filename>"
  fuente: f01-21
  ancla: https://git-scm.com/docs/git-checkout
  consultada: 2026-11-12

- id: h01-480
  hecho: HEAD normalmente apunta a una rama con nombre.
  evidencia: "HEAD normally refers to a named branch (e.g. master)."
  fuente: f01-21
  ancla: https://git-scm.com/docs/git-checkout
  consultada: 2026-11-12

- id: h01-481
  hecho: A veces resulta útil poder hacer checkout de un commit que no está en la punta de ninguna rama con nombre.
  evidencia: "It is sometimes useful to be able to checkout a commit that is not at the tip of any named branch, or even to create a new commit that is not referenced by a named branch."
  fuente: f01-21
  ancla: https://git-scm.com/docs/git-checkout
  consultada: 2026-11-12

- id: h01-482
  hecho: git checkout --detach o git checkout con un commit funciona como git checkout con una rama, salvo que en lugar de apuntar HEAD a la rama lo apunta al identificador del commit.
  evidencia: "git checkout --detach [<branch>] git checkout [--detach] <commit> The same as git checkout <branch>, except that instead of pointing HEAD at the branch, it points HEAD at the commit ID."
  fuente: f01-21
  ancla: https://git-scm.com/docs/git-checkout
  consultada: 2026-11-12

- id: h01-483
  hecho: Que HEAD apunte directamente a un commit, y no a una rama con nombre, se conoce como estado de HEAD desacoplado (detached HEAD).
  evidencia: "HEAD now refers directly to commit b. This is known as being in detached HEAD state. It means simply that HEAD refers to a specific commit, as opposed to referring to a named branch."
  fuente: f01-21
  ancla: https://git-scm.com/docs/git-checkout
  consultada: 2026-11-12

- id: h01-484
  hecho: En el ejemplo de la página, un commit nuevo creado con HEAD desacoplado (el commit e) queda referenciado solo por HEAD.
  evidencia: "There is now a new commit e, but it is referenced only by HEAD."
  fuente: f01-21
  ancla: https://git-scm.com/docs/git-checkout
  consultada: 2026-11-12

- id: h01-485
  hecho: En el ejemplo de la página, en ese punto nada referencia al commit f, y el commit f (y por extensión el e) acabará eliminado por el proceso rutinario de recolección de basura de Git, salvo que se cree antes una referencia.
  evidencia: "It is important to realize that at this point nothing refers to commit f. Eventually commit f (and by extension commit e) will be deleted by the routine Git garbage collection process, unless we create a reference before that happens."
  fuente: f01-21
  ancla: https://git-scm.com/docs/git-checkout
  consultada: 2026-11-12

- id: h01-486
  hecho: Si aún no te has movido del commit f, cualquiera de estas opciones crea una referencia a él: git checkout -b foo (o git switch -c foo), git branch foo o git tag foo.
  evidencia: "If we have not yet moved away from commit f, any of these will create a reference to it: $ git checkout -b foo # or "git switch -c foo" (1) $ git branch foo (2) $ git tag foo (3)"
  fuente: f01-21
  ancla: https://git-scm.com/docs/git-checkout
  consultada: 2026-11-12

- id: h01-487
  hecho: Si ya te has movido del commit f, primero hay que recuperar su nombre de objeto (normalmente con git reflog) y después se puede crear una referencia a él.
  evidencia: "If we have moved away from commit f, then we must first recover its object name (typically by using git reflog), and then we can create a reference to it."
  fuente: f01-21
  ancla: https://git-scm.com/docs/git-checkout
  consultada: 2026-11-12

- id: h01-488
  hecho: git merge se detiene si hay un conflicto que no puede resolverse automáticamente o si se usó --no-commit al iniciar la fusión; en ese punto se puede ejecutar git merge --abort o git merge --continue.
  evidencia: "A merge stops if there’s a conflict that cannot be resolved automatically or if --no-commit was provided when initiating the merge. At that point you can run git merge --abort or git merge --continue."
  fuente: f01-22
  ancla: https://git-scm.com/docs/git-merge
  consultada: 2026-11-12

- id: h01-489
  hecho: git merge --abort aborta el proceso de resolución de conflictos en curso e intenta reconstruir el estado previo a la fusión.
  evidencia: "--abort Abort the current conflict resolution process, and try to reconstruct the pre-merge state."
  fuente: f01-22
  ancla: https://git-scm.com/docs/git-merge
  consultada: 2026-11-12

- id: h01-490
  hecho: Si había cambios sin confirmar en el directorio de trabajo cuando empezó la fusión, git merge --abort en algunos casos no podrá reconstruirlos.
  evidencia: "If there were uncommitted worktree changes present when the merge started, git merge --abort will in some cases be unable to reconstruct these changes."
  fuente: f01-22
  ancla: https://git-scm.com/docs/git-merge
  consultada: 2026-11-12

- id: h01-491
  hecho: La documentación recomienda confirmar o guardar en el stash tus cambios antes de ejecutar git merge.
  evidencia: "It is therefore recommended to always commit or stash your changes before running git merge."
  fuente: f01-22
  ancla: https://git-scm.com/docs/git-merge
  consultada: 2026-11-12

- id: h01-492
  hecho: Cuando ambos lados cambian la misma zona de un archivo, Git no elige uno al azar y te pide que lo resuelvas dejando lo que hizo cada lado en esa zona.
  evidencia: "When both sides made changes to the same area, however, Git cannot randomly pick one side over the other, and asks you to resolve it by leaving what both sides did to that area."
  fuente: f01-22
  ancla: https://git-scm.com/docs/git-merge
  consultada: 2026-11-12

- id: h01-493
  hecho: La zona donde chocan dos cambios se marca con los marcadores <<<<<<<, ======= y >>>>>>>.
  evidencia: "The area where a pair of conflicting changes happened is marked with markers <<<<<<<, =======, and >>>>>>>."
  fuente: f01-22
  ancla: https://git-scm.com/docs/git-merge
  consultada: 2026-11-12

- id: h01-494
  hecho: En esa presentación, la parte anterior a ======= suele ser tu lado y la posterior suele ser el lado del otro.
  evidencia: "The part before the ======= is typically your side, and the part afterwards is typically their side."
  fuente: f01-22
  ancla: https://git-scm.com/docs/git-merge
  consultada: 2026-11-12

- id: h01-495
  hecho: Se puede usar un estilo alternativo de presentación de conflictos configurando la variable merge.conflictStyle con diff3 o zdiff3.
  evidencia: "An alternative style can be used by setting the merge.conflictStyle configuration variable to either diff3 or zdiff3."
  fuente: f01-22
  ancla: https://git-scm.com/docs/git-merge
  consultada: 2026-11-12

- id: h01-496
  hecho: El estilo alternativo diff3 añade un marcador ||||||| y el texto original antes del marcador =======.
  evidencia: "a ======= marker, changes made by the other side, and then a >>>>>>> marker. An alternate style, "diff3", adds a ||||||| marker and the original text before the ======= marker."
  fuente: f01-22
  ancla: https://git-scm.com/docs/git-merge
  consultada: 2026-11-12

- id: h01-497
  hecho: Con --ff, git merge resuelve la fusión como avance rápido cuando es posible, es decir, solo actualiza el puntero de la rama sin crear un commit de fusión.
  evidencia: "With --ff, when possible resolve the merge as a fast-forward (only update the branch pointer to match the merged branch; do not create a merge commit)."
  fuente: f01-22
  ancla: https://git-scm.com/docs/git-merge
  consultada: 2026-11-12

- id: h01-498
  hecho: Con --no-ff, git merge crea un commit de fusión en todos los casos, incluso cuando la fusión podría resolverse como avance rápido.
  evidencia: "With --no-ff, create a merge commit in all cases, even when the merge could instead be resolved as a fast-forward."
  fuente: f01-22
  ancla: https://git-scm.com/docs/git-merge
  consultada: 2026-11-12

- id: h01-499
  hecho: Con --ff-only, git merge resuelve la fusión como avance rápido cuando es posible y, si no lo es, se niega a fusionar y termina con un estado distinto de cero.
  evidencia: "With --ff-only, resolve the merge as a fast-forward when possible. When not possible, refuse to merge and exit with a non-zero status."
  fuente: f01-22
  ancla: https://git-scm.com/docs/git-merge
  consultada: 2026-11-12

> NOTA (huecos): ni la copia local de git-switch (f01-20) ni la de git-checkout (f01-21) contienen advertencia alguna de que git switch sea experimental; no se registra hecho al respecto. De f01-21 solo se ha recogido el modo dual y la sección DETACHED HEAD.

## 1.5 Rebase y reescribir historia

- id: h01-501
  hecho: Git ofrece dos formas de integrar cambios de una rama en otra: la fusión (merge) y la reorganización (rebase).
  evidencia: "En Git tenemos dos formas de integrar cambios de una rama en otra: la fusión (merge) y la reorganización (rebase)."
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-502
  hecho: git merge hace una fusión a tres bandas entre las dos últimas instantáneas de cada rama y su ancestro común.
  evidencia: "es el comando git merge. Realiza una fusión a tres bandas entre las dos últimas instantáneas de cada rama (C3 y C4) y el ancestro común a ambas (C2)"
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-503
  hecho: git rebase captura los cambios confirmados en una rama y los reaplica sobre otra.
  evidencia: "Con el comando git rebase, puedes capturar todos los cambios confirmados en una rama y reaplicarlos sobre otra."
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-504
  hecho: Git va al ancestro común de ambas ramas: la rama actual y aquella sobre la que se quiere reorganizar.
  evidencia: "Haciendo que Git vaya al ancestro común de ambas ramas (donde estás actualmente y de donde quieres reorganizar)"
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-505
  hecho: Saca las diferencias que introduce cada confirmación de la rama actual.
  evidencia: "saque las diferencias introducidas por cada confirmación en la rama donde estás"
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-506
  hecho: Guarda esas diferencias en archivos temporales.
  evidencia: "guarde esas diferencias en archivos temporales"
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-507
  hecho: Reinicia (reset) la rama actual hasta la misma confirmación que la rama sobre la que se reorganiza.
  evidencia: "reinicie (reset) la rama actual hasta llevarla a la misma confirmación que la rama de donde quieres reorganizar"
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-508
  hecho: Por último, vuelve a aplicar los cambios en orden.
  evidencia: "finalmente, vuelva a aplicar ordenadamente los cambios"
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-509
  hecho: Tras reorganizar los cambios de C4 sobre C3, se puede volver a la rama master y hacer una fusión con avance rápido (fast-forward merge).
  evidencia: "Reorganizando sobre C3 los cambios introducidos en C4 En este momento, puedes volver a la rama master y hacer una fusión con avance rápido (fast-forward merge)."
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-510
  hecho: La instantánea final es la misma tanto si se llega por rebase como por merge; solo cambia el historial.
  evidencia: "la instantánea (snapshot) apuntada por la confirmación (commit) final, tanto si es producto de una reorganización (rebase) como si lo es de una fusión (merge), es exactamente la misma instantánea; lo único diferente es el historial"
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-511
  hecho: El historial de una rama reorganizada aparece siempre como lineal.
  evidencia: "Si examinas el historial de una rama reorganizada, este aparece siempre como un historial lineal"
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-512
  hecho: Habitualmente se opta por reorganizar cuando se quiere estar seguro de que las confirmaciones propias se pueden aplicar limpiamente sobre una rama remota.
  evidencia: "Si examinas el historial de una rama reorganizada, este aparece siempre como un historial lineal: como si todo el trabajo se hubiera realizado en series, aunque realmente se haya hecho en paralelo. Habitualmente, optarás por esta vía cuando quieras estar seguro de que tus confirmaciones de cambio (commits) se pueden aplicar limpiamente sobre una rama remota"
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-513
  hecho: Si se reorganiza el trabajo sobre origin/master antes de enviarlo al proyecto principal, quien mantiene el proyecto no necesita integrarlo: le basta un avance rápido o una incorporación limpia.
  evidencia: "reorganizar lo realizado en la rama origin/master cuando lo tengas todo listo para enviarlo al proyecto principal. De esta forma, la persona que mantiene el proyecto no necesitará hacer ninguna integración con tu trabajo; le bastará con un avance rápido o una incorporación limpia."
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-514
  hecho: Rebase reaplica los cambios de una rama sobre otra en el mismo orden en que se introdujeron.
  evidencia: "La reorganización vuelve a aplicar cambios de una rama de trabajo sobre otra rama, en el mismo orden en que fueron introducidos en la primera"
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-515
  hecho: Merge combina entre sí los dos puntos finales de ambas ramas.
  evidencia: "mientras que la fusión combina entre sí los dos puntos finales de ambas ramas."
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-516
  hecho: Con la opción --onto de git rebase se pueden coger los cambios del cliente que no están en server y reaplicarlos sobre la rama principal.
  evidencia: "Puedes coger los cambios del cliente que no están en server (C8 y C9) y reaplicarlos sobre tu rama principal usando la opción --onto del comando git rebase"
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-517
  hecho: git rebase --onto master server client toma los cambios desde el ancestro común entre client y server y los aplica en master.
  evidencia: "git rebase --onto master server client Esto viene a decir: “Activa la rama client, averigua los cambios desde el ancestro común entre las ramas client y server, y aplicalos en la rama master”"
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-518
  hecho: La forma git rebase [rama-base] [rama-puntual] activa la rama puntual y la aplica sobre la rama base.
  evidencia: "git rebase [rama-base] [rama-puntual], el cual activa la rama puntual (server en este caso) y la aplica sobre la rama base (master en este caso)"
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-519
  hecho: Regla de Pro Git: no reorganizar confirmaciones enviadas (push) a un repositorio público.
  evidencia: "Nunca reorganices confirmaciones de cambio (commits) que hayas enviado (push) a un repositorio público."
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-520
  hecho: Al reorganizar se abandonan las confirmaciones ya creadas y se crean otras nuevas, similares pero diferentes.
  evidencia: "Cuando reorganizas algo, estás abandonando las confirmaciones de cambio ya creadas y estás creando unas nuevas; que son similares, pero diferentes."
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-521
  hecho: Si otros ya habían recogido las confirmaciones reescritas, deberán volver a fusionar su trabajo y recoger el suyo se complica mucho.
  evidencia: "Si envías (push) confirmaciones (commits) a alguna parte, y otros las recogen (pull) de allí; y después vas tú y las reescribes con git rebase y las vuelves a enviar (push); tus colaboradores tendrán que refusionar (re-merge) su trabajo y todo se volverá tremendamente complicado cuando intentes recoger (pull) su trabajo de vuelta sobre el tuyo."
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-522
  hecho: La persona que había llevado cambios al servidor central decide retroceder y reorganizar su trabajo, y sobrescribe el registro del servidor con git push --force.
  evidencia: "la persona que había llevado cambios al servidor central decide retroceder y reorganizar su trabajo; haciendo un git push --force para sobrescribir el registro en el servidor"
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-523
  hecho: Si alguien envió confirmaciones reorganizadas que abandonan aquellas en las que basabas tu trabajo y haces git pull, se crea una fusión confirmada que incluye ambas líneas del historial.
  evidencia: "Alguien envió (push) confirmaciones (commits) reorganizadas, abandonando las confirmaciones en las que tu habías basado tu trabajo Ahora los dos están en un aprieto. Si haces git pull crearás una fusión confirmada, la cual incluirá ambas líneas del historial"
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-524
  hecho: Cuando se vuelve a fusionar el mismo trabajo en una nueva fusión confirmada, git log muestra dos confirmaciones con el mismo autor, fecha y mensaje, lo que resulta confuso.
  evidencia: "Vuelves a fusionar el mismo trabajo en una nueva fusión confirmada Si ejecutas git log sobre un historial así, verás dos confirmaciones hechas por el mismo autor y con la misma fecha y mensaje, lo cual será confuso."
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-525
  hecho: Además del SHA-1, Git calcula una suma de control basada en el parche que introduce una confirmación, conocida como patch-id.
  evidencia: "Además de la suma de control SHA-1, Git calcula una suma de control basada en el parche que introduce una confirmación. A esta se le conoce como “patch-id”."
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-526
  hecho: Al reorganizar el trabajo sobrescrito sobre las nuevas confirmaciones del compañero, Git puede identificar qué parte es propia y aplicarla en la rama nueva.
  evidencia: "Si te traes el trabajo que ha sido sobreescrito y lo reorganizas sobre las nuevas confirmaciones de tu compañero, es posible que Git pueda identificar qué parte correspondía específicamente a tu trabajo y aplicarla de vuelta en la rama nueva."
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-527
  hecho: Esa identificación solo funciona si las dos versiones de la confirmación son parches muy similares.
  evidencia: "Esto solo funciona si C4 y el C4' de tu compañero son parches muy similares."
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-528
  hecho: Se puede ejecutar git pull --rebase en vez del git pull tradicional para simplificar el proceso.
  evidencia: "También puedes simplificar el proceso si ejecutas git pull --rebase en vez del tradicional git pull."
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-529
  hecho: Reorganizar solo confirmaciones que nunca han estado disponibles públicamente no da problemas.
  evidencia: "si sólo reorganizas confirmaciones (commits) que nunca han estado disponibles públicamente, no tendrás problemas."
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-530
  hecho: Si aun así se ve necesario reorganizar, Pro Git aconseja asegurarse de que todos sepan que deben ejecutar git pull --rebase para aliviar la frustración.
  evidencia: "Si tu compañero o tú ven que aun así es necesario hacerlo en algún momento, asegúrense que todos sepan que deben ejecutar git pull --rebase para intentar aliviar en lo posible la frustración."
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-531
  hecho: Primera visión del historial: es un registro de todo lo que ha pasado.
  evidencia: "Para algunos, el historial de confirmaciones de tu repositorio es un registro de todo lo que ha pasado."
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-532
  hecho: Para quien ve el historial como un documento histórico que no debería alterarse, cambiarlo es casi como blasfemar: estaría mintiendo sobre lo que en verdad ocurrió.
  evidencia: "Un documento histórico, valioso por sí mismo y que no debería ser alterado. Desde este punto de vista, cambiar el historial de confirmaciones es casi como blasfemar; estarías mintiendo sobre lo que en verdad ocurrió."
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-533
  hecho: Segunda visión del historial: es la historia de cómo se hizo el proyecto.
  evidencia: "el historial de confirmaciones es la historia de cómo se hizo tu proyecto."
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-534
  hecho: Herramientas como rebase y filter-branch se utilizan para contar la historia de la mejor manera para los futuros lectores.
  evidencia: "Esta es el área que utiliza herramientas como rebase y filter-branch para contar la historia de la mejor manera para los futuros lectores."
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-535
  hecho: Pro Git propone reorganizar el trabajo local aún no compartido antes de enviarlo, y nunca reorganizar lo ya compartido.
  evidencia: "Normalmente, la manera de sacar lo mejor de ambas es reorganizar tu trabajo local, que aún no has compartido, antes de enviarlo a algún lugar; pero nunca reorganizar nada que ya haya sido compartido."
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-536
  hecho: Cambiar la última confirmación es probablemente lo más común que se hace con el historial.
  evidencia: "Cambiar la última confirmación es probablemente lo más común que le harás a tu historia."
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-537
  hecho: git commit --amend abre el editor con el mensaje de la última confirmación para modificarlo.
  evidencia: "git commit --amend Esto te envía al editor de texto, el cual tiene tu confirmación final, listo para modificarse en el mensaje."
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-538
  hecho: Se manejan los cambios editando el archivo y usando git add o git rm, y el git commit --amend siguiente toma el área de trabajo actual y la convierte en la instantánea de la nueva confirmación.
  evidencia: "Tu manejas los cambios que quieras editando el archivo y oprimiendo git add en éste o git rm a un archivo adjunto, y el subsecuente git commit --amend toma tu área de trabajo actual y la vuelve una instantánea para la nueva confirmación"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-539
  hecho: Pro Git advierte de ser cuidadoso con la técnica de git commit --amend porque puede modificar el SHA-1 de la confirmación.
  evidencia: "y el subsecuente git commit --amend toma tu área de trabajo actual y la vuelve una instantánea para la nueva confirmación. Debes ser cuidadoso con esta técnica porque puedes modificar los cambios del SHA-1 de la confirmación"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-540
  hecho: Git no tiene una herramienta para modificar la historia, pero se puede usar la herramienta de rebase para modificar una confirmación que está más atrás en la historia.
  evidencia: "Para modificar una confirmación que está más atrás en tu historia, deberás aplicar herramientas más complejas Git no tiene una herramienta para modificar la historia, pero puedes usar la herramienta de rebase"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-541
  hecho: Con el rebase interactivo se puede parar tras cada confirmación a modificar para cambiar su mensaje o añadir archivos.
  evidencia: "Con la herramienta interactiva del rebase, puedes parar justo después de cada confirmación que quieras modificar y cambiar su mensaje, añadir archivos, o hacer cualquier cosa que quieras"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-542
  hecho: El rebase interactivo se ejecuta añadiendo -i a git rebase.
  evidencia: "Puedes ejecutar el rebase interactivamente agregando el comando -i a git rebase."
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-543
  hecho: Con git rebase -i HEAD~3 se reescribe cualquier confirmación del rango HEAD~3..HEAD, cambie o no su mensaje.
  evidencia: "git rebase -i HEAD~3 Recuerda de Nuevo que este es un comando de rebase – cualquier confirmación incluida en el rango de HEAD~3..HEAD será reescrita, aún si cambias el mensaje o no."
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-544
  hecho: En un comando de rebase, Pro Git advierte de no incluir cualquier confirmación que ya se haya enviado al servidor central.
  evidencia: "este es un comando de rebase – cualquier confirmación incluida en el rango de HEAD~3..HEAD será reescrita, aún si cambias el mensaje o no. No incluyas cualquier confirmación que ya hayas enviado al servidor central"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-545
  hecho: Incluir confirmaciones ya enviadas al servidor central confundirá a los demás desarrolladores, al proporcionar una versión alternativa del mismo cambio.
  evidencia: "No incluyas cualquier confirmación que ya hayas enviado al servidor central – si lo haces esto confundirá a los demás desarrolladores proporcionando una versión alternativa del mismo cambio"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-546
  hecho: Pro Git señala que las confirmaciones aparecen en el orden contrario al que normalmente se vería usando el comando log.
  evidencia: "Es importante el notar que estas confirmaciones son escuchadas en el orden contrario del que tú normalmente las verías usando el comando de log."
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-547
  hecho: El script del rebase interactivo reproduce los cambios de cada confirmación de arriba a abajo.
  evidencia: "El rebase interactivo te da un script que va a utilizarse. Este empezará en la confirmación que especificas en la línea de comandos (HEAD~3) y reproducirá los cambios introducidos en cada una de estas confirmaciones de arriba a abajo"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-548
  hecho: Acción pick: usar la confirmación.
  evidencia: "p, pick = use commit"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-549
  hecho: Acción reword: usar la confirmación pero editar su mensaje.
  evidencia: "r, reword = use commit, but edit the commit message"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-550
  hecho: Acción edit: usar la confirmación pero parar para modificarla.
  evidencia: "e, edit = use commit, but stop for amending"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-551
  hecho: Acción squash: usar la confirmación y fundirla con la anterior.
  evidencia: "s, squash = use commit, but meld into previous commit"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-552
  hecho: Acción fixup: como squash, pero descarta el mensaje de log de la confirmación.
  evidencia: "f, fixup = like "squash", but discard this commit's log message"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-553
  hecho: Las líneas del script se pueden reordenar y se ejecutan de arriba a abajo.
  evidencia: "These lines can be re-ordered; they are executed from top to bottom."
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-554
  hecho: Si se borra una línea del script, esa confirmación se pierde.
  evidencia: "If you remove a line here THAT COMMIT WILL BE LOST."
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-555
  hecho: Si se borra todo el contenido del script, el rebase se aborta.
  evidencia: "However, if you remove everything, the rebase will be aborted."
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-556
  hecho: Para detener el rebase en una confirmación hay que cambiar pick por edit en su línea.
  evidencia: "cambia la palabra pick por la frase edit para cada una de las confirmaciones en las que quieres que el script se detenga"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-557
  hecho: Con edit, Git se para en cada confirmación marcada para que se modifique y se continúe al terminar.
  evidencia: "Si decides cambiar y elegir editar en más líneas, puedes repetir estos pasos para cada confirmación que cambies en cada edición. Cada vez, Git se parará, permitiéndote modificar la confirmación y continuar cuando hayas terminado"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-558
  hecho: Cuando se esté satisfecho con los cambios, Git indica ejecutar git rebase --continue.
  evidencia: "Once you’re satisfied with your changes, run git rebase --continue"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-559
  hecho: Con el rebase interactivo se pueden reordenar o eliminar confirmaciones.
  evidencia: "De igual manera puedes usar rebases interactivos para reordenar o remover confirmaciones enteramente."
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-560
  hecho: El rebase interactivo permite unir series de confirmaciones en una sola.
  evidencia: "También es posible el tomar series de confirmaciones y unirlas todas en una sola confirmación con la herramienta interactiva de rebase."
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-561
  hecho: Dividir una confirmación consiste en deshacerla y hacer confirmaciones parciales tantas veces como se quiera.
  evidencia: "Dividir una confirmación la deshace y después realiza etapas parciales de las confirmaciones tantas veces como confirmaciones desees finalizar."
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-562
  hecho: En el script de rebase -i se cambia a edit la instrucción de la confirmación que se quiere dividir.
  evidencia: "Puedes hacer eso en el script rebase -i cambiando la instrucción en la confirmación que quieres dividir a “edit”"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-563
  hecho: Una vez Git envía a la consola, se puede hacer un reseteo mixto de esa confirmación con git reset HEAD^.
  evidencia: "y te enviará directamente a la consola. Ahí, puedes hacer un reseteo mixto de esa confirmación con el git reset HEAD^"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-564
  hecho: Después se preparan y confirman los archivos en varias confirmaciones y se ejecuta git rebase --continue.
  evidencia: "Ahora puedes organizar y confirmar los archivos hasta que tengas varias confirmaciones y ejecutar git rebase --continue cuando hayas terminado"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-565
  hecho: Pro Git avisa de que este procedimiento cambia el SHA-1 de todas las confirmaciones de la lista, así que ninguna debería estar ya en un repositorio compartido.
  evidencia: "esto cambia el SHA-1s de todas tus confirmaciones en tu lista, así que asegúrate de que ninguna confirmación esté en esa lista que ya has puesto en un repositorio compartido."
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-566
  hecho: Existe otra opción para reescribir la historia, útil cuando se necesita reescribir un gran número de confirmaciones de una manera que se pueda scriptear.
  evidencia: "Existe otra opción en la parte de volver a escribir la historia que puedes usar si necesitas reescribir un gran número de confirmaciones de una manera que se puedan scriptear"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-567
  hecho: Advertencia sobre filter-branch: probablemente no usarlo salvo que el proyecto no sea público y nadie se haya basado en las confirmaciones.
  evidencia: "El comando es filter-branch, y este puede reescribir una gran cantidad de franjas de tu historia, así que probablemente no lo deberías usar a menos que tu proyecto aún no sea público y otra persona no se haya basado en las confirmaciones que estás a punto de reescribir."
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-568
  hecho: El --tree-filter inicia el comando específico después de cada revisión del proyecto y entonces vuelve a confirmar los resultados.
  evidencia: "El --tree-filter inicia el comando específico después de cada revisión del proyecto y éste entonces vuelve a confirmar los resultados."
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-569
  hecho: Para remover un archivo nombrado passwords.txt de toda la historia, Pro Git aplica --tree-filter a filter-branch con git filter-branch --tree-filter 'rm -f passwords.txt' HEAD.
  evidencia: "Para remover un archivo nombrado passwords.txt de tu historia complete puedes aplicar el comando --tree-filter a filter-branch: $ git filter-branch --tree-filter 'rm -f passwords.txt' HEAD"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-570
  hecho: Cada confirmación contiene el SHA-1 de sus padres.
  evidencia: "cada confirmación contiene el SHA-1 de sus padres"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-571
  hecho: Al reescribir cada confirmación para tener la nueva dirección de e-mail, el comando cambia el SHA-1 de cada confirmación de la historia, no solo de aquellas cuyo e-mail coincide, porque cada confirmación contiene el SHA-1 de sus padres.
  evidencia: "Esto va a través de la re-escripción de cada confirmación para tener tu nuva dirección. Porque cada confirmación contiene el SHA-1 de sus padres, este comando cambia cada confirmación del SHA-1 en tu historia, no solamente aquellos en los cuales el e-mail es el mismo o encaja"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-572
  hecho: Pro Git considera generalmente una buena idea hacer esto en una parte de prueba de la rama y hacer un hard-reset de la rama principal después de haber determinado que el resultado es el deseado.
  evidencia: "Es generalmente una buena idea hacer esto en una parte de prueba de la rama y hacer un hard-reset de tu rama principal después de haber determinado que el resultado es lo que realmente deseas."
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-573
  hecho: El comando filter-branch puede reescribir una gran cantidad de franjas de la historia.
  evidencia: "El comando es filter-branch, y este puede reescribir una gran cantidad de franjas de tu historia"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

## 1.5 Rebase y reescribir historia (fuentes añadidas)

- id: h01-574
  hecho: Durante un rebase con conflictos, tras resolver todos los conflictos, se puede continuar el proceso con git rebase --continue.
  evidencia: "After resolving all of the conflicts, you can continue the rebasing process with git rebase --continue"
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-575
  hecho: Durante un rebase con conflictos, git rebase --abort detiene el rebase y devuelve la rama a su estado original.
  evidencia: "Stop the git rebase and return your branch to its original state with git rebase --abort"
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-576
  hecho: Durante un rebase con conflictos, git rebase --skip omite el commit que causó el conflicto.
  evidencia: "Skip the commit that caused the merge conflict with git rebase --skip"
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-577
  hecho: En el rebase interactivo, cambiar «pick» por «edit» hace que git rebase se detenga tras aplicar ese commit, para poder editar archivos o mensaje, enmendar el commit y continuar.
  evidencia: "By replacing the command "pick" with the command "edit", you can tell git rebase to stop after applying that commit, so that you can edit the files and/or the commit message, amend the commit, and continue rebasing."
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-578
  hecho: El comando «break» interrumpe el rebase como lo haría «edit», pero sin aplicar antes ningún commit con cherry-pick.
  evidencia: "To interrupt the rebase (just like an "edit" command would do, but without cherry-picking any commit first), use the "break" command."
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-579
  hecho: Para editar solo el mensaje de un commit en un rebase interactivo se cambia «pick» por «reword».
  evidencia: "If you just want to edit the commit message for a commit, replace the command "pick" with the command "reword"."
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-580
  hecho: Para descartar un commit en un rebase interactivo se cambia «pick» por «drop» o se borra la línea correspondiente.
  evidencia: "To drop a commit, replace the command "pick" with "drop", or just delete the matching line."
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-581
  hecho: Para fundir dos o más commits en uno, se cambia «pick» por «squash» o «fixup» en el segundo commit y en los siguientes.
  evidencia: "If you want to fold two or more commits into one, replace the command "pick" for the second and subsequent commits with "squash" or "fixup"."
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-582
  hecho: En el mensaje sugerido para el commit fundido, los mensajes de los commits marcados con «fixup» se omiten, salvo que se use «fixup -c»; los de «squash» se concatenan con el del primer commit.
  evidencia: "The suggested commit message for the folded commit is the concatenation of the first commit’s message with those identified by "squash" commands, omitting the messages of commits identified by "fixup" commands, unless "fixup -c" is used."
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-583
  hecho: Reordenar y editar commits suele crear pasos intermedios sin probar; para comprobarlos se puede usar el comando «exec» (abreviado «x») en la lista de tareas.
  evidencia: "Reordering and editing commits usually creates untested intermediate steps. You may want to check that your history editing did not break anything by running a test, or at least recompiling at intermediate points in history by using the "exec" command (shortcut "x")."
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-584
  hecho: El rebase interactivo se detiene cuando un comando falla (sale con estado distinto de 0), para dar la oportunidad de arreglar el problema.
  evidencia: "The interactive rebase will stop when a command fails (i.e. exits with non-0 status) to give you an opportunity to fix the problem."
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-585
  hecho: El comando «exec» lanza el comando en una shell (por defecto, normalmente /bin/sh).
  evidencia: "The "exec" command launches the command in a shell (the default one, usually /bin/sh)"
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-586
  hecho: Con git rebase -i --exec "make test" se puede comprobar que los commits intermedios compilan.
  evidencia: "$ git rebase -i --exec "make test" This command lets you check that intermediate commits are compilable."
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-587
  hecho: Con --autosquash, git rebase combina automáticamente en commits anteriores los commits cuyos mensajes tienen un formato especial.
  evidencia: "Automatically squash commits with specially formatted messages into previous commits being rebased."
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-588
  hecho: Si el mensaje de un commit empieza por «squash! », «fixup! » o «amend! », el resto del título se toma como especificador de un commit anterior, que coincide si es el título o el hash de ese commit.
  evidencia: "If a commit message starts with "squash! ", "fixup! " or "amend! ", the remainder of the title is taken as a commit specifier, which matches a previous commit if it matches the title or the hash of that commit."
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-589
  hecho: Con --autosquash, en la lista de tareas los commits squash, fixup y amend pasan de pick a squash, fixup o fixup -C, y se mueven justo después del commit que modifican.
  evidencia: "In the rebase todo list, the actions of squash, fixup and amend commits are changed from pick to squash, fixup or fixup -C, respectively, and they are moved right after the commit they modify."
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-590
  hecho: La forma recomendada de crear commits con marcas de squash es usar las opciones --squash, --fixup, --fixup=amend: o --fixup=reword: de git commit, que reciben el commit objetivo como argumento.
  evidencia: "The recommended way to create commits with squash markers is by using the --squash, --fixup, --fixup=amend: or --fixup=reword: options of git-commit[1], which take the target commit as an argument and automatically fill in the title of the new commit from that."
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-591
  hecho: La documentación de git rebase advierte de que rebasar (o reescribir de cualquier otro modo) una rama sobre la que otros han basado trabajo es mala idea: quien está aguas abajo debe arreglar su historial a mano.
  evidencia: "Rebasing (or any other form of rewriting) a branch that others have based work on is a bad idea: anyone downstream of it is forced to manually fix their history."
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-592
  hecho: La documentación sostiene que la verdadera solución es evitar rebasar la rama upstream desde el principio.
  evidencia: "The real fix, however, would be to avoid rebasing the upstream in the first place."
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-593
  hecho: En el ejemplo de la documentación, para limpiar los commits duplicados hay que hacer rebase de topic sobre la nueva punta de subsystem, lo que arrastra a quienes dependen de topic, que también deben hacer rebase.
  evidencia: "To clean things up, you need to transplant the commits on topic to the new subsystem tip, i.e., rebase topic. This becomes a ripple effect: anyone downstream from topic is forced to rebase too, and so on!"
  fuente: f01-23
  ancla: https://git-scm.com/docs/git-rebase
  consultada: 2026-11-12

- id: h01-594
  hecho: git revert registra nuevos commits que revierten el efecto de commits anteriores (a menudo solo uno defectuoso).
  evidencia: "Note: git revert is used to record some new commits to reverse the effect of some earlier commits (often only a faulty one)."
  fuente: f01-24
  ancla: https://git-scm.com/docs/git-revert
  consultada: 2026-11-12

- id: h01-595
  hecho: git revert requiere que el árbol de trabajo esté limpio, sin modificaciones respecto al commit HEAD.
  evidencia: "Given one or more existing commits, revert the changes that the related patches introduce, and record some new commits that record them. This requires your working tree to be clean (no modifications from the HEAD commit)."
  fuente: f01-24
  ancla: https://git-scm.com/docs/git-revert
  consultada: 2026-11-12

- id: h01-596
  hecho: Según la página de git revert, para descartar todos los cambios sin confirmar del directorio de trabajo hay que ver git reset, en particular la opción --hard.
  evidencia: "If you want to throw away all uncommitted changes in your working directory, you should see git-reset[1], particularly the --hard option."
  fuente: f01-24
  ancla: https://git-scm.com/docs/git-revert
  consultada: 2026-11-12

- id: h01-597
  hecho: Según la página de git revert, para extraer archivos concretos tal como estaban en otro commit hay que ver git restore, en concreto la opción --source.
  evidencia: "If you want to extract specific files as they were in another commit, you should see git-restore[1], specifically the --source option."
  fuente: f01-24
  ancla: https://git-scm.com/docs/git-revert
  consultada: 2026-11-12

- id: h01-598
  hecho: Normalmente no se puede revertir un merge porque no se sabe qué lado se considera la línea principal; la opción -m (--mainline) indica el número de padre (desde 1) de la línea principal y permite revertir el cambio respecto a ese padre.
  evidencia: "-m parent-number --mainline parent-number Usually you cannot revert a merge because you do not know which side of the merge should be considered the mainline. This option specifies the parent number (starting from 1) of the mainline and allows revert to reverse the change relative to the specified parent."
  fuente: f01-24
  ancla: https://git-scm.com/docs/git-revert
  consultada: 2026-11-12

## 1.6 Bajo el capó: objetos y referencias

- id: h01-601
  hecho: Git es, en esencia, un sistema de archivos de contenido localizable con una interfaz de usuario de control de versiones construida encima.
  evidencia: "Git es fundamentalmente un sistema de archivo de contenido localizable con una interfaz de usuario de VCS escrita sobre él"
  fuente: f01-14
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Fontaner%c3%ada-y-porcelana
  consultada: 2026-11-12

- id: h01-602
  hecho: Existen comandos de bajo nivel pensados para encadenarse al estilo UNIX o para usarse en scripts.
  evidencia: "existen unos cuantos verbos para realizar tareas de bajo nivel y que se diseñaron para poder ser utilizados de forma encadenada al estilo UNIX o para ser utilizados en scripts"
  fuente: f01-14
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Fontaner%c3%ada-y-porcelana
  consultada: 2026-11-12

- id: h01-603
  hecho: Existen unos comandos conocidos como «comandos de fontanería» y otros, más amigables, conocidos como «comandos de porcelana».
  evidencia: "Estos comandos son conocidos como los "comandos de fontanería", mientras que los comandos más amigables son conocidos como los "comandos de porcelana"."
  fuente: f01-14
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Fontaner%c3%ada-y-porcelana
  consultada: 2026-11-12

- id: h01-604
  hecho: Muchos comandos de fontanería no se piensan para uso manual, sino como bloques de construcción de herramientas y scripts propios.
  evidencia: "comandos de fontanería; comandos que te darán acceso a los entresijos internos de Git y que te ayudarán a comprender cómo y por qué hace Git lo que hace como lo hace. Muchos de estos comando no están pensados para ser utilizados manualmente desde la línea de comandos; sino más bien para ser utilizados como bloques de construcción para nuevas herramientas y scripts de usuario personalizados."
  fuente: f01-14
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Fontaner%c3%ada-y-porcelana
  consultada: 2026-11-12

- id: h01-605
  hecho: git init crea la carpeta .git, donde se ubica prácticamente todo lo que Git almacena y manipula.
  evidencia: "Cuando lanzas git init sobre una carpeta nueva o sobre una ya existente, Git crea la carpeta auxiliar .git; la carpeta donde se ubica prácticamente todo lo almacenado y manipulado por Git"
  fuente: f01-14
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Fontaner%c3%ada-y-porcelana
  consultada: 2026-11-12

- id: h01-606
  hecho: Copiar la carpeta .git a otro lugar basta para tener una copia completa del repositorio.
  evidencia: ".git; la carpeta donde se ubica prácticamente todo lo almacenado y manipulado por Git. Si deseas hacer una copia de seguridad de tu repositorio, con tan solo copiar esta carpeta a cualquier otro lugar ya tienes tu copia completa."
  fuente: f01-14
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Fontaner%c3%ada-y-porcelana
  consultada: 2026-11-12

- id: h01-607
  hecho: Un repositorio recién creado con git init contiene HEAD, config, description, hooks, info, objects y refs.
  evidencia: "HEAD config* description hooks/ info/ objects/ refs/ Puede que veas algunos otros archivos en tu carpeta .git, pero este es el contenido de un repositorio recién creado tras ejecutar git init"
  fuente: f01-14
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Fontaner%c3%ada-y-porcelana
  consultada: 2026-11-12

- id: h01-608
  hecho: El archivo config guarda las opciones de configuración específicas del proyecto.
  evidencia: "El archivo config contiene las opciones de configuración específicas de este proyecto concreto"
  fuente: f01-14
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Fontaner%c3%ada-y-porcelana
  consultada: 2026-11-12

- id: h01-609
  hecho: La carpeta hooks contiene los scripts de la parte cliente y de la parte servidor.
  evidencia: "La carpeta hooks contiene tus scripts, tanto de la parte cliente como de la parte servidor"
  fuente: f01-14
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Fontaner%c3%ada-y-porcelana
  consultada: 2026-11-12

- id: h01-610
  hecho: Hay cuatro entradas importantes: los archivos HEAD e index y las carpetas objects y refs.
  evidencia: "Esto nos deja con cuatro entradas importantes: los archivos HEAD e index (todavía por ser creado), y las carpetas objects y refs."
  fuente: f01-14
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Fontaner%c3%ada-y-porcelana
  consultada: 2026-11-12

- id: h01-611
  hecho: La carpeta objects guarda el contenido de la base de datos.
  evidencia: "La carpeta objects guarda el contenido de tu base de datos"
  fuente: f01-14
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Fontaner%c3%ada-y-porcelana
  consultada: 2026-11-12

- id: h01-612
  hecho: La carpeta refs guarda los apuntadores a las confirmaciones.
  evidencia: "la carpeta refs guarda los apuntadores a las confirmaciones de cambios (commits)"
  fuente: f01-14
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Fontaner%c3%ada-y-porcelana
  consultada: 2026-11-12

- id: h01-613
  hecho: El archivo HEAD apunta a la rama que tienes activa en ese momento.
  evidencia: "el archivo HEAD apunta a la rama que tengas activa (checked out) en este momento"
  fuente: f01-14
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Fontaner%c3%ada-y-porcelana
  consultada: 2026-11-12

- id: h01-614
  hecho: El archivo index es donde Git guarda la información del área de preparación.
  evidencia: "el archivo index es donde Git almacena la información sobre tu área de preparación (staging área)"
  fuente: f01-14
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Fontaner%c3%ada-y-porcelana
  consultada: 2026-11-12

- id: h01-615
  hecho: El núcleo de Git es un simple almacén de claves y valores.
  evidencia: "el núcleo Git es un simple almacén de claves y valores"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-616
  hecho: Al insertar cualquier contenido, Git devuelve una clave con la que se puede recuperar ese contenido cuando se quiera.
  evidencia: "Pues significa que el núcleo Git es un simple almacén de claves y valores. Cuando insertas cualquier tipo de contenido, él te devuelve una clave que puedes utilizar para recuperar de nuevo dicho contenido en cualquier momento."
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-617
  hecho: hash-object es un comando de fontanería que guarda datos en .git y devuelve la clave con la que se han guardado.
  evidencia: "Para verlo en acción, puedes utilizar el comando de fontanería hash-object. Este comando coge ciertos datos, los guarda en la carpeta .git. y te devuelve la clave bajo la cual se han guardado."
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-618
  hecho: Sin la opción -w, hash-object solo responde cuál sería la clave del objeto, sin guardarlo.
  evidencia: "La opción -w indica a hash-object que ha de guardar el objeto; de otro modo, el comando solo te respondería cual sería su clave."
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-619
  hecho: La clave que devuelve hash-object es una suma de comprobación de 40 caracteres.
  evidencia: "si no lo indicas, hash-object espera una ruta de archivo al final. La salida del comando es una suma de comprobación (checksum hash) de 40 caracteres."
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-620
  hecho: La suma SHA-1 se calcula sobre el contenido guardado más una cabecera.
  evidencia: "Este checksum hash SHA-1 es una suma de comprobación del contenido que estás guardando más una cabecera"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-621
  hecho: Git guarda cada pieza de contenido en un archivo propio, nombrado con el SHA-1 del contenido y su cabecera.
  evidencia: "En principio, esta es la forma en que guarda Git los contenidos; como un archivo por cada pieza de contenido, nombrado con la suma de comprobación SHA-1 del contenido y su cabecera"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-622
  hecho: La subcarpeta se nombra con los 2 primeros caracteres del SHA-1 y el archivo con los 38 restantes.
  evidencia: "La subcarpeta se nombra con los primeros 2 caracteres del SHA-1, y el archivo con los restantes 38 caracteres."
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-623
  hecho: cat-file sirve para inspeccionar objetos Git.
  evidencia: "Puedes volver a recuperar los contenidos usando el comando cat-file. Este comando es algo así como una "navaja suiza" para inspeccionar objetos Git."
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-624
  hecho: Con la opción -p, cat-file deduce el tipo de contenido y lo muestra de forma adecuada.
  evidencia: "Pasándole la opción -p, puedes indicar al comando cat-file que deduzca el tipo de contenido y te lo muestre adecuadamente"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-625
  hecho: Con cat-file -t se comprueba el tipo de cualquier objeto a partir de su clave SHA-1.
  evidencia: "Con la orden cat-file -t puedes comprobar el tipo de cualquier objeto almacenado en Git, sin mas que indicar su clave SHA-1"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-626
  hecho: Al guardar contenido en la base de datos no se guarda el nombre del archivo en el sistema, solo su contenido.
  evidencia: "realmente no estás guardando el nombre de tu archivo en el sistema, --solo su contenido--."
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-627
  hecho: El objeto que guarda solo el contenido de un archivo, sin su nombre, se denomina blob (binary large object).
  evidencia: "realmente no estás guardando el nombre de tu archivo en el sistema, --solo su contenido--. Este tipo de objeto se denomina un blob (binary large object)."
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-628
  hecho: Los árboles resuelven el problema de guardar nombres de archivo y agrupar varios archivos.
  evidencia: "El siguiente tipo de objeto a revisar serán los árboles, que se encargan de resolver el problema de guardar un nombre de archivo, a la par que guardamos conjuntamente un grupo de archivos."
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-629
  hecho: Los árboles corresponden a las entradas de carpetas y los blobs, más o menos, al contenido de los archivos.
  evidencia: "Todo el contenido se guarda como objetos árbol (tree) u objetos binarios (blob), correspondiendo los árboles a las entradas de carpetas; y correspondiendo los binarios, mas o menos, a los contenidos de los archivos (inodes)"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-630
  hecho: Cada entrada de un árbol tiene un puntero SHA-1 a un blob o a un subárbol, más el modo, el tipo y el nombre de archivo.
  evidencia: "Un objeto tipo árbol tiene una o más entradas de tipo árbol, cada una de las cuales consta de un puntero SHA-1 a un objeto binario (blob) o a un subárbol, más sus correspondientes datos de modo, tipo y nombre de archivo"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-631
  hecho: La expresión master^{tree} designa el árbol al que apunta la última confirmación de la rama master.
  evidencia: "La sentencia master^{tree} indica el objeto árbol apuntado por la última confirmación de cambios (commit) en tu rama principal (master)."
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-632
  hecho: En el ejemplo, la carpeta lib no es un blob, sino un puntero a otro objeto árbol.
  evidencia: "Fíjate en que la carpeta lib no es un objeto binario, sino un apuntador a otro objeto tipo árbol."
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-633
  hecho: Git suele crear un árbol a partir del estado del área de preparación (el índice).
  evidencia: "Habitualmente Git suele crear un árbol a partir del estado de tu área de preparación (staging area) o índice"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-634
  hecho: El comando write-tree escribe el área de preparación en un objeto árbol.
  evidencia: "Tras esto, puedes usar el comando write-tree para escribir el área de preparación a un objeto tipo árbol."
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-635
  hecho: El modo 100644 denota un archivo normal.
  evidencia: "En este caso, indicas un modo 100644, el modo que denota un archivo normal."
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-636
  hecho: El modo 100755 denota un archivo ejecutable y el 120000 un enlace simbólico.
  evidencia: "indicas un modo 100644, el modo que denota un archivo normal. Otras opciones son 100755, para un archivo ejecutable; o 120000, para un enlace simbólico."
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-637
  hecho: El comando commit-tree se invoca indicando el SHA-1 de un árbol y los objetos de confirmación de cambios que lo preceden, si hay alguno.
  evidencia: "Para crearlos, tan solo has de llamar al comando commit-tree, indicando uno de los árboles SHA-1 y los objetos de confirmación de cambios que lo preceden (si es que lo precede alguno)"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-638
  hecho: Un objeto de confirmación contiene el árbol que representa el estado del proyecto en ese momento.
  evidencia: "El formato para un objeto de confirmación de cambios (commit) es sencillo, contemplando: el objeto tipo árbol para la situación del proyecto en ese momento puntual"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-639
  hecho: La información sobre el autor/confirmador usa las opciones de configuración user.name y user.email y una marca de tiempo.
  evidencia: "la información sobre el autor/confirmador (que usa tus opciones de configuración user.name y user.email y una marca de tiempo)"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-640
  hecho: Tras la información sobre el autor/confirmador vienen una línea en blanco y el mensaje de la confirmación de cambios.
  evidencia: "la información sobre el autor/confirmador (que usa tus opciones de configuración user.name y user.email y una marca de tiempo); una línea en blanco; y el mensaje de la confirmación de cambios"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-641
  hecho: En el ejemplo, los otros dos objetos de confirmación de cambios se escriben relacionando cada uno con su inmediato anterior.
  evidencia: "Puedes seguir adelante, escribiendo los otros dos objetos de confirmación de cambios, y relacionando cada uno de ellos con su inmediato anterior"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-642
  hecho: En el ejemplo, cada una de las tres confirmaciones apunta a uno de los tres árboles creados antes.
  evidencia: "Cada uno de estos tres objetos de confirmación de cambios apunta a uno de los tres objetos tipo árbol que habías creado previamente."
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-643
  hecho: Con git add y git commit Git guarda blobs de los archivos modificados, actualiza el índice, escribe árboles y escribe las confirmaciones que los referencian, enlazadas con la anterior.
  evidencia: "Esto es básicamente lo que hace Git cada vez que utilizas los comandos git add y git commit: guardar objetos binarios (blobs) para los archivos modificados, actualizar el índice, escribir árboles (trees), escribir objetos de confirmación de cambios (commits) que los referencian y relacionar cada uno de ellos con su inmediato precedente"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-644
  hecho: Blobs, árboles y confirmaciones se guardan como archivos separados en .git/objects.
  evidencia: "Estos tres objetos Git, -binario, árbol y confirmación de cambios--, se guardan como archivos separados en la carpeta .git/objects."
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-645
  hecho: La cabecera de un objeto empieza por el tipo de objeto.
  evidencia: "Git construye la cabecera comenzando por el tipo de objeto, en este caso un objeto binario grande (blob)."
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-646
  hecho: Tras el tipo, la cabecera lleva un espacio, el tamaño del contenido y un byte nulo.
  evidencia: "Git construye la cabecera comenzando por el tipo de objeto, en este caso un objeto binario grande (blob). Después añade un espacio, seguido del tamaño del contenido y termina con un byte nulo"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-647
  hecho: Git concatena cabecera y contenido y calcula sobre el conjunto la suma SHA-1.
  evidencia: "Git concatena la cabecera y el contenido original, para calcular la suma de control SHA-1 conjunta."
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-648
  hecho: Git comprime todo el contenido con zlib.
  evidencia: "Git comprime todo el contenido con zlib"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-649
  hecho: Los demás objetos Git se almacenan de forma similar, pero sus cabeceras comienzan con un tipo diferente.
  evidencia: "Todos los demas objetos Git se almacenan de forma similar, pero con la diferencia de que sus cabeceras comienzan con un tipo diferente"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-650
  hecho: Las cabeceras de los demás objetos empiezan por commit o por tree en lugar de blob.
  evidencia: "Todos los demas objetos Git se almacenan de forma similar, pero con la diferencia de que sus cabeceras comienzan con un tipo diferente — en lugar de blob (objeto binario grande), comenzarán por commit (confirmación de cambios), o por tree (árbol)"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-651
  hecho: El contenido de un blob puede ser casi cualquier cosa, pero el de un commit o un árbol sigue un formato interno concreto.
  evidencia: "el contenido de un binario (blob) puede ser prácticamente cualquier cosa, mientras que el contenido de una confirmación de cambios (commit) o de un árbol (tree) han de seguir unos formatos internos muy concretos"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-652
  hecho: Las referencias (refs) son archivos de .git/refs que contienen valores SHA-1 y tienen un nombre.
  evidencia: "En Git, esto es lo que se conoce como "referencias" o "refs"; en la carpeta .git/refs puedes encontrar esos archivos con valores SHA-1 y nombres"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-653
  hecho: Una referencia permite usar un nombre simple en lugar de la suma SHA-1.
  evidencia: "junto con sus respectivos nombres simples que puedas utilizar como enlaces en lugar de la propia suma de comprobación. En Git, esto es lo que se conoce como "referencias" o "refs""
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-654
  hecho: En el repositorio de ejemplo, .git/refs contiene las subcarpetas heads y tags.
  evidencia: "pero sí contiene una estructura simple: $ find .git/refs .git/refs .git/refs/heads .git/refs/tags"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-655
  hecho: Técnicamente, una referencia se crea escribiendo un SHA-1 en un archivo de .git/refs/heads.
  evidencia: "Para crear una nueva referencia que te sirva de ayuda para recordar cual es tu última confirmación de cambios, puedes realizar técnicamente algo tan simple como: $ echo "1a410efbd13591db07496601ebc7a059dd55cfe9" > .git/refs/heads/master"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-656
  hecho: En el ejemplo, la referencia principal creada puede usarse en lugar del valor SHA-1 en todos los comandos.
  evidencia: "puedes utilizar esa referencia principal que acabas de crear, en lugar del valor SHA-1, en todos tus comandos"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-657
  hecho: No es conveniente editar directamente los archivos de referencia.
  evidencia: "No es conveniente editar directamente los archivos de referencia."
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-658
  hecho: El comando update-ref es un comando mucho más seguro que editar directamente los archivos de referencia para actualizar una referencia.
  evidencia: "No es conveniente editar directamente los archivos de referencia. Git suministra un comando mucho más seguro para hacer esto. Si necesitas actualizar una referencia, puedes utilizar el comando update-ref"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-659
  hecho: Una rama en Git es básicamente un simple apuntador o referencia a la cabeza de una línea de trabajo.
  evidencia: "Esto es lo que es básicamente una rama en Git: un simple apuntador o referencia a la cabeza de una línea de trabajo."
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-660
  hecho: En el ejemplo, git update-ref refs/heads/test cac0ca crea la rama test apuntando a la segunda confirmación.
  evidencia: "Para crear una rama hacia la segunda confirmación de cambios, puedes hacer: $ git update-ref refs/heads/test cac0ca"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-661
  hecho: En el ejemplo, la rama creada hacia la segunda confirmación contiene únicamente trabajo desde esa confirmación hacia atrás.
  evidencia: "Para crear una rama hacia la segunda confirmación de cambios, puedes hacer: $ git update-ref refs/heads/test cac0ca Y la rama contendrá únicamente trabajo desde esa confirmación de cambios hacia atrás."
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-662
  hecho: Con comandos como git branch (nombrederama), Git añade a la nueva referencia el valor SHA-1 de la última confirmación de cambios.
  evidencia: "Cuando lanzas comandos como git branch (nombrederama), lo que hace Git es añadir, a cualquier nueva referencia que vayas a crear, el valor SHA-1 de la última confirmación de cambios en esa rama"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-663
  hecho: Git sabe cuál es la última confirmación gracias al archivo HEAD.
  evidencia: "¿cómo sabe Git cuál es el valor SHA-1 de la última confirmación de cambios?. La respuesta a esta pregunta es el archivo HEAD (CABEZA)."
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-664
  hecho: HEAD es una referencia simbólica a la rama en la que estás.
  evidencia: "El archivo HEAD es una referencia simbólica a la rama donde te encuentras en cada momento."
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-665
  hecho: Una referencia simbólica contiene un enlace a otra referencia en lugar de un valor SHA-1.
  evidencia: "Por referencia simbólica nos referimos a que, a diferencia de una referencia normal, esta contiene un enlace a otra referencia en lugar de un valor SHA-1"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-666
  hecho: En el ejemplo, .git/HEAD contiene ref: refs/heads/master.
  evidencia: "$ cat .git/HEAD ref: refs/heads/master"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-667
  hecho: git checkout test cambia el contenido de HEAD a la rama test.
  evidencia: "Si lanzas el comando git checkout test, Git actualiza el contenido del archivo: $ cat .git/HEAD ref: refs/heads/test"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-668
  hecho: git commit crea una confirmación cuyo padre es el SHA-1 al que apunta HEAD en ese momento.
  evidencia: "se crea un nuevo objeto de confirmación de cambios teniendo como padre la confirmación con valor SHA-1 a la que en ese momento esté apuntando la referencia en HEAD"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-669
  hecho: El comando symbolic-ref es la alternativa más segura a editar HEAD a mano.
  evidencia: "en HEAD. Puedes editar manualmente este archivo, pero, también para esta tarea existe un comando más seguro: symbolic-ref."
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-670
  hecho: git symbolic-ref HEAD lee el valor de HEAD.
  evidencia: "Puedes leer el valor de HEAD a través de él: $ git symbolic-ref HEAD refs/heads/master"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-671
  hecho: git symbolic-ref HEAD refs/heads/test cambia el valor de HEAD.
  evidencia: "Y también puedes cambiar el valor de HEAD a través de él: $ git symbolic-ref HEAD refs/heads/test"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-672
  hecho: No se puede fijar una referencia simbólica fuera de refs.
  evidencia: "Pero no puedes fijar una referencia simbólica fuera de "refs""
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-673
  hecho: Hay tres tipos principales de objetos Git y un cuarto, el objeto tipo etiqueta.
  evidencia: "Acabamos de conocer los tres principales tipos de objetos Git, pero hay un cuarto. El objeto tipo etiqueta es muy parecido al tipo confirmación de cambios"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-674
  hecho: Un objeto etiqueta contiene un marcador, una fecha, un mensaje y un enlace.
  evidencia: "El objeto tipo etiqueta es muy parecido al tipo confirmación de cambios, --contiene un marcador, una fecha, un mensaje y un enlace--."
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-675
  hecho: Una etiqueta es como una referencia a una rama que permanece siempre inmóvil.
  evidencia: "El objeto tipo etiqueta es muy parecido al tipo confirmación de cambios, --contiene un marcador, una fecha, un mensaje y un enlace--. Su principal diferencia reside en que generalmente apunta a una confirmación de cambios (commit) en lugar de a un árbol (tree). Es como una referencia a una rama, pero permaneciendo siempre inmóvil"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-676
  hecho: Existen dos tipos de etiquetas: las anotativas y las ligeras.
  evidencia: "hay dos tipos de etiquetas: las anotativas y las ligeras"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-677
  hecho: Una etiqueta ligera es una referencia que nunca se mueve.
  evidencia: "Una etiqueta ligera es simplemente eso: una referencia que nunca se mueve."
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-678
  hecho: Se puede crear una etiqueta ligera con git update-ref sobre refs/tags.
  evidencia: "Puedes crear una etiqueta ligera lanzando un comando tal como: $ git update-ref refs/tags/v1.0 cac0cab538b970a37ea1e769cbbde608743bc96d"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-679
  hecho: Al crear una etiqueta anotada, Git crea un objeto etiqueta y escribe una referencia que apunta a él, no a la confirmación.
  evidencia: "Al crear una etiqueta anotativa, Git crea un objeto tipo etiqueta y luego escribe una referencia apuntando a él en lugar de apuntar directamente a una confirmación de cambios."
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-680
  hecho: La opción -a de git tag indica que la etiqueta es anotada.
  evidencia: "Puedes comprobarlo creando una: (la opción -a indica que la etiqueta es anotativa) $ git tag -a v1.1 1a410efbd13591db07496601ebc7a059dd55cfe9 -m 'test tag'"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-681
  hecho: En el ejemplo, el inicio del objeto apunta al SHA-1 de la confirmación de cambios recién etiquetada.
  evidencia: "Merece destacar que el inicio del objeto apunta al SHA-1 de la confirmación de cambios recién etiquetada."
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-682
  hecho: Se puede etiquetar cualquier tipo de objeto Git, no solo confirmaciones.
  evidencia: "Y también el que no ha sido necesario apuntar directamente a una confirmación de cambios; realmente puedes etiquetar cualquier tipo de objeto Git"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-683
  hecho: Las referencias a sitios remotos son un tercer tipo de referencia.
  evidencia: "El tercer tipo de referencia que puedes observar es la referencia a un sitio remoto."
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-684
  hecho: La rama master del remoto origin, en su último estado conocido, se consulta en refs/remotes/origin/master.
  evidencia: "puedes confirmar cual era la rama master en el remoto origin la última vez que comunicaste con el servidor, comprobando el archivo refs/remotes/origin/master"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-685
  hecho: Las referencias remotas se consideran de solo lectura, a diferencia de las ramas de refs/heads.
  evidencia: "Las referencias a sitios remotos son distintas de las ramas normales (referencias en refs/heads), principalmente porque se las considera de sólo lectura."
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-686
  hecho: Con git checkout a una referencia remota, Git no apunta HEAD a ella, así que commit nunca la actualiza.
  evidencia: "Las referencias a sitios remotos son distintas de las ramas normales (referencias en refs/heads), principalmente porque se las considera de sólo lectura. Puedes hacer git checkout a una, pero Git no apuntará HEAD a ella, de modo que nunca la actualizarás con el comando commit."
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-687
  hecho: Git usa las referencias remotas solo como marcadores del último estado conocido de cada rama en cada remoto.
  evidencia: "Las referencias a sitios remotos son distintas de las ramas normales (referencias en refs/heads), principalmente porque se las considera de sólo lectura. Puedes hacer git checkout a una, pero Git no apuntará HEAD a ella, de modo que nunca la actualizarás con el comando commit. Git las utiliza solamente como marcadores al último estado conocido de cada rama en cada servidor remoto declarado"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

## 1.7 reset sin miedo

- id: h01-701
  hecho: En su funcionamiento normal, Git maneja y manipula tres árboles.
  evidencia: "Git como sistema maneja y manipula tres árboles en su operación normal"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-702
  hecho: Aquí, «árbol» significa colección de archivos, no la estructura de datos en sentido estricto.
  evidencia: "Por “árbol”, aquí realmente queremos decir “colección de archivos”, no específicamente la estructura de datos."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-703
  hecho: El árbol HEAD guarda la última instantánea de commit, que será el padre del siguiente.
  evidencia: "HEAD Última instantánea del commit, próximo padre"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-704
  hecho: El árbol índice guarda la instantánea propuesta para el siguiente commit.
  evidencia: "Índice Siguiente instantánea del commit propuesta"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-705
  hecho: HEAD es un puntero a la referencia de la rama actual, y esa referencia apunta al último commit de la rama.
  evidencia: "HEAD es el puntero a la referencia de bifurcación actual, que es, a su vez, un puntero al último commit realizado en esa rama."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-706
  hecho: El índice es lo mismo que el área de preparación, porque es lo que Git ve al ejecutar git commit.
  evidencia: "El índice es tu siguiente commit propuesto. También nos hemos estado refiriendo a este concepto como el “Área de Preparación” de Git ya que esto es lo que Git ve cuando ejecutas git commit."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-707
  hecho: Técnicamente el índice no es un árbol: se implementa como un manifiesto aplanado.
  evidencia: "El índice no es técnicamente una estructura de árbol – en realidad se implementa como un manifiesto aplanado"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-708
  hecho: El directorio de trabajo descomprime el contenido de los otros dos árboles en archivos reales, que son mucho más fáciles de editar.
  evidencia: "Los otros dos árboles almacenan su contenido de manera eficiente pero inconveniente, dentro de la carpeta .git. El Directorio de trabajo los descomprime en archivos reales, lo que hace que sea mucho más fácil para ti editarlos."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-709
  hecho: El directorio de trabajo es una caja de arena donde se prueban cambios antes de pasarlos al área de preparación y al historial.
  evidencia: "Piensa en el Directorio de Trabajo como una caja de arena, donde puedes probar los cambios antes de enviarlos a tu área de ensayo (índice) y luego al historial."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-710
  hecho: git add copia contenido del directorio de trabajo al índice.
  evidencia: "usamos git add para tomar contenido en el directorio de trabajo y copiarlo en el índice."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-711
  hecho: git commit toma el contenido del índice y lo guarda como instantánea permanente.
  evidencia: "git commit, que toma los contenidos del índice y los guarda como una instantánea permanente"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-712
  hecho: git commit crea un objeto de commit que apunta a la instantánea y actualiza master para apuntar a ese commit.
  evidencia: "Luego ejecutamos git commit, que toma los contenidos del índice y los guarda como una instantánea permanente, crea un objeto de “commit” que apunta a esa instantánea y actualiza master para apuntar a ese “commit”."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-713
  hecho: Cuando los tres árboles son iguales, git status no muestra ningún cambio.
  evidencia: "Si ejecutamos git status, no veremos ningún cambio, porque los tres árboles son iguales."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-714
  hecho: Un archivo aparece como cambio sin preparar cuando su entrada difiere entre el índice y el directorio de trabajo.
  evidencia: "veremos el archivo en rojo como “Changes not staged for commit” porque esa entrada difiere entre el índice y el directorio de trabajo."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-715
  hecho: Un archivo aparece como cambio por confirmar cuando el índice y HEAD difieren.
  evidencia: "veremos el archivo en verde debajo de “Changes to be committed” porque el Índice y el HEAD difieren"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-716
  hecho: Al cambiar de rama, Git mueve HEAD a la nueva referencia, rellena el índice con esa instantánea y copia el índice al directorio de trabajo.
  evidencia: "Cuando verifica una rama, eso cambia HEAD para que apunte a la nueva “ref” de la rama, rellena su Índice con la instantánea de esa confirmación, luego copia los contenidos del Índice en tu Directorio de Trabajo."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-717
  hecho: reset hace hasta tres operaciones básicas sobre los tres árboles.
  evidencia: "Hablemos ahora sobre lo que reset hace exactamente cuando es llamado. Manipula directamente estos tres árboles de una manera simple y predecible. Hace hasta tres operaciones básicas."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-718
  hecho: El primer paso de reset es mover la rama a la que apunta HEAD, algo distinto de cambiar HEAD, que es lo que hace checkout.
  evidencia: "Lo primero que reset hará es mover a lo que HEAD apunta. Esto no es lo mismo que cambiar HEAD en sí mismo (que es lo que hace checkout), reset mueve la rama a la que HEAD apunta."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-719
  hecho: Estando en master, git reset 9e5e64a empieza haciendo que master apunte a 9e5e64a.
  evidencia: "ejecutar git reset 9e5e64a comenzará haciendo que master apunte a 9e5e64a."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-720
  hecho: Con reset --soft, el comando se detiene tras lo primero que siempre intenta hacer.
  evidencia: "esto es lo primero que siempre intentará hacer. Con reset --soft, simplemente se detendrá allí."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-721
  hecho: reset --soft esencialmente deshace el último comando git commit.
  evidencia: "Con reset --soft, simplemente se detendrá allí. Ahora tómate un segundo para mirar ese diagrama y darte cuenta de lo que sucedió: esencialmente deshizo el último comando git commit."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-722
  hecho: Al hacer reset de vuelta a HEAD~ (el padre de HEAD), la rama vuelve a donde estaba, sin cambiar el índice ni el directorio de trabajo.
  evidencia: "Cuando haces reset de vuelta a HEAD~ (el padre de HEAD), está volviendo a colocar la rama donde estaba, sin cambiar el Índice o el Directorio de Trabajo."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-723
  hecho: Tras volver con reset a HEAD~, se puede actualizar el índice y ejecutar git commit de nuevo para lograr lo que habría hecho git commit --amend.
  evidencia: "Cuando haces reset de vuelta a HEAD~ (el padre de HEAD), está volviendo a colocar la rama donde estaba, sin cambiar el Índice o el Directorio de Trabajo. Ahora puedes actualizar el Índice y ejecutar git commit nuevamente para lograr lo que git commit --amend hubiera hecho"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-724
  hecho: Lo siguiente que hace reset es actualizar el índice con el contenido de la instantánea a la que HEAD apunta ahora.
  evidencia: "Lo siguiente que reset hará es actualizar el Índice con los contenidos de cualquier instantánea que HEAD señale ahora."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-725
  hecho: Con --mixed, reset se detiene tras actualizar el índice.
  evidencia: "Lo siguiente que reset hará es actualizar el Índice con los contenidos de cualquier instantánea que HEAD señale ahora. Si especificas la opción --mixed, reset se detendrá en este punto."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-726
  hecho: --mixed es el comportamiento por defecto de reset.
  evidencia: "Si especificas la opción --mixed, reset se detendrá en este punto. Este también es el comportamiento por defecto, por lo que si no especificas ninguna opción (sólo git reset HEAD~, en este caso), aquí es donde el comando se detendrá."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-727
  hecho: En el ejemplo de git reset HEAD~ sin opciones, el comando deshizo el último commit y también hizo unstaged de todo.
  evidencia: "(sólo git reset HEAD~, en este caso), aquí es donde el comando se detendrá. Ahora tómate otro segundo para mirar ese diagrama y darte cuenta de lo que sucedió: deshizo tu último commit y también hizo unstaged de todo."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-728
  hecho: El tercer paso de reset es hacer que el directorio de trabajo se parezca al índice.
  evidencia: "Lo tercero que reset hará es hacer que el Directorio de Trabajo se parezca al Índice."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-729
  hecho: reset --hard deshace el último commit, los git add y git commit, y el trabajo hecho en el directorio de trabajo.
  evidencia: "Si usas la opción --hard, continuará en esta etapa. Entonces, pensemos en lo que acaba de pasar. Deshizo tu último commit, los comandos git add y git commit, y todo el trabajo que realizaste en tu Directorio de Trabajo."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-730
  hecho: --hard es la única forma de que reset sea peligroso, y uno de los pocos casos en que Git destruye datos.
  evidencia: "Es importante tener en cuenta que este indicador (--hard) es la única manera de hacer que el comando reset sea peligroso, y uno de los pocos casos en que Git realmente destruirá los datos."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-731
  hecho: Cualquier otra forma de reset se deshace con facilidad; --hard no, porque sobrescribe a la fuerza los archivos del directorio de trabajo.
  evidencia: "Cualquier otra invocación de reset puede deshacerse fácilmente, pero la opción --hard no puede, ya que sobrescribe forzosamente los archivos en el Directorio de Trabajo."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-732
  hecho: En el caso particular del ejemplo, la versión v3 del archivo sigue en un commit de la base de datos de Git y se podría recuperar mirando el reflog.
  evidencia: "En este caso particular, todavía tenemos la versión v3 de nuestro archivo en un “commit” en nuestro DB de Git, y podríamos recuperarla mirando nuestro reflog"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-733
  hecho: Si no se hubiera hecho commit al archivo, Git lo habría sobrescrito y sería irrecuperable.
  evidencia: "pero si no le hubiéramos hecho “commit”, Git hubiese sobrescrito el archivo y sería irrecuperable."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-734
  hecho: Con una ruta, reset omite el primer paso y limita el resto a esos archivos.
  evidencia: "Si especificas una ruta, reset omitirá el paso 1 y limitará el resto de sus acciones a un archivo o conjunto específico de archivos."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-735
  hecho: Que reset con ruta omita el paso 1 tiene sentido porque HEAD es solo un puntero y no puede apuntar a una parte de un commit y a otra de otro.
  evidencia: "reset omitirá el paso 1 y limitará el resto de sus acciones a un archivo o conjunto específico de archivos. Esto realmente tiene sentido – HEAD es solo un puntero, y no se puede apuntar a sólo una parte de un “commit” y otra parte de otro."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-736
  hecho: git reset file.txt equivale a git reset --mixed HEAD file.txt.
  evidencia: "Entonces, supongamos que ejecutamos git reset file.txt. Este formulario (ya que no especificó un commit SHA-1 o una rama, y no especificó --soft o --hard) es una abreviatura de git reset --mixed HEAD file.txt"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-737
  hecho: En ese caso, hacer que el índice se vea como HEAD básicamente solo copia archivo.txt de HEAD al índice.
  evidencia: "Haga que el Índice se vea como HEAD (deténgase aquí) Por lo tanto, básicamente solo copia archivo.txt de HEAD al Índice."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-738
  hecho: Copiar archivo.txt de HEAD al índice tiene el efecto práctico de hacer unstaging al archivo.
  evidencia: "Por lo tanto, básicamente solo copia archivo.txt de HEAD al Índice. Esto tiene el efecto práctico de hacer unstaging al archivo."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-739
  hecho: El diagrama del comando que hace unstaging al archivo y lo que hace git add son exactamente opuestos.
  evidencia: "Esto tiene el efecto práctico de hacer unstaging al archivo. Si miramos el diagrama para ese comando y pensamos en lo que hace git add, son exactamente opuestos."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-740
  hecho: Para extraer de un commit concreto la versión del archivo, en lugar de la de HEAD, bastaría ejecutar algo como git reset eb43bf file.txt.
  evidencia: "especificando un “commit” específico para extraer esa versión del archivo. Simplemente ejecutaríamos algo como git reset eb43bf file.txt."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-741
  hecho: Se puede ejecutar git reset --soft HEAD~2 para mover la rama HEAD a un commit anterior.
  evidencia: "Puedes ejecutar git reset --soft HEAD~2 para mover la rama HEAD a un “commit” anterior"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-742
  hecho: Después de git reset --soft HEAD~2 se ejecuta simplemente git commit de nuevo.
  evidencia: "Puedes ejecutar git reset --soft HEAD~2 para mover la rama HEAD a un “commit” anterior (el primer “commit” que deseas mantener): Y luego simplemente ejecuta git commit nuevamente:"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-743
  hecho: El commit con la versión v2 del archivo ya no está en el historial.
  evidencia: "El “commit” con la versión v2 del archivo ya no está en el historial."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-744
  hecho: git checkout [rama] se parece a git reset --hard [rama] porque actualiza los tres árboles.
  evidencia: "Ejecutar git checkout [branch] es bastante similar a ejecutar git reset --hard [branch] porque actualiza los tres árboles para que se vea como [branch]"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-745
  hecho: A diferencia de reset --hard, checkout protege el directorio de trabajo: comprueba que no pisa archivos con cambios.
  evidencia: "a diferencia de reset --hard, checkout está en el directorio-de-trabajo seguro; Verificará para asegurarse de que no está volando los archivos que tienen cambios en ellos."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-746
  hecho: reset --hard reemplaza todo sin comprobar nada.
  evidencia: "reset --hard, por otro lado, simplemente reemplazará todo en general sin verificar."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-747
  hecho: reset mueve la rama a la que apunta HEAD, mientras que checkout mueve el propio HEAD hacia otra rama.
  evidencia: "Donde reset moverá la rama a la que HEAD apunta, checkout moverá HEAD para señalar otra rama."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-748
  hecho: Estando en develop, git reset master hace que develop apunte al mismo commit que master.
  evidencia: "actualmente estamos en develop (así que HEAD la señala). Si ejecutamos git reset master, develop ahora apuntará al mismo “commit” que master."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-749
  hecho: Estando en develop, git checkout master no mueve develop: mueve HEAD.
  evidencia: "actualmente estamos en develop (así que HEAD la señala). Si ejecutamos git reset master, develop ahora apuntará al mismo “commit” que master. Si en cambio ejecutamos git checkout master, develop no se mueve, HEAD sí lo hace."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-750
  hecho: checkout con una ruta no mueve HEAD.
  evidencia: "La otra forma de ejecutar checkout es con una ruta de archivo, que como reset, no mueva HEAD."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-751
  hecho: checkout con ruta actualiza el índice con ese archivo y además sobrescribe el archivo del directorio de trabajo.
  evidencia: "La otra forma de ejecutar checkout es con una ruta de archivo, que como reset, no mueva HEAD. Es como git reset [branch] file en que actualiza el índice con ese archivo en ese “commit”, pero también sobrescribe el archivo en el Directorio de Trabajo."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-752
  hecho: Sería exactamente como git reset --hard [branch] file (si reset permitiera ejecutar eso): no está seguro para el directorio de trabajo y no mueve HEAD.
  evidencia: "Sería exactamente como git reset --hard [branch] file (si reset permitiera ejecutar eso) - no está directorio-de-trabajo seguro, y no mueve a HEAD."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-753
  hecho: En la tabla resumen, la columna HEAD indica REF si el comando mueve la rama a la que apunta HEAD y HEAD si mueve el propio HEAD.
  evidencia: "La columna “HEAD” dice “REF” si ese comando mueve la referencia (rama) a la que HEAD apunta, y “HEAD” si se mueve al propio HEAD."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-754
  hecho: Si en la columna WD Safe aparece NO, conviene pensarlo antes de ejecutar el comando.
  evidencia: "Presta especial atención a la columna WD Safe: si dice NO , tómate un segundo para pensar antes de ejecutar ese comando."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-755
  hecho: Según la tabla resumen, reset --soft [commit] tiene REF en HEAD, NO en Index, NO en Workdir y SI en WD Safe?.
  evidencia: "HEAD Index Workdir WD Safe? Nivel de Commit reset --soft [commit] REF NO NO SI"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-756
  hecho: Según la tabla resumen, reset [commit] tiene REF en HEAD, SI en Index, NO en Workdir y SI en WD Safe?.
  evidencia: "HEAD Index Workdir WD Safe? Nivel de Commit reset --soft [commit] REF NO NO SI reset [commit] REF SI NO SI"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-757
  hecho: Según la tabla resumen, reset --hard [commit] tiene REF en HEAD, SI en Index, SI en Workdir y NO en WD Safe?.
  evidencia: "HEAD Index Workdir WD Safe? Nivel de Commit reset --soft [commit] REF NO NO SI reset [commit] REF SI NO SI reset --hard [commit] REF SI SI NO"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-758
  hecho: Según la tabla resumen, checkout [commit] tiene HEAD en HEAD, SI en Index, SI en Workdir y SI en WD Safe?.
  evidencia: "HEAD Index Workdir WD Safe? Nivel de Commit reset --soft [commit] REF NO NO SI reset [commit] REF SI NO SI reset --hard [commit] REF SI SI NO checkout [commit] HEAD SI SI SI"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-759
  hecho: Según la tabla resumen, reset (commit) [archivo] tiene NO en HEAD, SI en Index, NO en Workdir y SI en WD Safe?.
  evidencia: "HEAD Index Workdir WD Safe? Nivel de Commit reset --soft [commit] REF NO NO SI reset [commit] REF SI NO SI reset --hard [commit] REF SI SI NO checkout [commit] HEAD SI SI SI Nivel de Archivo reset (commit) [file] NO SI NO SI"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-760
  hecho: Según la tabla resumen, checkout (commit) [archivo] tiene NO en HEAD, SI en Index, SI en Workdir y NO en WD Safe?.
  evidencia: "HEAD Index Workdir WD Safe? Nivel de Commit reset --soft [commit] REF NO NO SI reset [commit] REF SI NO SI reset --hard [commit] REF SI SI NO checkout [commit] HEAD SI SI SI Nivel de Archivo reset (commit) [file] NO SI NO SI checkout (commit) [file] NO SI SI NO"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-761
  hecho: En Git, el historial es un grafo acíclico dirigido de instantáneas.
  evidencia: "In Git, a history is a directed acyclic graph (DAG) of snapshots."
  fuente: f01-16
  ancla: https://missing.csail.mit.edu/2026/version-control/
  consultada: 2026-11-12

- id: h01-762
  hecho: Cada instantánea de Git se refiere a un conjunto de padres, las instantáneas que la precedieron.
  evidencia: "each snapshot in Git refers to a set of “parents”, the snapshots that preceded it."
  fuente: f01-16
  ancla: https://missing.csail.mit.edu/2026/version-control/
  consultada: 2026-11-12

- id: h01-763
  hecho: Los commits de Git son inmutables.
  evidencia: "Commits in Git are immutable."
  fuente: f01-16
  ancla: https://missing.csail.mit.edu/2026/version-control/
  consultada: 2026-11-12

- id: h01-764
  hecho: «Editar» el historial crea commits nuevos y actualiza las referencias para que apunten a ellos.
  evidencia: "“edits” to the commit history are actually creating entirely new commits, and references (see below) are updated to point to the new ones."
  fuente: f01-16
  ancla: https://missing.csail.mit.edu/2026/version-control/
  consultada: 2026-11-12

- id: h01-765
  hecho: Las referencias son punteros a commits.
  evidencia: "References are pointers to commits."
  fuente: f01-16
  ancla: https://missing.csail.mit.edu/2026/version-control/
  consultada: 2026-11-12

- id: h01-766
  hecho: A diferencia de los objetos, que son inmutables, las referencias son mutables y pueden apuntar a otro commit.
  evidencia: "Unlike objects, which are immutable, references are mutable (can be updated to point to a new commit)."
  fuente: f01-16
  ancla: https://missing.csail.mit.edu/2026/version-control/
  consultada: 2026-11-12

- id: h01-767
  hecho: HEAD es una referencia especial que indica dónde estamos en el historial.
  evidencia: "In Git, that “where we currently are” is a special reference called “HEAD”."
  fuente: f01-16
  ancla: https://missing.csail.mit.edu/2026/version-control/
  consultada: 2026-11-12

- id: h01-768
  hecho: Todos los comandos de Git equivalen a manipular el grafo de commits añadiendo objetos y añadiendo o actualizando referencias.
  evidencia: "All git commands map to some manipulation of the commit DAG by adding objects and adding/updating references."
  fuente: f01-16
  ancla: https://missing.csail.mit.edu/2026/version-control/
  consultada: 2026-11-12

- id: h01-769
  hecho: Para descartar los cambios sin confirmar y hacer que master apunte a un commit, Missing Semester propone git checkout master; git reset --hard.
  evidencia: "discard uncommitted changes and make the ‘master’ ref point to commit 5d83f9e”, there’s probably a command to do it (e.g. in this case, git checkout master; git reset --hard 5d83f9e)"
  fuente: f01-16
  ancla: https://missing.csail.mit.edu/2026/version-control/
  consultada: 2026-11-12

- id: h01-770
  hecho: El área de preparación permite elegir qué modificaciones entran en la siguiente instantánea.
  evidencia: "allowing you to specify which modifications should be included in the next snapshot through a mechanism called the “staging area”."
  fuente: f01-16
  ancla: https://missing.csail.mit.edu/2026/version-control/
  consultada: 2026-11-12

- id: h01-771
  hecho: Missing Semester resume git reset <file> como sacar un archivo del área de preparación.
  evidencia: "git reset <file>: unstage a file"
  fuente: f01-16
  ancla: https://missing.csail.mit.edu/2026/version-control/
  consultada: 2026-11-12

- id: h01-772
  hecho: Missing Semester resume git restore como descartar cambios.
  evidencia: "git restore: discard changes"
  fuente: f01-16
  ancla: https://missing.csail.mit.edu/2026/version-control/
  consultada: 2026-11-12

- id: h01-773
  hecho: Una serie de confirmaciones con mensajes como «oops.» o «WIP» se puede aplastar con reset en una sola confirmación.
  evidencia: "Supongamos que tienes una serie de confirmaciones con mensajes como “oops.”, “WIP” y “se olvidó de este archivo”. Puedes usar reset para aplastarlos rápida y fácilmente en una sola confirmación"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

## 1.7 reset sin miedo (fuentes añadidas)

- id: h01-774
  hecho: El reflog registra cuándo se actualizaron, en el repositorio local, las puntas de las ramas y de otras referencias.
  evidencia: "Reference logs, or "reflogs", record when the tips of branches and other references were updated in the local repository."
  fuente: f01-25
  ancla: https://git-scm.com/docs/git-reflog
  consultada: 2026-11-12

- id: h01-775
  hecho: Según la documentación, HEAD@{2} significa «dónde estaba HEAD hace dos movimientos».
  evidencia: "HEAD@{2} means "where HEAD used to be two moves ago""
  fuente: f01-25
  ancla: https://git-scm.com/docs/git-reflog
  consultada: 2026-11-12

- id: h01-776
  hecho: Según la documentación, master@{one.week.ago} significa dónde apuntaba master hace una semana en ese repositorio local.
  evidencia: "master@{one.week.ago} means "where master used to point to one week ago in this local repository""
  fuente: f01-25
  ancla: https://git-scm.com/docs/git-reflog
  consultada: 2026-11-12

- id: h01-777
  hecho: El subcomando «show» de git reflog es el predeterminado y muestra el log de la referencia indicada en la línea de comandos (o de HEAD, por defecto).
  evidencia: "The "show" subcommand (which is also the default, in the absence of any subcommands) shows the log of the reference provided in the command-line (or HEAD, by default)."
  fuente: f01-25
  ancla: https://git-scm.com/docs/git-reflog
  consultada: 2026-11-12

- id: h01-778
  hecho: El reflog cubre todas las acciones recientes y, además, el reflog de HEAD registra los cambios de rama.
  evidencia: "The reflog covers all recent actions, and in addition the HEAD reflog records branch switching."
  fuente: f01-25
  ancla: https://git-scm.com/docs/git-reflog
  consultada: 2026-11-12

- id: h01-779
  hecho: El subcomando «expire» elimina las entradas más antiguas del reflog.
  evidencia: "The "expire" subcommand prunes older reflog entries."
  fuente: f01-25
  ancla: https://git-scm.com/docs/git-reflog
  consultada: 2026-11-12

- id: h01-780
  hecho: Si no se indica --expire, el tiempo de caducidad sale de la configuración gc.reflogExpire, que por defecto es de 90 días.
  evidencia: "--expire=<time> Prune entries older than the specified time. If this option is not specified, the expiration time is taken from the configuration setting gc.reflogExpire, which in turn defaults to 90 days."
  fuente: f01-25
  ancla: https://git-scm.com/docs/git-reflog
  consultada: 2026-11-12

- id: h01-781
  hecho: Pro Git cita entre las causas habituales de perder una confirmación haber hecho un hard-reset de una rama, abandonando todas sus confirmaciones.
  evidencia: "o porque has reculado (hard-reset) una rama, abandonando todas sus confirmaciones de cambio, y luego te has dado cuenta que necesitabas alguna de ellas."
  fuente: f01-26
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Mantenimiento-y-recuperaci%c3%b3n-de-datos
  consultada: 2026-11-12

- id: h01-782
  hecho: En el ejemplo de Pro Git se pierden las dos últimas confirmaciones de cambios porque ninguna rama permite acceder a ellas.
  evidencia: "Vemos que se han perdido las dos últimas confirmaciones de cambios, --no tienes ninguna rama que te permita acceder a ellas--."
  fuente: f01-26
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Mantenimiento-y-recuperaci%c3%b3n-de-datos
  consultada: 2026-11-12

- id: h01-783
  hecho: Para recuperar una confirmación perdida hay que localizar su SHA-1 y luego añadir una rama que apunte hacia ella.
  evidencia: "Necesitas localizar el SHA-1 de la última confirmación de cambios y luego añadir una rama que apunte hacia ella."
  fuente: f01-26
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Mantenimiento-y-recuperaci%c3%b3n-de-datos
  consultada: 2026-11-12

- id: h01-784
  hecho: Pro Git presenta git reflog como el método que suele ser más rápido para localizar el SHA-1 de la confirmación perdida.
  evidencia: "El problema es cómo localizarla, --porque, ¿no te la sabrás de memoria, no?--. El método más rápido para conseguirlo suele ser utilizar una herramienta denominada git reflog."
  fuente: f01-26
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Mantenimiento-y-recuperaci%c3%b3n-de-datos
  consultada: 2026-11-12

- id: h01-785
  hecho: Git suele guardar un registro silencioso de dónde está HEAD en cada momento.
  evidencia: "Según trabajas, Git suele guardar un silencioso registro de donde está HEAD en cada momento."
  fuente: f01-26
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Mantenimiento-y-recuperaci%c3%b3n-de-datos
  consultada: 2026-11-12

- id: h01-786
  hecho: El reflog se actualiza cada vez que se confirman cambios o se cambia de rama.
  evidencia: "Cada vez que confirmas cambios o cambias de rama, el registro (reflog) es actualizado."
  fuente: f01-26
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Mantenimiento-y-recuperaci%c3%b3n-de-datos
  consultada: 2026-11-12

- id: h01-787
  hecho: Pro Git propone git log -g para ver con una salida de registro normal, más amigable, la información que muestra git reflog.
  evidencia: "Se pueden ver las dos confirmaciones de cambios que hemos activado, pero no hay mucha más información al respecto. Para ver la misma información de manera mucho más amigable, podemos utilizar el comando git log -g, que nos muestra una salida normal de registro"
  fuente: f01-26
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Mantenimiento-y-recuperaci%c3%b3n-de-datos
  consultada: 2026-11-12

- id: h01-788
  hecho: Una confirmación perdida se puede recuperar creando una nueva rama que apunte a ella.
  evidencia: "así que puedes recuperarla creando una nueva rama apuntando a ella."
  fuente: f01-26
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Mantenimiento-y-recuperaci%c3%b3n-de-datos
  consultada: 2026-11-12

- id: h01-789
  hecho: En el ejemplo, la rama recover-branch se crea en la confirmación perdida con git branch recover-branch ab1afef.
  evidencia: "Por ejemplo, puedes iniciar una rama llamada recover-branch con dicha confirmación de cambios (ab1afef): $ git branch recover-branch ab1afef"
  fuente: f01-26
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Mantenimiento-y-recuperaci%c3%b3n-de-datos
  consultada: 2026-11-12

- id: h01-790
  hecho: La información del reflog se guarda en la carpeta .git/logs/.
  evidencia: "La información de registro (reflog) se guarda en la carpeta .git/logs/"
  fuente: f01-26
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Mantenimiento-y-recuperaci%c3%b3n-de-datos
  consultada: 2026-11-12

- id: h01-791
  hecho: Cuando el reflog no sirve, una forma de recuperar confirmaciones es el comando de chequeo de integridad de la base de datos, git fsck.
  evidencia: "Una forma es utilizando el comando de chequeo de integridad de la base de datos: git fsck."
  fuente: f01-26
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Mantenimiento-y-recuperaci%c3%b3n-de-datos
  consultada: 2026-11-12

- id: h01-792
  hecho: git fsck con la opción --full muestra todos los objetos sin referencias a ningún otro objeto.
  evidencia: "Si lo lanzas con la opción --full, te mostrará todos los objetos sin referencias a ningún otro objeto"
  fuente: f01-26
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Mantenimiento-y-recuperaci%c3%b3n-de-datos
  consultada: 2026-11-12

- id: h01-793
  hecho: En la salida de git fsck --full, la confirmación perdida aparece tras el texto «dangling commit» y se recupera añadiendo una rama que apunte a su SHA-1.
  evidencia: "En este caso, puedes ver la confirmación de cambios perdida después del texto 'dangling commit'. Y la puedes recuperar del mismo modo, añadiendo una rama que apunte a esa clave SHA-1."
  fuente: f01-26
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Mantenimiento-y-recuperaci%c3%b3n-de-datos
  consultada: 2026-11-12

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

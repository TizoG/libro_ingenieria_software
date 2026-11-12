# Hechos del capítulo 1: Git por dentro

Hechos atómicos con evidencia literal (cortafuegos 2). Se generan juntando `secciones/1.X.md`; edita la sección y vuelve a juntar.
Ids por sección: la sección 1.k usa h01-k01 a h01-k99.

## 1.1 Qué es el control de versiones

- id: h01-101
  hecho: Un sistema de control de versiones registra los cambios hechos en un archivo o conjunto de archivos a lo largo del tiempo.
  evidencia: "Un control de versiones es un sistema que registra los cambios realizados en un archivo o conjunto de archivos a lo largo del tiempo"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-102
  hecho: El registro de cambios permite recuperar versiones concretas más adelante.
  evidencia: "de modo que puedas recuperar versiones específicas más adelante"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-103
  hecho: Un VCS permite volver a una versión anterior del proyecto completo, no solo de un archivo.
  evidencia: "regresar a una versión anterior del proyecto completo"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-104
  hecho: Con un VCS suele ser posible recuperar fácilmente archivos que se han estropeado o perdido.
  evidencia: "si arruinas o pierdes archivos, será posible recuperarlos fácilmente"
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
  hecho: Copiar archivos a mano como control de versiones es muy propenso a errores.
  evidencia: "pero también es tremendamente propenso a errores"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-107
  hecho: Un error típico de la copia manual es guardar en el archivo equivocado o sobrescribir archivos sin querer.
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
  hecho: RCS, un VCS local muy popular, guarda las diferencias entre archivos (parches) en un formato especial en disco.
  evidencia: "Esta herramienta funciona guardando conjuntos de parches (es decir, las diferencias entre archivos) en un formato especial en disco"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-110
  hecho: Los sistemas centralizados nacieron para colaborar con desarrolladores en otros sistemas.
  evidencia: "Los sistemas de Control de Versiones Centralizados (CVCS por sus siglas en inglés) fueron desarrollados para solucionar este problema."
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-111
  hecho: CVS, Subversion y Perforce son ejemplos de sistemas de control de versiones centralizados.
  evidencia: "Estos sistemas, como CVS, Subversion y Perforce, tienen un único servidor"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-112
  hecho: Un sistema centralizado tiene un único servidor con todos los archivos versionados y varios clientes que los descargan de ahí.
  evidencia: "tienen un único servidor que contiene todos los archivos versionados y varios clientes que descargan los archivos desde ese lugar central"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-113
  hecho: En un sistema centralizado, todas las personas saben hasta cierto punto en qué trabajan las demás.
  evidencia: "todas las personas saben hasta cierto punto en qué están trabajando los otros colaboradores del proyecto"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-114
  hecho: En un sistema centralizado, los administradores controlan al detalle qué puede hacer cada usuario.
  evidencia: "Los administradores tienen control detallado sobre qué puede hacer cada usuario"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-115
  hecho: Administrar un sistema centralizado es más fácil que gestionar bases de datos locales en cada cliente.
  evidencia: "es mucho más fácil administrar un CVCS que tener que lidiar con bases de datos locales en cada cliente"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-116
  hecho: La desventaja más obvia de un sistema centralizado es que el servidor es un punto único de fallo.
  evidencia: "La más obvia es el punto único de fallo que representa el servidor centralizado."
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-117
  hecho: Si el servidor centralizado se cae, nadie puede colaborar ni guardar cambios mientras dure la caída.
  evidencia: "Si ese servidor se cae durante una hora, entonces durante esa hora nadie podrá colaborar o guardar cambios en archivos en los que hayan estado trabajando."
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-118
  hecho: Si se corrompe el disco del servidor central y no hay copias de seguridad, se pierde la información del proyecto salvo las copias instantáneas que haya en máquinas locales.
  evidencia: "se perderá toda la información del proyecto, con excepción de las copias instantáneas que las personas tengan en sus máquinas locales"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-119
  hecho: Git, Mercurial, Bazaar y Darcs son ejemplos de sistemas de control de versiones distribuidos.
  evidencia: "En un DVCS (como Git, Mercurial, Bazaar o Darcs)"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-120
  hecho: En un sistema distribuido, los clientes replican completamente el repositorio, no solo descargan la última copia instantánea.
  evidencia: "los clientes no solo descargan la última copia instantánea de los archivos, sino que se replica completamente el repositorio"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-121
  hecho: En un sistema distribuido, cada clon es una copia completa de todos los datos.
  evidencia: "Cada clon es realmente una copia completa de todos los datos."
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-122
  hecho: Si el servidor de un sistema distribuido falla, cualquier repositorio de un cliente puede copiarse al servidor para restaurarlo.
  evidencia: "cualquiera de los repositorios disponibles en los clientes puede ser copiado al servidor con el fin de restaurarlo"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-123
  hecho: Muchos sistemas distribuidos permiten trabajar con varios repositorios remotos a la vez.
  evidencia: "muchos de estos sistemas se encargan de manejar numerosos repositorios remotos con los cuales pueden trabajar"
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-124
  hecho: Los sistemas distribuidos permiten flujos de trabajo imposibles en los centralizados, como los modelos jerárquicos.
  evidencia: "Esto permite establecer varios flujos de trabajo que no son posibles en sistemas centralizados, como pueden ser los modelos jerárquicos."
  fuente: f01-01
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones
  consultada: 2026-11-12

- id: h01-125
  hecho: Entre 1991 y 2002, el kernel de Linux gestionó sus cambios con parches y archivos.
  evidencia: "los cambios en el software se realizaban a través de parches y archivos"
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
  hecho: En 2005, BitKeeper dejó de ofrecerse gratis tras romperse la relación entre su compañía y la comunidad del kernel.
  evidencia: "En el 2005, la relación entre la comunidad que desarrollaba el kernel de Linux y la compañía que desarrollaba BitKeeper se vino abajo y la herramienta dejó de ser ofrecida de manera gratuita."
  fuente: f01-02
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Una-breve-historia-de-Git
  consultada: 2026-11-12

- id: h01-128
  hecho: Ese cambio impulsó a la comunidad de Linux, en particular a Linus Torvalds, a desarrollar su propia herramienta.
  evidencia: "Esto impulsó a la comunidad de desarrollo de Linux (y en particular a Linus Torvalds, el creador de Linux) a desarrollar su propia herramienta"
  fuente: f01-02
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Una-breve-historia-de-Git
  consultada: 2026-11-12

- id: h01-129
  hecho: Uno de los objetivos del nuevo sistema (Git) fue la velocidad.
  evidencia: "Algunos de los objetivos del nuevo sistema fueron los siguientes: Velocidad"
  fuente: f01-02
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Una-breve-historia-de-Git
  consultada: 2026-11-12

- id: h01-130
  hecho: Uno de los objetivos de Git era un gran soporte para el desarrollo no lineal, con miles de ramas paralelas.
  evidencia: "Gran soporte para desarrollo no lineal (miles de ramas paralelas)"
  fuente: f01-02
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Una-breve-historia-de-Git
  consultada: 2026-11-12

- id: h01-131
  hecho: Uno de los objetivos de Git era ser completamente distribuido.
  evidencia: "Completamente distribuido"
  fuente: f01-02
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Una-breve-historia-de-Git
  consultada: 2026-11-12

- id: h01-132
  hecho: Uno de los objetivos de Git era manejar grandes proyectos, como el kernel de Linux, con eficiencia en velocidad y tamaño de datos.
  evidencia: "Capaz de manejar grandes proyectos (como el kernel de Linux) eficientemente (velocidad y tamaño de los datos)"
  fuente: f01-02
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Una-breve-historia-de-Git
  consultada: 2026-11-12

- id: h01-133
  hecho: Otro de los objetivos de Git, en la misma lista, fue un diseño sencillo.
  evidencia: "Diseño sencillo"
  fuente: f01-02
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Una-breve-historia-de-Git
  consultada: 2026-11-12

## 1.2 Fotos, no diferencias; los tres estados

- id: h01-201
  hecho: La mayoría de los otros sistemas de control de versiones almacenan la información como una lista de cambios en los archivos.
  evidencia: "la mayoría de los otros sistemas almacenan la información como una lista de cambios en los archivos"
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
  hecho: Cada vez que confirmas, Git toma una foto del aspecto de todos los archivos en ese momento.
  evidencia: "toma una foto del aspecto de todos tus archivos en ese momento y guarda una referencia a esa copia instantánea"
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
  hecho: Con Git tienes toda la historia del proyecto en tu disco local.
  evidencia: "tienes toda la historia del proyecto ahí mismo, en tu disco local"
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-208
  hecho: Con Git puedes confirmar tus cambios sin conexión de red y subirlos más tarde.
  evidencia: "puedes confirmar tus cambios felizmente hasta que consigas una conexión de red para subirlos"
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
  evidencia: "Se trata de una cadena de 40 caracteres hexadecimales (0-9 y a-f)"
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-213
  hecho: El hash SHA-1 se calcula a partir de los contenidos del archivo o de la estructura del directorio.
  evidencia: "se calcula con base en los contenidos del archivo o estructura del directorio en Git"
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
  evidencia: "casi todas ellas sólo añaden información a la base de datos de Git"
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
  hecho: Un archivo confirmado tiene sus datos almacenados de forma segura en la base de datos local.
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
  evidencia: "es lo que se copia cuando clonas un repositorio desde otra computadora"
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
  evidencia: "Estos archivos se sacan de la base de datos comprimida en el directorio de Git, y se colocan en disco para que los puedas usar o modificar."
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
  hecho: El primer paso del flujo de trabajo básico es modificar archivos en el directorio de trabajo.
  evidencia: "Modificas una serie de archivos en tu directorio de trabajo."
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-228
  hecho: El segundo paso del flujo de trabajo básico es preparar los archivos añadiéndolos al área de preparación.
  evidencia: "Preparas los archivos, añadiéndolos a tu área de preparación."
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-229
  hecho: El tercer paso del flujo de trabajo básico es confirmar: toma los archivos tal como están en el área de preparación y guarda esa copia instantánea de forma permanente en el directorio de Git.
  evidencia: "Confirmas los cambios, lo que toma los archivos tal y como están en el área de preparación y almacena esa copia instantánea de manera permanente en tu directorio de Git."
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
  hecho: Un archivo que ha cambiado desde que se obtuvo del repositorio y ha sido añadido al área de preparación está preparado.
  evidencia: "Si ha sufrido cambios desde que se obtuvo del repositorio, pero ha sido añadida al área de preparación, está preparada (staged)."
  fuente: f01-03
  ancla: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git
  consultada: 2026-11-12

- id: h01-232
  hecho: Un archivo que ha cambiado desde que se obtuvo del repositorio y no se ha preparado está modificado.
  evidencia: "Y si ha sufrido cambios desde que se obtuvo del repositorio, pero no se ha preparado, está modificada (modified)."
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
  evidencia: "pueden ser archivos sin modificar, modificados o preparados"
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-235
  hecho: Los archivos sin rastrear son los del directorio de trabajo que no estaban en la última instantánea ni están en el área de preparación.
  evidencia: "cualquier otro archivo en tu directorio de trabajo que no estaba en tu última instantánea y que no está en el área de preparación (staging area)"
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
  evidencia: "Git no los incluirá en tu próximo commit a menos que se lo indiques explícitamente."
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
  hecho: Tras git add, un archivo nuevo queda rastreado y preparado para ser confirmado.
  evidencia: "verás que el archivo README está siendo rastreado y está preparado para ser confirmado"
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-244
  hecho: git add sirve para empezar a rastrear archivos nuevos, preparar archivos y marcar como resueltos los archivos en conflicto por combinación.
  evidencia: "lo usas para empezar a rastrear archivos nuevos, preparar archivos, y hacer otras cosas como marcar archivos en conflicto por combinación como resueltos"
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-245
  hecho: Un archivo puede aparecer a la vez como preparado y como no preparado si lo modificas después de git add.
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
  hecho: git status -s y git status --short muestran un estado abreviado.
  evidencia: "Si ejecutas git status -s o git status --short, obtendrás una salida mucho más simplificada."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-249
  hecho: En el estado abreviado, los archivos nuevos sin rastrear llevan ??, los preparados una A y los modificados una M.
  evidencia: "Los archivos nuevos que no están rastreados tienen un ?? a su lado, los archivos que están preparados tienen una A y los modificados una M."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-250
  hecho: En el estado abreviado hay dos columnas: la izquierda indica el estado preparado y la derecha el estado sin preparar.
  evidencia: "El estado aparece en dos columnas - la columna de la izquierda indica el estado preparado y la columna de la derecha indica el estado sin preparar."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-251
  hecho: Un archivo .gitignore lista patrones de archivos que Git debe ignorar.
  evidencia: "puedes crear un archivo llamado .gitignore que liste patrones a considerar"
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
  evidencia: "Emplear patrones glob estándar que se aplicarán recursivamente a todo el directorio del repositorio local."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-254
  hecho: Un patrón de .gitignore se niega añadiendo un signo de exclamación (!) al principio.
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
  hecho: git diff sin parámetros compara el directorio de trabajo con el área de preparación.
  evidencia: "Este comando compara lo que tienes en tu directorio de trabajo con lo que está en el área de preparación."
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
  evidencia: "Este comando compara tus cambios preparados con la última instantánea confirmada."
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
  evidencia: "--staged y --cached son sinónimos"
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
  evidencia: "debes eliminarlos de tus archivos rastreados (o mejor dicho, eliminarlos del área de preparación) y luego confirmar"
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-267
  hecho: git rm, además de quitar el archivo del seguimiento, lo elimina del directorio de trabajo.
  evidencia: "Para ello existe el comando git rm, que además elimina el archivo de tu directorio de trabajo"
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-268
  hecho: Si modificaste un archivo y ya lo habías añadido al índice, git rm exige forzar la eliminación con la opción -f.
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
  evidencia: "no se guardará ningún metadato que indique que renombraste el archivo"
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

- id: h01-271
  hecho: La única diferencia real entre git mv y hacer mv, git rm y git add es que git mv es un solo comando en vez de tres.
  evidencia: "La única diferencia real es que mv es un solo comando en vez de tres - existe por conveniencia."
  fuente: f01-04
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio
  consultada: 2026-11-12

## 1.3 Leer y deshacer el historial

- id: h01-301
  hecho: git log es la herramienta más básica y potente para mirar atrás y ver qué modificaciones se han hecho en un repositorio.
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
  evidencia: "este comando lista cada confirmación con su suma de comprobación SHA-1, el nombre y dirección de correo del autor, la fecha y el mensaje de confirmación."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-304
  hecho: La opción -p de git log muestra las diferencias introducidas en cada confirmación.
  evidencia: "Una de las opciones más útiles es -p, que muestra las diferencias introducidas en cada confirmación."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-305
  hecho: Ver las diferencias de cada confirmación con git log -p resulta útil para revisiones de código.
  evidencia: "Esto resulta muy útil para revisiones de código, o para visualizar rápidamente lo que ha pasado en las confirmaciones enviadas por un colaborador."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-306
  hecho: Con -<n>, siendo n un entero, git log muestra solo las últimas n confirmaciones.
  evidencia: "De hecho, puedes hacer -<n>, siendo n cualquier entero, para mostrar las últimas n confirmaciones."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-307
  hecho: Git pagina por defecto la salida de git log.
  evidencia: "ya que Git por defecto pagina su salida para que veas cada página del historial por separado."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-308
  hecho: La opción --stat de git log imprime tras cada confirmación una lista de los archivos modificados.
  evidencia: "la opción --stat imprime tras cada confirmación una lista de archivos modificados"
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-309
  hecho: Con --stat se indica, para cada archivo modificado, cuántas líneas se han añadido y eliminadas.
  evidencia: "cuántas líneas han sido añadidas y eliminadas para cada uno de ellos"
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-310
  hecho: La opción --pretty=oneline de git log imprime cada confirmación en una única línea.
  evidencia: "La opción oneline imprime cada confirmación en una única línea"
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-311
  hecho: Los estilos short, full y fuller de --pretty muestran un formato parecido al estándar, con menos o más información respectivamente.
  evidencia: "Otras opciones son short, full y fuller, que muestran la salida en un formato parecido, pero añadiendo menos o más información, respectivamente"
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-312
  hecho: La opción --pretty=format permite especificar un formato de salida propio.
  evidencia: "La opción más interesante es format, que te permite especificar tu propio formato."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-313
  hecho: Un formato especificado explícitamente con --pretty=format no cambiará en futuras actualizaciones de Git, lo que lo hace adecuado para que otro programa analice la salida.
  evidencia: "como especificas el formato explícitamente, sabes que no cambiará en futuras actualizaciones de Git"
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-314
  hecho: La opción --graph de git log añade un pequeño gráfico ASCII con el historial de ramificaciones y uniones.
  evidencia: "Ésta añade un pequeño gráfico ASCII mostrando tu historial de ramificaciones y uniones"
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
  evidencia: "mientras que el confirmador es quien lo aplicó."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-318
  hecho: Si envías un parche a un proyecto y un miembro lo aplica, tú figuras como autor y el miembro como confirmador.
  evidencia: "tú como autor, y el miembro del proyecto como confirmador"
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-319
  hecho: Las opciones --since y --until de git log limitan la salida por fecha.
  evidencia: "las opciones temporales como --since (desde) y --until (hasta) sí que resultan muy útiles."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-320
  hecho: git log --since=2.weeks lista las confirmaciones hechas durante las dos últimas semanas.
  evidencia: "Por ejemplo, este comando lista todas las confirmaciones hechas durante las dos últimas semanas:"
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-321
  hecho: La opción --author de git log filtra las confirmaciones por autor.
  evidencia: "La opción --author te permite filtrar por autor"
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-322
  hecho: La opción --grep de git log busca palabras clave entre los mensajes de confirmación.
  evidencia: "--grep te permite buscar palabras clave entre los mensajes de confirmación."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-323
  hecho: Para aplicar a la vez --author y --grep hay que añadir --all-match; sin ella se muestran las confirmaciones que cumplan cualquiera de los dos criterios.
  evidencia: "tienes que añadir --all-match, o el comando mostrará las confirmaciones que cumplan cualquiera de las dos"
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-324
  hecho: La opción -S de git log recibe una cadena y muestra solo las confirmaciones que cambiaron el código añadiendo o eliminando esa cadena.
  evidencia: "Otra opción útil es -S, la cual recibe una cadena y solo muestra las confirmaciones que cambiaron el código añadiendo o eliminando la cadena."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-325
  hecho: Indicar la ruta de un directorio o archivo limita la salida de git log a las confirmaciones que introdujeron un cambio en esos archivos.
  evidencia: "Si especificas la ruta de un directorio o archivo, puedes limitar la salida a aquellas confirmaciones que introdujeron un cambio en dichos archivos."
  fuente: f01-05
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Ver-el-Historial-de-Confirmaciones
  consultada: 2026-11-12

- id: h01-326
  hecho: En git log la ruta debe ser siempre la última opción y suele ir precedida de dos guiones (--) que la separan del resto de opciones.
  evidencia: "Ésta debe ser siempre la última opción, y suele ir precedida de dos guiones (--) para separar la ruta del resto de opciones."
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
  hecho: Deshacer es una de las pocas áreas en las que Git puede perder parte de tu trabajo si cometes un error.
  evidencia: "Esta es una de las pocas áreas en las que Git puede perder parte de tu trabajo si cometes un error."
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
  evidencia: "Si quieres rehacer la confirmación, puedes reconfirmar con la opción --amend:"
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-331
  hecho: git commit --amend utiliza el área de preparación para la confirmación.
  evidencia: "Este comando utiliza tu área de preparación para la confirmación."
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-332
  hecho: Si no hay cambios desde la última confirmación, git commit --amend solo cambia el mensaje de confirmación.
  evidencia: "entonces la instantánea lucirá exactamente igual y lo único que cambiarás será el mensaje de confirmación."
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-333
  hecho: git commit --amend lanza el editor de confirmación con el mensaje de la confirmación anterior ya incluido.
  evidencia: "Se lanzará el mismo editor de confirmación, pero verás que ya incluye el mensaje de tu confirmación anterior."
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-334
  hecho: Tras confirmar, preparar un archivo olvidado y ejecutar git commit --amend, queda una sola confirmación: la segunda reemplaza el resultado de la primera.
  evidencia: "Al final terminarás con una sola confirmación - la segunda confirmación reemplaza el resultado de la primera."
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-335
  hecho: git status indica cómo deshacer los cambios del área de preparación y del directorio de trabajo.
  evidencia: "el comando que usas para determinar el estado de esas dos áreas también te recuerda cómo deshacer los cambios en ellas."
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-336
  hecho: Bajo Changes to be committed, git status sugiere git reset HEAD <file>... para sacar un archivo del área de preparación.
  evidencia: "verás que dice que uses git reset HEAD <file>... para deshacer la preparación."
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-337
  hecho: Tras git reset HEAD CONTRIBUTING.md, el archivo queda modificado y no preparado.
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
  hecho: Al sacar un archivo del área de preparación con git reset HEAD, el archivo del directorio de trabajo no se toca, por lo que es relativamente seguro.
  evidencia: "el archivo que está en tu directorio de trabajo no se toca, por lo que es relativamente seguro."
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-340
  hecho: Tras descartar los cambios no preparados de un archivo, estos aparecen revertidos.
  evidencia: "Ahora puedes ver que los cambios se han revertido."
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
  evidencia: "Cualquier cambio que le hayas hecho a ese archivo desaparecerá - acabas de sobreescribirlo con otro archivo."
  fuente: f01-06
  ancla: https://git-scm.com/book/es/v2/Fundamentos-de-Git-Deshacer-Cosas
  consultada: 2026-11-12

- id: h01-343
  hecho: Pro Git recomienda no usar git checkout -- [archivo] salvo que estés absolutamente seguro de que ya no quieres el archivo.
  evidencia: "Nunca utilices este comando a menos que estés absolutamente seguro de que ya no quieres el archivo."
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

## 1.4 Las ramas son punteros

- id: h01-401
  hecho: Git guarda los datos como una serie de instantáneas, que son copias puntuales de los archivos completos.
  evidencia: "instantáneas (copias puntuales de los archivos completos, tal y como se encuentran en ese momento)"
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
  hecho: La confirmación lleva metadatos con el autor y el mensaje explicativo.
  evidencia: "Dicha instantánea contiene además unos metadatos con el autor y el mensaje explicativo"
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
  evidencia: "almacena una copia de cada uno en el repositorio (estas copias se denominan "blobs")"
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-406
  hecho: Al confirmar, Git calcula sumas de control de cada subdirectorio y las guarda como objetos árbol.
  evidencia: "Git realiza sumas de control de cada subdirectorio (en el ejemplo, solamente tenemos el directorio principal del proyecto), y las guarda como objetos árbol en el repositorio Git."
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
  hecho: Tras confirmar tres archivos por primera vez, el repositorio contiene cinco objetos.
  evidencia: "En este momento, el repositorio de Git contendrá cinco objetos"
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
  hecho: En cada confirmación, la rama actual avanza automáticamente.
  evidencia: "En cada confirmación de cambios que realicemos, la rama irá avanzando automáticamente."
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-412
  hecho: La rama master no es una rama especial.
  evidencia: "no es una rama especial"
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-413
  hecho: Master aparece en casi todos los repositorios porque es la que crea por defecto git init y casi nadie cambia el nombre.
  evidencia: "es la que crea por defecto el comando git init y la gente no se molesta en cambiarle el nombre"
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-414
  hecho: Crear una rama nueva solo crea un apuntador nuevo que se puede mover libremente.
  evidencia: "simplemente se crea un nuevo apuntador para que lo puedas mover libremente."
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-415
  hecho: git branch testing crea un apuntador nuevo a la misma confirmación en la que estás.
  evidencia: "Esto creará un nuevo apuntador apuntando a la misma confirmación donde estés actualmente."
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-416
  hecho: En Git, HEAD es el apuntador a la rama local en la que estás.
  evidencia: "En Git, es simplemente el apuntador a la rama local en la que tú estés en ese momento"
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
  evidencia: "Esto mueve el apuntador HEAD a la rama testing."
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-420
  hecho: Si confirmas estando en testing, esa rama avanza y master se queda donde estaba.
  evidencia: "la rama testing avanza, mientras que la rama master permanece en la confirmación donde estaba"
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-421
  hecho: Volver a master con git checkout mueve HEAD de nuevo a master.
  evidencia: "Mueve el apuntador HEAD de nuevo a la rama master"
  fuente: f01-07
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F
  consultada: 2026-11-12

- id: h01-422
  hecho: Ese mismo cambio de rama revierte los archivos del directorio de trabajo a la última instantánea confirmada en master.
  evidencia: "revierte los archivos de tu directorio de trabajo; dejándolos tal y como estaban en la última instantánea confirmada en dicha rama master"
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
  evidencia: "una rama Git es realmente un simple archivo que contiene los 40 caracteres de una suma de control SHA-1"
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
  hecho: En Git crear una rama es siempre instantáneo.
  evidencia: "mientras que en Git el proceso es siempre instantáneo"
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
  evidencia: "Esto es un atajo para: $ git branch iss53 $ git checkout iss53"
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
  hecho: Al activar una rama, Git añade, quita y modifica archivos para que la copia de trabajo sea como en la última confirmación de esa rama.
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
  hecho: En un avance rápido Git mueve el apuntador hacia adelante porque la confirmación a fusionar está directamente por delante de la actual.
  evidencia: "Git ha movido el apuntador hacia adelante, ya que la confirmación apuntada en la rama donde has fusionado estaba directamente arriba respecto a la confirmación actual."
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-435
  hecho: En el avance rápido no hay trabajo divergente que fusionar.
  evidencia: "ya que no hay ningún otro trabajo divergente a fusionar"
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-436
  hecho: El avance rápido ocurre cuando se fusiona una confirmación con otra accesible siguiendo el historial de la primera.
  evidencia: "cuando intentas fusionar una confirmación con otra confirmación accesible siguiendo directamente el historial de la primera; Git simplifica las cosas avanzando el puntero"
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-437
  hecho: Una rama ya fusionada puede borrarse con la opción -d de git branch.
  evidencia: "Esto lo puedes hacer con la opción -d del comando git branch"
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-438
  hecho: Lo hecho en una rama hotfix no aparece en otra rama iss53 hasta que se fusionan.
  evidencia: "todo el trabajo realizado en la rama hotfix no está en los archivos de la rama iss53"
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-439
  hecho: Se puede fusionar master sobre iss53 con git merge master para traer ese trabajo.
  evidencia: "puedes fusionar (merge) la rama master sobre la rama iss53 utilizando el comando git merge master"
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
  evidencia: "Git realizará una fusión a tres bandas"
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-442
  hecho: La fusión a tres bandas usa las instantáneas de los extremos de ambas ramas y el ancestro común.
  evidencia: "utilizando las dos instantáneas apuntadas por el extremo de cada una de las ramas y por el ancestro común a ambas"
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
  evidencia: "crea automáticamente una nueva confirmación de cambios (commit) que apunta a ella"
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-445
  hecho: La fusión confirmada se caracteriza por tener más de un padre.
  evidencia: "su particularidad es que tiene más de un padre."
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
  hecho: Hay conflicto cuando las dos ramas modifican de forma distinta una misma porción de un mismo archivo.
  evidencia: "Si hay modificaciones dispares en una misma porción de un mismo archivo en las dos ramas distintas que pretendes fusionar, Git no será capaz de fusionarlas directamente."
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-449
  hecho: Ante un conflicto, git merge informa de que la fusión automática ha fallado.
  evidencia: "Automatic merge failed; fix conflicts and then commit the result."
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-450
  hecho: Ante un conflicto, Git no crea la confirmación de fusión y hace una pausa esperando a que se resuelva.
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
  hecho: En el ejemplo, git status indica durante el conflicto que hay rutas sin fusionar.
  evidencia: "You have unmerged paths."
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
  hecho: Cuando todos los conflictos están resueltos pero la fusión no ha concluido, git status lo indica.
  evidencia: "All conflicts fixed but you are still merging."
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
  hecho: El mensaje por defecto de la confirmación de fusión empieza por Merge branch seguido del nombre de la rama.
  evidencia: "El mensaje de confirmación por defecto será algo parecido a: Merge branch 'iss53'"
  fuente: f01-08
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%c3%a1sicos-para-Ramificar-y-Fusionar
  consultada: 2026-11-12

- id: h01-462
  hecho: git branch sin parámetros lista las ramas del proyecto.
  evidencia: "Si lo lanzas sin parámetros, obtienes una lista de las ramas presentes en tu proyecto"
  fuente: f01-09
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Gesti%c3%b3n-de-Ramas
  consultada: 2026-11-12

- id: h01-463
  hecho: En esa lista, el asterisco marca la rama activa, a la que apunta HEAD.
  evidencia: "nos indica la rama activa en este momento (la rama a la que apunta HEAD)"
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
  hecho: Las ramas ya fusionadas que no llevan asterisco se pueden eliminar sin problemas.
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

## 1.5 Rebase y reescribir historia

- id: h01-501
  hecho: Git ofrece dos formas de integrar cambios de una rama en otra: la fusión (merge) y la reorganización (rebase).
  evidencia: "En Git tenemos dos formas de integrar cambios de una rama en otra: la fusión (merge) y la reorganización (rebase)."
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-502
  hecho: git merge hace una fusión a tres bandas entre las dos últimas instantáneas de cada rama y su ancestro común.
  evidencia: "Realiza una fusión a tres bandas entre las dos últimas instantáneas de cada rama (C3 y C4) y el ancestro común a ambas (C2)"
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
  hecho: Lo primero que hace rebase es ir al ancestro común de la rama actual y la rama sobre la que se reorganiza.
  evidencia: "Haciendo que Git vaya al ancestro común de ambas ramas (donde estás actualmente y de donde quieres reorganizar)"
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-505
  hecho: Después saca las diferencias que introduce cada confirmación de la rama actual.
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
  hecho: Tras el rebase, se puede volver a la rama principal y hacer una fusión con avance rápido (fast-forward).
  evidencia: "En este momento, puedes volver a la rama master y hacer una fusión con avance rápido (fast-forward merge)."
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-510
  hecho: La instantánea final es la misma tanto si se llega por rebase como por merge; solo cambia el historial.
  evidencia: "es exactamente la misma instantánea; lo único diferente es el historial"
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
  hecho: Rebase se usa para asegurarse de que las confirmaciones propias se aplican limpiamente sobre una rama remota.
  evidencia: "Habitualmente, optarás por esta vía cuando quieras estar seguro de que tus confirmaciones de cambio (commits) se pueden aplicar limpiamente sobre una rama remota"
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-513
  hecho: Con el trabajo reorganizado, quien mantiene el proyecto no necesita integrarlo: le basta un avance rápido o una incorporación limpia.
  evidencia: "la persona que mantiene el proyecto no necesitará hacer ninguna integración con tu trabajo; le bastará con un avance rápido o una incorporación limpia."
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
  hecho: La opción --onto de git rebase permite reaplicar sobre la rama principal los cambios de una rama que no están en otra rama puntual.
  evidencia: "Puedes coger los cambios del cliente que no están en server (C8 y C9) y reaplicarlos sobre tu rama principal usando la opción --onto del comando git rebase"
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-517
  hecho: git rebase --onto master server client toma los cambios desde el ancestro común entre client y server y los aplica en master.
  evidencia: "Activa la rama client, averigua los cambios desde el ancestro común entre las ramas client y server, y aplicalos en la rama master"
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
  evidencia: "tus colaboradores tendrán que refusionar (re-merge) su trabajo y todo se volverá tremendamente complicado cuando intentes recoger (pull) su trabajo de vuelta sobre el tuyo."
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-522
  hecho: En el ejemplo de Pro Git, quien reorganiza sobrescribe el historial del servidor con git push --force.
  evidencia: "haciendo un git push --force para sobrescribir el registro en el servidor"
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-523
  hecho: Si el otro colaborador sobrescribió el historial y tú haces git pull, se crea una fusión confirmada que incluye ambas líneas del historial.
  evidencia: "Si haces git pull crearás una fusión confirmada, la cual incluirá ambas líneas del historial"
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-524
  hecho: En ese historial git log muestra dos confirmaciones con el mismo autor, fecha y mensaje, lo que confunde.
  evidencia: "verás dos confirmaciones hechas por el mismo autor y con la misma fecha y mensaje, lo cual será confuso."
  fuente: f01-10
  ancla: https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Reorganizar-el-Trabajo-Realizado
  consultada: 2026-11-12

- id: h01-525
  hecho: Git calcula una suma de control basada en el parche que introduce cada confirmación, llamada patch-id.
  evidencia: "Git calcula una suma de control basada en el parche que introduce una confirmación"
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
  hecho: git pull --rebase sustituye al git pull tradicional para reorganizar en vez de fusionar.
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
  hecho: Si reorganizar un historial público es inevitable, Pro Git recomienda que todos sepan que deben ejecutar git pull --rebase.
  evidencia: "asegúrense que todos sepan que deben ejecutar git pull --rebase para intentar aliviar en lo posible la frustración."
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
  hecho: Desde esa visión, cambiar el historial equivale a mentir sobre lo que ocurrió.
  evidencia: "Desde este punto de vista, cambiar el historial de confirmaciones es casi como blasfemar; estarías mintiendo sobre lo que en verdad ocurrió."
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
  hecho: Desde la segunda visión, rebase y filter-branch sirven para contar la historia de la mejor manera a los futuros lectores.
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
  evidencia: "Esto te envía al editor de texto, el cual tiene tu confirmación final, listo para modificarse en el mensaje."
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-538
  hecho: Para cambiar la instantánea de la última confirmación, se editan los archivos, se usa git add o git rm y se ejecuta git commit --amend.
  evidencia: "el subsecuente git commit --amend toma tu área de trabajo actual y la vuelve una instantánea para la nueva confirmación"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-539
  hecho: git commit --amend puede modificar el SHA-1 de la confirmación.
  evidencia: "puedes modificar los cambios del SHA-1 de la confirmación"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-540
  hecho: Para modificar confirmaciones más antiguas se usa rebase, porque Git no tiene una herramienta propia para modificar la historia.
  evidencia: "Git no tiene una herramienta para modificar la historia, pero puedes usar la herramienta de rebase"
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
  evidencia: "cualquier confirmación incluida en el rango de HEAD~3..HEAD será reescrita, aún si cambias el mensaje o no."
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-544
  hecho: Pro Git advierte de no incluir en el rebase interactivo confirmaciones ya enviadas al servidor central.
  evidencia: "No incluyas cualquier confirmación que ya hayas enviado al servidor central"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-545
  hecho: Hacerlo confunde a otros desarrolladores porque les da una versión alternativa del mismo cambio.
  evidencia: "esto confundirá a los demás desarrolladores proporcionando una versión alternativa del mismo cambio"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-546
  hecho: La lista del rebase interactivo muestra las confirmaciones en orden contrario al de git log.
  evidencia: "Es importante el notar que estas confirmaciones son escuchadas en el orden contrario del que tú normalmente las verías usando el comando de log."
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-547
  hecho: El script del rebase interactivo reproduce los cambios de cada confirmación de arriba a abajo.
  evidencia: "reproducirá los cambios introducidos en cada una de estas confirmaciones de arriba a abajo"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-548
  hecho: Acción pick: usar la confirmación tal cual.
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
  hecho: Acción fixup: descarta el mensaje de la confirmación.
  evidencia: "but discard this commit's log message"
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
  evidencia: "Git se parará, permitiéndote modificar la confirmación y continuar cuando hayas terminado"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-558
  hecho: Git indica git rebase --continue como orden para seguir tras modificar la confirmación.
  evidencia: "git rebase --continue"
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
  hecho: Para dividir una confirmación, la línea de esa confirmación en el script de rebase -i lleva la acción edit.
  evidencia: "edit 310154e updated README formatting and added blame"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-563
  hecho: Al pararse en ella, se hace un reseteo mixto con git reset HEAD^.
  evidencia: "puedes hacer un reseteo mixto de esa confirmación con el git reset HEAD^"
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
  hecho: Dividir una confirmación cambia el SHA-1 de todas las confirmaciones de la lista.
  evidencia: "esto cambia el SHA-1s de todas tus confirmaciones en tu lista"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-566
  hecho: filter-branch sirve para reescribir muchas confirmaciones de forma programable.
  evidencia: "Existe otra opción en la parte de volver a escribir la historia que puedes usar si necesitas reescribir un gran número de confirmaciones de una manera que se puedan scriptear"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-567
  hecho: Advertencia sobre filter-branch: probablemente no usarlo salvo que el proyecto no sea público y nadie se haya basado en las confirmaciones.
  evidencia: "probablemente no lo deberías usar a menos que tu proyecto aún no sea público y otra persona no se haya basado en las confirmaciones que estás a punto de reescribir"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-568
  hecho: Con --tree-filter, filter-branch ejecuta un comando tras cada revisión del proyecto y vuelve a confirmar el resultado.
  evidencia: "El --tree-filter inicia el comando específico después de cada revisión del proyecto y éste entonces vuelve a confirmar los resultados."
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-569
  hecho: Pro Git propone filter-branch con --tree-filter para quitar un archivo llamado passwords.txt de todo el historial.
  evidencia: "git filter-branch --tree-filter 'rm -f passwords.txt' HEAD"
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
  hecho: Un cambio de e-mail con filter-branch cambia el SHA-1 de todas las confirmaciones de la historia, no solo las que coinciden.
  evidencia: "este comando cambia cada confirmación del SHA-1 en tu historia, no solamente aquellos en los cuales el e-mail es el mismo o encaja"
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
  consultada: 2026-11-12

- id: h01-572
  hecho: Pro Git aconseja probar filter-branch en una rama de prueba y hacer hard-reset de la rama principal solo si el resultado es el deseado.
  evidencia: "Es generalmente una buena idea hacer esto en una parte de prueba de la rama y hacer un hard-reset de tu rama principal después de haber determinado que el resultado es lo que realmente deseas."
  fuente: f01-11
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reescribiendo-la-Historia
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
  hecho: Los comandos de bajo nivel se llaman comandos de fontanería y los más amigables, comandos de porcelana.
  evidencia: "Estos comandos son conocidos como los "comandos de fontanería", mientras que los comandos más amigables son conocidos como los "comandos de porcelana"."
  fuente: f01-14
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Fontaner%c3%ada-y-porcelana
  consultada: 2026-11-12

- id: h01-604
  hecho: Muchos comandos de fontanería no se piensan para uso manual, sino como bloques de construcción de herramientas y scripts propios.
  evidencia: "Muchos de estos comando no están pensados para ser utilizados manualmente desde la línea de comandos; sino más bien para ser utilizados como bloques de construcción para nuevas herramientas y scripts de usuario personalizados."
  fuente: f01-14
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Fontaner%c3%ada-y-porcelana
  consultada: 2026-11-12

- id: h01-605
  hecho: git init crea la carpeta .git, donde se ubica prácticamente todo lo que Git almacena y manipula.
  evidencia: "Git crea la carpeta auxiliar .git; la carpeta donde se ubica prácticamente todo lo almacenado y manipulado por Git"
  fuente: f01-14
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Fontaner%c3%ada-y-porcelana
  consultada: 2026-11-12

- id: h01-606
  hecho: Copiar la carpeta .git a otro lugar basta para tener una copia completa del repositorio.
  evidencia: "con tan solo copiar esta carpeta a cualquier otro lugar ya tienes tu copia completa"
  fuente: f01-14
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Fontaner%c3%ada-y-porcelana
  consultada: 2026-11-12

- id: h01-607
  hecho: Un repositorio recién creado con git init contiene HEAD, config, description, hooks, info, objects y refs.
  evidencia: "HEAD config* description hooks/ info/ objects/ refs/"
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
  hecho: Las cuatro entradas importantes de .git son los archivos HEAD e index y las carpetas objects y refs.
  evidencia: "Esto nos deja con cuatro entradas importantes: los archivos HEAD e index (todavía por ser creado), y las carpetas objects y refs."
  fuente: f01-14
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Fontaner%c3%ada-y-porcelana
  consultada: 2026-11-12

- id: h01-611
  hecho: La carpeta objects guarda el contenido de la base de datos de Git.
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
  evidencia: "Cuando insertas cualquier tipo de contenido, él te devuelve una clave que puedes utilizar para recuperar de nuevo dicho contenido en cualquier momento."
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-617
  hecho: hash-object es un comando de fontanería que guarda datos en .git y devuelve la clave con la que se han guardado.
  evidencia: "Este comando coge ciertos datos, los guarda en la carpeta .git. y te devuelve la clave bajo la cual se han guardado."
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
  evidencia: "La salida del comando es una suma de comprobación (checksum hash) de 40 caracteres."
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
  evidencia: "como un archivo por cada pieza de contenido, nombrado con la suma de comprobación SHA-1 del contenido y su cabecera"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-622
  hecho: La subcarpeta de objects se nombra con los 2 primeros caracteres del SHA-1 y el archivo con los 38 restantes.
  evidencia: "La subcarpeta se nombra con los primeros 2 caracteres del SHA-1, y el archivo con los restantes 38 caracteres."
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-623
  hecho: cat-file sirve para inspeccionar objetos Git.
  evidencia: "Este comando es algo así como una "navaja suiza" para inspeccionar objetos Git."
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
  evidencia: "Con la orden cat-file -t puedes comprobar el tipo de cualquier objeto almacenado en Git"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-626
  hecho: Un objeto guardado con hash-object no incluye el nombre del archivo, solo su contenido.
  evidencia: "realmente no estás guardando el nombre de tu archivo en el sistema, --solo su contenido--."
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-627
  hecho: Ese tipo de objeto, que guarda solo contenido, se llama blob (binary large object).
  evidencia: "Este tipo de objeto se denomina un blob (binary large object)."
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
  evidencia: "correspondiendo los árboles a las entradas de carpetas; y correspondiendo los binarios, mas o menos, a los contenidos de los archivos (inodes)"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-630
  hecho: Cada entrada de un árbol tiene un puntero SHA-1 a un blob o a un subárbol, más el modo, el tipo y el nombre de archivo.
  evidencia: "cada una de las cuales consta de un puntero SHA-1 a un objeto binario (blob) o a un subárbol, más sus correspondientes datos de modo, tipo y nombre de archivo"
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
  hecho: Una carpeta dentro de un árbol no es un blob, sino un puntero a otro árbol.
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
  hecho: El comando de fontanería write-tree escribe el área de preparación en un objeto árbol.
  evidencia: "Tras esto, puedes usar el comando write-tree para escribir el área de preparación a un objeto tipo árbol."
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-635
  hecho: El modo 100644 denota un archivo normal en una entrada de árbol.
  evidencia: "En este caso, indicas un modo 100644, el modo que denota un archivo normal."
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-636
  hecho: El modo 100755 denota un archivo ejecutable y el 120000 un enlace simbólico.
  evidencia: "Otras opciones son 100755, para un archivo ejecutable; o 120000, para un enlace simbólico."
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-637
  hecho: El comando commit-tree crea una confirmación a partir de un árbol y de las confirmaciones que la preceden, si las hay.
  evidencia: "Para crearlos, tan solo has de llamar al comando commit-tree, indicando uno de los árboles SHA-1 y los objetos de confirmación de cambios que lo preceden (si es que lo precede alguno)"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-638
  hecho: Un objeto de confirmación contiene el árbol que representa el estado del proyecto en ese momento.
  evidencia: "el objeto tipo árbol para la situación del proyecto en ese momento puntual"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-639
  hecho: Un objeto de confirmación contiene la información del autor y del confirmador, que usa user.name, user.email y una marca de tiempo.
  evidencia: "la información sobre el autor/confirmador (que usa tus opciones de configuración user.name y user.email y una marca de tiempo)"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-640
  hecho: Un objeto de confirmación termina con una línea en blanco y el mensaje.
  evidencia: "una línea en blanco; y el mensaje de la confirmación de cambios"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-641
  hecho: En el ejemplo, cada confirmación se relaciona con la inmediatamente anterior.
  evidencia: "relacionando cada uno de ellos con su inmediato anterior"
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
  evidencia: "guardar objetos binarios (blobs) para los archivos modificados, actualizar el índice, escribir árboles (trees), escribir objetos de confirmación de cambios (commits) que los referencian y relacionar cada uno de ellos con su inmediato precedente"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-644
  hecho: Blobs, árboles y confirmaciones se guardan como archivos separados en .git/objects.
  evidencia: "se guardan como archivos separados en la carpeta .git/objects"
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
  evidencia: "Después añade un espacio, seguido del tamaño del contenido y termina con un byte nulo"
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
  hecho: Git comprime el contenido con zlib antes de escribirlo.
  evidencia: "Git comprime todo el contenido con zlib"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-649
  hecho: Los demás objetos se almacenan igual, pero su cabecera empieza por otro tipo.
  evidencia: "Todos los demas objetos Git se almacenan de forma similar, pero con la diferencia de que sus cabeceras comienzan con un tipo diferente"
  fuente: f01-12
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git
  consultada: 2026-11-12

- id: h01-650
  hecho: Las cabeceras de los demás objetos empiezan por commit o por tree en lugar de blob.
  evidencia: "en lugar de blob (objeto binario grande), comenzarán por commit (confirmación de cambios), o por tree (árbol)"
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
  evidencia: "en la carpeta .git/refs puedes encontrar esos archivos con valores SHA-1 y nombres"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-653
  hecho: Una referencia permite usar un nombre simple en lugar de la suma SHA-1.
  evidencia: "sus respectivos nombres simples que puedas utilizar como enlaces en lugar de la propia suma de comprobación"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-654
  hecho: En el repositorio de ejemplo, .git/refs contiene las subcarpetas heads y tags.
  evidencia: ".git/refs/heads .git/refs/tags"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-655
  hecho: Técnicamente, una referencia se crea escribiendo un SHA-1 en un archivo de .git/refs/heads.
  evidencia: "$ echo "1a410efbd13591db07496601ebc7a059dd55cfe9" > .git/refs/heads/master"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-656
  hecho: Una vez creada una referencia, se puede usar en lugar del SHA-1 en todos los comandos.
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
  hecho: El comando update-ref es la forma más segura de actualizar una referencia.
  evidencia: "Si necesitas actualizar una referencia, puedes utilizar el comando update-ref"
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
  evidencia: "$ git update-ref refs/heads/test cac0ca"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-661
  hecho: Esa rama contiene solo el trabajo desde la confirmación a la que apunta hacia atrás.
  evidencia: "Y la rama contendrá únicamente trabajo desde esa confirmación de cambios hacia atrás."
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-662
  hecho: Al crear una rama con git branch, Git le asigna el SHA-1 de la última confirmación de la rama actual.
  evidencia: "lo que hace Git es añadir, a cualquier nueva referencia que vayas a crear, el valor SHA-1 de la última confirmación de cambios en esa rama"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-663
  hecho: Git sabe cuál es la última confirmación gracias al archivo HEAD.
  evidencia: "La respuesta a esta pregunta es el archivo HEAD (CABEZA)."
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
  evidencia: "a diferencia de una referencia normal, esta contiene un enlace a otra referencia en lugar de un valor SHA-1"
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
  evidencia: "Si lanzas el comando git checkout test, Git actualiza el contenido del archivo"
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
  evidencia: "Puedes editar manualmente este archivo, pero, también para esta tarea existe un comando más seguro: symbolic-ref."
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-670
  hecho: git symbolic-ref HEAD lee el valor de HEAD.
  evidencia: "Puedes leer el valor de HEAD a través de él"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-671
  hecho: git symbolic-ref HEAD refs/heads/test cambia el valor de HEAD.
  evidencia: "$ git symbolic-ref HEAD refs/heads/test"
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
  hecho: Además de blob, árbol y confirmación, hay un cuarto tipo de objeto: la etiqueta.
  evidencia: "Acabamos de conocer los tres principales tipos de objetos Git, pero hay un cuarto."
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
  evidencia: "Es como una referencia a una rama, pero permaneciendo siempre inmóvil"
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
  evidencia: "$ git update-ref refs/tags/v1.0 cac0cab538b970a37ea1e769cbbde608743bc96d"
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
  evidencia: "la opción -a indica que la etiqueta es anotativa"
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-681
  hecho: El objeto etiqueta empieza apuntando al SHA-1 de la confirmación etiquetada.
  evidencia: "Merece destacar que el inicio del objeto apunta al SHA-1 de la confirmación de cambios recién etiquetada."
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-682
  hecho: Se puede etiquetar cualquier tipo de objeto Git, no solo confirmaciones.
  evidencia: "realmente puedes etiquetar cualquier tipo de objeto Git"
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
  evidencia: "Puedes hacer git checkout a una, pero Git no apuntará HEAD a ella, de modo que nunca la actualizarás con el comando commit."
  fuente: f01-13
  ancla: https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Referencias-Git
  consultada: 2026-11-12

- id: h01-687
  hecho: Git usa las referencias remotas solo como marcadores del último estado conocido de cada rama en cada remoto.
  evidencia: "Git las utiliza solamente como marcadores al último estado conocido de cada rama en cada servidor remoto declarado"
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
  evidencia: "Última instantánea del commit, próximo padre"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-704
  hecho: El árbol índice guarda la instantánea propuesta para el siguiente commit.
  evidencia: "Siguiente instantánea del commit propuesta"
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
  evidencia: "También nos hemos estado refiriendo a este concepto como el “Área de Preparación” de Git ya que esto es lo que Git ve cuando ejecutas git commit."
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
  hecho: El directorio de trabajo descomprime ese contenido en archivos reales, que son más fáciles de editar.
  evidencia: "El Directorio de trabajo los descomprime en archivos reales, lo que hace que sea mucho más fácil para ti editarlos."
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
  hecho: git commit también actualiza la rama para que apunte al nuevo commit.
  evidencia: "actualiza master para apuntar a ese “commit”."
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
  evidencia: "debajo de “Changes to be committed” porque el Índice y el HEAD difieren"
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
  evidencia: "Hace hasta tres operaciones básicas."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-718
  hecho: El primer paso de reset es mover la rama a la que apunta HEAD, algo distinto de cambiar HEAD, que es lo que hace checkout.
  evidencia: "Esto no es lo mismo que cambiar HEAD en sí mismo (que es lo que hace checkout), reset mueve la rama a la que HEAD apunta."
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
  hecho: Con --soft, reset se detiene tras mover la rama.
  evidencia: "Con reset --soft, simplemente se detendrá allí."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-721
  hecho: reset --soft deshace el último git commit.
  evidencia: "esencialmente deshizo el último comando git commit."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-722
  hecho: Un reset a HEAD~ devuelve la rama a su posición anterior sin cambiar el índice ni el directorio de trabajo.
  evidencia: "Cuando haces reset de vuelta a HEAD~ (el padre de HEAD), está volviendo a colocar la rama donde estaba, sin cambiar el Índice o el Directorio de Trabajo."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-723
  hecho: Tras un reset --soft se puede actualizar el índice y volver a hacer commit para lograr lo mismo que git commit --amend.
  evidencia: "Ahora puedes actualizar el Índice y ejecutar git commit nuevamente para lograr lo que git commit --amend hubiera hecho"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-724
  hecho: El segundo paso de reset es actualizar el índice con el contenido de la instantánea a la que apunta HEAD.
  evidencia: "Lo siguiente que reset hará es actualizar el Índice con los contenidos de cualquier instantánea que HEAD señale ahora."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-725
  hecho: Con --mixed, reset se detiene tras actualizar el índice.
  evidencia: "Si especificas la opción --mixed, reset se detendrá en este punto."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-726
  hecho: --mixed es el comportamiento por defecto de reset.
  evidencia: "Este también es el comportamiento por defecto, por lo que si no especificas ninguna opción (sólo git reset HEAD~, en este caso), aquí es donde el comando se detendrá."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-727
  hecho: Un reset mixto deshace el último commit y además saca todo del área de preparación.
  evidencia: "deshizo tu último commit y también hizo unstaged de todo."
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
  evidencia: "Deshizo tu último commit, los comandos git add y git commit, y todo el trabajo que realizaste en tu Directorio de Trabajo."
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
  hecho: Lo que se había confirmado antes de un reset --hard se puede recuperar mirando el reflog.
  evidencia: "todavía tenemos la versión v3 de nuestro archivo en un “commit” en nuestro DB de Git, y podríamos recuperarla mirando nuestro reflog"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-733
  hecho: Lo que no se había confirmado, Git lo sobrescribe en un reset --hard y es irrecuperable.
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
  hecho: Con una ruta no se mueve HEAD porque es un puntero y no puede apuntar a parte de un commit y parte de otro.
  evidencia: "HEAD es solo un puntero, y no se puede apuntar a sólo una parte de un “commit” y otra parte de otro."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-736
  hecho: git reset file.txt equivale a git reset --mixed HEAD file.txt.
  evidencia: "es una abreviatura de git reset --mixed HEAD file.txt"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-737
  hecho: git reset file.txt copia el archivo de HEAD al índice.
  evidencia: "Por lo tanto, básicamente solo copia archivo.txt de HEAD al Índice."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-738
  hecho: Ese reset con ruta tiene el efecto práctico de sacar el archivo del área de preparación.
  evidencia: "Esto tiene el efecto práctico de hacer unstaging al archivo."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-739
  hecho: Sobre el índice, git reset con ruta y git add son operaciones opuestas.
  evidencia: "Si miramos el diagrama para ese comando y pensamos en lo que hace git add, son exactamente opuestos."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-740
  hecho: Indicando un commit concreto, reset con ruta lleva al índice la versión del archivo de ese commit.
  evidencia: "especificando un “commit” específico para extraer esa versión del archivo."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-741
  hecho: Con git reset --soft HEAD~2 se puede mover la rama a un commit anterior para aplastar commits.
  evidencia: "Puedes ejecutar git reset --soft HEAD~2 para mover la rama HEAD a un “commit” anterior"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-742
  hecho: Tras ese reset --soft basta con ejecutar git commit de nuevo para obtener un único commit.
  evidencia: "Y luego simplemente ejecuta git commit nuevamente:"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-743
  hecho: El commit intermedio aplastado deja de estar en el historial alcanzable.
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
  evidencia: "Si ejecutamos git reset master, develop ahora apuntará al mismo “commit” que master."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-749
  hecho: Estando en develop, git checkout master no mueve develop: mueve HEAD.
  evidencia: "Si en cambio ejecutamos git checkout master, develop no se mueve, HEAD sí lo hace."
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
  evidencia: "Es como git reset [branch] file en que actualiza el índice con ese archivo en ese “commit”, pero también sobrescribe el archivo en el Directorio de Trabajo."
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-752
  hecho: checkout con ruta no es seguro para el directorio de trabajo.
  evidencia: "no está directorio-de-trabajo seguro, y no mueve a HEAD."
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
  hecho: Según la tabla, reset --soft [commit] mueve la rama, no toca el índice ni el directorio de trabajo y es seguro para este último.
  evidencia: "reset --soft [commit] REF NO NO SI"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-756
  hecho: Según la tabla, reset [commit] mueve la rama, cambia el índice, no toca el directorio de trabajo y es seguro para este último.
  evidencia: "reset [commit] REF SI NO SI"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-757
  hecho: Según la tabla, reset --hard [commit] mueve la rama, cambia índice y directorio de trabajo, y no es seguro para este último.
  evidencia: "reset --hard [commit] REF SI SI NO"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-758
  hecho: Según la tabla, checkout [commit] mueve HEAD, cambia índice y directorio de trabajo, y es seguro para este último.
  evidencia: "checkout [commit] HEAD SI SI SI"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-759
  hecho: Según la tabla, reset (commit) [archivo] no mueve nada, cambia el índice, no toca el directorio de trabajo y es seguro.
  evidencia: "reset (commit) [file] NO SI NO SI"
  fuente: f01-15
  ancla: https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado
  consultada: 2026-11-12

- id: h01-760
  hecho: Según la tabla, checkout (commit) [archivo] no mueve HEAD, cambia índice y directorio de trabajo, y no es seguro para este último.
  evidencia: "checkout (commit) [file] NO SI SI NO"
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

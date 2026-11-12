#!/usr/bin/env python3
"""Cortafuegos 3: ejecuta los ejemplos e inserta en el borrador el código y su salida real.

Uso:
    python scripts/insertar_ejemplos.py investigacion/cap-01/borrador.md
    python scripts/insertar_ejemplos.py investigacion/cap-01/borrador.md --comprobar

Marcas en el borrador:

    <!-- ejemplo: ejemplos/cap-10/tareas.py -->
    <!-- ejemplo: ejemplos/cap-11/division.py | falla -->   (se espera código de salida != 0)

El script ejecuta cada archivo en una carpeta temporal limpia y escribe debajo
de la marca el bloque de código y la salida, cerrados con <!-- /ejemplo -->.
Si se vuelve a ejecutar, sustituye lo que haya entre ambas marcas. Si un
ejemplo falla (o no falla cuando debía), el script termina con código 1.
Con --comprobar no escribe nada: falla si alguna salida del borrador ya no
coincide con la ejecución actual.

Tipos de ejemplo:
- .py: se ejecuta con el python3 actual. Bloque «python» + bloque «text» con la salida.
- .sh: sesión de terminal. Cada grupo de líneas separado por una línea en blanco
  es un comando; se muestra como «$ comando» seguido de su salida, en un bloque
  «console». Un grupo que termine con el comentario «# falla» puede acabar con
  error. Las líneas que empiezan por «#» antes del primer comando son cabecera
  y no se muestran.
- Otros lenguajes se añadirán cuando los pida el libro (node, go...).

La primera línea del archivo puede declarar herramientas extra cuya versión se
anota, p. ej. «# versiones: git». Git se ejecuta con autor y fechas fijas para
que los hashes de los commits sean reproducibles.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

import comun

TIEMPO_MAXIMO = 60
FECHA_FIJA = "2026-01-01T12:00:00+01:00"
LENGUAJE = {".py": "python", ".sh": "bash"}
COMENTARIO = {".py": "#", ".sh": "#"}
INTERPRETE_BASE = {".py": "python", ".sh": "bash"}


class ErrorEjemplo(Exception):
    pass


@dataclass
class Ejemplo:
    ruta: Path
    falla: bool = False


def entorno_reproducible(casa: Path) -> dict[str, str]:
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    env.update({
        "HOME": str(casa), "LC_ALL": "C.UTF-8", "LANG": "C.UTF-8", "TZ": "Europe/Madrid",
        "PYTHONHASHSEED": "0", "PYTHONDONTWRITEBYTECODE": "1",
        "GIT_AUTHOR_NAME": "devOC", "GIT_AUTHOR_EMAIL": "devoc@ejemplo.dev",
        "GIT_COMMITTER_NAME": "devOC", "GIT_COMMITTER_EMAIL": "devoc@ejemplo.dev",
        "GIT_AUTHOR_DATE": FECHA_FIJA, "GIT_COMMITTER_DATE": FECHA_FIJA,
        "GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_COUNT": "2",
        "GIT_CONFIG_KEY_0": "init.defaultBranch", "GIT_CONFIG_VALUE_0": "main",
        "GIT_CONFIG_KEY_1": "advice.detachedHead", "GIT_CONFIG_VALUE_1": "false",
    })
    return env


def version(herramienta: str) -> str:
    if herramienta == "python":
        return f"Python {sys.version.split()[0]}"
    try:
        salida = subprocess.run([herramienta, "--version"], capture_output=True, text=True, timeout=10)
    except FileNotFoundError:
        raise ErrorEjemplo(f"la herramienta {herramienta!r} no está instalada")
    primera = (salida.stdout or salida.stderr).strip().splitlines()[0]
    m = re.search(r"\d+\.\d+(\.\d+)?", primera)
    nombre = herramienta.capitalize() if herramienta != "git" else "Git"
    return f"{nombre} {m.group(0)}" if m else primera


def herramientas(codigo: str, sufijo: str) -> list[str]:
    lista = [INTERPRETE_BASE[sufijo]]
    m = re.match(r"^#\s*versiones:\s*(.+)$", codigo.splitlines()[0] if codigo else "")
    if m:
        lista += [h.strip() for h in m.group(1).split(",") if h.strip()]
    return lista


def _limpiar(salida: str, carpeta: Path) -> str:
    """Quita la ruta temporal de la salida para que sea estable entre ejecuciones."""
    return salida.replace(str(carpeta), "/tmp/ejemplo").rstrip()


def ejecutar_python(ej: Ejemplo, codigo: str) -> tuple[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        carpeta = Path(tmp).resolve()
        shutil.copy(ej.ruta, carpeta / ej.ruta.name)
        r = subprocess.run([sys.executable, ej.ruta.name], cwd=carpeta, capture_output=True,
                           text=True, timeout=TIEMPO_MAXIMO, env=entorno_reproducible(carpeta))
        salida = _limpiar(r.stdout + r.stderr, carpeta)
    if (r.returncode != 0) != ej.falla:
        estado = "falló" if r.returncode else "no falló y debía fallar"
        raise ErrorEjemplo(f"{ej.ruta} {estado} (código {r.returncode}):\n{salida}")
    cuerpo = "\n".join(l for l in codigo.rstrip().splitlines() if not l.startswith("# versiones:"))
    return cuerpo, f"```text\n{salida}\n```"


def grupos_shell(codigo: str) -> list[list[str]]:
    lineas = codigo.rstrip().splitlines()
    while lineas and (lineas[0].startswith("#") or not lineas[0].strip()):
        lineas.pop(0)
    grupos, actual = [], []
    for linea in lineas:
        if linea.strip():
            actual.append(linea)
        elif actual:
            grupos.append(actual)
            actual = []
    if actual:
        grupos.append(actual)
    return grupos


def ejecutar_shell(ej: Ejemplo, codigo: str) -> tuple[str, str]:
    """Ejecuta cada grupo en la misma shell y separa su salida con delimitadores."""
    grupos = grupos_shell(codigo)
    marca = "@@FIN-COMANDO-7f3a@@"
    guion = []
    for g in grupos:
        guion.append("\n".join(g))
        guion.append(f'echo "{marca}$?"')
    with tempfile.TemporaryDirectory() as tmp:
        carpeta = Path(tmp).resolve()
        r = subprocess.run(["bash", "--noprofile", "--norc", "-c", "exec 2>&1\n" + "\n".join(guion)],
                           cwd=carpeta, capture_output=True, text=True, timeout=TIEMPO_MAXIMO,
                           env=entorno_reproducible(carpeta))
        salida = _limpiar(r.stdout, carpeta) + "\n"
    trozos = re.split(rf"{re.escape(marca)}(\d+)\n", salida)
    if len(trozos) != 2 * len(grupos) + 1:
        raise ErrorEjemplo(f"{ej.ruta}: la sesión terminó antes de tiempo:\n{salida}")

    sesion = []
    for i, g in enumerate(grupos):
        texto, codigo_salida = trozos[2 * i], int(trozos[2 * i + 1])
        espera_fallo = g[-1].rstrip().endswith("# falla")
        visibles = [re.sub(r"\s*# falla\s*$", "", l) for l in g]
        if (codigo_salida != 0) != espera_fallo:
            estado = "falló" if codigo_salida else "no falló y debía fallar"
            raise ErrorEjemplo(f"{ej.ruta}: el comando «{visibles[0]}» {estado} "
                               f"(código {codigo_salida}):\n{texto}")
        sesion.append("$ " + visibles[0])
        sesion.extend("> " + l for l in visibles[1:])
        if texto.strip():
            sesion.append(texto.rstrip())
    return "\n".join(sesion), ""


def generar_bloque(ej: Ejemplo, raiz: Path = comun.RAIZ) -> str:
    ruta = ej.ruta if ej.ruta.is_absolute() else raiz / ej.ruta
    if not ruta.exists():
        raise ErrorEjemplo(f"no existe el ejemplo {ej.ruta}")
    sufijo = ruta.suffix
    if sufijo not in LENGUAJE:
        raise ErrorEjemplo(f"{ej.ruta}: tipo de ejemplo no soportado ({sufijo})")
    codigo = ruta.read_text(encoding="utf-8")
    versiones = ", ".join(version(h) for h in herramientas(codigo, sufijo))
    ej_abs = Ejemplo(ruta, ej.falla)
    cabecera = f"{COMENTARIO[sufijo]} Ejecutado con {versiones}"
    if sufijo == ".py":
        cuerpo, salida = ejecutar_python(ej_abs, codigo)
        return f"```python\n{cabecera}\n{cuerpo}\n```\n\n{salida}"
    sesion, _ = ejecutar_shell(ej_abs, codigo)
    return f"```console\n{cabecera}\n{sesion}\n```"


def procesar(texto: str, raiz: Path = comun.RAIZ) -> tuple[str, list[str]]:
    """Devuelve el texto con los ejemplos insertados y la lista de errores."""
    errores: list[str] = []
    partes: list[str] = []
    pos = 0
    for m in comun.MARCA_EJEMPLO.finditer(texto):
        if m.start() < pos:
            continue
        partes.append(texto[pos:m.end()])
        fin = texto.find(comun.FIN_EJEMPLO, m.end())
        siguiente = comun.MARCA_EJEMPLO.search(texto, m.end())
        if fin != -1 and (siguiente is None or fin < siguiente.start()):
            pos = fin + len(comun.FIN_EJEMPLO)
            anterior = texto[m.end():fin]
        else:
            pos = m.end()
            anterior = None
        opciones = (m.group("opciones") or "").split()
        ej = Ejemplo(Path(m.group("ruta").strip()), falla="falla" in opciones)
        try:
            bloque = generar_bloque(ej, raiz)
        except (ErrorEjemplo, subprocess.TimeoutExpired) as e:
            errores.append(str(e))
            bloque = anterior.strip("\n") if anterior else ""
        partes.append(f"\n{bloque}\n{comun.FIN_EJEMPLO}" if bloque else f"\n{comun.FIN_EJEMPLO}")
    partes.append(texto[pos:])
    return "".join(partes), errores


def quitar_marcas(texto: str) -> str:
    """Para publicar: deja el código y la salida y elimina las marcas."""
    texto = re.sub(comun.MARCA_EJEMPLO.pattern + r"\n?", "", texto)
    return re.sub(r"\n?" + re.escape(comun.FIN_EJEMPLO), "", texto)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("borrador", type=Path)
    p.add_argument("--comprobar", action="store_true", help="no escribe; falla si algo cambió")
    args = p.parse_args(argv)

    original = args.borrador.read_text(encoding="utf-8")
    nuevo, errores = procesar(original)
    total = len(comun.MARCA_EJEMPLO.findall(original))
    for e in errores:
        print(f"  FALLA {e}")
    if args.comprobar:
        if nuevo != original and not errores:
            print("  DIFERENTE: alguna salida del borrador no coincide con la ejecución actual")
            return 1
    elif nuevo != original:
        args.borrador.write_text(nuevo, encoding="utf-8")
    print(f"{total} ejemplos, {len(errores)} con fallos")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Comprueba los enlaces de uno o varios archivos Markdown.

Uso:
    python scripts/comprobar_enlaces.py contenido/parte-01-base/cap-01-git-por-dentro.md
    python scripts/comprobar_enlaces.py contenido --red     # además, que cada URL responda

- Enlaces relativos: el archivo existe y, si llevan #ancla, el encabezado existe
  (con las anclas al estilo de GitHub).
- Enlaces externos: la URL está en docs/03-indice-con-fuentes.md (regla 2).
  Con --red, además se pide la página y se exige una respuesta 2xx o 3xx.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import comun

ENLACE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
URL_SUELTA = re.compile(r"(?<![(<])https?://[^\s)>\]]+")


def ancla_github(titulo: str) -> str:
    titulo = re.sub(r"[`*_]", "", titulo.strip().lower())
    titulo = re.sub(r"[^\w\- ]", "", titulo)
    return titulo.replace(" ", "-")


def anclas(ruta: Path) -> set[str]:
    texto = comun.sin_bloques_de_codigo(ruta.read_text(encoding="utf-8"))
    vistas: dict[str, int] = {}
    resultado = set()
    for m in re.finditer(r"^#{1,6}\s+(.+?)\s*#*\s*$", texto, re.MULTILINE):
        base = ancla_github(m.group(1))
        n = vistas.get(base, 0)
        vistas[base] = n + 1
        resultado.add(base if n == 0 else f"{base}-{n}")
    return resultado


def enlaces(texto: str) -> list[str]:
    texto = comun.sin_bloques_de_codigo(texto)
    lista = ENLACE.findall(texto)
    sin_md = ENLACE.sub("", texto)
    lista += [u.rstrip(".,;:") for u in URL_SUELTA.findall(sin_md)]
    return lista


def comprobar_archivo(ruta: Path, autorizadas: set[str], red: bool = False) -> list[str]:
    errores = []
    for destino in enlaces(ruta.read_text(encoding="utf-8")):
        if destino.startswith(("http://", "https://")):
            if comun.normalizar_url(destino) not in autorizadas:
                errores.append(f"{ruta}: {destino} no está en docs/03-indice-con-fuentes.md")
            elif red:
                error = responde(destino)
                if error:
                    errores.append(f"{ruta}: {destino} {error}")
            continue
        if destino.startswith("mailto:"):
            continue
        archivo, _, ancla = destino.partition("#")
        objetivo = (ruta.parent / archivo).resolve() if archivo else ruta
        if not objetivo.exists():
            errores.append(f"{ruta}: el enlace {destino} apunta a un archivo que no existe")
        elif ancla and objetivo.suffix == ".md" and ancla not in anclas(objetivo):
            errores.append(f"{ruta}: el enlace {destino} apunta a un encabezado que no existe")
    return errores


def responde(url: str) -> str | None:
    import requests
    try:
        r = requests.get(url, timeout=20, allow_redirects=True,
                         headers={"User-Agent": "libro-devoc-verificador/1.0"})
    except requests.RequestException as e:
        return f"no responde ({e.__class__.__name__})"
    return None if r.status_code < 400 else f"responde {r.status_code}"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("rutas", nargs="+", type=Path)
    p.add_argument("--red", action="store_true", help="pide cada URL externa")
    args = p.parse_args(argv)
    autorizadas = comun.urls_autorizadas()
    archivos = []
    for r in args.rutas:
        archivos += sorted(r.rglob("*.md")) if r.is_dir() else [r]
    errores = []
    for a in archivos:
        errores += comprobar_archivo(a, autorizadas, args.red)
    for e in errores:
        print(f"  ROTO {e}")
    print(f"{len(archivos)} archivos, {len(errores)} enlaces con problemas")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())

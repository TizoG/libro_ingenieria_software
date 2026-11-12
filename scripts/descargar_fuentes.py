#!/usr/bin/env python3
"""Cortafuegos 1: descarga una copia local de cada fuente de un capítulo.

Uso:
    python scripts/descargar_fuentes.py 1             # descarga lo que falte
    python scripts/descargar_fuentes.py 1 --forzar    # vuelve a descargar todo
    python scripts/descargar_fuentes.py 1 --comprobar # avisa si alguna fuente cambió

Lee investigacion/cap-XX/fuentes.yaml:

    f01-01:
      titulo: "Pro Git 1.1, Acerca del control de versiones"
      url: https://git-scm.com/book/es/v2/...

y guarda fuentes-cache/cap-XX/<id>.md con una cabecera (fuente, url, fecha y
sha256 del texto) y el texto visible de la página. Solo descarga URLs que estén
en docs/03-indice-con-fuentes.md. La carpeta fuentes-cache/ no se publica.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import re
import sys

import requests
from bs4 import BeautifulSoup

import comun

AGENTE = "libro-devoc-verificador/1.0"
DESCARTAR = ("script", "style", "noscript", "nav", "header", "footer", "aside", "form", "svg")
# Contenedores conocidos que no son contenido (índices laterales, navegación anterior/siguiente).
DESCARTAR_SELECTORES = ("#book-chapters", "#nav", ".sidebar")
# Contenedor principal, del más específico al más general (div#main es el de git-scm.com).
CONTENEDORES = ("div#main", "main", "article", "body")
BLOQUES = ("p", "div", "li", "ul", "ol", "dl", "dt", "dd", "h1", "h2", "h3", "h4", "h5", "h6",
           "pre", "blockquote", "table", "tr", "td", "th", "section", "figure", "figcaption", "br", "hr")


def extraer_texto(html: str) -> str:
    """Texto visible del contenido principal, con un salto de línea por bloque.

    Las etiquetas en línea (<em>, <code>, <a>) no parten el texto, para que una
    frase con énfasis se pueda localizar literalmente.
    """
    sopa = BeautifulSoup(html, "html.parser")
    for etiqueta in sopa(DESCARTAR):
        etiqueta.decompose()
    for selector in DESCARTAR_SELECTORES:
        for etiqueta in sopa.select(selector):
            etiqueta.decompose()
    raiz = next((r for c in CONTENEDORES if (r := sopa.select_one(c))), sopa)
    for bloque in raiz.find_all(BLOQUES):
        bloque.insert_before("\n")
        bloque.append("\n")
    lineas = (re.sub(r"[ \t\r\f\v]+", " ", l).strip() for l in raiz.get_text().splitlines())
    return "\n".join(l for l in lineas if l) + "\n"


def huella(texto: str) -> str:
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def descargar(url: str) -> str:
    r = requests.get(url, headers={"User-Agent": AGENTE}, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding if r.encoding in (None, "ISO-8859-1") else r.encoding
    if "html" in r.headers.get("Content-Type", "html"):
        return extraer_texto(r.text)
    return r.text


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("capitulo", type=int)
    grupo = p.add_mutually_exclusive_group()
    grupo.add_argument("--forzar", action="store_true", help="vuelve a descargar aunque exista copia")
    grupo.add_argument("--comprobar", action="store_true", help="compara con la copia sin sobrescribirla")
    args = p.parse_args(argv)

    fuentes = comun.leer_fuentes_capitulo(args.capitulo)
    if not fuentes:
        print(f"No hay investigacion/{comun.carpeta_capitulo(args.capitulo)}/fuentes.yaml")
        return 1
    autorizadas = comun.urls_autorizadas()
    fallo = False

    for fid, datos in fuentes.items():
        url = (datos or {}).get("url", "")
        if comun.normalizar_url(url) not in autorizadas:
            print(f"  NO AUTORIZADA {fid}: {url} no está en docs/03-indice-con-fuentes.md")
            fallo = True
            continue
        destino = comun.ruta_cache(args.capitulo, fid)
        if destino.exists() and not (args.forzar or args.comprobar):
            print(f"  ya existe   {fid}")
            continue
        try:
            texto = descargar(url)
        except requests.RequestException as e:
            print(f"  ERROR       {fid}: {e}")
            fallo = True
            continue

        if args.comprobar:
            if not destino.exists():
                print(f"  sin copia   {fid}")
                fallo = True
            elif comun.leer_cache(destino)[0].get("sha256") != huella(texto):
                print(f"  CAMBIADA    {fid}: la página ya no coincide con la copia; revisa el capítulo")
                fallo = True
            else:
                print(f"  igual       {fid}")
            continue

        destino.parent.mkdir(parents=True, exist_ok=True)
        cabecera = {"fuente": fid, "titulo": datos.get("titulo", ""), "url": url,
                    "descargada": dt.date.today().isoformat(), "sha256": huella(texto)}
        destino.write_text(comun.escribir_frontmatter(cabecera, texto), encoding="utf-8")
        print(f"  descargada  {fid} ({len(texto)} caracteres)")
    return 1 if fallo else 0


if __name__ == "__main__":
    sys.exit(main())

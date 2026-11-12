#!/usr/bin/env python3
"""Valida que contenido/ cumple docs/06-contrato-con-la-web.md (versión 1).

Uso:
    python scripts/validar_contrato.py              # todo contenido/
    python scripts/validar_contrato.py contenido/parte-01-base/cap-01-git-por-dentro.md

Comprueba nombres y rutas, la cabecera YAML, que no haya HTML (salvo
comentarios), que los recuadros usen solo los cuatro títulos, que cada [n]
tenga su línea en «## Fuentes» y que no queden marcas internas.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

import comun

PARTES = ("base", "python", "backend", "ia", "agentes", "agentica", "typescript", "arquitectura", "go")
CARPETAS_FIJAS = ("00-preliminares", "99-apendices", "_img")
ESTADOS = ("borrador", "revisado", "publicado")
CAMPOS_CAPITULO = ("id", "parte", "capitulo", "titulo", "estado", "actualizado", "palabras", "versiones")
CAMPOS_PARTE = ("parte", "titulo", "estado")
ETIQUETA_HTML = re.compile(r"</?[a-zA-Z][a-zA-Z0-9-]*(\s[^<>]*)?/?>")
REFERENCIA = re.compile(r"(?<![\]\w])\[(\d+(?:\s*,\s*\d+)*)\](?![(:\[])")
LINEA_FUENTE = re.compile(r"^\[(\d+)\]\s+\S")


def _sin_codigo_en_linea(texto: str) -> str:
    return re.sub(r"`[^`\n]*`", "", texto)


def validar_ruta(ruta: Path, contenido: Path, rutas_catalogo: set[str]) -> list[str]:
    rel = ruta.relative_to(contenido)
    errores = []
    if len(rel.parts) == 1:
        return [f"{rel}: los archivos van dentro de una carpeta (preliminares, parte o apéndices)"]
    carpeta = rel.parts[0]
    if carpeta in CARPETAS_FIJAS:
        return []
    m = re.fullmatch(r"parte-(\d{2})-([a-z]+)", carpeta)
    if not m or m.group(2) not in PARTES or int(m.group(1)) != PARTES.index(m.group(2)) + 1:
        return [f"{rel}: carpeta de parte no válida (parte-NN-<id> con los ids del catálogo)"]
    if len(rel.parts) != 2:
        return [f"{rel}: no se admiten subcarpetas dentro de una parte"]
    nombre = rel.parts[1]
    if nombre in ("_parte.md", "soluciones.md"):
        return []
    if not re.fullmatch(r"cap-\d{2}-[a-z0-9-]+\.md", nombre):
        errores.append(f"{rel}: nombre de capítulo no válido (cap-NN-<slug>.md)")
    elif f"contenido/{rel.as_posix()}" not in rutas_catalogo:
        errores.append(f"{rel}: la ruta no coincide con la de docs/04-catalogo-capitulos.md")
    return errores


def validar_cabecera(ruta: Path, datos: dict | None, capitulos: dict[str, comun.Capitulo],
                     contenido: Path) -> list[str]:
    rel = ruta.relative_to(contenido)
    carpeta = rel.parts[0]
    if carpeta in CARPETAS_FIJAS:
        return []
    if datos is None:
        return [f"{rel}: falta la cabecera YAML"]
    es_capitulo = ruta.name.startswith("cap-")
    campos = CAMPOS_CAPITULO if es_capitulo else CAMPOS_PARTE
    errores = [f"{rel}: falta el campo «{c}» en la cabecera" for c in campos if c not in datos]
    if datos.get("estado") not in ESTADOS:
        errores.append(f"{rel}: «estado» debe ser uno de {', '.join(ESTADOS)}")
    m = re.match(r"parte-(\d{2})", carpeta)
    if m and datos.get("parte") != int(m.group(1)):
        errores.append(f"{rel}: «parte» no coincide con la carpeta")
    if es_capitulo:
        cap = capitulos.get(f"contenido/{rel.as_posix()}")
        if cap:
            if datos.get("capitulo") != cap.numero:
                errores.append(f"{rel}: «capitulo» debería ser {cap.numero}")
            if datos.get("id") != cap.id:
                errores.append(f"{rel}: «id» debería ser {cap.id}")
        actualizado = datos.get("actualizado")
        if "actualizado" in datos and not isinstance(actualizado, dt.date):
            errores.append(f"{rel}: «actualizado» debe ser una fecha AAAA-MM-DD")
        if "palabras" in datos and not isinstance(datos.get("palabras"), int):
            errores.append(f"{rel}: «palabras» debe ser un número entero")
        if "versiones" in datos and not isinstance(datos.get("versiones"), dict):
            errores.append(f"{rel}: «versiones» debe ser un mapa herramienta: versión")
    return errores


def validar_cuerpo(rel: Path | str, cuerpo: str) -> list[str]:
    errores = []
    sin_codigo = comun.sin_bloques_de_codigo(cuerpo)
    lineas = sin_codigo.splitlines()

    sin_comentarios = re.sub(r"<!--.*?-->", "", _sin_codigo_en_linea(sin_codigo), flags=re.DOTALL)
    for etiqueta in sorted(set(m.group(0) for m in ETIQUETA_HTML.finditer(sin_comentarios))):
        errores.append(f"{rel}: HTML no permitido: {etiqueta}")

    for n, linea in enumerate(lineas, 1):
        m = re.match(r"^\s*>\s*\*\*([^*]+?)\.?\*\*", linea)
        if m and m.group(1).rstrip(".") not in comun.RECUADROS:
            errores.append(f"{rel}:{n}: recuadro con título no permitido: «{m.group(1)}»")

    if comun.MARCA_EJEMPLO.search(cuerpo) or comun.FIN_EJEMPLO in cuerpo:
        errores.append(f"{rel}: quedan marcas de ejemplo sin resolver")
    if comun.ids_citados(sin_codigo):
        errores.append(f"{rel}: quedan ids de hechos sin convertir en referencias")
    if comun.PENDIENTE.search(sin_codigo):
        errores.append(f"{rel}: quedan marcas PENDIENTE")

    partes = re.split(r"^## Fuentes\s*$", sin_codigo, maxsplit=1, flags=re.MULTILINE)
    texto = _sin_codigo_en_linea(partes[0])
    citadas = set()
    for grupo in REFERENCIA.findall(texto):
        citadas |= {int(x) for x in grupo.split(",")}
    definidas = set()
    if len(partes) == 2:
        for linea in partes[1].splitlines():
            m = LINEA_FUENTE.match(linea)
            if m:
                definidas.add(int(m.group(1)))
    for n in sorted(citadas - definidas):
        errores.append(f"{rel}: la referencia [{n}] no tiene línea en «## Fuentes»")
    return errores


def validar(rutas: list[Path], contenido: Path = comun.CONTENIDO) -> list[str]:
    capitulos = {c.archivo: c for c in comun.leer_catalogo()}
    errores = []
    for ruta in rutas:
        ruta = ruta.resolve()
        rel = ruta.relative_to(contenido)
        if "_img" in rel.parts:
            continue
        if ruta.suffix != ".md":
            errores.append(f"{rel}: solo se admiten archivos .md fuera de _img/")
            continue
        errores += validar_ruta(ruta, contenido, set(capitulos))
        datos, cuerpo = comun.leer_frontmatter(ruta.read_text(encoding="utf-8"))
        errores += validar_cabecera(ruta, datos, capitulos, contenido)
        errores += validar_cuerpo(rel, cuerpo)
    return errores


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("rutas", nargs="*", type=Path)
    args = p.parse_args(argv)
    rutas = args.rutas or [comun.CONTENIDO]
    archivos = []
    for r in rutas:
        r = r.resolve()
        archivos += sorted(f for f in r.rglob("*") if f.is_file() and f.name != ".gitkeep") if r.is_dir() else [r]
    errores = validar(archivos)
    for e in errores:
        print(f"  INCUMPLE {e}")
    print(f"{len(archivos)} archivos, {len(errores)} incumplimientos del contrato")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())

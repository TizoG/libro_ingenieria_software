#!/usr/bin/env python3
"""Junta investigacion/cap-XX/secciones/*.md en investigacion/cap-XX/hechos.md.

Uso:
    python scripts/juntar_hechos.py 1

La investigación se hace por secciones, cada una en su archivo y con su rango de
ids (la sección N.k usa hNN-k01 a hNN-k99), para que varias pasadas trabajen en
paralelo sin pisarse. Este script las concatena en orden y avisa si hay ids
repetidos. hechos.md no se edita a mano: se edita la sección y se vuelve a juntar.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import comun


def orden(ruta: Path) -> tuple[int, ...]:
    return tuple(int(x) for x in re.findall(r"\d+", ruta.stem))


def juntar(numero: int, base: Path = comun.INVESTIGACION) -> tuple[str, list[str]]:
    carpeta = base / comun.carpeta_capitulo(numero)
    secciones = sorted((carpeta / "secciones").glob("*.md"), key=orden)
    cap = next((c for c in comun.leer_catalogo() if c.numero == numero), None)
    titulo = f": {cap.titulo}" if cap else ""
    partes = [f"# Hechos del capítulo {numero}{titulo}", "",
              "Hechos atómicos con evidencia literal (cortafuegos 2). Se generan con "
              "`scripts/juntar_hechos.py` a partir de `secciones/`; edita la sección y vuelve a juntar.", ""]
    vistos: dict[str, str] = {}
    errores = []
    for s in secciones:
        texto = s.read_text(encoding="utf-8").strip()
        for b in comun.leer_bloques(texto):
            hid = b.get("id")
            if hid in vistos:
                errores.append(f"{hid} repetido en {vistos[hid]} y {s.name}")
            vistos.setdefault(hid, s.name)
        partes += [texto, ""]
    return "\n".join(partes), errores


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("capitulo", type=int)
    args = p.parse_args(argv)
    texto, errores = juntar(args.capitulo)
    for e in errores:
        print(f"  REPETIDO {e}")
    if errores:
        return 1
    destino = comun.INVESTIGACION / comun.carpeta_capitulo(args.capitulo) / "hechos.md"
    destino.write_text(texto, encoding="utf-8")
    print(f"Escrito {destino.relative_to(comun.RAIZ)} ({len(comun.leer_bloques(texto))} hechos)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

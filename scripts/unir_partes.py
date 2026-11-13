#!/usr/bin/env python3
"""Une investigacion/cap-XX/borrador-v2/parte-*.md en investigacion/cap-XX/borrador.md.

Uso:
    python scripts/unir_partes.py 1

La primera parte lleva la cabecera YAML y el título; las demás empiezan por su
primera sección. Las junta en orden numérico separadas por una línea en blanco.
No ejecuta los ejemplos: después hay que pasar scripts/insertar_ejemplos.py.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import comun


def orden(ruta: Path) -> int:
    return int(re.search(r"\d+", ruta.stem).group(0))


def unir(numero: int, base: Path = comun.INVESTIGACION) -> str:
    carpeta = base / comun.carpeta_capitulo(numero) / "borrador-v2"
    partes = sorted(carpeta.glob("parte-*.md"), key=orden)
    if not partes:
        raise SystemExit(f"No hay partes en {carpeta}")
    textos = [p.read_text(encoding="utf-8").strip("\n") for p in partes]
    return "\n\n".join(textos) + "\n"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("capitulo", type=int)
    args = p.parse_args(argv)
    destino = comun.INVESTIGACION / comun.carpeta_capitulo(args.capitulo) / "borrador.md"
    destino.write_text(unir(args.capitulo), encoding="utf-8")
    print(f"Escrito {destino.relative_to(comun.RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

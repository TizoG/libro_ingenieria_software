#!/usr/bin/env python3
"""Redacción cerrada: cada id de hecho citado en el borrador existe y ha pasado el cortafuegos 2.

Uso:
    python scripts/comprobar_ids.py 1

Lee investigacion/cap-XX/borrador.md, busca citas como [h01-003] o
[h01-003, h01-004] fuera de los bloques de código y comprueba que cada id
está en hechos.md y que verificar_evidencias.py lo da por válido.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field
from pathlib import Path

import comun
import verificar_evidencias


@dataclass
class ResultadoIds:
    citados: list[str] = field(default_factory=list)
    inexistentes: list[str] = field(default_factory=list)
    rechazados: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not (self.inexistentes or self.rechazados)


def ruta_borrador(numero: int, base: Path = comun.INVESTIGACION) -> Path:
    return base / comun.carpeta_capitulo(numero) / "borrador.md"


def comprobar(numero: int, texto: str | None = None, investigacion: Path = comun.INVESTIGACION,
              cache: Path = comun.FUENTES_CACHE, indice: Path = comun.INDICE_FUENTES) -> ResultadoIds:
    if texto is None:
        texto = ruta_borrador(numero, investigacion).read_text(encoding="utf-8")
    citados = comun.ids_citados(comun.sin_bloques_de_codigo(texto))
    existentes = {h.get("id") for h in comun.leer_hechos(numero, investigacion)}
    validos = set(verificar_evidencias.verificar(numero, investigacion, cache, indice).validos)
    res = ResultadoIds(citados=citados)
    for hid in dict.fromkeys(citados):
        if hid not in existentes:
            res.inexistentes.append(hid)
        elif hid not in validos:
            res.rechazados.append(hid)
    return res


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("capitulo", type=int)
    args = p.parse_args(argv)
    res = comprobar(args.capitulo)
    print(f"{len(res.citados)} citas, {len(set(res.citados))} ids distintos")
    for hid in res.inexistentes:
        print(f"  INEXISTENTE {hid}: no está en hechos.md")
    for hid in res.rechazados:
        print(f"  RECHAZADO   {hid}: su evidencia no pasa verificar_evidencias.py")
    return 0 if res.ok else 1


if __name__ == "__main__":
    sys.exit(main())

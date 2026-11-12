#!/usr/bin/env python3
"""Cortafuegos 2: cada evidencia de hechos.md aparece literalmente en la copia local de su fuente.

Uso:
    python scripts/verificar_evidencias.py 1        # capítulo 1
    python scripts/verificar_evidencias.py --todos

Comprueba también que cada hecho tiene todos sus campos, que los ids son únicos
y siguen el formato hNN-NNN del capítulo, que la fuente está declarada en
fuentes.yaml y que su URL está en docs/03-indice-con-fuentes.md.
Sale con código 1 si algún hecho se rechaza.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import comun

CAMPOS = ("id", "hecho", "evidencia", "fuente", "ancla", "consultada")


@dataclass
class Resultado:
    validos: list[str] = field(default_factory=list)
    errores: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errores


def verificar(numero: int, investigacion: Path = comun.INVESTIGACION,
              cache: Path = comun.FUENTES_CACHE,
              indice: Path = comun.INDICE_FUENTES) -> Resultado:
    res = Resultado()
    hechos = comun.leer_hechos(numero, investigacion)
    fuentes = comun.leer_fuentes_capitulo(numero, investigacion)
    autorizadas = comun.urls_autorizadas(indice)
    textos: dict[str, str | None] = {}
    vistos: set[str] = set()

    for fid, datos in fuentes.items():
        url = (datos or {}).get("url", "")
        if comun.normalizar_url(url) not in autorizadas:
            res.errores.append(f"fuente {fid}: la URL {url!r} no está en docs/03-indice-con-fuentes.md")

    for h in hechos:
        hid = h.get("id")
        donde = f"{hid or '¿sin id?'} (línea {h.linea})"
        faltan = [c for c in CAMPOS if not h.get(c)]
        if faltan:
            res.errores.append(f"{donde}: faltan campos {', '.join(faltan)}")
            continue
        m = comun.ID_HECHO.fullmatch(hid)
        if not m or int(m.group(1)) != numero:
            res.errores.append(f"{donde}: el id debe tener el formato h{numero:02d}-NNN")
            continue
        if hid in vistos:
            res.errores.append(f"{donde}: id repetido")
            continue
        vistos.add(hid)
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", h.get("consultada")):
            res.errores.append(f"{donde}: «consultada» debe ser AAAA-MM-DD")
            continue

        fuente = h.get("fuente")
        if fuente not in fuentes:
            res.errores.append(f"{donde}: la fuente {fuente} no está en fuentes.yaml")
            continue
        url_fuente = comun.normalizar_url(fuentes[fuente].get("url", ""))
        if comun.normalizar_url(h.get("ancla")) != url_fuente:
            res.errores.append(f"{donde}: el ancla no corresponde a la URL de {fuente}")
            continue

        if fuente not in textos:
            ruta = comun.ruta_cache(numero, fuente, cache)
            textos[fuente] = comun.normalizar(comun.leer_cache(ruta)[1]) if ruta.exists() else None
        texto = textos[fuente]
        if texto is None:
            res.errores.append(f"{donde}: no hay copia local de {fuente} (ejecuta descargar_fuentes.py)")
            continue
        if comun.normalizar(h.get("evidencia")) not in texto:
            res.errores.append(f"{donde}: la evidencia no aparece en la copia local de {fuente}")
            continue
        res.validos.append(hid)
    return res


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("capitulo", nargs="?", type=int)
    p.add_argument("--todos", action="store_true", help="todos los capítulos con hechos.md")
    args = p.parse_args(argv)
    if args.todos:
        numeros = sorted(int(d.name[4:]) for d in comun.INVESTIGACION.glob("cap-[0-9][0-9]")
                         if (d / "hechos.md").exists())
    elif args.capitulo:
        numeros = [args.capitulo]
    else:
        p.error("indica un capítulo o --todos")

    fallo = False
    for n in numeros:
        res = verificar(n)
        print(f"Capítulo {n}: {len(res.validos)} hechos válidos, {len(res.errores)} rechazados")
        for e in res.errores:
            print(f"  RECHAZADO {e}")
        fallo |= not res.ok
    return 1 if fallo else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Detecta texto del borrador que coincide literalmente con las copias locales de las fuentes.

Uso:
    python scripts/detectar_copia.py 1                # borrador del capítulo 1
    python scripts/detectar_copia.py 1 --minimo 6     # umbral más estricto
    python scripts/detectar_copia.py 1 --archivo contenido/parte-01-base/cap-01-git-por-dentro.md

Regla del proyecto: se escribe con palabras propias; las citas literales al
lector tienen menos de 15 palabras y van entre comillas. Este script busca, en
la prosa del capítulo (sin código, salidas ni diagramas), secuencias de palabras
consecutivas que aparecen tal cual en alguna fuente de fuentes-cache/cap-XX/:

- 8 o más palabras seguidas (--minimo) fuera de comillas: fragmento literal sin comillas.
- 15 o más palabras seguidas, aunque vayan entre comillas: cita demasiado larga.

No detecta la paráfrasis cercana (cambiar alguna palabra) ni el calco de la
estructura de un capítulo: eso sigue siendo trabajo del revisor de fuentes.
Sale con código 1 si encuentra algo.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import comun
import comprobar_ids

CITA_MAXIMA = 15
PALABRA = re.compile(r"[0-9a-záéíóúüñ]+(?:[-'][0-9a-záéíóúüñ]+)*", re.IGNORECASE)
ENTRE_COMILLAS = re.compile(r"«[^»]*»|“[^”]*”|\"[^\"\n]*\"")


@dataclass
class Coincidencia:
    linea: int
    palabras: int
    fuente: str
    texto: str
    entre_comillas: bool


def palabras(texto: str) -> list[str]:
    return [p.lower() for p in PALABRA.findall(texto)]


def prosa(texto: str) -> list[tuple[int, str]]:
    """Líneas de prosa con su número: sin cabecera, código, comentarios, ids ni tablas de salida."""
    _, cuerpo = comun.leer_frontmatter(texto)
    desfase = texto.count("\n") - cuerpo.count("\n")
    limpio = comun.sin_bloques_de_codigo(cuerpo)
    limpio = re.sub(r"<!--.*?-->", lambda m: "\n" * m.group(0).count("\n"), limpio, flags=re.DOTALL)
    limpio = comun.CITA_HECHOS.sub("", limpio)
    limpio = re.sub(r"`[^`\n]*`", " § ", limpio)  # el código en línea corta las secuencias
    return [(n + desfase, l) for n, l in enumerate(limpio.splitlines(), start=1) if l.strip()]


def indice_ngramas(textos: dict[str, list[str]], n: int) -> dict[tuple[str, ...], str]:
    indice: dict[tuple[str, ...], str] = {}
    for fuente, ps in textos.items():
        for i in range(len(ps) - n + 1):
            indice.setdefault(tuple(ps[i:i + n]), fuente)
    return indice


def buscar(texto: str, fuentes: dict[str, str], minimo: int = 8) -> list[Coincidencia]:
    fuentes_p = {f: palabras(t) for f, t in fuentes.items()}
    indice = indice_ngramas(fuentes_p, minimo)
    cadenas = {f: " " + " ".join(p) + " " for f, p in fuentes_p.items()}
    res: list[Coincidencia] = []

    for linea, contenido in prosa(texto):
        citado = [(m.start(), m.end()) for m in ENTRE_COMILLAS.finditer(contenido)]
        # Posición de cada palabra para saber si la coincidencia cae dentro de unas comillas.
        tokens = [(m.group(0).lower(), m.start(), m.end()) for m in PALABRA.finditer(contenido)]
        # «§» marca un corte (código en línea): se parte la línea en tramos.
        cortes = [m.start() for m in re.finditer("§", contenido)]
        i = 0
        while i <= len(tokens) - minimo:
            ventana = tuple(t[0] for t in tokens[i:i + minimo])
            ini, fin = tokens[i][1], tokens[i + minimo - 1][2]
            if any(ini < c < fin for c in cortes) or ventana not in indice:
                i += 1
                continue
            fuente = indice[ventana]
            j = i + minimo
            # Alarga la coincidencia mientras siga apareciendo seguida en la misma fuente.
            while j < len(tokens) and not any(ini < c < tokens[j][2] for c in cortes):
                candidata = " " + " ".join(t[0] for t in tokens[i:j + 1]) + " "
                if candidata not in cadenas[fuente]:
                    break
                j += 1
            ini, fin = tokens[i][1], tokens[j - 1][2]
            dentro = any(a <= ini and fin <= b for a, b in citado)
            n = j - i
            if not dentro or n >= CITA_MAXIMA:
                res.append(Coincidencia(linea, n, fuente, contenido[ini:fin], dentro))
            i = j
    return res


def cargar_fuentes(numero: int, cache: Path = comun.FUENTES_CACHE) -> dict[str, str]:
    carpeta = cache / comun.carpeta_capitulo(numero)
    return {f.stem: comun.leer_cache(f)[1] for f in sorted(carpeta.glob("*.md"))}


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("capitulo", type=int)
    p.add_argument("--archivo", type=Path, help="archivo a analizar (por defecto, el borrador)")
    p.add_argument("--minimo", type=int, default=8, help="palabras seguidas a partir de las que se avisa")
    args = p.parse_args(argv)

    ruta = args.archivo or comprobar_ids.ruta_borrador(args.capitulo)
    fuentes = cargar_fuentes(args.capitulo)
    if not fuentes:
        print(f"No hay copias locales en fuentes-cache/{comun.carpeta_capitulo(args.capitulo)}/")
        return 1
    hallazgos = buscar(ruta.read_text(encoding="utf-8"), fuentes, args.minimo)
    for c in hallazgos:
        tipo = "CITA LARGA" if c.entre_comillas else "LITERAL"
        print(f"  {tipo} {ruta.name}:{c.linea} ({c.palabras} palabras, {c.fuente}): {c.texto}")
    print(f"{len(hallazgos)} fragmentos literales de {args.minimo} o más palabras")
    return 1 if hallazgos else 0


if __name__ == "__main__":
    sys.exit(main())

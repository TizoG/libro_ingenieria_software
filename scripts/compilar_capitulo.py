#!/usr/bin/env python3
"""Fase 8: convierte el borrador de un capítulo en el archivo que se publica en contenido/.

Uso:
    python scripts/compilar_capitulo.py 1
    python scripts/compilar_capitulo.py 1 --salida /tmp/prueba.md

Toma investigacion/cap-XX/borrador.md (con ids de hechos y marcas de ejemplo) y
escribe la ruta del catálogo en contenido/:

- cambia los ids [h01-003] por referencias numeradas [1], una por fuente, en
  orden de aparición, y añade al final la sección «## Fuentes»;
- quita las marcas <!-- ejemplo --> dejando el código y la salida;
- actualiza «palabras» y «actualizado» en la cabecera.

Se niega a compilar si quedan PENDIENTES, ids que no pasan la verificación,
ejemplos sin insertar o si el resultado no cumple el contrato con la web.
El estado lo decide la cabecera del borrador; «publicado» solo lo pone devOC.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

import comun
import comprobar_ids
import insertar_ejemplos
import validar_contrato


class ErrorCompilacion(Exception):
    pass


def contar_palabras(cuerpo: str) -> int:
    texto = comun.sin_bloques_de_codigo(cuerpo)
    texto = re.sub(r"<!--.*?-->", " ", texto, flags=re.DOTALL)
    return len(re.findall(r"[\wáéíóúüñÁÉÍÓÚÜÑ]+(?:[-'][\w]+)*", texto))


def compilar(numero: int, borrador: str, hechos: list[comun.Bloque], fuentes: dict[str, dict],
             hoy: dt.date | None = None) -> str:
    datos, cuerpo = comun.leer_frontmatter(borrador)
    if datos is None:
        raise ErrorCompilacion("el borrador no tiene cabecera YAML")
    sin_codigo = comun.sin_bloques_de_codigo(cuerpo)
    if comun.PENDIENTE.search(sin_codigo):
        raise ErrorCompilacion("el borrador tiene PENDIENTES abiertos")
    if re.search(r"^## Fuentes\s*$", sin_codigo, re.MULTILINE):
        raise ErrorCompilacion("el borrador no debe tener «## Fuentes»: la genera este script")
    for m in comun.MARCA_EJEMPLO.finditer(cuerpo):
        if not cuerpo[m.end():].lstrip("\n").startswith("```"):
            raise ErrorCompilacion(f"ejemplo sin insertar: {m.group('ruta')} (ejecuta insertar_ejemplos.py)")

    por_id = {h.get("id"): h for h in hechos}
    numeros: dict[str, int] = {}
    consultas: dict[str, str] = {}

    def sustituir(m: re.Match) -> str:
        refs = []
        for hid in (i.strip() for i in m.group(1).split(",")):
            hecho = por_id.get(hid)
            if hecho is None:
                raise ErrorCompilacion(f"id inexistente: {hid}")
            fuente = hecho.get("fuente")
            numeros.setdefault(fuente, len(numeros) + 1)
            consultas[fuente] = max(consultas.get(fuente, ""), hecho.get("consultada"))
            if numeros[fuente] not in refs:
                refs.append(numeros[fuente])
        return "[" + ", ".join(str(r) for r in sorted(refs)) + "]"

    # Solo fuera de los bloques de código.
    trozos = re.split(r"(^\s*```.*?^\s*```[^\n]*$)", cuerpo, flags=re.MULTILINE | re.DOTALL)
    cuerpo = "".join(t if i % 2 else comun.CITA_HECHOS.sub(sustituir, t) for i, t in enumerate(trozos))
    cuerpo = insertar_ejemplos.quitar_marcas(cuerpo).rstrip() + "\n"

    if numeros:
        lineas = ["", "## Fuentes", ""]
        for fuente, n in sorted(numeros.items(), key=lambda x: x[1]):
            info = fuentes.get(fuente) or {}
            if not info.get("url"):
                raise ErrorCompilacion(f"la fuente {fuente} no está en fuentes.yaml")
            titulo = info.get("titulo") or fuente
            lineas.append(f"[{n}] {titulo}. {info['url']} (consultada {consultas[fuente]})")
            lineas.append("")
        cuerpo += "\n".join(lineas)

    datos["palabras"] = contar_palabras(cuerpo)
    datos["actualizado"] = hoy or dt.date.today()
    return comun.escribir_frontmatter(datos, cuerpo)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("capitulo", type=int)
    p.add_argument("--salida", type=Path, help="ruta alternativa (para previsualizar)")
    args = p.parse_args(argv)

    cap = comun.capitulo_por_numero(args.capitulo)
    ruta = comprobar_ids.ruta_borrador(args.capitulo)
    borrador = ruta.read_text(encoding="utf-8")
    ids = comprobar_ids.comprobar(args.capitulo, borrador)
    if not ids.ok:
        print("No se compila: hay ids inexistentes o rechazados (ejecuta comprobar_ids.py)")
        return 1
    try:
        resultado = compilar(args.capitulo, borrador, comun.leer_hechos(args.capitulo),
                             comun.leer_fuentes_capitulo(args.capitulo))
    except ErrorCompilacion as e:
        print(f"No se compila: {e}")
        return 1

    destino = args.salida or comun.RAIZ / cap.archivo
    errores = validar_contrato.validar_cuerpo(destino.name, comun.leer_frontmatter(resultado)[1])
    if errores:
        for e in errores:
            print(f"  INCUMPLE {e}")
        print("No se compila: el resultado no cumple el contrato con la web")
        return 1
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(resultado, encoding="utf-8")
    print(f"Escrito {destino.relative_to(comun.RAIZ) if destino.is_relative_to(comun.RAIZ) else destino}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

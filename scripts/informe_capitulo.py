#!/usr/bin/env python3
"""Métricas de un capítulo (docs/05-metodo-sin-alucinaciones.md, sección 7).

Uso:
    python scripts/informe_capitulo.py 1             # muestra el informe
    python scripts/informe_capitulo.py 1 --guardar   # y lo guarda en docs/estado.md
    python scripts/informe_capitulo.py 1 --sin-ejecutar   # no ejecuta los ejemplos

Métricas bloqueantes (deben ser 0 para pasar a «revisado»):
1. Frases técnicas sin id de hecho: las que el revisor marcó «SIN HECHO» y siguen sin resolver.
2. Evidencias que no aparecen en su fuente (y, además, ids citados inexistentes o rechazados).
3. Ejemplos que fallan al ejecutarse o cuya salida ya no coincide con el borrador.
4. Frases del informe de revisión que no salieron SOPORTADA y siguen sin resolver.
5. Fragmentos copiados literalmente de una fuente (scripts/detectar_copia.py).

Informativas: PENDIENTES abiertos, párrafos sin ningún id (pista para el revisor) y palabras.

El informe de revisión es investigacion/cap-XX/revision.md (o varios archivos en
investigacion/cap-XX/revision/, uno por tramo), con bloques:

    - frase: "Una rama es un puntero móvil a un commit."
      hechos: h01-020
      veredicto: SOPORTADA | PARCIAL | NO SOPORTADA | SIN HECHO
      nota: qué sobra o qué falta
      resuelto: sí | no
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import comun
import comprobar_ids
import detectar_copia
import compilar_capitulo
import insertar_ejemplos
import verificar_evidencias

VEREDICTOS = ("SOPORTADA", "PARCIAL", "NO SOPORTADA", "SIN HECHO")
SECCIONES_SIN_HECHOS = ("lo que podrás hacer", "lo que necesitas antes", "el problema", "resumen",
                        "ejercicios", "preguntas de examen", "el proyecto avanza", "para profundizar")


@dataclass
class Informe:
    capitulo: int
    hechos_validos: int = 0
    evidencias_rechazadas: int = 0
    ids_mal: int = 0
    ejemplos: int = 0
    ejemplos_mal: int = 0
    ejemplos_sin_ejecutar: bool = False
    sin_hecho: int = 0
    no_soportadas: int = 0
    revision_existe: bool = False
    pendientes: int = 0
    parrafos_sin_id: int = 0
    literales: int = 0
    palabras: int = 0

    @property
    def bloqueantes(self) -> dict[str, int]:
        return {
            "Frases técnicas sin id de hecho": self.sin_hecho,
            "Evidencias que no aparecen en su fuente (y ids mal citados)": self.evidencias_rechazadas + self.ids_mal,
            "Ejemplos que fallan al ejecutarse": self.ejemplos_mal,
            "Frases NO SOPORTADAS o PARCIALES sin resolver": self.no_soportadas,
            "Fragmentos literales de una fuente (8+ palabras sin comillas, o citas de 15+)": self.literales,
        }

    @property
    def puede_pasar_a_revisado(self) -> bool:
        return (self.revision_existe and not self.ejemplos_sin_ejecutar
                and not any(self.bloqueantes.values()))

    def markdown(self) -> str:
        hoy = dt.date.today().isoformat()
        filas = [f"| {k} | {v} | 0 |" for k, v in self.bloqueantes.items()]
        filas.append(f"| PENDIENTES abiertos | {self.pendientes} | visibles y comunicados |")
        filas.append(f"| Párrafos sin ningún id (pista) | {self.parrafos_sin_id} | revisar |")
        filas.append(f"| Hechos válidos | {self.hechos_validos} | |")
        filas.append(f"| Ejemplos | {self.ejemplos}{' (sin ejecutar)' if self.ejemplos_sin_ejecutar else ''} | |")
        filas.append(f"| Palabras | {self.palabras} | 5.000 a 10.000 |")
        notas = []
        if not self.revision_existe:
            notas.append("- Falta el informe de revisión (`revision.md`): las métricas 1 y 4 no son fiables.")
        veredicto = "sí" if self.puede_pasar_a_revisado else "no"
        return "\n".join([
            f"### Capítulo {self.capitulo} (informe del {hoy})", "",
            "| Métrica | Valor | Objetivo |", "| --- | --- | --- |", *filas, "",
            *notas, f"Puede pasar a «revisado»: **{veredicto}**.",
        ])


def parrafos_sin_id(cuerpo: str) -> int:
    texto = re.sub(r"<!--.*?-->", "", comun.sin_bloques_de_codigo(cuerpo), flags=re.DOTALL)
    total, seccion = 0, ""
    for parrafo in re.split(r"\n\s*\n", texto):
        p = parrafo.strip()
        if not p:
            continue
        if p.startswith("#"):
            seccion = p.lstrip("#").strip().lower()
            if "\n" not in p:
                continue
        if p.startswith(("|", "```")) or seccion.startswith(SECCIONES_SIN_HECHOS):
            continue
        if comun.PENDIENTE.search(p):
            continue
        if len(p.split()) >= 12 and not comun.CITA_HECHOS.search(p):
            total += 1
    return total


def generar(numero: int, ejecutar: bool = True) -> Informe:
    inf = Informe(numero)
    ev = verificar_evidencias.verificar(numero)
    inf.hechos_validos, inf.evidencias_rechazadas = len(ev.validos), len(ev.errores)

    ruta = comprobar_ids.ruta_borrador(numero)
    if ruta.exists():
        borrador = ruta.read_text(encoding="utf-8")
        _, cuerpo = comun.leer_frontmatter(borrador)
        ids = comprobar_ids.comprobar(numero, borrador)
        inf.ids_mal = len(ids.inexistentes) + len(ids.rechazados)
        inf.pendientes = len(comun.PENDIENTE.findall(comun.sin_bloques_de_codigo(cuerpo)))
        inf.parrafos_sin_id = parrafos_sin_id(cuerpo)
        inf.literales = len(detectar_copia.buscar(borrador, detectar_copia.cargar_fuentes(numero)))
        # Sin ids de hechos: el lector no los verá (se convierten en [n] al compilar).
        inf.palabras = compilar_capitulo.contar_palabras(comun.CITA_HECHOS.sub("", cuerpo))
        inf.ejemplos = len(comun.MARCA_EJEMPLO.findall(cuerpo))
        if ejecutar:
            nuevo, errores = insertar_ejemplos.procesar(borrador)
            inf.ejemplos_mal = len(errores) or (1 if nuevo != borrador else 0)
        else:
            inf.ejemplos_sin_ejecutar = inf.ejemplos > 0

    carpeta = comun.INVESTIGACION / comun.carpeta_capitulo(numero)
    # El informe puede estar en revision.md o repartido en revision/*.md (un archivo por tramo).
    informes = [carpeta / "revision.md"] + sorted((carpeta / "revision").glob("*.md"))
    informes = [r for r in informes if r.exists()]
    if informes:
        inf.revision_existe = True
        texto = "\n".join(r.read_text(encoding="utf-8") for r in informes)
        for b in comun.leer_bloques(texto, "frase"):
            veredicto = b.get("veredicto").upper()
            resuelto = b.get("resuelto").lower() in ("sí", "si", "yes")
            if resuelto or veredicto == "SOPORTADA":
                continue
            if veredicto == "SIN HECHO":
                inf.sin_hecho += 1
            else:
                inf.no_soportadas += 1
    return inf


def guardar(informe: Informe, estado: Path = comun.ESTADO) -> None:
    texto = estado.read_text(encoding="utf-8")
    inicio = f"<!-- informe:cap-{informe.capitulo:02d} -->"
    fin = f"<!-- /informe:cap-{informe.capitulo:02d} -->"
    bloque = f"{inicio}\n{informe.markdown()}\n{fin}"
    if inicio in texto and fin in texto:
        texto = re.sub(re.escape(inicio) + r".*?" + re.escape(fin), lambda _: bloque, texto, flags=re.DOTALL)
    else:
        texto = texto.rstrip() + "\n\n" + bloque + "\n"
    estado.write_text(texto, encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("capitulo", type=int)
    p.add_argument("--guardar", action="store_true", help="guarda el informe en docs/estado.md")
    p.add_argument("--sin-ejecutar", action="store_true", help="no ejecuta los ejemplos")
    args = p.parse_args(argv)
    inf = generar(args.capitulo, ejecutar=not args.sin_ejecutar)
    print(inf.markdown())
    if args.guardar:
        guardar(inf)
        print("\nGuardado en docs/estado.md")
    return 0 if inf.puede_pasar_a_revisado else 1


if __name__ == "__main__":
    sys.exit(main())

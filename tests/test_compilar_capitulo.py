import datetime as dt
import re

import pytest

import comun
import compilar_capitulo as cc
import validar_contrato

BORRADOR = """---
id: base/git-modelo
parte: 1
capitulo: 1
titulo: Git por dentro
estado: borrador
actualizado: 2026-01-01
palabras: 0
versiones:
  git: "2.47"
---
# Capítulo 1. Git por dentro

Una rama es un puntero [h01-002]. Un commit es una foto [h01-001, h01-003].

<!-- ejemplo: ejemplos/cap-01/a.py -->
```python
print("[h01-009]")
```
<!-- /ejemplo -->

Otra vez [h01-002].
"""

HECHOS = [
    comun.Bloque({"id": "h01-001", "fuente": "f01-01", "consultada": "2026-11-10"}, None, 1),
    comun.Bloque({"id": "h01-002", "fuente": "f01-02", "consultada": "2026-11-12"}, None, 2),
    comun.Bloque({"id": "h01-003", "fuente": "f01-01", "consultada": "2026-11-12"}, None, 3),
]
FUENTES = {"f01-01": {"titulo": "Pro Git 1.3", "url": "https://a"},
           "f01-02": {"titulo": "Pro Git 3.1", "url": "https://b"}}


def test_compila_referencias_fuentes_y_cabecera():
    salida = cc.compilar(1, BORRADOR, HECHOS, FUENTES, hoy=dt.date(2026, 11, 12))
    datos, cuerpo = comun.leer_frontmatter(salida)
    assert "Una rama es un puntero [1]. Un commit es una foto [2]." in cuerpo
    assert "Otra vez [1]." in cuerpo
    assert 'print("[h01-009]")' in cuerpo  # el código no se toca
    assert "<!--" not in cuerpo
    assert "[1] Pro Git 3.1. https://b (consultada 2026-11-12)" in cuerpo
    assert "[2] Pro Git 1.3. https://a (consultada 2026-11-12)" in cuerpo
    assert datos["actualizado"] == dt.date(2026, 11, 12)
    assert datos["palabras"] > 10
    assert validar_contrato.validar_cuerpo("x.md", cuerpo) == []


@pytest.mark.parametrize("cambio, mensaje", [
    ("\n> PENDIENTE: falta algo\n", "PENDIENTES"),
    ("\n## Fuentes\n", "Fuentes"),
    ("\n<!-- ejemplo: ejemplos/cap-01/b.py -->\nTexto\n", "sin insertar"),
    ("\nAlgo [h01-050].\n", "inexistente"),
])
def test_se_niega_a_compilar(cambio, mensaje):
    with pytest.raises(cc.ErrorCompilacion, match=mensaje):
        cc.compilar(1, BORRADOR + cambio, HECHOS, FUENTES)


def test_contar_palabras_ignora_codigo():
    assert cc.contar_palabras("Hola mundo.\n```\nmuchas palabras aquí dentro\n```\n") == 2


def test_vista_previa_admite_pendientes():
    con_pendiente = BORRADOR + "\n> PENDIENTE: falta algo\n"
    with pytest.raises(cc.ErrorCompilacion, match="PENDIENTES"):
        cc.compilar(1, con_pendiente, HECHOS, FUENTES)
    salida = cc.compilar(1, con_pendiente, HECHOS, FUENTES, permitir_pendientes=True)
    assert "> PENDIENTE: falta algo" in salida


def test_palabras_de_cabecera_no_cuentan_referencias_ni_fuentes():
    salida = cc.compilar(1, BORRADOR, HECHOS, FUENTES, hoy=dt.date(2026, 11, 12))
    datos, cuerpo = comun.leer_frontmatter(salida)
    sin_fuentes = cuerpo.split("## Fuentes")[0]
    assert datos["palabras"] == cc.contar_palabras(re.sub(r"\[\d+(?:, \d+)*\]", "", sin_fuentes))

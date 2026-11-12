from conftest import URL, anadir_hecho

import verificar_evidencias


def verificar(p):
    return verificar_evidencias.verificar(1, p["investigacion"], p["cache"], p["indice"])


def hecho(hid="h01-002", evidencia="apuntando a una de esas confirmaciones", fuente="f01-01",
          ancla=URL, consultada="2026-11-12"):
    return (f"- id: {hid}\n  hecho: algo\n  evidencia: \"{evidencia}\"\n  fuente: {fuente}\n"
            f"  ancla: {ancla}\n  consultada: {consultada}\n")


def test_evidencia_literal_con_salto_de_linea_es_valida(proyecto):
    res = verificar(proyecto)
    assert res.ok, res.errores
    assert res.validos == ["h01-001"]


def test_comillas_tipograficas_se_normalizan(proyecto):
    anadir_hecho(proyecto, hecho(evidencia="Dice “hola” con comillas"))
    assert verificar(proyecto).ok


def test_evidencia_inventada_se_rechaza(proyecto):
    anadir_hecho(proyecto, hecho(evidencia="Una rama es una copia del proyecto"))
    res = verificar(proyecto)
    assert not res.ok
    assert "no aparece" in res.errores[0]


def test_evidencia_parafraseada_se_rechaza(proyecto):
    anadir_hecho(proyecto, hecho(evidencia="Una rama de Git es simplemente un apuntador móvil"))
    assert not verificar(proyecto).ok


def test_faltan_campos(proyecto):
    anadir_hecho(proyecto, "- id: h01-002\n  hecho: sin evidencia\n")
    assert "faltan campos" in verificar(proyecto).errores[0]


def test_id_de_otro_capitulo(proyecto):
    anadir_hecho(proyecto, hecho(hid="h02-001"))
    assert "formato" in verificar(proyecto).errores[0]


def test_id_repetido(proyecto):
    anadir_hecho(proyecto, hecho(hid="h01-001"))
    assert "repetido" in verificar(proyecto).errores[0]


def test_fecha_mal(proyecto):
    anadir_hecho(proyecto, hecho(consultada="12/11/2026"))
    assert "AAAA-MM-DD" in verificar(proyecto).errores[0]


def test_fuente_no_declarada(proyecto):
    anadir_hecho(proyecto, hecho(fuente="f01-09"))
    assert "fuentes.yaml" in verificar(proyecto).errores[0]


def test_ancla_de_otra_pagina(proyecto):
    anadir_hecho(proyecto, hecho(ancla="https://git-scm.com/book/es/v2/otra"))
    assert "ancla" in verificar(proyecto).errores[0]


def test_ancla_con_fragmento_es_valida(proyecto):
    anadir_hecho(proyecto, hecho(ancla=URL + "#_seccion"))
    assert verificar(proyecto).ok


def test_sin_copia_local(proyecto):
    (proyecto["cache"] / "cap-01" / "f01-01.md").unlink()
    assert "copia local" in verificar(proyecto).errores[0]


def test_url_no_autorizada(proyecto):
    proyecto["indice"].write_text("nada\n", encoding="utf-8")
    res = verificar(proyecto)
    assert any("03-indice-con-fuentes" in e for e in res.errores)

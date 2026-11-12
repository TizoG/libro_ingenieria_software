from conftest import URL, anadir_hecho

import comprobar_ids


def comprobar(p, texto):
    return comprobar_ids.comprobar(1, texto, p["investigacion"], p["cache"], p["indice"])


def test_ids_correctos(proyecto):
    assert comprobar(proyecto, "Una rama es un puntero [h01-001].").ok


def test_id_inexistente(proyecto):
    res = comprobar(proyecto, "Algo [h01-001, h01-099].")
    assert res.inexistentes == ["h01-099"]


def test_id_con_evidencia_rechazada(proyecto):
    anadir_hecho(proyecto, f'- id: h01-002\n  hecho: x\n  evidencia: "inventada"\n  fuente: f01-01\n'
                           f"  ancla: {URL}\n  consultada: 2026-11-12\n")
    res = comprobar(proyecto, "Algo [h01-002].")
    assert res.rechazados == ["h01-002"]


def test_ids_en_codigo_no_cuentan(proyecto):
    assert comprobar(proyecto, "```\n[h01-077]\n```\n").citados == []

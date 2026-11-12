import comprobar_enlaces as ce


def test_ancla_github():
    assert ce.ancla_github("10.1 Modelo mental: el bucle de eventos") == "101-modelo-mental-el-bucle-de-eventos"
    assert ce.ancla_github("1.4 Las ramas son `punteros`") == "14-las-ramas-son-punteros"
    assert ce.ancla_github("¿Qué es una rama?") == "qué-es-una-rama"


def test_enlaces_relativos_y_externos(tmp_path):
    (tmp_path / "otro.md").write_text("# Uno\n\n## Dos dos\n", encoding="utf-8")
    doc = tmp_path / "doc.md"
    doc.write_text(
        "[a](otro.md#dos-dos) [b](otro.md#tres) [c](falta.md) [d](https://ok.org/x) "
        "[e](https://malo.org) [f](#local)\n\n# Local\n\n```\n[g](no-cuenta.md)\n```\n",
        encoding="utf-8")
    errores = ce.comprobar_archivo(doc, {"https://ok.org/x"})
    assert len(errores) == 3
    assert any("#tres" in e for e in errores)
    assert any("falta.md" in e for e in errores)
    assert any("malo.org" in e for e in errores)


def test_url_suelta_en_fuentes(tmp_path):
    doc = tmp_path / "d.md"
    doc.write_text("## Fuentes\n\n[1] Algo. https://no-autorizada.org/p (consultada 2026-11-12)\n", encoding="utf-8")
    assert len(ce.comprobar_archivo(doc, set())) == 1

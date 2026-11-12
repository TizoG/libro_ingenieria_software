import juntar_hechos


def test_junta_en_orden_numerico_y_detecta_repetidos(tmp_path):
    sec = tmp_path / "cap-01" / "secciones"
    sec.mkdir(parents=True)
    (sec / "1.10.md").write_text("## 1.10\n\n- id: h01-001\n  hecho: b\n", encoding="utf-8")
    (sec / "1.2.md").write_text("## 1.2\n\n- id: h01-201\n  hecho: a\n", encoding="utf-8")
    texto, errores = juntar_hechos.juntar(1, tmp_path)
    assert errores == []
    assert texto.index("## 1.2") < texto.index("## 1.10")
    assert texto.startswith("# Hechos del capítulo 1: Git por dentro")
    (sec / "1.3.md").write_text("- id: h01-201\n  hecho: c\n", encoding="utf-8")
    _, errores = juntar_hechos.juntar(1, tmp_path)
    assert errores == ["h01-201 repetido en 1.2.md y 1.3.md"]

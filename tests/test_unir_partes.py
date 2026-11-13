import unir_partes


def test_une_en_orden_numerico(tmp_path):
    carpeta = tmp_path / "cap-01" / "borrador-v2"
    carpeta.mkdir(parents=True)
    (carpeta / "parte-10.md").write_text("## diez\n", encoding="utf-8")
    (carpeta / "parte-2.md").write_text("## dos\n\n", encoding="utf-8")
    (carpeta / "parte-1.md").write_text("---\nid: x\n---\n# Cap\n", encoding="utf-8")
    texto = unir_partes.unir(1, tmp_path)
    assert texto == "---\nid: x\n---\n# Cap\n\n## dos\n\n## diez\n"

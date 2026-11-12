import informe_capitulo as ic


def test_parrafos_sin_id():
    cuerpo = (
        "## Lo que podrás hacer al terminar\n\n"
        "Un párrafo largo sin ids que no cuenta porque está en una sección que no lleva hechos.\n\n"
        "## 1.4 Las ramas son punteros\n\n"
        "Una rama es un puntero móvil que apunta a un commit concreto del historial siempre [h01-001].\n\n"
        "Una rama es un puntero móvil que apunta a un commit concreto del historial sin cita alguna.\n\n"
        "Corto sin id.\n"
    )
    assert ic.parrafos_sin_id(cuerpo) == 1


def test_markdown_y_bloqueo():
    inf = ic.Informe(1, revision_existe=True)
    assert inf.puede_pasar_a_revisado
    inf.no_soportadas = 1
    assert not inf.puede_pasar_a_revisado
    assert "| Frases NO SOPORTADAS o PARCIALES sin resolver | 1 | 0 |" in inf.markdown()


def test_sin_revision_no_pasa():
    assert not ic.Informe(1).puede_pasar_a_revisado


def test_guardar_reemplaza_el_bloque(tmp_path):
    estado = tmp_path / "estado.md"
    estado.write_text("# Estado\n", encoding="utf-8")
    ic.guardar(ic.Informe(1, palabras=10), estado)
    ic.guardar(ic.Informe(1, palabras=20), estado)
    texto = estado.read_text(encoding="utf-8")
    assert texto.count("<!-- informe:cap-01 -->") == 1
    assert "| Palabras | 20 |" in texto


def test_palabras_sin_ids():
    import comun, compilar_capitulo
    cuerpo = "Una rama es un puntero [h01-401, h01-402]."
    assert compilar_capitulo.contar_palabras(comun.CITA_HECHOS.sub("", cuerpo)) == 5

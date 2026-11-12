import comun


def test_leer_bloques_con_comillas_y_continuacion():
    texto = (
        "## 1.1 Sección\n\n"
        "- id: h01-001\n"
        '  hecho: Dice "algo" dentro\n'
        '  evidencia: "una cita con "comillas" internas"\n'
        "- id: h01-002\n"
        "  hecho: otro\n"
    )
    bloques = comun.leer_bloques(texto)
    assert [b.get("id") for b in bloques] == ["h01-001", "h01-002"]
    assert bloques[0].get("evidencia") == 'una cita con "comillas" internas'
    assert bloques[0].seccion == "1.1 Sección"
    assert bloques[0].get("hecho") == 'Dice "algo" dentro'


def test_continuacion_se_une_al_valor():
    b = comun.leer_bloques("- id: h01-001\n  hecho: primera\n    segunda\n")[0]
    assert b.get("hecho") == "primera segunda"


def test_normalizar_espacios_y_comillas():
    assert comun.normalizar("«hola»\n  “mundo”  ‘x’") == "\"hola\" \"mundo\" 'x'"


def test_normalizar_url_ignora_codificacion_fragmento_y_barra():
    a = "https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F#seccion"
    b = "https://git-scm.com/book/es/v2/Ramificaciones-en-Git-¿Qué-es-una-rama?"
    assert comun.normalizar_url(a) == comun.normalizar_url(b)
    assert comun.normalizar_url("https://x.org/a/") == comun.normalizar_url("https://x.org/a")


def test_catalogo_real_tiene_59_capitulos():
    caps = comun.leer_catalogo()
    assert len(caps) == 59
    assert [c.numero for c in caps] == list(range(1, 60))
    uno = caps[0]
    assert uno.id == "base/git-modelo"
    assert uno.archivo == "contenido/parte-01-base/cap-01-git-por-dentro.md"
    assert uno.parte == 1
    assert uno.secciones[3] == "1.4 Las ramas son punteros"
    assert caps[-1].parte == 9
    assert all(c.id and c.archivo and c.secciones for c in caps)


def test_indice_real_autoriza_pro_git():
    autorizadas = comun.urls_autorizadas()
    assert comun.normalizar_url("https://git-scm.com/book/es/v2/Los-entresijos-internos-de-Git-Los-objetos-Git") in autorizadas


def test_frontmatter_ida_y_vuelta():
    texto = comun.escribir_frontmatter({"id": "a/b", "parte": 1}, "cuerpo\n")
    datos, cuerpo = comun.leer_frontmatter(texto)
    assert datos == {"id": "a/b", "parte": 1}
    assert cuerpo == "cuerpo\n"


def test_ids_citados_y_codigo():
    texto = "Algo [h01-001]. Otro [h01-002, h01-003].\n```\n[h01-009]\n```\n"
    assert comun.ids_citados(comun.sin_bloques_de_codigo(texto)) == ["h01-001", "h01-002", "h01-003"]

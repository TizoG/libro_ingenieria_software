import detectar_copia as dc

FUENTE = {"f01-06": "Esta es una de las pocas áreas en las que Git puede perder parte de tu trabajo si cometes un error.\n"
                    "El directorio de trabajo es una copia de una versión del proyecto.\n"}


def buscar(cuerpo, minimo=8):
    return dc.buscar("---\nid: x\n---\n" + cuerpo, FUENTE, minimo)


def test_detecta_fragmento_literal_sin_comillas():
    r = buscar("Texto propio.\n\nDeshacer es una de las pocas áreas en las que Git puede perder parte de tu trabajo si te equivocas [h01-327].\n")
    assert len(r) == 1
    assert r[0].palabras == 17 and r[0].fuente == "f01-06" and not r[0].entre_comillas
    assert r[0].linea == 6
    assert r[0].texto.startswith("es una de las pocas áreas")


def test_texto_propio_no_avisa():
    assert buscar("Aquí sí puedes perder trabajo: un error en este rincón de Git no tiene vuelta atrás.\n") == []


def test_cita_corta_entre_comillas_se_permite_y_larga_no():
    corta = "Pro Git lo define así: «El directorio de trabajo es una copia de una versión del proyecto».\n"
    assert buscar(corta) == []
    larga = "Dice: «una de las pocas áreas en las que Git puede perder parte de tu trabajo si cometes un error».\n"
    r = buscar(larga)
    assert len(r) == 1 and r[0].entre_comillas and r[0].palabras >= 15


def test_ignora_codigo_ids_y_codigo_en_linea():
    cuerpo = ("```text\nEl directorio de trabajo es una copia de una versión del proyecto.\n```\n\n"
              "El directorio de trabajo es `una copia` de una versión del proyecto.\n")
    assert buscar(cuerpo) == []


def test_umbral_configurable():
    cuerpo = "Luego verás que es una copia de una versión cualquiera.\n"
    assert buscar(cuerpo, 8) == []
    assert len(buscar(cuerpo, 6)) == 1

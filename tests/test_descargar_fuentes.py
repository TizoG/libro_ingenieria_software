import descargar_fuentes as df


def test_extrae_contenido_principal_sin_indice_ni_navegacion():
    html = """<html><body><main><div id="content">
      <div id="book-chapters"><a>Chapters ▾</a><li>1.1 Otra cosa</li></div>
      <div id="main" class="book"><h2>¿Qué es una rama?</h2>
        <p>Una rama Git es <em>simplemente</em> un apuntador
           móvil, apuntando a <code>master</code>.</p>
        <div id="nav"><a>prev</a> | <a>next</a></div>
      </div></div></main></body></html>"""
    texto = df.extraer_texto(html)
    assert "Chapters" not in texto and "Otra cosa" not in texto and "prev" not in texto
    assert "¿Qué es una rama?\n" in texto
    assert "Una rama Git es simplemente un apuntador" in texto
    assert "móvil, apuntando a master." in texto


def test_sin_main_usa_body():
    assert df.extraer_texto("<html><body><p>Hola <b>mundo</b>.</p></body></html>") == "Hola mundo.\n"

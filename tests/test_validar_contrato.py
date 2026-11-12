import datetime as dt
from pathlib import Path

import comun
import validar_contrato as vc

CABECERA = """---
id: base/git-modelo
parte: 1
capitulo: 1
titulo: Git por dentro
estado: borrador
actualizado: 2026-11-12
palabras: 10
versiones:
  git: "2.47"
---
"""


def crear(contenido: Path, rel: str, texto: str) -> Path:
    ruta = contenido / rel
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(texto, encoding="utf-8")
    return ruta


def test_capitulo_correcto(tmp_path):
    r = crear(tmp_path, "parte-01-base/cap-01-git-por-dentro.md",
              CABECERA + "# Git\n\nTexto [1].\n\n> **Bajo el capó.** Algo [1, 2].\n\n## Fuentes\n\n[1] A. https://a\n[2] B. https://b\n")
    assert vc.validar([r], tmp_path) == []


def test_ruta_que_no_es_del_catalogo(tmp_path):
    r = crear(tmp_path, "parte-01-base/cap-01-otro-nombre.md", CABECERA)
    assert any("04-catalogo" in e for e in vc.validar([r], tmp_path))


def test_carpeta_de_parte_mal_numerada(tmp_path):
    r = crear(tmp_path, "parte-02-base/_parte.md", "---\nparte: 2\ntitulo: x\nestado: borrador\n---\n")
    assert any("carpeta de parte" in e for e in vc.validar([r], tmp_path))


def test_cabecera_incompleta_y_estado_invalido(tmp_path):
    r = crear(tmp_path, "parte-01-base/cap-01-git-por-dentro.md", "---\nid: base/git-modelo\nestado: listo\n---\n")
    errores = vc.validar([r], tmp_path)
    assert any("«palabras»" in e for e in errores)
    assert any("«estado»" in e for e in errores)


def test_capitulo_e_id_incorrectos(tmp_path):
    cab = CABECERA.replace("capitulo: 1", "capitulo: 2").replace("base/git-modelo", "base/otro")
    r = crear(tmp_path, "parte-01-base/cap-01-git-por-dentro.md", cab)
    errores = vc.validar([r], tmp_path)
    assert any("«capitulo»" in e for e in errores) and any("«id»" in e for e in errores)


def test_sin_cabecera(tmp_path):
    r = crear(tmp_path, "parte-01-base/soluciones.md", "# Soluciones\n")
    assert any("cabecera" in e for e in vc.validar([r], tmp_path))


def test_preliminares_no_exigen_cabecera(tmp_path):
    r = crear(tmp_path, "00-preliminares/prologo.md", "# Prólogo\n")
    assert vc.validar([r], tmp_path) == []


def test_html_prohibido_pero_comentarios_y_codigo_si():
    cuerpo = "<!-- nota -->\nTexto `<div>` y\n```html\n<p>ok</p>\n```\n<details>no</details>\n"
    errores = vc.validar_cuerpo("x.md", cuerpo)
    assert len(errores) == 2  # <details> y </details>
    assert all("HTML" in e for e in errores)


def test_recuadro_con_titulo_no_permitido():
    errores = vc.validar_cuerpo("x.md", "> **Consejo.** algo\n\n> **Error típico.** bien\n")
    assert len(errores) == 1 and "Consejo" in errores[0]


def test_marcas_internas():
    cuerpo = "Algo [h01-001].\n\n> PENDIENTE: falta hecho\n\n<!-- ejemplo: ejemplos/a.py -->\n"
    errores = vc.validar_cuerpo("x.md", cuerpo)
    assert len(errores) == 3


def test_referencia_sin_fuente():
    errores = vc.validar_cuerpo("x.md", "Uno [1] y dos [2].\n\n## Fuentes\n\n[1] A. https://a\n")
    assert errores == ["x.md: la referencia [2] no tiene línea en «## Fuentes»"]


def test_enlaces_markdown_no_son_referencias():
    assert vc.validar_cuerpo("x.md", "Mira [1](https://a) y la lista [ ] vacía.\n") == []


def test_contenido_real_cumple():
    archivos = [f for f in comun.CONTENIDO.rglob("*") if f.is_file() and f.name != ".gitkeep"]
    assert vc.validar(archivos) == []

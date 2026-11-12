import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

URL = "https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%c2%bfQu%c3%a9-es-una-rama%3F"


@pytest.fixture
def proyecto(tmp_path):
    """Un mini proyecto con índice de fuentes, fuentes.yaml, copia local y hechos del capítulo 1."""
    indice = tmp_path / "indice.md"
    indice.write_text(f"| 1.4 | [Pro Git 3.1]({URL}) |\n", encoding="utf-8")
    inv = tmp_path / "investigacion" / "cap-01"
    inv.mkdir(parents=True)
    (inv / "fuentes.yaml").write_text(
        f'f01-01:\n  titulo: "Pro Git 3.1, ¿Qué es una rama?"\n  url: {URL}\n', encoding="utf-8")
    cache = tmp_path / "fuentes-cache" / "cap-01"
    cache.mkdir(parents=True)
    (cache / "f01-01.md").write_text(
        "---\nfuente: f01-01\nurl: x\n---\n"
        "Una rama Git es simplemente un apuntador móvil\napuntando a una de esas confirmaciones.\n"
        "Dice «hola» con comillas.\n", encoding="utf-8")
    (inv / "hechos.md").write_text(
        "## 1.4 Las ramas son punteros\n\n"
        "- id: h01-001\n"
        "  hecho: Una rama es un puntero móvil a un commit.\n"
        '  evidencia: "Una rama Git es simplemente un apuntador móvil apuntando"\n'
        "  fuente: f01-01\n"
        f"  ancla: {URL}\n"
        "  consultada: 2026-11-12\n", encoding="utf-8")
    return {
        "raiz": tmp_path, "indice": indice, "investigacion": tmp_path / "investigacion",
        "cache": tmp_path / "fuentes-cache", "hechos": inv / "hechos.md", "inv": inv,
    }


def anadir_hecho(proyecto, texto):
    with proyecto["hechos"].open("a", encoding="utf-8") as f:
        f.write("\n" + texto)

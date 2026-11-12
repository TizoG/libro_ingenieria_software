"""Utilidades compartidas por los scripts de verificación del libro.

Rutas del proyecto, lectura de la cabecera YAML, lectura de los bloques
«clave: valor» de hechos.md y revision.md, normalización de texto para
comparar evidencias y lectura del catálogo y del índice de fuentes.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote, urldefrag

import yaml

RAIZ = Path(__file__).resolve().parent.parent
DOCS = RAIZ / "docs"
CONTENIDO = RAIZ / "contenido"
INVESTIGACION = RAIZ / "investigacion"
FUENTES_CACHE = RAIZ / "fuentes-cache"
EJEMPLOS = RAIZ / "ejemplos"
INDICE_FUENTES = DOCS / "03-indice-con-fuentes.md"
CATALOGO = DOCS / "04-catalogo-capitulos.md"
ESTADO = DOCS / "estado.md"

ID_HECHO = re.compile(r"\bh(\d{2})-(\d{3})\b")
CITA_HECHOS = re.compile(r"\[(h\d{2}-\d{3}(?:\s*,\s*h\d{2}-\d{3})*)\]")
MARCA_EJEMPLO = re.compile(r"<!--\s*ejemplo:\s*(?P<ruta>[^|>]+?)\s*(?:\|\s*(?P<opciones>[^>]*?))?\s*-->")
FIN_EJEMPLO = "<!-- /ejemplo -->"
PENDIENTE = re.compile(r"^\s*>\s*PENDIENTE\b", re.MULTILINE)
RECUADROS = ("Bajo el capó", "Error típico", "En un proyecto real", "Ojo con la versión")


def carpeta_capitulo(numero: int) -> str:
    """Nombre de carpeta de un capítulo dentro de investigacion/, ejemplos/ y fuentes-cache/."""
    return f"cap-{numero:02d}"


# --- Cabecera YAML -----------------------------------------------------------

def leer_frontmatter(texto: str) -> tuple[dict | None, str]:
    """Separa la cabecera YAML del cuerpo. Devuelve (None, texto) si no hay cabecera."""
    if not texto.startswith("---\n"):
        return None, texto
    fin = texto.find("\n---\n", 4)
    if fin == -1:
        return None, texto
    datos = yaml.safe_load(texto[4:fin]) or {}
    if not isinstance(datos, dict):
        return None, texto
    return datos, texto[fin + 5:]


def escribir_frontmatter(datos: dict, cuerpo: str) -> str:
    cabecera = yaml.safe_dump(datos, allow_unicode=True, sort_keys=False).strip()
    return f"---\n{cabecera}\n---\n{cuerpo}"


# --- Bloques «clave: valor» -------------------------------------------------

@dataclass
class Bloque:
    """Un elemento de lista con campos, como los hechos de hechos.md."""

    campos: dict[str, str]
    seccion: str | None
    linea: int

    def get(self, clave: str, defecto: str = "") -> str:
        return self.campos.get(clave, defecto)


def _quitar_comillas(valor: str) -> str:
    valor = valor.strip()
    if len(valor) >= 2 and valor[0] == valor[-1] and valor[0] in "\"'":
        return valor[1:-1]
    return valor


def leer_bloques(texto: str, primera_clave: str = "id") -> list[Bloque]:
    """Lee bloques con este formato (sin depender de YAML, para tolerar comillas):

        ## 10.1 Sección
        - id: h10-003
          hecho: ...
          evidencia: "..."

    Un bloque empieza en «- <primera_clave>:». Las líneas sangradas sin «clave:»
    continúan el valor anterior.
    """
    bloques: list[Bloque] = []
    seccion: str | None = None
    actual: Bloque | None = None
    ultima_clave: str | None = None
    inicio = re.compile(rf"^-\s+{re.escape(primera_clave)}:\s*(.*)$")
    campo = re.compile(r"^\s+([a-záéíóúñ_]+):\s?(.*)$")

    for n, linea in enumerate(texto.splitlines(), start=1):
        if linea.startswith("#"):
            seccion = linea.lstrip("#").strip()
            actual = None
            continue
        m = inicio.match(linea)
        if m:
            actual = Bloque({primera_clave: m.group(1).strip()}, seccion, n)
            bloques.append(actual)
            ultima_clave = primera_clave
            continue
        if actual is None:
            continue
        if not linea.strip():
            continue
        m = campo.match(linea)
        if m:
            ultima_clave = m.group(1)
            actual.campos[ultima_clave] = m.group(2)
        elif linea.startswith((" ", "\t")) and ultima_clave:
            actual.campos[ultima_clave] += " " + linea.strip()
        else:
            actual = None

    for b in bloques:
        b.campos = {k: _quitar_comillas(v) for k, v in b.campos.items()}
    return bloques


# --- Normalización para comparar evidencias ----------------------------------

_COMILLAS = str.maketrans({
    "“": '"', "”": '"', "„": '"', "«": '"', "»": '"',
    "‘": "'", "’": "'", "‚": "'", "′": "'", "´": "'",
})


def normalizar(texto: str) -> str:
    """Solo normaliza espacios y comillas, como exige el cortafuegos 2."""
    texto = unicodedata.normalize("NFC", texto).translate(_COMILLAS)
    return re.sub(r"\s+", " ", texto).strip()


# --- Fuentes -------------------------------------------------------------------

def normalizar_url(url: str) -> str:
    """Forma comparable de una URL: sin fragmento, decodificada, en minúsculas y sin barra final."""
    sin_fragmento, _ = urldefrag(url.strip())
    return unquote(sin_fragmento).lower().rstrip("/")


def urls_autorizadas(indice: Path = INDICE_FUENTES) -> set[str]:
    """URLs que aparecen en docs/03-indice-con-fuentes.md, normalizadas."""
    texto = indice.read_text(encoding="utf-8")
    return {normalizar_url(u) for u in re.findall(r"https?://[^\s)\]>|]+", texto)}


def leer_fuentes_capitulo(numero: int, base: Path = INVESTIGACION) -> dict[str, dict]:
    """Lee investigacion/cap-XX/fuentes.yaml: {id: {url, titulo, ...}}."""
    ruta = base / carpeta_capitulo(numero) / "fuentes.yaml"
    if not ruta.exists():
        return {}
    datos = yaml.safe_load(ruta.read_text(encoding="utf-8")) or {}
    return {str(k): v for k, v in datos.items()}


def ruta_cache(numero: int, fuente: str, base: Path = FUENTES_CACHE) -> Path:
    return base / carpeta_capitulo(numero) / f"{fuente}.md"


def leer_cache(ruta: Path) -> tuple[dict, str]:
    datos, cuerpo = leer_frontmatter(ruta.read_text(encoding="utf-8"))
    return datos or {}, cuerpo


# --- Catálogo -----------------------------------------------------------------

@dataclass
class Capitulo:
    numero: int
    titulo: str
    id: str
    archivo: str
    parte: int
    secciones: list[str] = field(default_factory=list)


def leer_catalogo(catalogo: Path = CATALOGO) -> list[Capitulo]:
    texto = catalogo.read_text(encoding="utf-8")
    capitulos: list[Capitulo] = []
    parte = 0
    actual: Capitulo | None = None
    for linea in texto.splitlines():
        if linea.startswith("## Parte "):
            parte += 1
            continue
        m = re.match(r"^### Capítulo (\d+)\. (.+)$", linea)
        if m:
            actual = Capitulo(int(m.group(1)), m.group(2).strip(), "", "", parte)
            capitulos.append(actual)
            continue
        if actual is None:
            continue
        m = re.match(r"^\| (id|Archivo|Secciones) \| (.+) \|$", linea)
        if not m:
            continue
        clave, valor = m.groups()
        if clave == "id":
            actual.id = valor.strip("` ")
        elif clave == "Archivo":
            actual.archivo = valor.strip("` ")
        else:
            actual.secciones = [s.strip() for s in valor.split("<br>") if s.strip()]
    return capitulos


def capitulo_por_numero(numero: int) -> Capitulo:
    for cap in leer_catalogo():
        if cap.numero == numero:
            return cap
    raise SystemExit(f"El capítulo {numero} no está en el catálogo.")


# --- Hechos -------------------------------------------------------------------

def leer_hechos(numero: int, base: Path = INVESTIGACION) -> list[Bloque]:
    ruta = base / carpeta_capitulo(numero) / "hechos.md"
    if not ruta.exists():
        return []
    return leer_bloques(ruta.read_text(encoding="utf-8"), "id")


def ids_citados(texto: str) -> list[str]:
    """Ids de hechos citados como [h01-003] o [h01-003, h01-004]."""
    ids: list[str] = []
    for grupo in CITA_HECHOS.findall(texto):
        ids.extend(i.strip() for i in grupo.split(","))
    return ids


def sin_bloques_de_codigo(texto: str) -> str:
    """Sustituye el contenido de los bloques de código por líneas vacías (conserva la numeración)."""
    salida, dentro, valla = [], False, ""
    for linea in texto.splitlines():
        m = re.match(r"^\s*(```+|~~~+)", linea)
        if m and (not dentro or m.group(1).startswith(valla)):
            dentro, valla = (not dentro), m.group(1)
            salida.append("")
            continue
        salida.append("" if dentro else linea)
    return "\n".join(salida)

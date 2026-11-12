import insertar_ejemplos as ie
import comun


def escribir(tmp_path, nombre, codigo):
    ruta = tmp_path / "ejemplos" / "cap-01" / nombre
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(codigo, encoding="utf-8")
    return f"ejemplos/cap-01/{nombre}"


def test_python_inserta_codigo_y_salida_real(tmp_path):
    rel = escribir(tmp_path, "suma.py", "print(2 + 3)\n")
    texto, errores = ie.procesar(f"Antes\n<!-- ejemplo: {rel} -->\nDespués\n", tmp_path)
    assert errores == []
    assert "```python\n# Ejecutado con Python 3." in texto
    assert "print(2 + 3)" in texto
    assert "```text\n5\n```" in texto
    assert texto.endswith(f"{comun.FIN_EJEMPLO}\nDespués\n")


def test_es_idempotente(tmp_path):
    rel = escribir(tmp_path, "suma.py", "print(2 + 3)\n")
    una, _ = ie.procesar(f"<!-- ejemplo: {rel} -->\n", tmp_path)
    dos, _ = ie.procesar(una, tmp_path)
    assert una == dos


def test_salida_editada_a_mano_se_sobrescribe(tmp_path):
    rel = escribir(tmp_path, "suma.py", "print(2 + 3)\n")
    una, _ = ie.procesar(f"<!-- ejemplo: {rel} -->\n", tmp_path)
    trucada = una.replace("```text\n5\n```", "```text\n6\n```")
    dos, _ = ie.procesar(trucada, tmp_path)
    assert dos == una


def test_ejemplo_que_falla_es_error(tmp_path):
    rel = escribir(tmp_path, "mal.py", "1 / 0\n")
    _, errores = ie.procesar(f"<!-- ejemplo: {rel} -->\n", tmp_path)
    assert len(errores) == 1 and "ZeroDivisionError" in errores[0]


def test_fallo_esperado(tmp_path):
    rel = escribir(tmp_path, "mal.py", "1 / 0\n")
    texto, errores = ie.procesar(f"<!-- ejemplo: {rel} | falla -->\n", tmp_path)
    assert errores == []
    assert "ZeroDivisionError: division by zero" in texto
    assert "/tmp/ejemplo" in texto or "mal.py" in texto


def test_fallo_esperado_que_no_falla_es_error(tmp_path):
    rel = escribir(tmp_path, "bien.py", "print(1)\n")
    _, errores = ie.procesar(f"<!-- ejemplo: {rel} | falla -->\n", tmp_path)
    assert "debía fallar" in errores[0]


def test_archivo_inexistente(tmp_path):
    _, errores = ie.procesar("<!-- ejemplo: ejemplos/no.py -->\n", tmp_path)
    assert "no existe" in errores[0]


def test_shell_git_reproducible_con_fallo_marcado(tmp_path):
    codigo = (
        "# versiones: git\n"
        "# Cabecera que no se muestra\n\n"
        "git init -q\n\n"
        "echo hola > a.txt\n\n"
        "git add a.txt\n\n"
        "git commit -q -m 'Primer commit'\n\n"
        "git log --format='%h %s'\n\n"
        "git checkout rama-que-no-existe  # falla\n"
    )
    rel = escribir(tmp_path, "sesion.sh", codigo)
    una, errores = ie.procesar(f"<!-- ejemplo: {rel} -->\n", tmp_path)
    assert errores == [], errores
    assert "```console\n# Ejecutado con Bash" in una and "Git 2." in una
    assert "$ git log --format='%h %s'\n" in una
    assert "Primer commit" in una
    assert "# falla" not in una
    assert "Cabecera" not in una
    dos, _ = ie.procesar(una, tmp_path)
    assert una == dos  # mismo hash en cada ejecución


def test_shell_fallo_no_marcado(tmp_path):
    rel = escribir(tmp_path, "s.sh", "false\n\necho no-llega\n")
    _, errores = ie.procesar(f"<!-- ejemplo: {rel} -->\n", tmp_path)
    assert "«false» falló" in errores[0]


def test_shell_grupo_multilinea(tmp_path):
    rel = escribir(tmp_path, "s.sh", "for i in 1 2; do\n  echo $i\ndone\n")
    texto, errores = ie.procesar(f"<!-- ejemplo: {rel} -->\n", tmp_path)
    assert errores == []
    assert "$ for i in 1 2; do\n>   echo $i\n> done\n1\n2\n" in texto


def test_quitar_marcas(tmp_path):
    rel = escribir(tmp_path, "suma.py", "print(1)\n")
    texto, _ = ie.procesar(f"A\n\n<!-- ejemplo: {rel} -->\n\nB\n", tmp_path)
    limpio = ie.quitar_marcas(texto)
    assert "<!--" not in limpio
    assert "```text\n1\n```" in limpio

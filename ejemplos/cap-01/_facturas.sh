# Ayudas comunes del capítulo 1: montan el repositorio «facturas» en el estado
# que necesita cada ejemplo. No es un ejemplo: se carga con
#   source "$EJEMPLO_DIR/_facturas.sh"  # preparación
#
# Todas las funciones trabajan en la carpeta actual, crean ./facturas y se
# quedan dentro de ella. Los commits salen con autor y fecha fijos (los fija
# insertar_ejemplos.py), así que todos tienen la misma fecha y cada commit
# cambia contenido o mensaje: si no, dos commits con el mismo padre, árbol y
# mensaje tendrían el mismo hash.

# --- Contenido de los archivos -------------------------------------------

# Versión 1: IVA del 20 %.
f_factura_v1() { cat > factura.py <<'EOF'
IVA = 0.20
def total(base, iva=IVA):
    """Calcula el total de una factura."""
    return base * (1 + iva)
EOF
}

# Versión 2: IVA del 21 %.
f_factura_v2() { cat > factura.py <<'EOF'
IVA = 0.21
def total(base, iva=IVA):
    """Calcula el total de una factura."""
    return base * (1 + iva)
EOF
}

# Versión 3: versión 2 con el total redondeado.
f_factura_v3() { cat > factura.py <<'EOF'
IVA = 0.21
def total(base, iva=IVA):
    """Calcula el total de una factura."""
    return round(base * (1 + iva), 2)
EOF
}

# Versión de la rama «descuentos»: versión 2 con descuento (choca con v3).
f_factura_descuento() { cat > factura.py <<'EOF'
IVA = 0.21
def total(base, iva=IVA, descuento=0):
    """Calcula el total de una factura."""
    return base * (1 + iva) * (1 - descuento)
EOF
}

# --- Commits -------------------------------------------------------------

f_commit() { git add -A && git commit -q -m "$1"; }

# Los cinco commits de la rama principal, en orden.
f_c_primera() {
    printf '# facturas\n\nCalcula el total de una factura con IVA.\n' > README.md
    printf '__pycache__/\n*.pyc\n' > .gitignore
    f_factura_v1
    f_commit "Primera versión de la factura"
}
f_c_readme() {
    printf 'Uso: from factura import total; total(100)\n' >> README.md
    f_commit "Añade un ejemplo de uso al README"
}
f_c_iva() {
    f_factura_v2
    f_commit "Cambia el tipo de IVA al 21 %"
}
# Si FACTURAS_AUTOR_TESTS tiene valor, ese nombre es el autor del commit
# (el confirmador sigue siendo devOC).
f_c_tests() {
    mkdir -p tests
    cat > tests/test_factura.py <<'EOF'
from factura import total
def test_total_con_iva_general():
    assert total(100) == 121.0
EOF
    if [ -n "$FACTURAS_AUTOR_TESTS" ]; then
        GIT_AUTHOR_NAME="$FACTURAS_AUTOR_TESTS" GIT_AUTHOR_EMAIL="marta@ejemplo.dev" f_commit "Añade tests de total"
    else
        f_commit "Añade tests de total"
    fi
}
f_c_readme_iva() {
    printf 'El IVA general es del 21 %%.\n' >> README.md
    f_commit "Documenta el IVA en el README"
}
f_c_redondeo() {
    f_factura_v3
    f_commit "Redondea el total a dos decimales"
}

# --- Repositorios --------------------------------------------------------

# facturas_nueva: carpeta facturas con un repositorio vacío, y entra en ella.
facturas_nueva() {
    mkdir facturas && cd facturas && git init -q
}

# facturas_historial N: los N primeros commits de la rama principal (1 a 5).
facturas_historial() {
    facturas_nueva || return 1
    local pasos=(f_c_primera f_c_readme f_c_iva f_c_tests f_c_readme_iva)
    local i
    for ((i = 0; i < $1; i++)); do
        ${pasos[i]} || return 1
    done
}

# --- Rama exportar-csv (secciones 1.5) -----------------------------------

f_e_exportar() {
    cat > exportar.py <<'EOF'
from factura import total
def a_csv(base):
    return f"{base},{total(base)}"
EOF
    f_commit "Añade exportación a CSV"
}
f_e_wip() {
    echo "pendiente: separador configurable" > notas.txt
    f_commit "WIP"
}
# f_e_cabecera "mensaje": añade la cabecera al CSV.
f_e_cabecera() {
    cat > exportar.py <<'EOF'
from factura import total
def a_csv(base):
    return "base,total\n" + f"{base},{total(base)}"
EOF
    f_commit "$1"
}
f_e_prueba() {
    echo "# probando otro formato" > prueba.py
    f_commit "Prueba descartada"
}

# facturas_divergentes: tres commits en main y dos en exportar-csv que salen
# del tercero; main avanza con un cuarto commit. Termina en main.
facturas_divergentes() {
    facturas_historial 3 || return 1
    git switch -q -c exportar-csv || return 1
    f_e_exportar || return 1
    f_e_cabecera "Añade la cabecera al CSV" || return 1
    git switch -q main || return 1
    f_c_tests
}

# Ayudas comunes del capítulo 1: montan el repositorio «facturas» en el estado
# que necesita cada ejemplo. No es un ejemplo: se carga con
#   source "$EJEMPLO_DIR/_facturas.sh"  # preparación
#
# Todas las funciones trabajan en la carpeta actual, crean ./facturas y se
# quedan dentro de ella. Los commits salen con autor y fecha fijos (los fija
# insertar_ejemplos.py), así que todos tienen la misma fecha y cada commit
# cambia contenido o mensaje: si no, dos commits con el mismo padre, árbol y
# mensaje tendrían el mismo hash.
#
# Marta Ruiz es siempre la autora del commit «Añade tests de total» (el
# confirmador sigue siendo devOC).

# Otra fecha de confirmación, solo para los rebases. Con autor, confirmador y
# fecha fijos, un commit reaplicado sin cambios tendría el mismo hash aunque
# Git lo reescribiera. Con esta fecha en los rebases, que un hash se conserve
# prueba que Git no reescribió ese commit.
FACTURAS_FECHA_REBASE="2026-01-02T12:00:00+01:00"

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
# Autora: Marta Ruiz. Confirmador: devOC.
f_c_tests() {
    mkdir -p tests
    cat > tests/test_factura.py <<'EOF'
from factura import total
def test_total_con_iva_general():
    assert total(100) == 121.0
EOF
    GIT_AUTHOR_NAME="Marta Ruiz" GIT_AUTHOR_EMAIL="marta@ejemplo.dev" f_commit "Añade tests de total"
}
f_c_readme_iva() {
    printf 'El IVA general es del 21 %%.\n' >> README.md
    f_commit "Documenta el IVA en el README"
}
f_c_redondeo() {
    f_factura_v3
    f_commit "Redondea el total a dos decimales"
}
# Rama «descuentos» a partir del tercer commit, con un commit; termina en main.
f_r_descuentos() {
    git switch -q -c descuentos || return 1
    f_factura_descuento
    f_commit "Empieza los descuentos" || return 1
    git switch -q main
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

# --- Rama exportar-csv (secciones 1.5 y 1.7) -------------------------------

# Los cuatro commits de «El problema», sobre el tercer commit de main:
#   A: Añade exportación a CSV
#   B: Añade la cabecera al CSV (con un separador equivocado)
#   C: Corrige el separador de la cabecera (corrige B)
#   D: Prueba el formato con punto y coma (experimento que sobra)
f_e_exportar() {
    cat > exportar.py <<'EOF'
from factura import total
def a_csv(base):
    return f"{base},{total(base)}"
EOF
    f_commit "Añade exportación a CSV"
}
# B: cabecera con punto y coma, que no es el separador de las filas.
f_e_cabecera_mal() {
    cat > exportar.py <<'EOF'
from factura import total
def a_csv(base):
    return "base;total\n" + f"{base},{total(base)}"
EOF
    f_commit "Añade la cabecera al CSV"
}
# B': la cabecera ya correcta, con el mismo mensaje que B. Es el contenido que
# queda al fundir C en B, y el que usa facturas_divergentes.
f_e_cabecera() {
    cat > exportar.py <<'EOF'
from factura import total
def a_csv(base):
    return "base,total\n" + f"{base},{total(base)}"
EOF
    f_commit "Añade la cabecera al CSV"
}
# C: corrige el separador de la cabecera.
f_e_corrige() {
    cat > exportar.py <<'EOF'
from factura import total
def a_csv(base):
    return "base,total\n" + f"{base},{total(base)}"
EOF
    f_commit "Corrige el separador de la cabecera"
}
# D: experimento que sobra.
f_e_prueba() {
    cat > exportar.py <<'EOF'
from factura import total
def a_csv(base):
    return "base,total\n" + f"{base};{total(base)}"
EOF
    f_commit "Prueba el formato con punto y coma"
}

# facturas_exportar_csv: sobre un repositorio con tres commits, crea la rama
# exportar-csv con A, B, C y D y se queda en ella.
facturas_exportar_csv() {
    git switch -q -c exportar-csv || return 1
    f_e_exportar || return 1
    f_e_cabecera_mal || return 1
    f_e_corrige || return 1
    f_e_prueba
}

# facturas_asistente [rebase]: reproduce las órdenes del asistente de «El
# problema» sobre tres commits de main más los cuatro de exportar-csv:
#   1. git rebase -i HEAD~4 con fixup en la línea 3 y drop en la 4 (A se
#      conserva y B' es nuevo)
#   2. git reset --soft HEAD~2
#   3. git commit -m "Añade la exportación a CSV"
# Con el argumento «rebase» se detiene tras el paso 1 (rama con A y B').
# Crea el repositorio desde cero y termina en exportar-csv.
facturas_asistente() {
    facturas_historial 3 || return 1
    facturas_exportar_csv || return 1
    GIT_COMMITTER_DATE="$FACTURAS_FECHA_REBASE" \
        GIT_SEQUENCE_EDITOR="sed -i -e '3s/^pick/fixup/' -e '4s/^pick/drop/'" \
        git rebase -q -i HEAD~4 || return 1
    if [ "$1" = "rebase" ]; then
        return 0
    fi
    git reset -q --soft HEAD~2 || return 1
    git commit -q -m "Añade la exportación a CSV"
}

# facturas_divergentes: tres commits en main y dos en exportar-csv (A y B')
# que salen del tercero; main avanza con el cuarto commit (los tests de
# Marta). Termina en main.
facturas_divergentes() {
    facturas_historial 3 || return 1
    git switch -q -c exportar-csv || return 1
    f_e_exportar || return 1
    f_e_cabecera || return 1
    git switch -q main || return 1
    f_c_tests
}

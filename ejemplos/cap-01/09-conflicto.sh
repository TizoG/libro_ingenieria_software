# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_historial 3  # preparación

f_r_descuentos  # preparación

f_c_redondeo  # preparación

git log --oneline --graph --all

git merge descuentos  # falla

git status

cat factura.py

cat > factura.py <<'PY'
IVA = 0.21
def total(base, iva=IVA, descuento=0):
    """Calcula el total de una factura."""
    return round(base * (1 + iva) * (1 - descuento), 2)
PY

git add factura.py

git commit -m "Fusiona los descuentos con el redondeo"

git log --oneline --graph

git cat-file -p HEAD

git log --oneline -1 HEAD^2

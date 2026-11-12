# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_historial 3  # preparación

git switch -q -c descuentos  # preparación

f_factura_descuento  # preparación

f_commit "Aplica un descuento al total"  # preparación

git switch -q main  # preparación

f_c_redondeo  # preparación

git log --oneline --graph --all

git merge descuentos  # falla

git status

git merge --abort

git status -s

git merge descuentos  # falla

cat factura.py

cat > factura.py <<'PY'
IVA = 0.21
def total(base, iva=IVA, descuento=0):
    """Calcula el total de una factura."""
    return round(base * (1 + iva) * (1 - descuento), 2)
PY

git add factura.py

git commit --no-edit

git log --oneline --graph

git cat-file -p HEAD

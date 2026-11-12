# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_historial 3  # preparación

git branch descuentos

cat .git/refs/heads/main

cat .git/refs/heads/descuentos

cat .git/HEAD

git switch descuentos

cat .git/HEAD

f_factura_descuento  # preparación

git add factura.py

git commit -m "Empieza los descuentos"

git log --oneline --decorate --graph --all

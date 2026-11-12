# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_historial 3  # preparación

f_factura_v3  # preparación

git add factura.py

git commit -m "Cambia la función total"

git commit --amend -m "Redondea el total a dos decimales"

git cat-file -p HEAD

git cat-file -p HEAD@{1}

git reflog -2

# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_historial 3  # preparación

git switch -c redondeo

f_factura_v3  # preparación

git add factura.py

git commit -m "Redondea el total a dos decimales"

git switch main

git merge redondeo

git branch -d redondeo

git log --oneline --graph

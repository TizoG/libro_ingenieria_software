# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_historial 1  # preparación

f_c_iva  # preparación

f_c_redondeo  # preparación

git log --oneline

git reset --soft HEAD~

git status -s

git commit -q -m "Redondea el total"  # preparación

git reset HEAD~

git status -s

f_commit "Redondea el total a dos decimales"  # preparación

git reset --hard HEAD~

git status -s

cat factura.py

git log --oneline

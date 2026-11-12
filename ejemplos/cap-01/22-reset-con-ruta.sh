# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_historial 3  # preparación

f_c_redondeo  # preparación

git log --oneline

git reset HEAD~2 factura.py

git status -s

git restore --staged factura.py  # preparación

git restore --source=HEAD~2 --staged factura.py

git status -s

git log --oneline -1

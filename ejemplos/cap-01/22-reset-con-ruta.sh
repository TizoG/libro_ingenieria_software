# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_historial 1  # preparación

f_c_iva  # preparación

f_c_redondeo  # preparación

echo "IVA_REDUCIDO = 0.10" >> factura.py

git add factura.py

git reset factura.py

git status -s

git add factura.py

git restore --staged factura.py

git status -s

git reset HEAD~2 factura.py

git status -s

git log --oneline

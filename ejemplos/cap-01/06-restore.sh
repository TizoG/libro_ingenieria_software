# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_historial 3  # preparación

echo "IVA_REDUCIDO = 0.10" >> factura.py

git add factura.py

git status

git restore --staged factura.py

git status -s

git restore factura.py

git status -s

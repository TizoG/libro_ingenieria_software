# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_historial 4  # preparación

find .git/objects -type f | wc -l

cat .git/refs/heads/main

echo "def test_sin_iva():" >> tests/test_factura.py

echo "    assert total(100, iva=0) == 100" >> tests/test_factura.py

git add tests/test_factura.py

git commit -m "Prueba el total sin IVA"

find .git/objects -type f | wc -l

cat .git/refs/heads/main

git rev-list --objects HEAD~1..HEAD

# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_historial 3  # preparación

f_factura_v3  # preparación

mkdir tests  # preparación

printf 'from factura import total\ndef test_redondeo():\n    assert total(0.1) == 0.12\n' > tests/test_factura.py  # preparación

git add factura.py

git commit -m "Redondea el total y lo prueba"

git status -s

git log --oneline -1

git add tests/test_factura.py

git commit --amend --no-edit

git log --oneline

git reflog

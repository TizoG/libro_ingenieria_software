# versiones: git

git init facturas

cd facturas

echo "# facturas" > README.md

cat > factura.py <<'PY'
IVA = 0.20
def total(base, iva=IVA):
    return base * (1 + iva)
PY

git status -s

git add README.md

git status -s

git add factura.py

git commit -m "Primera versión de la factura"

echo "IVA_REDUCIDO = 0.10" >> factura.py

git status -s

git add factura.py

echo "IVA_SUPERREDUCIDO = 0.04" >> factura.py

git status -s

git diff

git diff --staged

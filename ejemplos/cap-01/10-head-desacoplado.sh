# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_historial 3  # preparación

git switch --detach HEAD~1

cat .git/HEAD

printf 'IVA_CANARIAS = 0.07\n' >> factura.py  # preparación

git add factura.py  # preparación

git commit -m "Experimento: IVA de Canarias"

git switch main

git log --oneline --all

git reflog -4

git branch experimento HEAD@{1}

git log --oneline --all

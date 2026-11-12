# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_asistente rebase  # preparación

inicio=$(git rev-parse HEAD)  # preparación

cat .git/HEAD

cat .git/refs/heads/exportar-csv

git reset --soft HEAD~2

cat .git/HEAD

cat .git/refs/heads/exportar-csv

git reset -q --hard "$inicio"  # preparación

git switch --detach HEAD~2

cat .git/HEAD

cat .git/refs/heads/exportar-csv

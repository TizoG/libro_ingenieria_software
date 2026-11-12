# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_asistente rebase  # preparación

inicio=$(git rev-parse HEAD)  # preparación

git log --oneline

git reset --soft HEAD~2

git status -s

ls

git reset -q --hard "$inicio"  # preparación

git reset HEAD~2

git status -s

ls

git reset -q --hard "$inicio"  # preparación

git reset --hard HEAD~2

git status -s

ls

# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_asistente rebase  # preparación

git log --oneline

git reset --soft HEAD~2

git status -s

git log --oneline

git commit -m "Añade la exportación a CSV"

git log --oneline

git reflog -3

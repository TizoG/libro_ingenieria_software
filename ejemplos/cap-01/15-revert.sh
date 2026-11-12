# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_historial 5  # preparación

git log --oneline

git revert --no-edit HEAD~2

git log --oneline

git log --stat -1

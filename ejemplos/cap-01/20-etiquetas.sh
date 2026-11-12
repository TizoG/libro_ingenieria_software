# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_historial 3  # preparación

git log --oneline

git tag v0.1 HEAD~2

git tag -a v1.0 -m "Primera versión estable"

cat .git/refs/tags/v0.1

cat .git/refs/tags/v1.0

git cat-file -t v0.1

git cat-file -t v1.0

git cat-file -p v1.0

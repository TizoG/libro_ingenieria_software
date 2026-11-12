# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

FACTURAS_AUTOR_TESTS="Marta Ruiz" facturas_historial 5  # preparación

git log --oneline

git log --stat -1

git log -S "0.21" --oneline

git log --oneline -- README.md

git log --format=fuller -1 HEAD~1

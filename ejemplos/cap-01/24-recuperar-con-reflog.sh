# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_asistente  # preparación

git log --oneline

git reflog exportar-csv

git branch rescate exportar-csv@{3}

git log --oneline -4 rescate

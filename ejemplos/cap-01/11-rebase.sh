# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_divergentes  # preparación

git switch exportar-csv

git log --oneline --graph --all

git rebase -q main

git log --oneline --graph --all

git switch main

git merge exportar-csv

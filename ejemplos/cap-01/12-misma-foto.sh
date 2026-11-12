# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_divergentes  # preparación

git branch con-merge exportar-csv  # preparación

git branch con-rebase exportar-csv  # preparación

git switch con-merge

git merge main -m "Integra main en con-merge"

git switch con-rebase

git rebase -q main

git diff con-merge con-rebase

git cat-file -p con-merge | head -n 1

git cat-file -p con-rebase | head -n 1

git log --oneline --graph con-merge

git log --oneline --graph con-rebase

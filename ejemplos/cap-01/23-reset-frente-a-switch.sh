# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_historial 3  # preparación

git switch -q -c develop  # preparación

f_c_tests  # preparación

inicio=$(git rev-parse develop)  # preparación

cat .git/HEAD

git log --oneline --all --decorate

git reset main

cat .git/HEAD

git log --oneline --all --decorate

git reset -q --hard "$inicio"  # preparación

git switch main

cat .git/HEAD

git log --oneline --all --decorate

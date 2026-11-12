# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_historial 3  # preparación

f_r_descuentos  # preparación

cat .git/refs/heads/main

cat .git/refs/heads/descuentos

git merge descuentos

cat .git/refs/heads/main

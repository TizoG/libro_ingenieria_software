# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_historial 1  # preparación

f_c_iva  # preparación

git log --oneline

git cat-file -p HEAD~1^{tree}

git cat-file -p HEAD^{tree}

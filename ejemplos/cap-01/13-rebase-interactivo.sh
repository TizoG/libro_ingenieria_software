# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_historial 3  # preparación

facturas_exportar_csv  # preparación

export GIT_COMMITTER_DATE="$FACTURAS_FECHA_REBASE"  # preparación

git log --oneline

GIT_SEQUENCE_EDITOR="grep '^[a-z]'" git rebase -q -i HEAD~4

git log --oneline

GIT_SEQUENCE_EDITOR="sed -i -e '3s/^pick/fixup/' -e '4s/^pick/drop/'" git rebase -q -i HEAD~4

git log --oneline

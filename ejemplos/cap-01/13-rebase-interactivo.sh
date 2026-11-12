# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_historial 1  # preparación

git switch -q -c exportar-csv  # preparación

f_e_exportar  # preparación

f_e_wip  # preparación

f_e_cabecera "oops, falta la cabecera"  # preparación

f_e_prueba  # preparación

git log --oneline

GIT_SEQUENCE_EDITOR="grep '^[a-z]'" git rebase -q -i HEAD~4

GIT_SEQUENCE_EDITOR="sed -i -e '2,3s/^pick/fixup/' -e '4s/^pick/drop/'" git rebase -q -i HEAD~4

git log --oneline

echo "def a_json(base): ..." > exportar_json.py  # preparación

git add exportar_json.py  # preparación

git commit -q -m "Exporta también a JSON"  # preparación

echo "# formato: base,total" >> exportar.py  # preparación

git add exportar.py  # preparación

git commit --fixup HEAD~1

git log --oneline -3

GIT_SEQUENCE_EDITOR="grep '^[a-z]'" git rebase -q -i --autosquash HEAD~3

git log --oneline -2

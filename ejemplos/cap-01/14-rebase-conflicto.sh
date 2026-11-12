# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_historial 3  # preparación

git switch -q -c exportar-csv  # preparación

f_e_exportar  # preparación

printf 'Exportar: python exportar.py\n' >> README.md  # preparación

f_commit "Documenta la exportación en el README"  # preparación

git switch -q main  # preparación

printf 'Tests: python -m pytest\n' >> README.md  # preparación

f_commit "Documenta cómo ejecutar los tests"  # preparación

git switch exportar-csv

git log --oneline --graph --all

git rebase main  # falla

git status

git rebase --abort

git log --oneline --graph --all

# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_historial 3  # preparación

cd ..  # preparación

cd facturas && git log --oneline

cd .. && git clone facturas copia

cd copia && git log --oneline

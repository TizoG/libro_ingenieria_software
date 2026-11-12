# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_historial 5  # preparación

git reset --hard HEAD~2

git log --oneline

git reflog

git branch recuperada HEAD@{1}

git log --oneline recuperada

git branch -D recuperada

rm -rf .git/logs

git fsck --full

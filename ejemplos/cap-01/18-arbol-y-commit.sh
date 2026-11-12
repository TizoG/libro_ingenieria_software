# versiones: git
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_historial 4  # preparación

cat .git/HEAD

cat .git/refs/heads/main

git cat-file -t $(cat .git/refs/heads/main)

git cat-file -p $(cat .git/refs/heads/main)

git cat-file -p HEAD^{tree}

git cat-file -p e11b3b861512536ee23c90a2742f7f968593a4a7

git cat-file -p 549689f79d442dbb2706af1b1c4bf69f0cbc3ef3

ls .git/objects/54

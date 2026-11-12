# versiones: git

git init facturas

cd facturas

ls .git

find .git/objects -type f

echo 'hola' | git hash-object -w --stdin

find .git/objects -type f

git cat-file -t 5c1b14949828006ed75a3e8858957f86a2f7e2eb

git cat-file -p 5c1b14949828006ed75a3e8858957f86a2f7e2eb

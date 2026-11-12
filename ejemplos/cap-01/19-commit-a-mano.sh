# versiones: git

git init facturas

cd facturas

echo "# facturas" > README.md

git add README.md

git write-tree

c1=$(git commit-tree $(git write-tree) -m "Primer commit a mano")

echo "$c1"

echo "Calcula el total de una factura con IVA." >> README.md

git add README.md

c2=$(git commit-tree $(git write-tree) -p $c1 -m "Segundo commit a mano")

echo "$c2"

git update-ref refs/heads/main $c2

git symbolic-ref HEAD

git log --oneline

git commit-tree $(git write-tree) -p $c1 -m "Segundo commit a mano"

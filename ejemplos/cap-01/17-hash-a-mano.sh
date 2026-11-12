# versiones: git, python
source "$EJEMPLO_DIR/_facturas.sh"  # preparación

facturas_historial 3  # preparación

git ls-tree HEAD factura.py

git hash-object factura.py

python3 - <<'PY'
import hashlib, zlib
contenido = open("factura.py", "rb").read()
cabecera = b"blob %d\0" % len(contenido)
hash_a_mano = hashlib.sha1(cabecera + contenido).hexdigest()
print("hash a mano:", hash_a_mano)
ruta = f".git/objects/{hash_a_mano[:2]}/{hash_a_mano[2:]}"
guardado = zlib.decompress(open(ruta, "rb").read())
print("cabecera guardada:", guardado.split(b"\0")[0])
print("contenido igual:", guardado == cabecera + contenido)
PY

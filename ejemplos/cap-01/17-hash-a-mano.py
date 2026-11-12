# versiones: git
import hashlib
import subprocess
import zlib

contenido = b"hola\n"
subprocess.run(["git", "init", "-q", "repo"], check=True)

cabecera = b"blob %d\0" % len(contenido)
a_mano = hashlib.sha1(cabecera + contenido).hexdigest()
git = subprocess.run(["git", "hash-object", "-w", "--stdin"], cwd="repo", input=contenido,
                     capture_output=True, check=True).stdout.decode().strip()
print("a mano:", a_mano)
print("git:   ", git)
print("iguales:", a_mano == git)

ruta = f"repo/.git/objects/{git[:2]}/{git[2:]}"
with open(ruta, "rb") as archivo:
    descomprimido = zlib.decompress(archivo.read())
print("archivo:", ruta)
print("contenido:", descomprimido)

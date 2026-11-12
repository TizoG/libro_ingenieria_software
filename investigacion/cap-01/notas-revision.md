# Notas para la pasada final y la revisión del capítulo 1

Cosas detectadas durante la redacción que no son PENDIENTES pero hay que mirar.

- **Hilo de `facturas` (1.3 frente a 1.5).** En la 1.3, el commit «Añade tests de total» es de Marta Ruiz (`795693a`); en los ejemplos 11, 12 y 15 lo crea devOC (`7971f23`) y el quinto commit del 15 es `9af4ac5`, no `938b805`. Decidir si se unifica el autor en `_facturas.sh` (cambian hashes citados en la prosa y diagramas de 1.5: `7971f23`, `649bb22`, `f8f6c01`, `4b2e63c`, `15aa51f`) o se acepta y se dice en el texto.
- **Ejemplo 13.** El commit «WIP» añade `notas.txt` y al fundirlo con `fixup` ese archivo queda en el commit «limpio». Revisar si conviene que el WIP no añada un archivo.
- **Esquema, 1.5.** `exec` no es nuevo (Pro Git en español ya lo lista); la lista de tareas del 13 se filtra con `grep` y no muestra los comandos.
- **Hashes en la prosa.** Están copiados de la salida real; si cambia un ejemplo o `_facturas.sh`, hay que revisarlos (insertar_ejemplos `--comprobar` no los detecta).
- **Extensión.** Tras 1.5 el cuerpo va por 7.240 (contador con ids); objetivo total ≤ 10.000 de prosa.

# Notas para la pasada final y la revisión del capítulo 1

**Pasada final (2026-11-12):** resueltos el hilo de autoría (frase en 1.3), la promesa de SHA-256 en 1.2, el commit que faltaba en «El problema», el PENDIENTE de packfiles (quitado) y la extensión (9.563 sin ids). Quedan abiertas las notas del cierre (ejercicios) para las soluciones y `_parte.md`, y el ejemplo 20, que ya no se usa.

Cosas detectadas durante la redacción que no son PENDIENTES pero hay que mirar.

- **Hilo de `facturas` (1.3 frente a 1.5).** En la 1.3, el commit «Añade tests de total» es de Marta Ruiz (`795693a`); en los ejemplos 11, 12 y 15 lo crea devOC (`7971f23`) y el quinto commit del 15 es `9af4ac5`, no `938b805`. Decidir si se unifica el autor en `_facturas.sh` (cambian hashes citados en la prosa y diagramas de 1.5: `7971f23`, `649bb22`, `f8f6c01`, `4b2e63c`, `15aa51f`) o se acepta y se dice en el texto.
- **Ejemplo 13.** El commit «WIP» añade `notas.txt` y al fundirlo con `fixup` ese archivo queda en el commit «limpio». Revisar si conviene que el WIP no añada un archivo.
- **Esquema, 1.5.** `exec` no es nuevo (Pro Git en español ya lo lista); la lista de tareas del 13 se filtra con `grep` y no muestra los comandos.
- **Hashes en la prosa.** Están copiados de la salida real; si cambia un ejemplo o `_facturas.sh`, hay que revisarlos (insertar_ejemplos `--comprobar` no los detecta).
- **Extensión.** Tras 1.5 el cuerpo va por 7.240 (contador con ids); objetivo total ≤ 10.000 de prosa.
- **1.2 → 1.6.** El «Ojo con la versión» de 1.2 promete contar «por qué se eligió SHA-256»; los hechos solo dicen por qué dejar SHA-1 y que SHA-256 se eligió entre candidatos. Cambiar 1.2 a «por qué Git busca un sucesor de SHA-1».
- **1.6, packfiles.** Hay un PENDIENTE sobre *packfiles*, pero la decisión 7 deja ese tema fuera. En la pasada final: quitarlo, o consultar a devOC si se da de alta Pro Git 10.4 para una sola frase.
- **Extensión tras 1.6:** 8.531 sin ids. Quedan 1.7 y el cierre; habrá que recortar en la pasada final (lista de recortes del esquema, decisión 9).
- **El problema (apertura) frente a 1.7.** El asistente da `rebase -i`, `reset --soft HEAD~2` y `push --force`, sin un `git commit` tras el reset; la 1.7 dice que el reset «era solo la primera mitad de aplastar». Añadir el commit a la lista de «El problema» o hacerlo explícito.
- **1.7, h01-732.** Se aplica por analogía al ejemplo 21 (misma forma que el de Pro Git). El revisor debe mirarlo.
- **Extensión tras 1.7:** 9.728 sin ids, sin el cierre. Hará falta recortar unas 1.000 palabras en la pasada final.
- **Cierre.** Ejercicio 3: el lector no tiene `facturas` montado (las soluciones deben decir cómo, o admitir cualquier repositorio). Ejercicio 4: volver al punto de partida exige reflog o rama de respaldo. Reto: solo funciona con objetos sueltos (sin explicar packfiles). Proyecto: clonar desde GitHub es del capítulo 2. Preguntas de defensa 2 y 6 quizá demasiado guiadas por el texto. Confirmar en `_parte.md` que la reimplementación del PR llega en el capítulo 5.
- **Extensión con el cierre:** 10.427 sin ids.

## Entrega a devOC (2026-11-13)

- El capítulo se entrega sin segunda revisión independiente, por decisión de devOC. Verificado por script: ids existentes, evidencias, 23 ejemplos ejecutados dos veces con salida idéntica, 16 diagramas renderizados, 0 fragmentos copiados de 8+ palabras, contrato con la web.
- No verificado por un revisor: que cada reformulación de los hallazgos de `revision-v1/` sostenga su hecho (lo afirman los redactores), la paráfrasis cercana y el calco de estructura.
- `soluciones.md` de la Parte I y `_parte.md` no existen aún; el ejercicio 3 y el proyecto los necesitan (montar `facturas`, capítulo 5).
- Frases que los redactores señalaron como deducciones: el tercer bloque de `diff3` en 1.4 (se deduce sin verlo en una salida), `21c1b83` en 1.2, y `git rev-list --objects` en 1.6 (se lee su salida sin hecho propio).
- Los ejemplos conservan los números 21 a 25 (faltan 19 y 20): renumerar es cosmético.

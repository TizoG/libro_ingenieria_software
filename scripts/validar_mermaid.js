#!/usr/bin/env node
// Valida (y renderiza) los bloques ```mermaid de uno o varios archivos Markdown.
//
// Uso:
//   npm install            (una vez: instala mermaid, fijado en package.json)
//   node scripts/validar_mermaid.js investigacion/cap-01/borrador.md
//   node scripts/validar_mermaid.js contenido
//
// Usa el Chromium de Playwright para ejecutar mermaid.render() sobre cada bloque.
// Sale con código 1 si algún diagrama no se puede renderizar.

const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");

const MERMAID = require.resolve("mermaid/dist/mermaid.min.js");

function archivos(rutas) {
  const lista = [];
  for (const r of rutas) {
    const st = fs.statSync(r);
    if (st.isDirectory()) {
      for (const f of fs.readdirSync(r, { recursive: true })) {
        if (String(f).endsWith(".md")) lista.push(path.join(r, String(f)));
      }
    } else lista.push(r);
  }
  return lista.sort();
}

function bloques(texto) {
  const res = [];
  const lineas = texto.split("\n");
  for (let i = 0; i < lineas.length; i++) {
    if (/^\s*```mermaid\s*$/.test(lineas[i])) {
      const inicio = i + 1;
      let j = inicio;
      while (j < lineas.length && !/^\s*```\s*$/.test(lineas[j])) j++;
      res.push({ linea: inicio, codigo: lineas.slice(inicio, j).join("\n") });
      i = j;
    }
  }
  return res;
}

(async () => {
  const rutas = process.argv.slice(2);
  if (!rutas.length) {
    console.error("Indica uno o varios archivos o carpetas.");
    process.exit(2);
  }
  const navegador = await chromium.launch();
  const pagina = await navegador.newPage();
  await pagina.setContent("<html><body></body></html>");
  await pagina.addScriptTag({ path: MERMAID });
  await pagina.evaluate(() => window.mermaid.initialize({ startOnLoad: false }));

  let total = 0;
  let errores = 0;
  for (const archivo of archivos(rutas)) {
    for (const b of bloques(fs.readFileSync(archivo, "utf8"))) {
      total++;
      const error = await pagina.evaluate(async ({ codigo, n }) => {
        try {
          await window.mermaid.render("d" + n, codigo);
          return null;
        } catch (e) {
          return String(e && e.message ? e.message : e).split("\n").slice(0, 4).join(" | ");
        }
      }, { codigo: b.codigo, n: total });
      if (error) {
        errores++;
        console.log(`  ROTO ${archivo}:${b.linea}: ${error}`);
      }
    }
  }
  await navegador.close();
  console.log(`${total} diagramas, ${errores} con errores`);
  process.exit(errores ? 1 : 0);
})();

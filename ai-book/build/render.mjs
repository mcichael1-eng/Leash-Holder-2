// Render many mermaid diagrams in one browser session.
// Usage: node render.mjs input.json output.json
// input: [{id, code}], output: {id: {svg} | {error}}
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import puppeteer from 'puppeteer';

const here = path.dirname(fileURLToPath(import.meta.url));
const [, , inFile, outFile] = process.argv;
const items = JSON.parse(fs.readFileSync(inFile, 'utf8'));
const mermaidJs = fs.readFileSync(path.join(here, 'node_modules/mermaid/dist/mermaid.min.js'), 'utf8');

// Light palette matching the book page (PCB green / gold contacts on cool paper).
const config = {
  startOnLoad: false,
  securityLevel: 'strict',
  theme: 'base',
  fontFamily: 'Archivo, "Helvetica Neue", Arial, sans-serif',
  flowchart: { htmlLabels: false, curve: 'basis', useMaxWidth: true, padding: 12 },
  sequence: { useMaxWidth: true },
  themeVariables: {
    fontFamily: 'Archivo, "Helvetica Neue", Arial, sans-serif',
    fontSize: '15px',
    background: '#ffffff',
    primaryColor: '#e3f1e8',
    primaryTextColor: '#17201c',
    primaryBorderColor: '#2f7d57',
    secondaryColor: '#fbf1d9',
    secondaryTextColor: '#17201c',
    secondaryBorderColor: '#b07d12',
    tertiaryColor: '#eef2ef',
    tertiaryTextColor: '#17201c',
    tertiaryBorderColor: '#8a9a91',
    lineColor: '#4d5c55',
    textColor: '#17201c',
    mainBkg: '#e3f1e8',
    nodeBorder: '#2f7d57',
    clusterBkg: '#f3f7f4',
    clusterBorder: '#a9bcb1',
    edgeLabelBackground: '#ffffff',
    actorBkg: '#e3f1e8',
    actorBorder: '#2f7d57',
    actorTextColor: '#17201c',
    signalColor: '#17201c',
    signalTextColor: '#17201c',
    noteBkgColor: '#fbf1d9',
    noteBorderColor: '#b07d12',
    noteTextColor: '#17201c',
    labelBoxBkgColor: '#e3f1e8',
    labelBoxBorderColor: '#2f7d57',
    pie1: '#2f7d57', pie2: '#c8952a', pie3: '#7fb89a', pie4: '#8a6a3f', pie5: '#b9d9c6',
    pie6: '#e6c47a', pie7: '#4d5c55', pie8: '#a9bcb1', pie9: '#d9a94a', pie10: '#5e9e7b',
    pieTitleTextSize: '17px', pieSectionTextSize: '14px', pieStrokeColor: '#ffffff',
    pieOuterStrokeColor: '#ffffff',
    quadrant1Fill: '#e3f1e8', quadrant2Fill: '#f3f7f4', quadrant3Fill: '#fbf6ea', quadrant4Fill: '#eef2ef',
    quadrantPointFill: '#2f7d57',
    cScale0: '#e3f1e8', cScale1: '#fbf1d9', cScale2: '#d7ebdf', cScale3: '#f5e6c4', cScale4: '#cfe3d6',
    cScale5: '#efe0b8', cScale6: '#c3dccc', cScale7: '#eadaa8', cScale8: '#e9efeb', cScale9: '#f7efdb',
    cScale10: '#dbe7e0', cScale11: '#f2e8cf',
    cScaleLabel0: '#17201c', cScaleLabel1: '#17201c', cScaleLabel2: '#17201c', cScaleLabel3: '#17201c',
    cScaleLabel4: '#17201c', cScaleLabel5: '#17201c', cScaleLabel6: '#17201c', cScaleLabel7: '#17201c',
    cScaleLabel8: '#17201c', cScaleLabel9: '#17201c', cScaleLabel10: '#17201c', cScaleLabel11: '#17201c',
    git0: '#2f7d57', git1: '#c8952a',
  },
};

const browser = await puppeteer.launch({
  executablePath: process.env.CHROME_PATH || undefined,
  args: ['--no-sandbox'],
});
const page = await browser.newPage();
await page.setContent('<!doctype html><html><body><div id="c"></div></body></html>');
await page.addScriptTag({ content: mermaidJs });
await page.evaluate((cfg) => { window.mermaid.initialize(cfg); }, config);

const out = {};
for (const it of items) {
  const res = await page.evaluate(async ({ id, code }) => {
    try {
      const { svg } = await window.mermaid.render(id, code);
      return { svg };
    } catch (e) {
      document.querySelectorAll('[id^="d' + id + '"], #' + id).forEach((n) => n.remove());
      return { error: String(e && e.message ? e.message : e).slice(0, 400) };
    }
  }, it);
  out[it.id] = res;
}
await browser.close();
fs.writeFileSync(outFile, JSON.stringify(out));
const bad = Object.entries(out).filter(([, v]) => v.error);
console.log(`rendered ${items.length - bad.length}/${items.length}`);
for (const [id, v] of bad) console.log(`FAIL ${id}: ${v.error.split('\n')[0]}`);

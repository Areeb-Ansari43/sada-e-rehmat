// Renders a unique 1200×630 social preview for every page listed in og-manifest.json.
// Usage: node _src/og.mjs   (run python3 _src/build.py first)
import { readFileSync, mkdirSync, writeFileSync, unlinkSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);
const { chromium } = require('playwright');

const here = dirname(fileURLToPath(import.meta.url));
const root = join(here, '..');
const out = join(root, 'assets', 'og');
mkdirSync(out, { recursive: true });
const items = JSON.parse(readFileSync(join(here, 'og-manifest.json'), 'utf8'));
const asset = p => pathToFileURL(join(root, p)).href;
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/\uFDFA/g, '<span style="font-family:Amiri">\uFDFA</span>');

// Italicise the last two words of the title, like the site's headlines.
const styled = t => {
  const w = esc(t).split(' ');
  if (w.length < 3) return `<em>${w.join(' ')}</em>`;
  return w.slice(0, -2).join(' ') + ' <em>' + w.slice(-2).join(' ') + '</em>';
};

const css = `
*{box-sizing:border-box;margin:0}
body{width:1200px;height:630px;overflow:hidden;font-family:Inter,Amiri,sans-serif;-webkit-font-smoothing:antialiased}
.f{position:relative;width:1200px;height:630px;overflow:hidden;background:#0b1424;color:#fff}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(5,10,20,.88) 0%,rgba(5,10,20,.55) 48%,rgba(5,10,20,.1) 100%)}
.shade.b{background:linear-gradient(180deg,rgba(5,10,20,.45) 0%,rgba(5,10,20,.35) 35%,rgba(5,10,20,.92) 75%)}
.logo{position:absolute;left:64px;top:52px;height:58px}
.copy{position:absolute;left:64px;right:64px;bottom:60px}
.eb{display:flex;align-items:center;gap:12px;font:600 19px Inter;letter-spacing:.1em;text-transform:uppercase;color:#d2b47e;margin-bottom:20px}
.eb:before{content:"";width:28px;height:2px;background:#d2b47e}
h1{font:600 76px/0.98 "Inter Tight";letter-spacing:-.045em;max-width:15ch}
h1 em{font:italic 400 82px/0.98 "Instrument Serif";letter-spacing:-.01em;color:#f1e6d1}
.d{margin-top:22px;font:500 24px Inter,Amiri;color:rgba(255,255,255,.82);letter-spacing:-.01em}
.chips{display:flex;gap:10px;margin-top:24px}
.chips span{padding:9px 18px;border-radius:999px;border:1.5px solid rgba(255,255,255,.35);font:500 18px Inter;background:rgba(255,255,255,.08)}
.url{position:absolute;right:64px;top:62px;font:500 17px Inter;color:rgba(255,255,255,.7);letter-spacing:.02em}
/* split layout for guides */
.split .panel{position:absolute;left:0;top:0;bottom:0;width:660px;background:#0b1424;padding:52px 60px}
.split .ph{position:absolute;right:0;top:0;bottom:0;width:540px;overflow:hidden}
.split .ph img{width:100%;height:100%;object-fit:cover}
.split .ph:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,#0b1424 0%,rgba(11,20,36,0) 30%)}
.split .copy{left:60px;right:auto;width:560px;bottom:56px}
.split h1{font-size:62px;max-width:none}
.split h1 em{font-size:68px}
.split .d{font-size:22px;line-height:1.35;max-width:540px}
.split .ar{position:absolute;right:40px;bottom:30px;font:400 92px Amiri;color:rgba(210,180,126,.9);direction:rtl;z-index:2;text-shadow:0 4px 30px rgba(0,0,0,.6)}
/* paper layout for legal/contact */
.paper{background:#fbfaf7;color:#0b1424}
.paper .eb{color:#a9834a}.paper .eb:before{background:#a9834a}
.paper h1 em{color:#a9834a}.paper .d{color:#5d6676}
.paper .circle{position:absolute;right:-60px;top:50%;transform:translateY(-50%);width:560px;height:560px;border-radius:50%;overflow:hidden}
.paper .circle img{width:100%;height:100%;object-fit:cover}
.paper .copy{right:520px}
.paper .chips span{border-color:rgba(11,20,36,.2);background:#f3eee5}
.paper .url{color:#5d6676;right:auto;left:64px;top:auto;bottom:24px;font-size:15px}
.bar{position:absolute;left:0;right:0;bottom:0;height:8px;background:linear-gradient(90deg,#a9834a,#d2b47e)}
`;

const AR = { guide: 'لَبَّيْك' };
function html(it) {
  const img = asset(`assets/img/${it.image}-2000.webp`);
  const chips = (it.chips || []).map(c => `<span>${esc(c)}</span>`).join('');
  const copy = `<div class="copy"><div class="eb">${esc(it.eyebrow)}</div><h1>${styled(it.title)}</h1><div class="d">${esc(it.detail)}</div>${chips ? `<div class="chips">${chips}</div>` : ''}</div>`;
  if (it.theme === 'guide') {
    return `<div class="f split"><div class="ph"><img src="${img}"></div><div class="panel"><img class="logo" style="left:60px" src="${asset('assets/img/logo-white.png')}"></div>${copy}<div class="bar"></div></div>`;
  }
  if (it.theme === 'legal' || it.theme === 'contact') {
    return `<div class="f paper"><div class="circle"><img src="${img}"></div><img class="logo" src="${asset('assets/img/logo-ink.png')}">${copy}<div class="url">sada-e-rehmat · UK &amp; Pakistan</div><div class="bar"></div></div>`;
  }
  const bottom = it.theme === 'sites' || it.theme === 'hero';
  return `<div class="f"><img class="bg" src="${img}"><div class="shade${bottom ? ' b' : ''}"></div><img class="logo" src="${asset('assets/img/logo-white.png')}"><div class="url">Hajj &amp; Umrah · UK &amp; Pakistan</div>${copy}<div class="bar"></div></div>`;
}

const b = await chromium.launch();
const page = await b.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
for (const it of items) {
  const doc = `<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Amiri&family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@600&family=Inter:wght@500;600&display=swap" rel="stylesheet"><style>${css}</style></head><body>${html(it)}</body></html>`;
  const tmp = join(here, '.og-tmp.html');
  writeFileSync(tmp, doc);
  await page.goto(pathToFileURL(tmp).href, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: join(out, `${it.slug}.jpg`), type: 'jpeg', quality: 84 });
  console.log('og', it.slug);
}
await b.close();
try { unlinkSync(join(here, '.og-tmp.html')); } catch (e) {}

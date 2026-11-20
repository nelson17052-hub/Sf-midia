// Cole este arquivo inteiro numa chamada do javascript_tool na aba do Instagram (@imoveissemfiltro).
// Ele define as funções usadas para programar posts. Rode de novo sempre que a página recarregar.
window.__w = ms => new Promise(r => setTimeout(r, ms));
window.__dlg = () => { const ds = [...document.querySelectorAll('[role=dialog]')]; return ds[ds.length - 1] || null; };
window.__waitFor = async (fn, ms = 15000) => { const t = Date.now(); while (Date.now() - t < ms) { const v = fn(); if (v) return v; await __w(250); } return null; };
window.__btnTxt = (root, t) => [...(root || document).querySelectorAll('[role=button],button,a')].find(b => (b.innerText || '').trim() === t);
window.__setReact = (el, val) => { const proto = el.tagName === 'TEXTAREA' ? HTMLTextAreaElement.prototype : HTMLInputElement.prototype; Object.getOwnPropertyDescriptor(proto, 'value').set.call(el, val); el.dispatchEvent(new Event('input', { bubbles: true })); el.dispatchEvent(new Event('change', { bubbles: true })); };

// IndexedDB "sf": store items (n -> {n, blob, legenda, alt, v}) e kv ('kit', 'specs')
window.__sfdb = () => new Promise((res, rej) => { const r = indexedDB.open('sf', 2); r.onupgradeneeded = () => { const db = r.result; if (!db.objectStoreNames.contains('items')) db.createObjectStore('items', { keyPath: 'n' }); if (!db.objectStoreNames.contains('kv')) db.createObjectStore('kv'); }; r.onsuccess = () => res(r.result); r.onerror = () => rej(r.error); });
window.__idb = async (store, mode, fn) => { const db = await __sfdb(); return new Promise((res, rej) => { const tx = db.transaction(store, mode); const st = tx.objectStore(store); const r = fn(st); tx.oncomplete = () => res(r && 'result' in r ? r.result : undefined); tx.onerror = () => rej(tx.error); }); };
window.__getItem = n => __idb('items', 'readonly', st => st.get(n));
window.__putItem = it => __idb('items', 'readwrite', st => st.put(it));
window.__kv = k => __idb('kv', 'readonly', st => st.get(k));

// Recebe artes da janelinha (send.html) por postMessage
if (window.__sflistener) removeEventListener('message', window.__sflistener);
window.__sflistener = async (e) => { if (!e.data || e.data.type !== 'sf') return; if (window.__sfkey === e.data.key) { try { e.source.postMessage({ type: 'sf-ack' }, '*'); } catch (err) {} return; }
  const db = await __sfdb(); await new Promise((res, rej) => { const tx = db.transaction(['items', 'kv'], 'readwrite'); const st = tx.objectStore('items'); for (const it of e.data.items) st.put(it); if (e.data.kit) tx.objectStore('kv').put(e.data.kit, 'kit'); if (e.data.specs) tx.objectStore('kv').put(e.data.specs, 'specs'); tx.oncomplete = res; tx.onerror = () => rej(tx.error); });
  window.__sfkey = e.data.key; window.__sfgot = { batch: e.data.batch, count: e.data.items.length, kit: !!e.data.kit, at: new Date().toISOString() }; try { e.source.postMessage({ type: 'sf-ack' }, '*'); } catch (err) {} };
addEventListener('message', window.__sflistener);

// Gera a arte DENTRO do Instagram a partir do HTML da seção (spec) + kit (fontes, css, mascote)
window.__renderSpec = async (specHtml) => {
  const kit = await __kv('kit'); if (!kit) throw new Error('sem kit');
  let ff = kit.ff; for (const k of ['FN', 'FI6', 'FI4', 'MO']) ff = ff.replace('%' + k + '%', 'data:font/woff2;base64,' + kit.fonts[k]);
  const tpl = document.createElement('template'); tpl.innerHTML = specHtml.replace('%M%', kit.mascote);
  const xhtml = new XMLSerializer().serializeToString(tpl.content.firstElementChild);
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1350"><foreignObject x="0" y="0" width="1080" height="1350"><div xmlns="http://www.w3.org/1999/xhtml"><style>${ff}${kit.css}</style>${xhtml}</div></foreignObject></svg>`;
  const img = new Image(); img.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg); await img.decode(); await __w(400);
  const c = document.createElement('canvas'); c.width = 1080; c.height = 1350; c.getContext('2d').drawImage(img, 0, 0);
  return await new Promise(r => c.toBlob(r, 'image/jpeg', 0.92));
};
// Cria/atualiza um item a partir de spec: {n, html, legenda, alt, v}
window.__itemFromSpec = async (s) => { const blob = await __renderSpec(s.html); const it = { n: s.n, file: 'n' + String(s.n).padStart(3, '0') + '.jpg', legenda: s.legenda, alt: s.alt, v: s.v || 1, blob }; await __putItem(it); return blob.size; };

// Fluxo de criação de post
window.__openCreate = async () => {
  if (__dlg() && /Criar novo post/.test(__dlg().innerText)) return true;
  let postar = [...document.querySelectorAll('svg[aria-label="Postar"]')].find(s => s.getBoundingClientRect().width > 0);
  if (!postar) { const criar = [...document.querySelectorAll('a,[role=link],[role=button],div')].find(e => e.childElementCount < 6 && /^Criar( novo)?$/.test((e.innerText || '').trim())) || document.querySelector('svg[aria-label="Novo post"]')?.closest('a,[role=link],[role=button]'); if (criar) criar.click(); await __w(800); postar = [...document.querySelectorAll('svg[aria-label="Postar"]')].find(s => s.getBoundingClientRect().width > 0) || document.querySelector('svg[aria-label="Postar"]'); }
  if (!postar) return 'sem botao postar';
  (postar.closest('a,[role=link],[role=button],[role=menuitem]') || postar.parentElement).click();
  return !!(await __waitFor(() => __dlg() && /Criar novo post/.test(__dlg().innerText)));
};
window.__toCaption = async (item) => {
  const inp = [...document.querySelectorAll('input[type=file]')].find(i => i.multiple && /video\/mp4/.test(i.accept)); if (!inp) return 'sem input';
  const f = new File([item.blob], 'sf' + String(item.n).padStart(3, '0') + '.jpg', { type: 'image/jpeg' });
  const dt = new DataTransfer(); dt.items.add(f); inp.files = dt.files; inp.dispatchEvent(new Event('change', { bubbles: true }));
  if (!await __waitFor(() => __dlg() && __dlg().querySelector('svg[aria-label="Selecionar corte"]'))) return 'sem corte';
  __dlg().querySelector('svg[aria-label="Selecionar corte"]').closest('[role=button],button').click(); await __w(500);
  const r45 = __btnTxt(__dlg(), '4:5'); if (r45) r45.click(); await __w(500);
  __btnTxt(__dlg(), 'Avançar').click(); await __w(1500); __btnTxt(__dlg(), 'Avançar').click();
  if (!await __waitFor(() => __dlg() && __dlg().querySelector('[aria-label="Adicione uma legenda..."]'))) return 'sem legenda';
  return 'ok';
};
window.__setCaption = async (text) => { const ed = __dlg().querySelector('[aria-label="Adicione uma legenda..."]'); ed.focus(); await __w(200); const dt = new DataTransfer(); dt.setData('text/plain', text); ed.dispatchEvent(new ClipboardEvent('paste', { clipboardData: dt, bubbles: true, cancelable: true })); await __w(600); return ed.innerText; };
window.__setAlt = async (alt) => { let inp = __dlg().querySelector('input[aria-label="Texto alternativo"]'); if (!inp) { const acc = [...__dlg().querySelectorAll('[role=button]')].find(b => (b.innerText || '').trim() === 'Acessibilidade'); acc && acc.click(); await __w(700); inp = __dlg().querySelector('input[aria-label="Texto alternativo"]'); } if (!inp) return 'sem alt'; inp.focus(); __setReact(inp, alt); await __w(300); return inp.value; };
window.__switches = () => { const d = __dlg(); return [...d.querySelectorAll('input[role=switch]')].map(s => { let p = s, t = ''; for (let i = 0; i < 8 && !t; i++) { p = p.parentElement; t = (p.innerText || '').trim(); } return { s, label: t.split('\n')[0] + ' ' + (t.split('\n')[1] || '') }; }); };
const MESES = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'];
window.__pickDate = async (iso) => {
  const [y, m, d] = iso.split('-').map(Number); let grid = document.querySelector('[role=grid]');
  if (!grid) { const dl = __dlg(); const dateEl = [...dl.querySelectorAll('span')].filter(e => e.childElementCount === 0 && /de [a-zç]{3}\. de 20\d\d/.test(e.textContent))[0]; if (!dateEl) return 'sem campo data'; dateEl.closest('[role=button]').click(); grid = await __waitFor(() => document.querySelector('[role=grid]'), 5000); if (!grid) return 'sem calendario'; }
  let cal = grid.closest('[role=dialog]');
  for (let i = 0; i < 14; i++) { const head = cal.innerText.split('\n')[0].trim().toLowerCase(); if (head === MESES[m - 1] + ' de ' + y) break; const nxt = [...cal.querySelectorAll('[role=button],button')].find(b => b.getAttribute('aria-label') === 'Next month'); nxt.click(); await __w(400); grid = document.querySelector('[role=grid]'); cal = grid.closest('[role=dialog]'); }
  const head = cal.innerText.split('\n')[0].trim().toLowerCase(); if (head !== MESES[m - 1] + ' de ' + y) return 'mes nao achado: ' + head;
  const cells = [...grid.querySelectorAll('[role=gridcell]')]; const start = cells.findIndex(c => c.innerText.trim() === '1'); let target = null;
  for (let i = start; i < cells.length; i++) { const t = cells[i].innerText.trim(); if (i > start && t === '1') break; if (t === String(d)) { target = cells[i]; break; } }
  if (!target) return 'dia nao achado'; if (target.getAttribute('aria-disabled') === 'true') return 'dia desabilitado';
  (target.querySelector('[role=button],button') || target).click(); await __w(600);
  const shown = [...__dlg().querySelectorAll('span')].filter(e => e.childElementCount === 0 && /de [a-zç]{3}\. de 20\d\d/.test(e.textContent))[0]; return shown ? shown.textContent : '?';
};
// Passo 1: abre, sobe a arte, legenda, alt, liga "Programar conteúdo", desliga Threads/Facebook, escolhe a data.
window.__prep = async (n, iso) => {
  const it = await __getItem(n); if (!it) return 'sem item ' + n;
  const o = await __openCreate(); if (o !== true) return 'abrir: ' + o;
  const r = await __toCaption(it); if (r !== 'ok') return 'upload: ' + r;
  const cap = await __setCaption(it.legenda); if (cap.trim() !== it.legenda.trim()) return 'legenda diferente';
  await __w(300); document.activeElement && document.activeElement.blur();
  const a = await __setAlt(it.alt); if (a !== it.alt) return 'alt falhou';
  const prog = __switches().find(x => /Programar/.test(x.label)); if (!prog.s.checked) { prog.s.click(); await __w(1000); }
  for (const x of __switches()) { if (/Threads|Facebook/.test(x.label) && x.s.checked) { x.s.click(); await __w(400); } }
  const d = await __pickDate(iso); return 'pronto: ' + d;
};
// Passo 2 (fora do JS): foco em Minutes -> tecla real dos 2 dígitos; foco em Hours -> tecla real dos 2 dígitos.
//   javascript: __dlg().querySelector('input[aria-label="Minutes"]').focus()  -> computer key "4 0"
//   javascript: __dlg().querySelector('input[aria-label="Hours"]').focus()    -> computer key "0 7"
// Passo 3: confere data, hora, legenda e compartilhamentos e clica em Programar.
window.__finish = async (iso, hh, mm) => {
  const dl = __dlg(); const m = dl.innerText.match(/Hora\s*(\d\d)\s*:\s*(\d\d)/); const dm = dl.innerText.match(/Data\s*([^\n]+)/);
  if (!m || m[1] !== hh || m[2] !== mm) return 'hora errada: ' + (m ? m[1] + ':' + m[2] : '?');
  const d = Number(iso.split('-')[2]); if (!dm || !new RegExp('\\b' + d + ' de ').test(dm[1])) return 'data errada: ' + (dm && dm[1]);
  const cap = dl.querySelector('[aria-label="Adicione uma legenda..."]'); if (!cap || cap.innerText.trim().length < 5) return 'legenda vazia';
  for (const x of __switches()) { if (/Threads|Facebook/.test(x.label) && x.s.checked) return 'compartilhamento ligado'; }
  __btnTxt(dl, 'Programar').click();
  const ok = await __waitFor(() => { const d2 = __dlg(); return d2 && /Seu post foi programado/.test(d2.innerText); }, 40000);
  if (!ok) return 'sem confirmacao';
  const c = __btnTxt(__dlg(), 'Concluir'); if (c) c.click(); await __w(1200); return 'programado';
};
// Lista o que já está programado na semana visível de instagram.com/scheduled_content/
window.__cards = () => [...document.querySelectorAll('span,div')].filter(e => e.childElementCount === 0 && /^\d{1,2}:\d{2}$/.test(e.textContent.trim())).map(t => { let p = t; for (let i = 0; i < 6; i++) { p = p.parentElement; if (p.querySelector('img')) break; } return t.textContent + ' ' + p.innerText.replace(/\n+/g, ' | ').replace(/^\d{1,2}:\d{2}\s*\|?\s*/, '').slice(0, 60); });
'helpers ok';

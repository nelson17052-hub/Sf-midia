import html, re, sys
sys.path.insert(0, '.')
from frases import K, Y, W, EXTRA, EXTRA2, MODINHA, EXTRA3, EXTRA4

CAT = {'k': 'VERDADE CRUA', 'y': 'COMÉDIA', 'w': 'MODINHA', 'p': 'PATRIMÔNIO', 'q': 'REFERÊNCIA'}
THEME = {'k':'k','y':'y','w':'w','p':'k','q':'k'}

# ordem de postagem: semana = K Y K W Y K Y
pools = {'k': list(K), 'y': list(Y), 'w': list(W)}
order = []
pat = 'kykwyky'
i = 0
while any(pools.values()):
    t = pat[i % len(pat)]; i += 1
    if pools[t]:
        order.append((t,) + pools[t].pop(0))
order += EXTRA
order += EXTRA2
order += EXTRA3
order += EXTRA4

def rich(s):
    s = html.escape(s)
    s = re.sub(r'\*(.+?)\*', lambda m: f'<span class="hl{" nw" if len(m.group(1))<=18 else ""}">{m.group(1)}</span>', s)
    return s

def block(txt, cls):
    paras = txt.split('\n\n')
    return ''.join(f'<p class="{cls}">{rich(p).replace(chr(10), "<br>")}</p>' for p in paras)

def section(n, t, kicker, item):
    top = f'<div class="top"><span class="kick">{html.escape(kicker) if kicker else ""}</span><span class="num">Nº {n:03d}</span></div>'
    foot = f'<div class="foot"><span class="me"><img src="mascote.png">@imoveissemfiltro</span><span class="cat">{CAT[t]}</span></div>'
    if item[0] == 'frase':
        mx = 82 if max(p.count(chr(10)) for p in item[1].split(chr(10)*2)) >= 2 and n > 44 else 118
        body = f'<div class="body"><div class="fit" data-max="{mx}">{block(item[1], "h")}</div></div>'
    elif item[0] == 'citacao':
        _, q, autor, fonte, nota = item
        body = (f'<div class="body"><div class="fit" data-max="96">'
                f'{block(q, "h q cit")}'
                f'<div class="attr">— {html.escape(autor)}<span>{html.escape(fonte)}</span></div>'
                f'<div class="lab l2">SEM FILTRO</div>{block(nota, "h a")}</div></div>')
    else:
        _, l1, f1, l2, f2 = item
        body = (f'<div class="body"><div class="fit" data-max="104">'
                f'<div class="lab">{l1}</div>{block(f1, "h q")}'
                f'<div class="lab l2">{l2}</div>{block(f2, "h a")}</div></div>')
    return f'<section class="s {THEME[t]}{" haskick" if kicker else ""}" id="n{n:03d}">{top}{body}{foot}</section>'

mk = lambda c: ("data:image/svg+xml;utf8," +
  f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 40' preserveAspectRatio='none'>"
  f"<path d='M2 9 C20 4 45 6 70 4 S96 5 98 8 L99 31 C80 36 55 33 30 36 S6 35 1 32 Z' fill='{c}'/></svg>").replace('#', '%23')

css = f'''
@font-face{{font-family:F;src:url(node_modules/@fontsource-variable/fraunces/files/fraunces-latin-full-normal.woff2);font-weight:100 900}}
@font-face{{font-family:F;font-style:italic;src:url(node_modules/@fontsource-variable/fraunces/files/fraunces-latin-full-italic.woff2);font-weight:100 900}}
@font-face{{font-family:M;src:url(node_modules/@fontsource/jetbrains-mono/files/jetbrains-mono-latin-500-normal.woff2);font-weight:500}}
*{{margin:0;box-sizing:border-box}}
body{{background:#888}}
.s{{width:1080px;height:1350px;position:relative;overflow:hidden;padding:92px 96px;display:flex;flex-direction:column}}
.k{{background:#0A0A0A;color:#F5F2EA;--hl:#F4C531;--hlt:#0A0A0A;--dim:#6E6A62;--acc:#F4C531}}
.y{{background:#F4C531;color:#121212;--hl:#121212;--hlt:#F4C531;--dim:#8A6F12;--acc:#121212}}
.w{{background:#FAF8F3;color:#121212;--hl:#F4C531;--hlt:#121212;--dim:#A39E93;--acc:#121212}}
.top,.foot{{display:flex;justify-content:space-between;align-items:center;font-family:M;font-size:25px;letter-spacing:.12em}}
.kick{{color:var(--acc);font-size:27px}}
.k .kick::before{{content:"";display:inline-block;width:14px;height:14px;background:var(--acc);border-radius:50%;margin-right:18px;vertical-align:2px}}
.num{{color:var(--dim)}}
.body{{flex:1;display:flex;align-items:center;min-height:0}}
.fit{{width:100%}}
.h{{font-family:F;font-weight:560;font-variation-settings:"opsz" 144,"SOFT" 30,"WONK" 0;line-height:1.04;letter-spacing:-.012em;word-spacing:.06em}}
.h+.h{{margin-top:.62em}}
.h{{text-wrap:balance}}.nw{{white-space:nowrap}}
.hl{{font-style:italic;font-weight:600;color:var(--hlt);background:url("{{HL}}") center/100% 100% no-repeat;padding:0 .14em;margin:0 -.04em;-webkit-box-decoration-break:clone;box-decoration-break:clone}}
.k .h+.h{{color:#F5F2EA}}
.lab{{font-family:M;font-size:max(.24em,26px);letter-spacing:.16em;color:var(--dim);margin-bottom:.7em}}
.lab.l2{{margin-top:1.5em}}
.q{{font-weight:420;font-style:italic}}
.a{{font-size:.86em}}
.attr{{font-family:M;font-size:max(.27em,27px);letter-spacing:.12em;color:var(--acc);margin-top:1em;line-height:1.5}}
.attr span{{display:block;color:var(--dim);font-size:.8em}}
.cit{{font-size:1.02em}}
.foot{{color:var(--dim);font-size:23px}}
.me{{display:flex;align-items:center;gap:16px;color:var(--acc)}}
.me img{{width:62px;height:62px}}
.k .me{{color:#F5F2EA}}
.y .me img{{filter:drop-shadow(0 0 0 #000)}}
'''
fitjs = '''
<script>
document.fonts.ready.then(()=>{
 for(const f of document.querySelectorAll('.fit')){
  const box=f.parentElement; let s=+f.dataset.max; f.style.fontSize=s+'px';
  while((f.scrollHeight>box.clientHeight*0.92||f.scrollWidth>f.clientWidth+1)&&s>40){s-=2;f.style.fontSize=s+'px';}
 }
 document.body.dataset.ready=1;
});
</script>'''

def page(items, extra_css=''):
    secs = ''.join(section(n, t, k, it) for n, t, k, it in items)
    c = css + extra_css
    out = f'<!doctype html><meta charset=utf-8><style>{c}</style>{secs}{fitjs}'
    # marca-texto por tema
    return out

numbered = [(n + 1,) + o for n, o in enumerate(order)]
numbered = [(n, 'w', None, MODINHA[n]) if n in MODINHA else (n, t, k, it) for n, t, k, it in numbered]
html_out = page(numbered)
# substitui o marca-texto por tema
html_out = html_out.replace('url("{HL}")', 'var(--mk)')
html_out = html_out.replace('.k{background', f'.k{{--mk:url("{mk("#F4C531")}")}}.y{{--mk:url("{mk("#121212")}")}}.w{{--mk:url("{mk("#F4C531")}")}}\n.k{{background', 1)
open('artes.html', 'w').write(html_out)
open('ordem.txt', 'w').write('\n'.join(f'Nº {n:03d}  {CAT[t]:<13} {(k or ""):<18} {it[1] if it[0]=="frase" else (it[1]+" — "+it[2]+" ("+it[3]+") / "+it[4] if it[0]=="citacao" else it[2]+" → "+it[4])}'.replace('\n', ' / ') for n, t, k, it in numbered))
print(len(numbered))

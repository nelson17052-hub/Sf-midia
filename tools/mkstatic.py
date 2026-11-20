import re
s=open('artes.html').read()
css=s[s.index('<style>')+7:s.index('</style>')]
body=s[s.index('</style>')+8:s.index('<script>')]
css=re.sub(r'@font-face\{[^}]*\}\s*','',css)
css=css.replace('.h{font-family:F;font-weight:560;font-variation-settings:"opsz" 144,"SOFT" 30,"WONK" 0;','.h{font-family:FN;font-weight:400;')
css=css.replace('.hl{font-style:italic;font-weight:600;','.hl{font-family:FI6;font-style:normal;font-weight:400;')
css=css.replace('.q{font-weight:420;font-style:italic}','.q{font-family:FI4;font-weight:400}.q .hl{font-family:FI6}')
css=css.replace('font-family:M;','font-family:MO;')
css=css.replace('body{background:#888}','')
assert 'FN' in css and 'FI6' in css and 'FI4' in css
msvg=open('../mascote/m.min.svg').read().replace('<g >','<g clip-path="url(#c)">').replace('<svg ','<svg width="62" height="62" ')
body=body.replace('<img src="mascote.png">',msvg)
ff='''@font-face{font-family:FN;src:url(%FN%)}@font-face{font-family:FI6;src:url(%FI6%)}@font-face{font-family:FI4;src:url(%FI4%)}@font-face{font-family:MO;src:url(%MO%)}'''
import base64,urllib.parse
def fixmk(m):
    raw=urllib.parse.unquote(m.group(1))
    return 'url("data:image/svg+xml;base64,'+base64.b64encode(raw.encode()).decode()+'")'
css=re.sub(r'url\("data:image/svg\+xml;utf8,(.*?)"\)',fixmk,css)
assert '<svg' not in css
open('static.css','w').write(css)
open('fontface.css','w').write(ff)
fit=s[s.index('<script>'):]
loc=ff.replace('%FN%','fonts/f560.woff2').replace('%FI6%','fonts/f600i.woff2').replace('%FI4%','fonts/f420i.woff2').replace('%MO%','fonts/m500.woff2')
open('static.html','w').write(f'<!doctype html><meta charset=utf-8><style>{loc}{css}</style>{body}{fit}')
print(len(css), len(body))

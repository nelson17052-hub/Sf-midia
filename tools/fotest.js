const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('about:blank');
const b64=f=>fs.readFileSync(f).toString('base64');
const data={css:fs.readFileSync('static.css','utf8'),ff:fs.readFileSync('fontface.css','utf8'),
 fonts:{FN:b64('fonts/f560.woff2'),FI6:b64('fonts/f600i.woff2'),FI4:b64('fonts/f420i.woff2'),MO:b64('fonts/m500.woff2')},
 posts:JSON.parse(fs.readFileSync('posts.json','utf8'))};
const ids=process.argv.slice(2);
const res=await p.evaluate(async ({data,ids})=>{
 let ff=data.ff; for(const k of ['FN','FI6','FI4','MO']) ff=ff.replace('%'+k+'%','data:font/woff2;base64,'+data.fonts[k]);
 const out={};
 for(const id of ids){const post=data.posts.find(x=>x.id===id);
  const xhtml=post.html.replace(/<br>/g,'<br/>');
  const svg=`<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1350"><foreignObject x="0" y="0" width="1080" height="1350"><div xmlns="http://www.w3.org/1999/xhtml"><style>${ff}${data.css}</style>${xhtml}</div></foreignObject></svg>`;
  const img=new Image(); img.src='data:image/svg+xml;charset=utf-8,'+encodeURIComponent(svg); await img.decode(); await new Promise(r=>setTimeout(r,300));
  const c=document.createElement('canvas');c.width=1080;c.height=1350;c.getContext('2d').drawImage(img,0,0);
  out[id]=c.toDataURL('image/png');}
 return out;},{data,ids});
for(const [id,u] of Object.entries(res)) fs.writeFileSync('fo_'+id+'.png',Buffer.from(u.split(',')[1],'base64'));
await b.close();})();

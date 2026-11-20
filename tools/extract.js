const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+process.cwd()+'/static.html');await p.waitForSelector('body[data-ready]');await p.waitForTimeout(300);
const posts=await p.$$eval('section.s',ss=>ss.map(s=>({id:s.id,html:s.outerHTML})));
require('fs').writeFileSync('posts.json',JSON.stringify(posts));
require('fs').mkdirSync('out_static',{recursive:true});
for(const s of await p.$$('section.s')){const id=await s.getAttribute('id');await s.screenshot({path:`out_static/${id}.png`});}
await b.close();console.log(posts.length, Math.max(...posts.map(x=>x.html.length)));})();

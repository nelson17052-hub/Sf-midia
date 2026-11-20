const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
require('fs').mkdirSync('out',{recursive:true});
await p.goto('file://'+process.cwd()+'/artes.html');await p.waitForSelector('body[data-ready]');await p.waitForTimeout(200);
for(const s of await p.$$('section.s')){const id=await s.getAttribute('id');await s.screenshot({path:`out/${id}.png`});}await b.close();})();

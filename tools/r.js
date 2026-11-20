const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1000,height:1000}});
await p.goto('file://'+process.argv[2]);await p.screenshot({path:process.argv[3],omitBackground:true});await b.close();})();

const fs=require('fs');const path=require('path');const {chromium}=require('playwright');
const [src,out]=process.argv.slice(2);
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
for(let i=1;i<=6;i++){const h=fs.readFileSync(path.join(src,`slide${i}.html`),'utf8');
await p.setContent(h);await p.waitForTimeout(300);
await p.screenshot({path:path.join(out,`slide${i}.jpg`),type:'jpeg',quality:92,clip:{x:0,y:0,width:1080,height:1350}});}
await b.close();})();

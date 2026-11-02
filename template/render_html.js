// usage: node template/render_html.js <dir with s1.html..s6.html> <outdir>  -> slide1..6.jpg (1080x1350, q92)
const {chromium}=require('playwright');const path=require('path');
const [src,out]=process.argv.slice(2);
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
for(let i=1;i<=6;i++){await p.goto('file://'+path.resolve(src,`s${i}.html`));await p.waitForTimeout(250);
await p.screenshot({path:path.join(out,`slide${i}.jpg`),type:'jpeg',quality:92});}
await b.close();})();

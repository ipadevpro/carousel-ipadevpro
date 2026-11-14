const fs=require('fs');const path=require('path');const {chromium}=require('playwright');
const [src,out]=process.argv.slice(2); // usage: node render.js <dir with Main/Slide2..6 .dc.html> <outdir>
const files=['Main','Slide2','Slide3','Slide4','Slide5','Slide6'];
(async()=>{
 const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
 for(let i=0;i<files.length;i++){
  const h=fs.readFileSync(path.join(src,files[i]+'.dc.html'),'utf8');
  const body=h.split('</helmet>')[1].split('</x-dc>')[0];
  const page='<!doctype html><html lang="id"><head><meta charset="utf-8"><style>body{margin:0}</style></head><body>'+body+'</body></html>';
  await p.setContent(page);await p.waitForTimeout(300);
  await p.screenshot({path:path.join(out,`slide${i+1}.jpg`),type:'jpeg',quality:92,clip:{x:0,y:0,width:1080,height:1350}});
 }
 await b.close();
})();

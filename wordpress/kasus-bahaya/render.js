const { chromium } = require('playwright'); const fs=require('fs');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'}).catch(async()=>await chromium.launch());
const p=await b.newPage({viewport:{width:800,height:520},deviceScaleFactor:1.5});
fs.mkdirSync('png',{recursive:true});
for (const f of fs.readdirSync('svg').sort()){
  await p.setContent('<html><body style="margin:0">'+fs.readFileSync('svg/'+f,'utf8')+'</body></html>');
  await p.locator('svg').screenshot({path:'png/'+f.replace('.svg','.png')});
}
await b.close();})();

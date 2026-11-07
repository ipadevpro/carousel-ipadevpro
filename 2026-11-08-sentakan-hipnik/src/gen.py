import sys,os
out=sys.argv[1]
HL="background: linear-gradient(transparent 10%, #FFE14D 10%, #FFE14D 94%, transparent 94%); padding: 0 8px; margin: 0 -8px; box-decoration-break: clone; -webkit-box-decoration-break: clone"
def hl(t): return f'<span style="{HL}">{t}</span>'
def page(n,inner,extra=''):
    return f'''<!doctype html>
<html lang="id"><head><meta charset="utf-8"><title>Slide {n}</title></head><body>
<x-dc>
<helmet></helmet>
<div style="position: relative; width: 1080px; height: 1350px; box-sizing: border-box; overflow: hidden; background-color: #FBF3DF; background-image: repeating-linear-gradient(to bottom, transparent 0, transparent 71px, rgba(120,150,185,0.35) 71px, rgba(120,150,185,0.35) 73px); background-position: 0 40px; font-family: 'Inter', system-ui, sans-serif; color: #1B1B1F">
<div aria-hidden="true" style="position: absolute; left: 160px; top: 0; width: 4px; height: 1350px; background: #B5483A"></div>
<div aria-hidden="true" style="position: absolute; left: 52px; top: 180px; width: 44px; height: 44px; border-radius: 22px; background: #D9CFB6"></div>
<div aria-hidden="true" style="position: absolute; left: 52px; top: 640px; width: 44px; height: 44px; border-radius: 22px; background: #D9CFB6"></div>
<div aria-hidden="true" style="position: absolute; left: 52px; top: 1100px; width: 44px; height: 44px; border-radius: 22px; background: #D9CFB6"></div>
<div style="position: absolute; left: 210px; top: 56px; font-size: 30px; font-weight: 800; color: #B5483A">@ipadevpro</div>
<div style="position: absolute; right: 80px; top: 56px; font-size: 30px; font-weight: 800; color: #6B6558">{n}/6</div>
{inner}
</div>
</x-dc>
</body></html>'''

H='font-weight: 900; font-variation-settings: \'opsz\' 32; letter-spacing: -1px'
def ban(cx,cy,r):
    a=0.7071*r
    return f'<g fill="none" stroke-linecap="round"><circle cx="{cx}" cy="{cy}" r="{r}" stroke="#1B1B1F" stroke-width="30"/><line x1="{cx-a}" y1="{cy-a}" x2="{cx+a}" y2="{cy+a}" stroke="#1B1B1F" stroke-width="30"/><circle cx="{cx}" cy="{cy}" r="{r}" stroke="#B5483A" stroke-width="20"/><line x1="{cx-a}" y1="{cy-a}" x2="{cx+a}" y2="{cy+a}" stroke="#B5483A" stroke-width="20"/></g>'
def epi(cid,x,y,s,eyes):
    return f'''<g transform="translate({x} {y}) scale({s})">
<path d="M250 30 C 300 120 372 200 372 275 A122 122 0 0 1 128 275 C 128 200 200 120 250 30 Z" fill="#C99A2E" transform="translate(8 8)"/>
<path d="M250 30 C 300 120 372 200 372 275 A122 122 0 0 1 128 275 C 128 200 200 120 250 30 Z" fill="#EDBE4E" stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round"/>
<path d="M165 285 C 165 240 190 205 214 170" fill="none" stroke="#F8E0A0" stroke-width="20" stroke-linecap="round"/>
<g transform="translate(0 62)">{eyes}</g></g>'''
def e_calm(): return '<circle cx="205" cy="190" r="32" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="6"/><circle cx="295" cy="190" r="32" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="6"/><circle cx="213" cy="196" r="13" fill="#1B1B1F"/><circle cx="303" cy="196" r="13" fill="#1B1B1F"/><circle cx="217" cy="191" r="4" fill="#FFFDF6"/><circle cx="307" cy="191" r="4" fill="#FFFDF6"/><path d="M 218 300 Q 250 318 282 300" fill="none" stroke="#1B1B1F" stroke-width="7" stroke-linecap="round"/>'
def e_worried(): return '<circle cx="205" cy="190" r="32" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="6"/><circle cx="295" cy="190" r="32" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="6"/><circle cx="211" cy="198" r="13" fill="#1B1B1F"/><circle cx="301" cy="198" r="13" fill="#1B1B1F"/><circle cx="215" cy="193" r="4" fill="#FFFDF6"/><circle cx="305" cy="193" r="4" fill="#FFFDF6"/><path d="M 168 158 L 226 140 M 332 158 L 274 140" fill="none" stroke="#1B1B1F" stroke-width="8" stroke-linecap="round"/><path d="M 218 312 Q 250 292 282 312" fill="none" stroke="#1B1B1F" stroke-width="7" stroke-linecap="round"/>'
def e_happy(): return '<path d="M 175 200 Q 205 165 235 200 M 265 200 Q 295 165 325 200" fill="none" stroke="#1B1B1F" stroke-width="8" stroke-linecap="round"/><path d="M 214 280 Q 250 322 286 280" fill="none" stroke="#1B1B1F" stroke-width="8" stroke-linecap="round"/>'
def bubble(y,l1,l2):
    return f'''<rect x="330" y="{y}" width="430" height="130" rx="28" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="5"/>
<polygon points="332,{y+50} 290,{y+80} 332,{y+86}" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="5" stroke-linejoin="round"/>
<rect x="328" y="{y+54}" width="10" height="30" fill="#FFFDF6"/>
<text x="545" y="{y+55}" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-weight="900" font-size="38" fill="#1B1B1F">{l1}</text>
<text x="545" y="{y+100}" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-weight="900" font-size="34" fill="#1B1B1F">{l2}</text>'''
def scene(cid,eyes,l1,l2,label,h=260):
    return f'''<svg width="790" height="{h}" viewBox="0 0 790 {h}" role="img" aria-label="{label}">
<ellipse cx="170" cy="{h-14}" rx="100" ry="10" fill="#BCCADA"/>
{epi(cid,-5,-10,0.6,eyes)}
{bubble(30,l1,l2)}
</svg>'''

# ---- mascot override: Sentakan Hipnik
def epi(cid,x,y,s,eyes):
    body='M250 110 C 350 100 396 190 384 290 C 372 390 316 424 250 422 C 184 424 128 390 116 290 C 104 190 150 120 250 110 Z'
    return f'''<g transform="translate({x} {y}) scale({s})"><g transform="translate(0 -40)">
<path d="{body}" fill="#4F5FA8" transform="translate(8 8)"/>
<path d="{body}" fill="#8FA0E6" stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round"/>
<path d="M170 170 C 150 250 160 340 200 395" fill="none" stroke="#B9C4F4" stroke-width="16" stroke-linecap="round"/>
<path d="M262 60 L 226 128 L 258 128 L 236 190 L 296 112 L 262 112 L 284 60 Z" fill="#EDBE4E" stroke="#1B1B1F" stroke-width="6" stroke-linejoin="round" transform="translate(0 6)"/>
<g transform="translate(0 62)">{eyes}</g></g></g>'''
tangan='''<ellipse cx="130" cy="318" rx="90" ry="12" fill="#BCCADA"/>
<g stroke="#1B1B1F" stroke-width="6" stroke-linejoin="round" fill="#E9C9A6"><rect x="82" y="210" width="96" height="90" rx="28"/><rect x="82" y="120" width="22" height="110" rx="11"/><rect x="108" y="100" width="22" height="130" rx="11"/><rect x="134" y="108" width="22" height="122" rx="11"/><rect x="160" y="130" width="20" height="100" rx="10"/></g>'''
hati='''<ellipse cx="395" cy="318" rx="100" ry="12" fill="#BCCADA"/>
<path d="M395 290 C 300 225 320 140 365 150 C 385 154 395 170 395 180 C 395 170 405 154 425 150 C 470 140 490 225 395 290 Z" fill="#D9695A" stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round"/>'''
s1=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 30px">
<div style="font-size: 66px; line-height: 1.04; font-weight: 900; font-variation-settings: 'opsz' 32; letter-spacing: -1.5px">TUBUH YANG TERSENTAK SEPERTI JATUH SAAT BARU TERTIDUR BUKAN TANDA ADA YANG {hl("MENARIK KAKIMU.")}</div>
<div style="font-size: 44px; line-height: 1.1; font-weight: 900; font-variation-settings: 'opsz' 32; color: #B5483A">DAN BUKAN TANDA JANTUNGMU SEMPAT BERHENTI.</div>
<svg style="margin-top: 70px" width="790" height="350" viewBox="0 0 790 350" role="img" aria-label="Sebuah tangan dan sebuah hati, masing-masing dicoret tanda larangan">
<g transform="translate(130 0)">{tangan}</g>{hati}{ban(260,190,110)}{ban(525,190,110)}
</svg>
</div>
<div style="position: absolute; left: 210px; right: 80px; bottom: 56px; font-size: 32px; font-weight: 700; color: #1B1B1F">Geser untuk tahu kenapa →</div>"""
s1=s1.replace('<g transform="translate(130 0)">'+tangan+'</g>'+hati,'<g transform="translate(130 0)">'+tangan+'</g><g transform="translate(135 0)">'+hati+'</g>')

s2=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 28px">
<div style="align-self: flex-start; padding: 10px 22px; border: 3px solid #1B1B1F; border-radius: 6px; background: #FFFDF6; font-size: 32px; line-height: 1.3; font-weight: 800">Namaku: Sentakan Hipnik.<br>Julukanku: Si Jurang Palsu.</div>
<div style="font-size: 58px; line-height: 1.07; {H}">KAMU MENGIRA ADA YANG MENDORONGMU DARI TEPI JURANG.</div>
<div style="font-size: 58px; line-height: 1.07; {H}">{hl("ITU AKU, SEDANG BERGANTI SHIFT.")}</div>
<div style="font-size: 34px; line-height: 1.4; font-weight: 500">Aku kontraksi otot mendadak di perbatasan antara terjaga dan tidur. Kadang disertai rasa jatuh, kilatan cahaya, atau bunyi keras di kepala.</div>
<svg width="790" height="400" viewBox="0 0 790 400" role="img" aria-label="Sentakan Hipnik, tokoh biru bersambar petir kecil, tersenyum tenang">
<ellipse cx="200" cy="382" rx="150" ry="12" fill="#BCCADA"/>
{epi("e2",20,-14,0.98,e_calm())}
<text x="605" y="190" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-weight="800" font-size="34" fill="#6B6558">banyak orang pernah</text>
<text x="605" y="236" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-weight="800" font-size="34" fill="#6B6558">bertemu denganku</text>
</svg>
</div>"""

def item(label,txt):
    return f'''<div style="display: flex; flex-direction: column; gap: 14px">
<div style="align-self: flex-start; padding: 6px 20px; background: #FFFDF6; border: 3px solid #1B1B1F; color: #1B1B1F; border-radius: 6px; font-size: 32px; font-weight: 800">{label}</div>
<div style="font-size: 41px; line-height: 1.34; font-weight: 500">{txt}</div></div>'''
s3=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 32px">
<div style="font-size: 70px; line-height: 1.05; {H}">KENAPA MITOSNYA {hl("KELIRU?")}</div>
{item("PERALIHAN YANG TIDAK MULUS","Saat mulai tertidur, otak perlahan melepas kendali yang membuat otot tetap siaga. Sebagian ilmuwan menduga ada letupan sinyal mendadak ke otot, lalu otak menafsirkannya sebagai rasa jatuh. Penjelasan pastinya masih diteliti.")}
{item("BUKAN JANTUNG BERHENTI","Ini gerakan normal saat transisi ke tidur dan dialami banyak orang sesekali. Tidak ada bukti bahwa ini tanda jantung berhenti.")}
<div style="font-size: 38px; line-height: 1.35; font-weight: 800; color: #B5483A; margin-top: 8px">Kelelahan, kafein, stres, dan jadwal tidur yang tidak teratur diduga membuatku lebih sering datang.</div>
</div>"""

def step(n,t):
    return f'''<div style="display: flex; gap: 26px; align-items: flex-start">
<div style="flex: 0 0 72px; width: 72px; height: 72px; border-radius: 36px; background: #B5483A; border: 4px solid #1B1B1F; box-sizing: border-box; color: #FBF3DF; display: flex; align-items: center; justify-content: center; font-size: 40px; font-weight: 900">{n}</div>
<div style="flex: 1 1 0; min-width: 0; font-size: 40px; line-height: 1.34; font-weight: 600">{t}</div></div>'''
s4=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 40px">
<div style="font-size: 70px; line-height: 1.04; {H}">WAHAI {hl("GURU:")}</div>
{step(1,'<span style="font-weight: 900">Jadikan contoh</span> saat membahas sistem saraf: otak tetap bekerja saat kita mulai tidur.')}
{step(2,'<span style="font-weight: 900">Jelang ujian,</span> ingatkan bahwa begadang dan kafein malam justru mengganggu kualitas tidur.')}
{step(3,'<span style="font-weight: 900">Tanyai baik-baik</span> murid yang tampak sangat mengantuk setiap hari tentang tidurnya.')}
<div style="margin-top: 10px">{scene("e4",e_calm(),"TARIK NAPAS","DULU, YA","Sentakan Hipnik tenang berkata: tarik napas dulu ya",250)}</div>
</div>"""

def bul(t): return f'<div style="display: flex; gap: 22px"><span aria-hidden="true" style="flex: 0 0 18px; width: 18px; height: 18px; margin-top: 15px; background: #B5483A; border: 3px solid #1B1B1F; box-sizing: border-box; border-radius: 3px"></span><span>{t}</span></div>'
s5=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 34px">
<div style="background: #B5483A; color: #FBF3DF; border-radius: 16px; padding: 32px 40px">
<div style="font-size: 52px; line-height: 1.06; {H}">SEMAKIN TAKUT, SEMAKIN BESAR KEMUNGKINAN AKU MUNCUL LAGI.</div>
</div>
<div style="font-size: 52px; line-height: 1.06; {H}">UNTUK {hl("AYAH DAN BUNDA:")}</div>
<div style="display: flex; flex-direction: column; gap: 18px; font-size: 36px; line-height: 1.25; font-weight: 700">
{bul("tenangkan anak: sentakan ini umum dan umumnya tidak berbahaya")}
{bul("kurangi kafein di sore hari dan batasi layar sebelum tidur")}
{bul("ke dokter bila sangat sering sampai anak sulit tidur, muncul juga saat terjaga, atau disertai mengompol, lidah tergigit, atau bingung setelahnya")}
</div>
<div style="margin-top: 4px">{scene("e5",e_worried(),"BUKAN TANGAN","TAK TERLIHAT","Sentakan Hipnik tampak cemas dan berkata: bukan tangan tak terlihat",250)}</div>
</div>"""

s6=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 30px">
<div style="font-size: 40px; line-height: 1.3; font-weight: 500">Aku bukan tangan tak terlihat. Aku juga bukan jantung yang lupa berdetak. Aku hanya hentakan kecil di pintu masuk tidur.</div>
<div style="font-size: 62px; line-height: 1.06; {H}">KALAU AKU DATANG, TARIK NAPAS, BETULKAN SELIMUT, {hl("LALU TIDURLAH LAGI.")}</div>
<div style="font-size: 44px; font-weight: 800; color: #B5483A">Salam, Sentakan Hipnik.</div>
<div style="margin-top: 4px; display: flex; gap: 20px; align-items: center">
<div style="flex: 1 1 0; min-width: 0; border: 4px solid #1B1B1F; border-radius: 16px; padding: 22px 28px; background: #FFFDF6; display: flex; flex-direction: column; gap: 10px">
<div style="font-size: 36px; line-height: 1.2; font-weight: 900">Simpan, lalu kirim ke guru yang kamu kenal.</div>
</div>
<svg width="200" height="240" viewBox="0 0 200 240" role="img" aria-label="Sentakan Hipnik tersenyum lega" style="flex: 0 0 200px">
<ellipse cx="100" cy="226" rx="70" ry="9" fill="#BCCADA"/>
{epi("e6",-48,-6,0.6,e_happy())}
</svg>
</div></div>
<div style="position: absolute; left: 210px; right: 80px; bottom: 40px; font-size: 25px; line-height: 1.35; font-weight: 600; color: #6B6558">Ceritanya fiksi. Nyata: sentakan hipnik umum dan umumnya jinak, terjadi saat transisi ke tidur; kelelahan, kafein, dan stres diduga memperberatnya. Penyebab pastinya belum diketahui. Gerakan saat tidur yang tidak biasa perlu diperiksa dokter.</div>"""
import os
os.makedirs(out,exist_ok=True)
for i,s in enumerate([s1,s2,s3,s4,s5,s6],1):
    open(f'{out}/slide{i}.html','w').write(page(i,s))

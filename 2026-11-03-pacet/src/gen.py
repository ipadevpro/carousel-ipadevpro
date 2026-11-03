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
DROP="M250 40 C 290 120 372 190 372 272 A122 122 0 0 1 128 272 C128 190 210 120 250 40 Z"
def drop(cid,x=0,y=0,s=1.0):
    return f'''<g transform="translate({x} {y}) scale({s})"><defs><clipPath id="{cid}"><path d="{DROP}"/></clipPath></defs>
<g clip-path="url(#{cid})"><rect x="100" y="30" width="300" height="380" fill="#B5483A"/>
<path d="{DROP}" transform="translate(-14 -12)" fill="#DC7E6E"/>
<path d="M250 40 C 250 40 150 150 150 250 C 150 300 170 330 190 330 C 170 300 190 200 250 90 Z" fill="#F0B5A8" opacity="0.9"/></g>
<path d="{DROP}" fill="none" stroke="#1B1B1F" stroke-width="7"/>
<ellipse cx="170" cy="292" rx="22" ry="13" fill="#B5483A" opacity="0.55"/><ellipse cx="330" cy="292" rx="22" ry="13" fill="#B5483A" opacity="0.55"/>
EYES</g>'''
def eyes_happy(): return '<path d="M 192 245 Q 212 218 232 245 M 268 245 Q 288 218 308 245" fill="none" stroke="#1B1B1F" stroke-width="8" stroke-linecap="round"/><path d="M 218 292 Q 250 326 282 292" fill="none" stroke="#1B1B1F" stroke-width="8" stroke-linecap="round"/>'
def eyes_calm(): return '<circle cx="212" cy="245" r="30" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="6"/><circle cx="288" cy="245" r="30" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="6"/><circle cx="220" cy="250" r="12" fill="#1B1B1F"/><circle cx="296" cy="250" r="12" fill="#1B1B1F"/><circle cx="224" cy="245" r="4" fill="#FFFDF6"/><circle cx="300" cy="245" r="4" fill="#FFFDF6"/><path d="M 222 298 Q 250 314 278 298" fill="none" stroke="#1B1B1F" stroke-width="7" stroke-linecap="round"/>'
def eyes_worried(): return '<circle cx="212" cy="245" r="30" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="6"/><circle cx="288" cy="245" r="30" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="6"/><circle cx="218" cy="252" r="12" fill="#1B1B1F"/><circle cx="294" cy="252" r="12" fill="#1B1B1F"/><circle cx="222" cy="247" r="4" fill="#FFFDF6"/><circle cx="298" cy="247" r="4" fill="#FFFDF6"/><path d="M 178 216 L 232 200 M 322 216 L 268 200" fill="none" stroke="#1B1B1F" stroke-width="8" stroke-linecap="round"/><path d="M 222 306 Q 250 288 278 306" fill="none" stroke="#1B1B1F" stroke-width="7" stroke-linecap="round"/>'
def worm(d,w=1):
    return f'<path d="{d}" fill="none" stroke="#1B1B1F" stroke-width="{46*w}" stroke-linecap="round"/><path d="{d}" fill="none" stroke="#5E4440" stroke-width="{34*w}" stroke-linecap="round"/><path d="{d}" fill="none" stroke="#8E6A60" stroke-width="{10*w}" stroke-linecap="round" transform="translate(0 -8)"/>'

def scene(cid,eyes,l1,l2,label,x=-10):
    return f'''<svg width="790" height="260" viewBox="0 0 790 260" role="img" aria-label="{label}">
<ellipse cx="170" cy="246" rx="100" ry="10" fill="#BCCADA"/>
{drop(cid,x,40,0.5).replace("EYES",eyes)}
<rect x="330" y="70" width="430" height="130" rx="28" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="5"/>
<polygon points="332,120 290,150 332,156" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="5" stroke-linejoin="round"/>
<rect x="328" y="124" width="10" height="30" fill="#FFFDF6"/>
<text x="545" y="125" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-weight="900" font-size="40" fill="#1B1B1F">{l1}</text>
<text x="545" y="170" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-weight="900" font-size="34" fill="#1B1B1F">{l2}</text>
</svg>'''
# ---- slide 1
salt='''<ellipse cx="190" cy="318" rx="110" ry="14" fill="#BCCADA"/>
<path d="M120 120 L260 120 L275 305 Q275 315 265 315 L115 315 Q105 315 105 305 Z" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="6" stroke-linejoin="round"/>
<path d="M135 120 L125 305" stroke="#BCCADA" stroke-width="12" stroke-linecap="round"/>
<path d="M112 120 Q112 70 190 70 Q268 70 268 120 Z" fill="#D9CFB6" stroke="#1B1B1F" stroke-width="6" stroke-linejoin="round"/>
<circle cx="160" cy="98" r="6" fill="#1B1B1F"/><circle cx="190" cy="92" r="6" fill="#1B1B1F"/><circle cx="220" cy="98" r="6" fill="#1B1B1F"/>
'''
fire='''<ellipse cx="610" cy="318" rx="120" ry="14" fill="#BCCADA"/>
<line x1="520" y1="300" x2="660" y2="170" stroke="#1B1B1F" stroke-width="20" stroke-linecap="round"/>
<line x1="520" y1="300" x2="660" y2="170" stroke="#D9CFB6" stroke-width="10" stroke-linecap="round"/>
<circle cx="672" cy="158" r="22" fill="#B5483A" stroke="#1B1B1F" stroke-width="6"/>
<path d="M 672 40 C 700 85 740 110 722 150 C 712 175 690 182 672 182 C 650 182 630 168 632 140 C 634 112 662 90 672 40 Z" fill="#FFE14D" stroke="#1B1B1F" stroke-width="6" stroke-linejoin="round"/>
<path d="M 674 106 C 690 128 704 140 696 158 C 690 170 678 172 672 172 C 660 170 654 158 660 144 C 666 130 672 124 674 106 Z" fill="#DC7E6E"/>'''
def ban(cx,cy,r):
    a=0.7071*r
    return f'<g fill="none" stroke-linecap="round"><circle cx="{cx}" cy="{cy}" r="{r}" stroke="#1B1B1F" stroke-width="38"/><line x1="{cx-a}" y1="{cy-a}" x2="{cx+a}" y2="{cy+a}" stroke="#1B1B1F" stroke-width="38"/><circle cx="{cx}" cy="{cy}" r="{r}" stroke="#B5483A" stroke-width="26"/><line x1="{cx-a}" y1="{cy-a}" x2="{cx+a}" y2="{cy+a}" stroke="#B5483A" stroke-width="26"/></g>'
s1=f'''<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 30px">
<div style="font-size: 76px; line-height: 1.04; font-weight: 900; font-variation-settings: 'opsz' 32; letter-spacing: -1.5px">PACET YANG MENEMPEL DI KAKI MURID SAAT KEMAH JANGAN {hl("DITARIK PAKSA.")}</div>
<div style="font-size: 44px; line-height: 1.1; font-weight: 900; font-variation-settings: 'opsz' 32; color: #B5483A">DAN JANGAN DITABURI GARAM ATAU DISUNDUT API.</div>
<svg width="790" height="350" viewBox="0 0 790 350" role="img" aria-label="Botol garam dan korek api menyala, masing-masing dicoret tanda larangan">
{salt}{fire}{ban(190,190,128)}{ban(620,190,128)}
</svg>
</div>
<div style="position: absolute; left: 210px; right: 80px; bottom: 56px; font-size: 32px; font-weight: 700; color: #1B1B1F">Geser untuk tahu kenapa →</div>'''

# ---- slide 2
s2=f'''<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 28px">
<div style="align-self: flex-start; padding: 10px 22px; border: 3px solid #1B1B1F; border-radius: 6px; background: #FFFDF6; font-size: 32px; line-height: 1.3; font-weight: 800">Namaku: Hirudin.<br>Julukanku: Si Pengencer.</div>
<div style="font-size: 58px; line-height: 1.07; {H}">KAMU MENGIRA LUKANYA SEPERTI ADA YANG SALAH.</div>
<div style="font-size: 58px; line-height: 1.07; {H}">{hl("AKU TETAP BEKERJA DI LUKA ITU, LAMA SETELAH PACETNYA PERGI.")}</div>
<div style="font-size: 34px; line-height: 1.4; font-weight: 500">Aku zat di air liur pacet dan lintah. Tugasku menahan darah supaya tidak membeku selama mereka mengisap.</div>
<svg width="790" height="370" viewBox="0 0 790 370" role="img" aria-label="Hirudin, tokoh tetesan berwarna merah bata, berdiri tenang di samping pacet kecil berwarna cokelat gelap">
<ellipse cx="200" cy="352" rx="130" ry="12" fill="#BCCADA"/><ellipse cx="600" cy="352" rx="140" ry="12" fill="#BCCADA"/>
{drop("d2",-6,-6,0.9).replace("EYES",eyes_calm())}
{worm("M 470 300 C 520 230, 570 330, 620 265 S 700 300, 740 245",0.8)}
<circle cx="742" cy="242" r="7" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="3"/>
</svg>
</div>'''

# ---- slide 3
def item(label,txt):
    return f'''<div style="display: flex; flex-direction: column; gap: 14px">
<div style="align-self: flex-start; padding: 6px 20px; background: #FFFDF6; border: 3px solid #1B1B1F; color: #1B1B1F; border-radius: 6px; font-size: 32px; font-weight: 800">{label}</div>
<div style="font-size: 40px; line-height: 1.34; font-weight: 500">{txt}</div></div>'''
s3=f'''<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 40px">
<div style="font-size: 70px; line-height: 1.05; {H}">KENAPA CARA LAMA {hl("KELIRU?")}</div>
{item("DITARIK PAKSA","Tarikan paksa bisa meninggalkan luka yang lebih robek.")}
{item("GARAM ATAU API","Pacet memang jadi lepas. Tapi sebagian panduan menyebut ia bisa memuntahkan isi perutnya ke luka sebelum pergi.")}
<div style="font-size: 36px; line-height: 1.35; font-weight: 800; color: #B5483A">Anjuran ini lebih banyak berdasar pengalaman praktisi daripada uji penelitian.</div>
<svg width="790" height="240" viewBox="0 0 790 240" role="img" aria-label="Hirudin tampak cemas dan berkata: tunggu, aku masih bekerja">
<ellipse cx="170" cy="206" rx="100" ry="10" fill="#BCCADA"/>
DROP3
<rect x="330" y="50" width="430" height="130" rx="28" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="5"/>
<polygon points="332,100 290,130 332,136" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="5" stroke-linejoin="round"/>
<rect x="328" y="104" width="10" height="30" fill="#FFFDF6"/>
<text x="545" y="105" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-weight="900" font-size="40" fill="#1B1B1F">TUNGGU!</text>
<text x="545" y="150" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-weight="900" font-size="34" fill="#1B1B1F">AKU MASIH BEKERJA</text>
</svg>
</div>'''

s3=s3.replace('DROP3',drop('d3',-10,-4,0.5).replace('EYES',eyes_worried()))
# ---- slide 4
def step(n,t):
    return f'''<div style="display: flex; gap: 26px; align-items: flex-start">
<div style="flex: 0 0 72px; width: 72px; height: 72px; border-radius: 36px; background: #B5483A; border: 4px solid #1B1B1F; box-sizing: border-box; color: #FBF3DF; display: flex; align-items: center; justify-content: center; font-size: 40px; font-weight: 900">{n}</div>
<div style="flex: 1 1 0; min-width: 0; font-size: 40px; line-height: 1.34; font-weight: 600">{t}</div></div>'''
s4=f'''<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 44px">
<div style="font-size: 76px; line-height: 1.04; {H}">YANG {hl("BENAR")} DILAKUKAN</div>
{step(1,'<span style="font-weight: 900">Selipkan kuku di bawah mulut kecil pacet,</span> geser ke samping, lalu ujung lainnya.')}
{step(2,'<span style="font-weight: 900">Cuci lukanya.</span>')}
{step(3,'<span style="font-weight: 900">Tekan dengan kasa,</span> lalu tutup dengan plester.')}
<div style="font-size: 34px; line-height: 1.4; font-weight: 700; color: #B5483A">Sebelum kemah di area lembap, minta murid memakai kaus kaki panjang dan memasukkan celana ke dalam kaus kaki.</div>
{scene("d4",eyes_calm(),"PELAN-PELAN,","JANGAN DITARIK","Hirudin tenang berkata: pelan-pelan, jangan ditarik")}
</div>'''

# ---- slide 5
def bul(t): return f'<div style="display: flex; gap: 22px"><span aria-hidden="true" style="flex: 0 0 18px; width: 18px; height: 18px; margin-top: 17px; background: #B5483A; border: 3px solid #1B1B1F; box-sizing: border-box; border-radius: 3px"></span><span>{t}</span></div>'
s5=f'''<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 40px">
<div style="background: #B5483A; color: #FBF3DF; border-radius: 16px; padding: 36px 40px; display: flex; flex-direction: column; gap: 18px">
<div style="font-size: 58px; line-height: 1.06; {H}">DARAH YANG TERUS MEMBASAHI LUKA ITU BUKAN TANDA BAHAYA BESAR.</div>
<div style="font-size: 38px; line-height: 1.3; font-weight: 600">Itu hanya aku yang belum selesai bekerja.</div>
</div>
<div style="font-size: 52px; line-height: 1.06; {H}">PERIKSAKAN KE {hl("FASILITAS KESEHATAN")} BILA:</div>
<div style="display: flex; flex-direction: column; gap: 22px; font-size: 42px; line-height: 1.25; font-weight: 700">
{bul("luka makin merah, bengkak, atau bernanah")}
{bul("anak tampak sesak")}
{bul("ada bengkak di wajah")}
{bul("muncul ruam yang luas")}
</div>
</div>'''

# ---- slide 6
s6=f'''<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 44px">
<div style="font-size: 44px; line-height: 1.34; font-weight: 500">Aku tidak ingin menakutimu. Tekan lukanya dengan sabar.</div>
<div style="font-size: 76px; line-height: 1.06; {H}">TENANGKAN ANAKNYA. {hl("SEBENTAR LAGI AKU PERGI.")}</div>
<div style="font-size: 44px; font-weight: 800; color: #B5483A">Salam, Hirudin.</div>
<div style="margin-top: 4px; display: flex; gap: 20px; align-items: center">
<div style="flex: 1 1 0; min-width: 0; border: 4px solid #1B1B1F; border-radius: 16px; padding: 22px 28px; background: #FFFDF6; display: flex; flex-direction: column; gap: 10px">
<div style="font-size: 42px; line-height: 1.2; font-weight: 900">Simpan, lalu kirim ke guru pembina yang akan kemah.</div>
<div style="font-size: 34px; line-height: 1.3; font-weight: 600; color: #6B6558">Sebelum ada yang menarik atau menaburi garam.</div>
</div>
<svg width="230" height="253" viewBox="0 0 200 220" role="img" aria-label="Hirudin tersenyum lega" style="flex: 0 0 230px">
<ellipse cx="100" cy="206" rx="72" ry="9" fill="#BCCADA"/>
{drop("d6",-18,-6,0.46).replace("EYES",eyes_happy())}
</svg>
</div></div>
<div style="position: absolute; left: 210px; right: 80px; bottom: 48px; font-size: 26px; line-height: 1.35; font-weight: 600; color: #6B6558">Ceritanya fiksi, hirudin tidak berbicara. Yang nyata: air liur lintah dan pacet mengandung antikoagulan sehingga luka bisa berdarah lama; gigitannya jarang berbahaya.</div>'''
os.makedirs(out,exist_ok=True)
for i,s in enumerate([s1,s2,s3,s4,s5,s6],1):
    open(f'{out}/slide{i}.html','w').write(page(i,s))

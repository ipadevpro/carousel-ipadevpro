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
    return f'''<g transform="translate({x} {y}) scale({s})"><defs><clipPath id="{cid}"><rect x="130" y="40" width="240" height="330" rx="46"/></clipPath></defs>
<g clip-path="url(#{cid})"><rect x="120" y="30" width="270" height="350" fill="#C98768"/>
<rect x="110" y="24" width="250" height="340" rx="46" fill="#E6A98A"/>
<rect x="150" y="56" width="26" height="250" rx="13" fill="#F5CDB6"/>
<path d="M130 120 H370 M130 330 H370" stroke="#C98768" stroke-width="5" opacity="0.55"/></g>
<rect x="130" y="40" width="240" height="330" rx="46" fill="none" stroke="#1B1B1F" stroke-width="7"/>
<ellipse cx="170" cy="262" rx="24" ry="14" fill="#B5483A" opacity="0.5"/><ellipse cx="330" cy="262" rx="24" ry="14" fill="#B5483A" opacity="0.5"/>
{eyes}</g>'''
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

# ---- slide 1
tube='''<ellipse cx="130" cy="318" rx="100" ry="12" fill="#BCCADA"/>
<g transform="rotate(-18 130 190)"><rect x="95" y="70" width="70" height="215" rx="10" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="6"/>
<rect x="95" y="70" width="70" height="46" fill="#B5483A" stroke="#1B1B1F" stroke-width="6"/><rect x="108" y="40" width="44" height="34" rx="6" fill="#D9CFB6" stroke="#1B1B1F" stroke-width="6"/>
<rect x="104" y="120" width="12" height="150" rx="6" fill="#BCCADA"/><rect x="118" y="165" width="34" height="60" rx="6" fill="#DC7E6E"/></g>'''
butter='''<ellipse cx="395" cy="318" rx="110" ry="12" fill="#BCCADA"/>
<polygon points="300,190 470,190 490,150 320,150" fill="#FFF3A8" stroke="#1B1B1F" stroke-width="6" stroke-linejoin="round"/>
<polygon points="300,190 470,190 470,260 300,260" fill="#FFE14D" stroke="#1B1B1F" stroke-width="6" stroke-linejoin="round"/>
<polygon points="470,190 490,150 490,220 470,260" fill="#E0BE2E" stroke="#1B1B1F" stroke-width="6" stroke-linejoin="round"/>
<path d="M318 205 H452" stroke="#FFF3A8" stroke-width="8" stroke-linecap="round"/>'''
kecap='''<ellipse cx="660" cy="318" rx="100" ry="12" fill="#BCCADA"/>
<rect x="615" y="110" width="90" height="175" rx="22" fill="#3A2A22" stroke="#1B1B1F" stroke-width="6"/>
<rect x="630" y="170" width="60" height="70" rx="6" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="4"/>
<rect x="640" y="62" width="70" height="52" rx="8" fill="#B5483A" stroke="#1B1B1F" stroke-width="6"/><rect x="626" y="118" width="12" height="150" rx="6" fill="#6B5446"/>'''
s1=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 30px">
<div style="font-size: 72px; line-height: 1.04; font-weight: 900; font-variation-settings: 'opsz' 32; letter-spacing: -1.5px">BETIS ANAK YANG TERKENA KNALPOT MOTOR JANGAN DIOLESI {hl("PASTA GIGI.")}</div>
<div style="font-size: 44px; line-height: 1.1; font-weight: 900; font-variation-settings: 'opsz' 32; color: #B5483A">DAN JANGAN DIOLESI KECAP ATAU MENTEGA.</div>
<svg style="margin-top: 70px" width="790" height="350" viewBox="0 0 790 350" role="img" aria-label="Tabung pasta gigi, sebongkah mentega, dan botol kecap, masing-masing dicoret tanda larangan">
{tube}{butter}{kecap}{ban(130,190,110)}{ban(395,190,110)}{ban(660,190,110)}
</svg>
</div>
<div style="position: absolute; left: 210px; right: 80px; bottom: 56px; font-size: 32px; font-weight: 700; color: #1B1B1F">Geser untuk tahu kenapa →</div>"""

# ---- slide 2
s2=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 28px">
<div style="align-self: flex-start; padding: 10px 22px; border: 3px solid #1B1B1F; border-radius: 6px; background: #FFFDF6; font-size: 32px; line-height: 1.3; font-weight: 800">Namaku: Epidermis.<br>Julukanku: Si Dinding Luar.</div>
<div style="font-size: 58px; line-height: 1.07; {H}">KAMU MENGIRA RASA DINGIN ITU TANDA PANASNYA SUDAH PERGI.</div>
<div style="font-size: 58px; line-height: 1.07; {H}">{hl("SERING KALI PANASNYA MASIH TERPERANGKAP DI DALAMKU.")}</div>
<div style="font-size: 34px; line-height: 1.4; font-weight: 500">Aku lapisan kulit paling luar. Tipis, tetapi aku menahan kuman di luar dan cairan tubuh di dalam.</div>
<svg width="790" height="330" viewBox="0 0 790 330" role="img" aria-label="Epidermis, tokoh dinding kulit, berdiri tenang di samping knalpot motor yang panas">
<ellipse cx="200" cy="312" rx="130" ry="12" fill="#BCCADA"/><ellipse cx="600" cy="312" rx="150" ry="12" fill="#BCCADA"/>
{epi("e2",20,-10,0.8,e_calm())}
<rect x="470" y="205" width="270" height="62" rx="31" fill="#8E9AA6" stroke="#1B1B1F" stroke-width="6"/>
<rect x="480" y="215" width="210" height="14" rx="7" fill="#C9D2DA"/>
<rect x="718" y="196" width="30" height="80" rx="8" fill="#6B7682" stroke="#1B1B1F" stroke-width="6"/>
<path d="M530 190 C 515 160 545 150 530 118 M 590 190 C 575 160 605 150 590 118 M 650 190 C 635 160 665 150 650 118" fill="none" stroke="#B5483A" stroke-width="7" stroke-linecap="round"/>
</svg>
</div>"""

# ---- slide 3
def item(label,txt):
    return f'''<div style="display: flex; flex-direction: column; gap: 14px">
<div style="align-self: flex-start; padding: 6px 20px; background: #FFFDF6; border: 3px solid #1B1B1F; color: #1B1B1F; border-radius: 6px; font-size: 32px; font-weight: 800">{label}</div>
<div style="font-size: 40px; line-height: 1.34; font-weight: 500">{txt}</div></div>'''
s3=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 36px">
<div style="font-size: 70px; line-height: 1.05; {H}">KENAPA OLESAN ITU {hl("KELIRU?")}</div>
{item("MENUTUP SEPERTI SELIMUT","Pasta gigi, mentega, dan kecap menutup permukaan kulit. Panas di bawahnya jadi lebih sulit keluar.")}
{item("MENGIRITASI DAN MENGOTORI","Olesan juga menyulitkan petugas kesehatan menilai seberapa dalam lukanya.")}
<div style="font-size: 36px; line-height: 1.35; font-weight: 800; color: #B5483A">Luka bakar knalpot sering lebih dalam dari tampaknya, karena logam panas menempel langsung ke kulit.</div>
{scene("e3",e_worried(),"RASA DINGINNYA","MENIPU","Epidermis tampak cemas dan berkata: rasa dinginnya menipu",230)}
</div>"""

# ---- slide 4
def step(n,t):
    return f'''<div style="display: flex; gap: 26px; align-items: flex-start">
<div style="flex: 0 0 72px; width: 72px; height: 72px; border-radius: 36px; background: #B5483A; border: 4px solid #1B1B1F; box-sizing: border-box; color: #FBF3DF; display: flex; align-items: center; justify-content: center; font-size: 40px; font-weight: 900">{n}</div>
<div style="flex: 1 1 0; min-width: 0; font-size: 40px; line-height: 1.34; font-weight: 600">{t}</div></div>'''
s4=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 40px">
<div style="font-size: 76px; line-height: 1.04; {H}">YANG {hl("BENAR")} DILAKUKAN</div>
{step(1,'<span style="font-weight: 900">Aliri dengan air mengalir bersuhu biasa</span> sekitar 20 menit, sesegera mungkin.')}
{step(2,'<span style="font-weight: 900">Lepas perhiasan</span> di dekat luka.')}
{step(3,'<span style="font-weight: 900">Tutup longgar</span> dengan kain bersih.')}
<div style="font-size: 34px; line-height: 1.4; font-weight: 700; color: #B5483A">Ajari anak turun dari sisi kiri motor, jauh dari knalpot.</div>
<div style="margin-top: 40px">{scene("e4",e_calm(),"ALIRI AKU AIR","SEKITAR 20 MENIT","Epidermis tenang berkata: aliri aku air sekitar 20 menit",260)}</div>
</div>"""

# ---- slide 5
def bul(t): return f'<div style="display: flex; gap: 22px"><span aria-hidden="true" style="flex: 0 0 18px; width: 18px; height: 18px; margin-top: 17px; background: #B5483A; border: 3px solid #1B1B1F; box-sizing: border-box; border-radius: 3px"></span><span>{t}</span></div>'
s5=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 40px">
<div style="background: #B5483A; color: #FBF3DF; border-radius: 16px; padding: 36px 40px; display: flex; flex-direction: column; gap: 18px">
<div style="font-size: 56px; line-height: 1.06; {H}">ES, PASTA GIGI, MENTEGA, MINYAK, DAN KECAP TIDAK DIANJURKAN.</div>
</div>
<div style="font-size: 52px; line-height: 1.06; {H}">PERIKSAKAN KE {hl("TENAGA KESEHATAN")} BILA:</div>
<div style="display: flex; flex-direction: column; gap: 22px; font-size: 42px; line-height: 1.25; font-weight: 700">
{bul("lepuh lebar, lebih besar dari telapak tangan anak")}
{bul("kulit tampak putih atau keras")}
{bul("tanda infeksi muncul")}
</div>
<div style="margin-top: 30px">{scene("e5",e_worried(),"LEPUH JANGAN","DIPECAHKAN","Epidermis tampak cemas dan berkata: lepuh jangan dipecahkan",260)}</div>
</div>"""

# ---- slide 6
s6=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 40px">
<div style="font-size: 44px; line-height: 1.34; font-weight: 500">Aku dinding yang tipis, dan hari ini aku retak. Aku tidak butuh selimut olesan.</div>
<div style="font-size: 72px; line-height: 1.06; {H}">DINGINKAN AKU DULU. {hl("AKU AKAN BERUSAHA MENUTUP DIRI LAGI.")}</div>
<div style="font-size: 44px; font-weight: 800; color: #B5483A">Salam, Epidermis.</div>
<div style="margin-top: 4px; display: flex; gap: 20px; align-items: center">
<div style="flex: 1 1 0; min-width: 0; border: 4px solid #1B1B1F; border-radius: 16px; padding: 22px 28px; background: #FFFDF6; display: flex; flex-direction: column; gap: 10px">
<div style="font-size: 42px; line-height: 1.2; font-weight: 900">Simpan, lalu kirim ke petugas gerbang sekolahmu.</div>
<div style="font-size: 34px; line-height: 1.3; font-weight: 600; color: #6B6558">Simpan juga ember dan kain bersih di pos satpam.</div>
</div>
<svg width="200" height="240" viewBox="0 0 200 240" role="img" aria-label="Epidermis tersenyum lega" style="flex: 0 0 200px">
<ellipse cx="100" cy="226" rx="70" ry="9" fill="#BCCADA"/>
{epi("e6",-34,-6,0.6,e_happy())}
</svg>
</div></div>
<div style="position: absolute; left: 210px; right: 80px; bottom: 48px; font-size: 26px; line-height: 1.35; font-weight: 600; color: #6B6558">Ceritanya fiksi, epidermis tidak berbicara. Yang didukung bukti: mendinginkan luka bakar dengan air mengalir sekitar 20 menit dianjurkan. Luka yang dalam atau luas perlu diperiksa tenaga kesehatan.</div>"""
os.makedirs(out,exist_ok=True)
for i,s in enumerate([s1,s2,s3,s4,s5,s6],1):
    open(f'{out}/slide{i}.html','w').write(page(i,s))

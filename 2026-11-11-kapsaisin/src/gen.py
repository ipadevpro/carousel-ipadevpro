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
<path d="M 200 100 C 200 60 300 60 300 100 C 322 200 312 300 272 400 C 262 426 238 426 233 400 C 193 300 188 200 200 100 Z" fill="#A82418" transform="translate(9 9)"/>
<path d="M 245 78 C 245 40 270 24 292 18 L 299 38 C 283 44 270 56 270 80 Z" fill="#4E9A3E" stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round"/>
<path d="M 200 100 C 200 60 300 60 300 100 C 322 200 312 300 272 400 C 262 426 238 426 233 400 C 193 300 188 200 200 100 Z" fill="#E03A2B" stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round"/>
<path d="M 188 98 C 188 66 312 66 312 98 C 290 122 210 122 188 98 Z" fill="#4E9A3E" stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round"/>
<path d="M 214 160 C 208 210 212 260 228 320" fill="none" stroke="#F5A79B" stroke-width="12" stroke-linecap="round"/>
<g transform="translate(0 0)">{eyes}</g></g>'''
def _eyes(dy=0,brow=False):
    b='<path d="M 205 148 L 238 160 M 305 148 L 272 160" fill="none" stroke="#1B1B1F" stroke-width="7" stroke-linecap="round"/>' if brow else ''
    return f'<circle cx="238" cy="200" r="25" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="5"/><circle cx="278" cy="200" r="25" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="5"/><circle cx="243" cy="{205+dy}" r="10" fill="#1B1B1F"/><circle cx="283" cy="{205+dy}" r="10" fill="#1B1B1F"/><circle cx="246" cy="{201+dy}" r="3" fill="#FFFDF6"/><circle cx="286" cy="{201+dy}" r="3" fill="#FFFDF6"/>{b}'
def e_calm(): return _eyes()+'<path d="M 240 262 Q 258 276 276 262" fill="none" stroke="#1B1B1F" stroke-width="6" stroke-linecap="round"/>'
def e_worried(): return _eyes(2,True)+'<path d="M 240 276 Q 258 258 276 276" fill="none" stroke="#1B1B1F" stroke-width="6" stroke-linecap="round"/>'
def e_happy(): return '<path d="M 218 208 Q 238 180 258 208 M 262 208 Q 282 180 302 208" fill="none" stroke="#1B1B1F" stroke-width="7" stroke-linecap="round"/><path d="M 236 256 Q 258 284 282 256" fill="none" stroke="#1B1B1F" stroke-width="7" stroke-linecap="round"/>'
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


drop="""<ellipse cx="130" cy="318" rx="80" ry="12" fill="#BCCADA"/>
<g stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round"><path d="M 130 120 C 170 180 200 220 200 262 A 70 70 0 0 1 60 262 C 60 220 90 180 130 120 Z" fill="#6FB3E0"/></g><path d="M 95 250 C 95 232 105 218 115 205" fill="none" stroke="#FFFDF6" stroke-width="10" stroke-linecap="round"/>"""
mata="""<ellipse cx="395" cy="318" rx="100" ry="12" fill="#BCCADA"/>
<g stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round"><path d="M 310 230 C 350 160 440 160 480 230 C 440 300 350 300 310 230 Z" fill="#FFFDF6"/><circle cx="395" cy="230" r="38" fill="#B5483A"/><circle cx="395" cy="230" r="16" fill="#1B1B1F"/></g>
"""
s1=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 30px">
<div style="font-size: 58px; line-height: 1.04; font-weight: 900; font-variation-settings: 'opsz' 32; letter-spacing: -1.5px">TANGAN ANAK YANG PANAS SETELAH MENGULEK CABAI TIDAK CUKUP {hl("DISIRAM AIR BERKALI-KALI.")}</div>
<div style="font-size: 44px; line-height: 1.1; font-weight: 900; font-variation-settings: 'opsz' 32; color: #B5483A">DAN MATANYA JANGAN DIKUCEK DENGAN TANGAN ITU.</div>
<svg style="margin-top: 120px" width="790" height="350" viewBox="0 0 790 350" role="img" aria-label="Setetes air dan sebuah mata, masing-masing dicoret tanda larangan">
<g transform="translate(130 0)">{drop}</g><g transform="translate(135 0)">{mata}</g>{ban(260,190,110)}{ban(525,190,110)}
</svg>
</div>
<div style="position: absolute; left: 210px; right: 80px; bottom: 56px; font-size: 32px; font-weight: 700; color: #1B1B1F">Geser untuk tahu kenapa →</div>"""

s2=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 28px">
<div style="align-self: flex-start; padding: 10px 22px; border: 3px solid #1B1B1F; border-radius: 6px; background: #FFFDF6; font-size: 32px; line-height: 1.3; font-weight: 800">Namaku: Kapsaisin.<br>Julukanku: Si Api Tanpa Api.</div>
<div style="font-size: 56px; line-height: 1.07; {H}">KAMU MENGIRA AIR CUKUP UNTUK MENGANGKATKU.</div>
<div style="font-size: 56px; line-height: 1.07; {H}">{hl("AIR HAMPIR TIDAK BISA MELARUTKANKU.")}</div>
<div style="font-size: 34px; line-height: 1.4; font-weight: 500">Aku senyawa di dalam cabai, paling banyak di bagian urat putih dan sekitar bijinya. Aku tidak membakar kulit sungguhan. Aku menipu saraf, membuatnya mengirim sinyal "panas" padahal suhu kulit tidak naik.</div>
<svg width="790" height="400" viewBox="0 0 790 400" role="img" aria-label="Kapsaisin, tokoh cabai merah, tersenyum tenang">
<ellipse cx="200" cy="382" rx="120" ry="12" fill="#BCCADA"/>
{epi("e2",20,-14,0.9,e_calm())}
<text x="560" y="170" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-weight="800" font-size="32" fill="#6B6558">sinyal panas,</text>
<text x="560" y="214" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-weight="800" font-size="32" fill="#6B6558">suhu kulit</text>
<text x="560" y="258" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-weight="800" font-size="32" fill="#6B6558">tidak naik</text>
</svg>
</div>"""

def item(label,txt):
    return f"""<div style="display: flex; flex-direction: column; gap: 14px">
<div style="align-self: flex-start; padding: 6px 20px; background: #FFFDF6; border: 3px solid #1B1B1F; color: #1B1B1F; border-radius: 6px; font-size: 32px; font-weight: 800">{label}</div>
<div style="font-size: 44px; line-height: 1.34; font-weight: 500">{txt}</div></div>"""
s3=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 40px">
<div style="font-size: 76px; line-height: 1.05; {H}">KENAPA MITOSNYA {hl("KELIRU?")}</div>
{item("AKU LARUT DI MINYAK","Aku larut dalam minyak, bukan dalam air. Es mengurangi panasnya sebentar, tapi perihnya kembali karena aku masih menempel.")}
{item("MENGUCEK = MENGGOSOK RATA","Mengucek mata hanya menggosokku lebih rata. Mata bisa makin merah dan perih, dan permukaan kornea bisa tergores.")}
<div style="font-size: 42px; line-height: 1.35; font-weight: 800; color: #B5483A; margin-top: 10px">Seperti noda minyak di piring: disiram air berkali-kali tetap licin. Baru terangkat begitu ada sabun.</div>
</div>"""

def step(n,t):
    return f"""<div style="display: flex; gap: 26px; align-items: flex-start">
<div style="flex: 0 0 72px; width: 72px; height: 72px; border-radius: 36px; background: #B5483A; border: 4px solid #1B1B1F; box-sizing: border-box; color: #FBF3DF; display: flex; align-items: center; justify-content: center; font-size: 40px; font-weight: 900">{n}</div>
<div style="flex: 1 1 0; min-width: 0; font-size: 40px; line-height: 1.34; font-weight: 600">{t}</div></div>"""
s4=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 54px">
<div style="font-size: 76px; line-height: 1.04; {H}">WAHAI {hl("GURU:")}</div>
{step(1,'<span style="font-weight: 900">Wajibkan</span> sarung tangan saat memotong cabai di kegiatan memasak atau praktikum.')}
{step(2,'<span style="font-weight: 900">Ajarkan</span> aturan: jangan sentuh mata, hidung, dan wajah setelah memegang cabai.')}
{step(3,'<span style="font-weight: 900">Jadikan</span> contoh sains: reseptor saraf dan kelarutan zat, polar dan nonpolar.')}
<div style="margin-top: 50px">{scene("e4",e_calm(),"JANGAN","DIKUCEK, YA","Kapsaisin tenang berkata: jangan dikucek ya",250)}</div>
</div>"""

def bul(t): return f'<div style="display: flex; gap: 22px"><span aria-hidden="true" style="flex: 0 0 18px; width: 18px; height: 18px; margin-top: 15px; background: #B5483A; border: 3px solid #1B1B1F; box-sizing: border-box; border-radius: 3px"></span><span>{t}</span></div>'
s5=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 34px">
<div style="font-size: 62px; line-height: 1.06; {H}">UNTUK {hl("AYAH DAN BUNDA:")}</div>
<div style="display: flex; flex-direction: column; gap: 30px; font-size: 40px; line-height: 1.28; font-weight: 700">
{bul("tangan panas karena cabai: cuci dengan sabun berkali-kali; sedikit minyak goreng lalu dicuci sabun juga bisa dicoba")}
{bul("cabai kena mata: jangan dikucek, bilas dengan air bersih mengalir beberapa menit")}
{bul("ke dokter atau IGD bila mata tetap sangat nyeri, merah, penglihatan kabur, atau tidak bisa dibuka setelah dibilas")}
</div>
<div style="margin-top: 36px">{scene("e5",e_worried(),"SABUN UNTUK","TANGAN","Kapsaisin tampak cemas dan berkata: sabun untuk tangan",250)}</div>
</div>"""

s6=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 30px">
<div style="font-size: 40px; line-height: 1.3; font-weight: 500">Aku tidak bermaksud melukai. Cabai membuatku untuk melindungi bijinya dari hewan pemakan.</div>
<div style="font-size: 58px; line-height: 1.06; {H}">KALAU AKU MENEMPEL DI TANGAN ANAKMU, JANGAN LAWAN AKU DENGAN ES. {hl("LEPASKAN AKU DENGAN SABUN.")}</div>
<div style="font-size: 44px; font-weight: 800; color: #B5483A">Salam, Kapsaisin.</div>
<div style="margin-top: 4px; display: flex; gap: 20px; align-items: center">
<div style="flex: 1 1 0; min-width: 0; border: 4px solid #1B1B1F; border-radius: 16px; padding: 22px 28px; background: #FFFDF6; display: flex; flex-direction: column; gap: 10px">
<div style="font-size: 36px; line-height: 1.2; font-weight: 900">Simpan, lalu kirim ke guru yang kamu kenal.</div>
</div>
<svg width="200" height="240" viewBox="0 0 200 240" role="img" aria-label="Kapsaisin tersenyum lega" style="flex: 0 0 200px">
<ellipse cx="100" cy="226" rx="50" ry="9" fill="#BCCADA"/>
{epi("e6",-40,-6,0.55,e_happy())}
</svg>
</div></div>
<div style="position: absolute; left: 210px; right: 80px; bottom: 40px; font-size: 25px; line-height: 1.35; font-weight: 600; color: #6B6558">Ceritanya fiksi. Yang didukung bukti: kapsaisin mengaktifkan reseptor TRPV1 dan larut dalam lemak, bukan air; bilasan air mengalir adalah pertolongan pertama yang dianjurkan untuk zat yang mengenai mata. Penelitian tentang cara terbaik menghilangkan rasa panas cabai di kulit masih sedikit.</div>
"""
import os
out=sys.argv[1]
os.makedirs(out,exist_ok=True)
for i,x in enumerate([s1,s2,s3,s4,s5,s6],1):
    open(f'{out}/slide{i}.html','w').write(page(i,x))

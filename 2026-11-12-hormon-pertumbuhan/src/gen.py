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
<ellipse cx="150" cy="240" rx="112" ry="142" fill="#3A4585" transform="translate(9 9)"/>
<ellipse cx="150" cy="240" rx="112" ry="142" fill="#6674C9" stroke="#1B1B1F" stroke-width="7"/>
<path d="M 70 130 C 70 40 230 40 230 130 Z" fill="#FFC93C" stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round"/>
<rect x="50" y="124" width="200" height="26" rx="13" fill="#FFC93C" stroke="#1B1B1F" stroke-width="7"/>
<path d="M 150 44 L 150 124" stroke="#1B1B1F" stroke-width="6"/>
<path d="M 100 215 C 90 255 95 300 110 335" fill="none" stroke="#A9B3EC" stroke-width="12" stroke-linecap="round"/>
<g transform="translate(-108 -4)">{eyes}</g></g>'''
def _eyes(dy=0,brow=False):
    b='<path d="M 205 165 L 238 177 M 305 165 L 272 177" fill="none" stroke="#1B1B1F" stroke-width="7" stroke-linecap="round"/>' if brow else ''
    return f'<circle cx="238" cy="220" r="25" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="5"/><circle cx="278" cy="220" r="25" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="5"/><circle cx="243" cy="{225+dy}" r="10" fill="#1B1B1F"/><circle cx="283" cy="{225+dy}" r="10" fill="#1B1B1F"/><circle cx="246" cy="{221+dy}" r="3" fill="#FFFDF6"/><circle cx="286" cy="{221+dy}" r="3" fill="#FFFDF6"/>{b}'
def e_calm(): return _eyes()+'<path d="M 240 282 Q 258 296 276 282" fill="none" stroke="#1B1B1F" stroke-width="6" stroke-linecap="round"/>'
def e_worried(): return _eyes(2,True)+'<path d="M 240 296 Q 258 278 276 296" fill="none" stroke="#1B1B1F" stroke-width="6" stroke-linecap="round"/>'
def e_happy(): return '<path d="M 218 228 Q 238 200 258 228 M 262 228 Q 282 200 302 228" fill="none" stroke="#1B1B1F" stroke-width="7" stroke-linecap="round"/><path d="M 236 276 Q 258 304 282 276" fill="none" stroke="#1B1B1F" stroke-width="7" stroke-linecap="round"/>'
def e_sleep(): return '<path d="M 215 224 Q 238 240 261 224 M 259 224 Q 282 240 305 224" fill="none" stroke="#1B1B1F" stroke-width="7" stroke-linecap="round"/><path d="M 240 282 Q 258 292 276 282" fill="none" stroke="#1B1B1F" stroke-width="6" stroke-linecap="round"/>'
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



bar="""<ellipse cx="130" cy="318" rx="100" ry="12" fill="#BCCADA"/>
<g stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"><rect x="40" y="130" width="26" height="188" rx="6" fill="#8A8F9C"/><rect x="194" y="130" width="26" height="188" rx="6" fill="#8A8F9C"/><rect x="30" y="118" width="200" height="26" rx="13" fill="#B5483A"/></g>"""
milk="""<ellipse cx="130" cy="318" rx="90" ry="12" fill="#BCCADA"/>
<g stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round"><path d="M 70 150 L 190 150 L 190 310 L 70 310 Z" fill="#FFFDF6"/><path d="M 70 150 L 100 110 L 160 110 L 190 150 Z" fill="#6FB3E0"/><rect x="70" y="200" width="120" height="60" fill="#6FB3E0"/></g>"""
s1=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 30px">
<div style="font-size: 56px; line-height: 1.04; font-weight: 900; font-variation-settings: 'opsz' 32; letter-spacing: -1.5px">ANAK YANG DISURUH BERGELANTUNGAN DI PALANG SETIAP SORE {hl("TIDAK AKAN BERTAMBAH TINGGI")} KARENA ITU.</div>
<div style="font-size: 44px; line-height: 1.1; font-weight: 900; font-variation-settings: 'opsz' 32; color: #B5483A">DAN SUSU "PENINGGI BADAN" BUKAN TOMBOL AJAIB.</div>
<svg style="margin-top: 90px" width="790" height="350" viewBox="0 0 790 350" role="img" aria-label="Palang besi dan kotak susu, masing-masing dicoret tanda larangan">
<g transform="translate(130 0)">{bar}</g><g transform="translate(400 0)">{milk}</g>{ban(260,190,110)}{ban(525,190,110)}
</svg>
</div>
<div style="position: absolute; left: 210px; right: 80px; bottom: 56px; font-size: 32px; font-weight: 700; color: #1B1B1F">Geser untuk tahu kenapa →</div>"""

s2=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 28px">
<div style="align-self: flex-start; padding: 10px 22px; border: 3px solid #1B1B1F; border-radius: 6px; background: #FFFDF6; font-size: 32px; line-height: 1.3; font-weight: 800">Namaku: Hormon Pertumbuhan.<br>Julukanku: Si Pekerja Malam.</div>
<div style="font-size: 54px; line-height: 1.07; {H}">KAMU MENGIRA AKU BEKERJA SAAT DIA BERGELANTUNGAN.</div>
<div style="font-size: 54px; line-height: 1.07; {H}">{hl("AKU PALING BANYAK BEKERJA SAAT DIA TIDUR NYENYAK.")}</div>
<div style="font-size: 34px; line-height: 1.4; font-weight: 500">Aku dilepaskan oleh kelenjar hipofisis di dasar otak. Aku membantu tulang, otot, dan organ tumbuh, terutama di masa anak dan remaja. Pelepasanku yang besar banyak terjadi di fase tidur dalam.</div>
<svg width="790" height="330" viewBox="0 0 790 330" role="img" aria-label="Hormon Pertumbuhan, tokoh biru bertopi proyek kuning, tersenyum tenang">
<ellipse cx="190" cy="314" rx="120" ry="12" fill="#BCCADA"/>
{epi("e2",20,-10,0.72,e_calm())}
<text x="560" y="130" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-weight="800" font-size="32" fill="#6B6558">jam kerjaku:</text>
<text x="560" y="174" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-weight="800" font-size="32" fill="#6B6558">saat dia tidur</text>
<text x="560" y="218" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-weight="800" font-size="32" fill="#6B6558">nyenyak</text>
</svg>
</div>"""

def item(label,txt):
    return f"""<div style="display: flex; flex-direction: column; gap: 14px">
<div style="align-self: flex-start; padding: 6px 20px; background: #FFFDF6; border: 3px solid #1B1B1F; color: #1B1B1F; border-radius: 6px; font-size: 32px; font-weight: 800">{label}</div>
<div style="font-size: 42px; line-height: 1.34; font-weight: 500">{txt}</div></div>"""
s3=f"""<div style="position: absolute; left: 210px; right: 80px; top: 140px; display: flex; flex-direction: column; gap: 32px">
<div style="font-size: 76px; line-height: 1.05; {H}">KENAPA MITOSNYA {hl("KELIRU?")}</div>
{item("GANTUNG = PANJANG SEMENTARA","Bergelantungan meregangkan bantalan di antara tulang belakang sedikit, jadi tubuh bisa sedikit lebih panjang sesaat. Setelah berdiri dan beraktivitas, kembali seperti semula.")}
{item("TULANG MEMANJANG DI UJUNGNYA","Tulang memanjang di lempeng pertumbuhan dekat ujung tulang. Di sana aku bekerja, dibantu gizi cukup, hormon lain, dan tidur.")}
<div style="font-size: 40px; line-height: 1.33; font-weight: 800; color: #B5483A; margin-top: 0px">Seperti tukang bangunan yang hanya datang malam hari: kalau malamnya terang dan bising, ia tidak bisa bekerja.</div>
</div>"""

def step(n,t):
    return f"""<div style="display: flex; gap: 26px; align-items: flex-start">
<div style="flex: 0 0 72px; width: 72px; height: 72px; border-radius: 36px; background: #B5483A; border: 4px solid #1B1B1F; box-sizing: border-box; color: #FBF3DF; display: flex; align-items: center; justify-content: center; font-size: 40px; font-weight: 900">{n}</div>
<div style="flex: 1 1 0; min-width: 0; font-size: 40px; line-height: 1.34; font-weight: 600">{t}</div></div>"""
s4=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 46px">
<div style="font-size: 76px; line-height: 1.04; {H}">WAHAI {hl("GURU:")}</div>
{step(1,'<span style="font-weight: 900">Hindari</span> menjadikan tinggi badan bahan ejekan atau julukan di kelas.')}
{step(2,'<span style="font-weight: 900">Jelaskan</span> peran tidur dan gizi saat membahas pertumbuhan, bukan janji iklan.')}
{step(3,'<span style="font-weight: 900">Sampaikan</span> ke orang tua lewat jalur sekolah bila ada murid yang tampak tidak tumbuh selama setahun.')}
<div style="margin-top: 20px">{scene("e4",e_calm(),"BUKAN JANJI","IKLAN, YA","Hormon Pertumbuhan tenang berkata: bukan janji iklan ya",250)}</div>
</div>"""

def bul(t): return f'<div style="display: flex; gap: 22px"><span aria-hidden="true" style="flex: 0 0 18px; width: 18px; height: 18px; margin-top: 15px; background: #B5483A; border: 3px solid #1B1B1F; box-sizing: border-box; border-radius: 3px"></span><span>{t}</span></div>'
s5=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 30px">
<div style="font-size: 62px; line-height: 1.06; {H}">UNTUK {hl("AYAH DAN BUNDA:")}</div>
<div style="display: flex; flex-direction: column; gap: 26px; font-size: 38px; line-height: 1.28; font-weight: 700">
{bul("utamakan makan bergizi seimbang (protein, sayur, buah) dan tidur cukup, sekitar 8 sampai 10 jam untuk remaja")}
{bul("olahraga apa pun bagus untuk kesehatan, tetapi bukan alat peninggi")}
{bul("konsultasikan ke dokter anak bila tinggi anak tidak bertambah dalam setahun, jauh di bawah teman sebaya dan keluarga, atau tanda pubertas belum muncul saat teman seusianya sudah")}
</div>
<div style="margin-top: 14px">{scene("e5",e_sleep(),"MATIKAN LAMPU,","SIMPAN PONSEL","Hormon Pertumbuhan memejamkan mata dan berkata: matikan lampu, simpan ponsel",250)}</div>
</div>"""

s6=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 40px">
<div style="font-size: 46px; line-height: 1.3; font-weight: 500">Aku tidak bisa dipaksa dengan tarikan. Aku juga tidak bisa dibeli dalam satu kaleng.</div>
<div style="font-size: 66px; line-height: 1.06; {H}">MATIKAN LAMPUNYA, SIMPAN PONSELNYA, DAN {hl("BIARKAN AKU BEKERJA.")}</div>
<div style="font-size: 48px; font-weight: 800; color: #B5483A">Salam, Hormon Pertumbuhan.</div>
<div style="margin-top: 4px; display: flex; gap: 20px; align-items: center">
<div style="flex: 1 1 0; min-width: 0; border: 4px solid #1B1B1F; border-radius: 16px; padding: 30px 34px; background: #FFFDF6; display: flex; flex-direction: column; gap: 10px">
<div style="font-size: 42px; line-height: 1.2; font-weight: 900">Simpan, lalu kirim ke guru yang kamu kenal.</div>
</div>
<svg width="230" height="280" viewBox="0 0 200 240" role="img" aria-label="Hormon Pertumbuhan tersenyum lega" style="flex: 0 0 230px">
<ellipse cx="100" cy="226" rx="50" ry="9" fill="#BCCADA"/>
{epi("e6",-18,2,0.56,e_happy())}
</svg>
</div></div>
<div style="position: absolute; left: 210px; right: 80px; bottom: 40px; font-size: 25px; line-height: 1.35; font-weight: 600; color: #6B6558">Ceritanya fiksi. Yang didukung bukti: tinggi badan sangat dipengaruhi genetik, gizi, dan kesehatan; hormon pertumbuhan banyak dilepaskan saat tidur dalam; peregangan tulang belakang hanya menambah panjang sementara. Seberapa besar tidur memengaruhi tinggi akhir pada anak sehat belum bisa diukur pasti.</div>
"""
import os
out=sys.argv[1]
os.makedirs(out,exist_ok=True)
for i,x in enumerate([s1,s2,s3,s4,s5,s6],1):
    open(f'{out}/slide{i}.html','w').write(page(i,x))

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
<path d="M250 30 C 300 120 372 200 372 275 A122 122 0 0 1 128 275 C 128 200 200 120 250 30 Z" fill="#B8431F" transform="translate(8 8)"/>
<path d="M250 30 C 300 120 372 200 372 275 A122 122 0 0 1 128 275 C 128 200 200 120 250 30 Z" fill="#E8743A" stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round"/>
<path d="M165 285 C 165 240 190 205 214 170" fill="none" stroke="#F7C4A0" stroke-width="20" stroke-linecap="round"/>
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


silet="""<ellipse cx="130" cy="318" rx="95" ry="12" fill="#BCCADA"/>
<g stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round"><polygon points="50,200 210,150 210,270 50,270" fill="#D5DADF"/><rect x="56" y="206" width="40" height="40" rx="6" fill="#FFFDF6"/><line x1="90" y1="262" x2="205" y2="262" stroke="#9AA4AE" stroke-width="5"/></g>"""
jerigen="""<ellipse cx="395" cy="318" rx="100" ry="12" fill="#BCCADA"/>
<g stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round"><path d="M 335 150 L 435 150 L 460 180 L 460 300 L 335 300 Z" fill="#C0392B"/><rect x="345" y="120" width="44" height="34" rx="6" fill="#1B1B1F"/><rect x="360" y="195" width="70" height="60" rx="8" fill="#FFFDF6"/></g>
<path d="M 385 232 q 10 -26 20 0 q -10 14 -20 0 Z" fill="#1B1B1F"/>"""
s1=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 30px">
<div style="font-size: 60px; line-height: 1.04; font-weight: 900; font-variation-settings: 'opsz' 32; letter-spacing: -1.5px">ANAK YANG DIGIGIT LIPAN SAAT KERJA BAKTI JANGAN DISAYAT SUPAYA {hl('"RACUNNYA KELUAR".')}</div>
<div style="font-size: 44px; line-height: 1.1; font-weight: 900; font-variation-settings: 'opsz' 32; color: #B5483A">DAN LUKANYA JANGAN DIOLESI BENSIN ATAU MINYAK TANAH.</div>
<svg style="margin-top: 170px" width="790" height="350" viewBox="0 0 790 350" role="img" aria-label="Sebuah silet dan sebuah jerigen bensin, masing-masing dicoret tanda larangan">
<g transform="translate(130 0)">{silet}</g><g transform="translate(135 0)">{jerigen}</g>{ban(260,190,110)}{ban(525,190,110)}
</svg>
</div>
<div style="position: absolute; left: 210px; right: 80px; bottom: 56px; font-size: 32px; font-weight: 700; color: #1B1B1F">Geser untuk tahu kenapa →</div>"""

s2=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 28px">
<div style="align-self: flex-start; padding: 10px 22px; border: 3px solid #1B1B1F; border-radius: 6px; background: #FFFDF6; font-size: 32px; line-height: 1.3; font-weight: 800">Namaku: Bisa Lipan.<br>Julukanku: Si Api di Ujung Taring.</div>
<div style="font-size: 56px; line-height: 1.07; {H}">KAMU MENGIRA AKU BISA DIKELUARKAN LEWAT SAYATAN.</div>
<div style="font-size: 56px; line-height: 1.07; {H}">{hl("SAYATAN TIDAK BISA MENYUSULKU.")}</div>
<div style="font-size: 34px; line-height: 1.4; font-weight: 500">Aku cairan dari kelenjar di sepasang "taring" depan lipan, yang sebenarnya kaki pertama yang berubah bentuk. Pada manusia, aku lebih sering membuat sakit hebat daripada bahaya besar.</div>
<svg width="790" height="400" viewBox="0 0 790 400" role="img" aria-label="Bisa Lipan, tokoh tetesan oranye kemerahan, tersenyum tenang">
<ellipse cx="200" cy="382" rx="150" ry="12" fill="#BCCADA"/>
{epi("e2",20,-14,0.98,e_calm())}
<text x="610" y="170" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-weight="800" font-size="32" fill="#6B6558">lebih sering sakit</text>
<text x="610" y="214" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-weight="800" font-size="32" fill="#6B6558">hebat daripada</text>
<text x="610" y="258" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-weight="800" font-size="32" fill="#6B6558">bahaya besar</text>
</svg>
</div>"""

def item(label,txt):
    return f"""<div style="display: flex; flex-direction: column; gap: 14px">
<div style="align-self: flex-start; padding: 6px 20px; background: #FFFDF6; border: 3px solid #1B1B1F; color: #1B1B1F; border-radius: 6px; font-size: 32px; font-weight: 800">{label}</div>
<div style="font-size: 44px; line-height: 1.34; font-weight: 500">{txt}</div></div>"""
s3=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 44px">
<div style="font-size: 76px; line-height: 1.05; {H}">KENAPA MITOSNYA {hl("KELIRU?")}</div>
{item("AKU SUDAH MENYEBAR","Aku sudah masuk sejak gigitan pertama dan menyebar di jaringan sekitar. Aku memicu nyeri tajam, panas, kemerahan, dan bengkak.")}
{item("SAYATAN = LUKA BARU","Sayatan hanya menambah luka terbuka yang bisa terinfeksi. Bensin dan minyak tanah juga bisa mengiritasi kulit.")}
<div style="font-size: 42px; line-height: 1.35; font-weight: 800; color: #B5483A; margin-top: 12px">Seperti tinta tumpah di kain: menggunting kain tidak mengembalikan tintanya ke botol. Kainmu justru berlubang.</div>
</div>"""

def step(n,t):
    return f"""<div style="display: flex; gap: 26px; align-items: flex-start">
<div style="flex: 0 0 72px; width: 72px; height: 72px; border-radius: 36px; background: #B5483A; border: 4px solid #1B1B1F; box-sizing: border-box; color: #FBF3DF; display: flex; align-items: center; justify-content: center; font-size: 40px; font-weight: 900">{n}</div>
<div style="flex: 1 1 0; min-width: 0; font-size: 40px; line-height: 1.34; font-weight: 600">{t}</div></div>"""
s4=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 54px">
<div style="font-size: 76px; line-height: 1.04; {H}">WAHAI {hl("GURU:")}</div>
{step(1,'<span style="font-weight: 900">Wajibkan</span> sarung tangan dan alas kaki tertutup saat kerja bakti, terutama di gudang dan tumpukan barang lembap.')}
{step(2,'<span style="font-weight: 900">Siapkan</span> sabun, air bersih, kompres dingin, dan kotak P3K di lokasi.')}
{step(3,'<span style="font-weight: 900">Bawa segera</span> ke fasilitas kesehatan murid yang sesak, pusing berat, atau bengkaknya cepat meluas.')}
<div style="margin-top: 50px">{scene("e4",e_calm(),"JANGAN","DISAYAT, YA","Bisa Lipan tenang berkata: jangan disayat ya",250)}</div>
</div>"""

def bul(t): return f'<div style="display: flex; gap: 22px"><span aria-hidden="true" style="flex: 0 0 18px; width: 18px; height: 18px; margin-top: 15px; background: #B5483A; border: 3px solid #1B1B1F; box-sizing: border-box; border-radius: 3px"></span><span>{t}</span></div>'
s5=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 34px">
<div style="font-size: 62px; line-height: 1.06; {H}">UNTUK {hl("AYAH DAN BUNDA:")}</div>
<div style="display: flex; flex-direction: column; gap: 30px; font-size: 40px; line-height: 1.28; font-weight: 700">
{bul("cuci luka dengan sabun dan air mengalir, kompres dingin, dan tinggikan bagian yang digigit")}
{bul("jangan disayat, diisap, diikat kencang, atau diolesi bensin atau minyak tanah")}
{bul("ke fasilitas kesehatan bila nyeri tak tertahankan, bengkak meluas, muncul sesak atau biduran di tempat lain, ada tanda infeksi, atau status imunisasi tetanus anak tidak jelas")}
</div>
<div style="margin-top: 36px">{scene("e5",e_worried(),"CUCI, KOMPRES,","TINGGIKAN","Bisa Lipan tampak cemas dan berkata: cuci, kompres, tinggikan",250)}</div>
</div>"""

s6=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 30px">
<div style="font-size: 40px; line-height: 1.3; font-weight: 500">Aku bukan musuh yang sengaja mencari anakmu. Lipan itu hanya terkejut rumahnya diangkat.</div>
<div style="font-size: 60px; line-height: 1.06; {H}">SAKITKU SEPERTI API, TAPI BIASANYA PADAM DALAM SATU-DUA HARI {hl("KALAU LUKANYA DIRAWAT DENGAN BENAR.")}</div>
<div style="font-size: 44px; font-weight: 800; color: #B5483A">Salam, Bisa Lipan.</div>
<div style="margin-top: 4px; display: flex; gap: 20px; align-items: center">
<div style="flex: 1 1 0; min-width: 0; border: 4px solid #1B1B1F; border-radius: 16px; padding: 22px 28px; background: #FFFDF6; display: flex; flex-direction: column; gap: 10px">
<div style="font-size: 36px; line-height: 1.2; font-weight: 900">Simpan, lalu kirim ke guru yang kamu kenal.</div>
</div>
<svg width="200" height="240" viewBox="0 0 200 240" role="img" aria-label="Bisa Lipan tersenyum lega" style="flex: 0 0 200px">
<ellipse cx="100" cy="226" rx="70" ry="9" fill="#BCCADA"/>
{epi("e6",-48,-6,0.6,e_happy())}
</svg>
</div></div>
<div style="position: absolute; left: 210px; right: 80px; bottom: 40px; font-size: 25px; line-height: 1.35; font-weight: 600; color: #6B6558">Ceritanya fiksi. Yang didukung bukti: gigitan lipan umumnya menyebabkan nyeri dan bengkak setempat yang membaik dalam satu sampai dua hari, dan menyayat luka tidak dianjurkan. Reaksi berat jarang, tetapi perlu penanganan medis segera.</div>
"""
import os
out=sys.argv[1]
os.makedirs(out,exist_ok=True)
for i,x in enumerate([s1,s2,s3,s4,s5,s6],1):
    open(f'{out}/slide{i}.html','w').write(page(i,x))

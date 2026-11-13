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
<circle cx="150" cy="240" r="100" fill="#9A6414" transform="translate(9 9)"/>
<circle cx="150" cy="240" r="100" fill="#F2B73D" stroke="#1B1B1F" stroke-width="7"/>
<path d="M 82 215 C 86 180 108 160 130 152" fill="none" stroke="#FFE9A8" stroke-width="12" stroke-linecap="round"/>
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



drum="""<ellipse cx="130" cy="318" rx="100" ry="12" fill="#BCCADA"/>
<g stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"><path d="M 150 250 L 95 300" fill="none" stroke-width="16"/><circle cx="84" cy="300" r="12" fill="#FFFDF6"/><circle cx="104" cy="312" r="12" fill="#FFFDF6"/><path d="M 130 70 C 200 60 230 140 190 210 C 160 255 110 250 90 215 C 65 170 80 80 130 70 Z" fill="#D98B3A"/><path d="M 120 100 C 140 90 175 100 180 130" fill="none" stroke="#F4C27A" stroke-width="10"/></g>"""
syr="""<ellipse cx="130" cy="318" rx="100" ry="12" fill="#BCCADA"/>
<g stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"><rect x="95" y="90" width="70" height="150" rx="8" fill="#FFFDF6"/><rect x="108" y="150" width="44" height="82" fill="#F2B73D" stroke-width="0"/><rect x="95" y="90" width="70" height="150" rx="8" fill="none"/><path d="M 80 90 L 180 90 M 130 90 L 130 40 M 105 40 L 155 40" fill="none"/><path d="M 130 240 L 130 306" fill="none" stroke-width="6"/><path d="M 100 130 L 125 130 M 100 160 L 125 160 M 100 190 L 125 190" fill="none" stroke-width="5"/></g>"""

s1=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 30px">
<div style="font-size: 60px; line-height: 1.04; font-weight: 900; font-variation-settings: 'opsz' 32; letter-spacing: -1.5px">REMAJA PUTRI YANG {hl("HAID LEBIH CEPAT")} DARI IBUNYA DULU BUKAN KARENA AYAM "SUNTIKAN HORMON".</div>
<div style="font-size: 44px; line-height: 1.1; font-weight: 900; font-variation-settings: 'opsz' 32; color: #B5483A">AYAMNYA TIDAK DISUNTIK, DAN TIDAK PERLU DILARANG.</div>
<svg style="margin-top: 80px" width="790" height="350" viewBox="0 0 790 350" role="img" aria-label="Paha ayam dan jarum suntik, masing-masing dicoret tanda larangan">
<g transform="translate(130 0)">{drum}</g><g transform="translate(400 0)">{syr}</g>{ban(260,190,110)}{ban(525,190,110)}
</svg>
</div>
<div style="position: absolute; left: 210px; right: 80px; bottom: 56px; font-size: 32px; font-weight: 700; color: #1B1B1F">Geser untuk tahu kenapa →</div>"""

s2=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 28px">
<div style="align-self: flex-start; padding: 10px 22px; border: 3px solid #1B1B1F; border-radius: 6px; background: #FFFDF6; font-size: 32px; line-height: 1.3; font-weight: 800">Namaku: Leptin.<br>Julukanku: Si Pelapor Cadangan.</div>
<div style="font-size: 54px; line-height: 1.07; {H}">KAMU MENGIRA AKU SUNTIKAN.</div>
<div style="font-size: 54px; line-height: 1.07; {H}">{hl("AKU HANYA LAPORAN DARI SEL LEMAK.")}</div>
<div style="font-size: 34px; line-height: 1.4; font-weight: 500">Aku hormon yang dibuat sel-sel lemak. Tugasku melapor ke otak: "Cadangan energi tubuh cukup." Laporanku ikut menjadi salah satu syarat otak memulai pubertas. Tubuh yang cadangannya cukup, apalagi berlebih, cenderung memulai pubertas lebih awal.</div>
<svg width="790" height="330" viewBox="0 0 790 330" role="img" aria-label="Leptin, tokoh bulat keemasan, tersenyum tenang">
<ellipse cx="190" cy="314" rx="120" ry="12" fill="#BCCADA"/>
{epi("e2",20,-4,0.84,e_calm())}
<text x="560" y="130" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-weight="800" font-size="32" fill="#6B6558">dari sel lemak</text>
<text x="560" y="174" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-weight="800" font-size="32" fill="#6B6558">ke otak:</text>
<text x="560" y="218" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-weight="800" font-size="32" fill="#6B6558">"bekal cukup"</text>
</svg>
</div>"""

def item(label,txt):
    return f"""<div style="display: flex; flex-direction: column; gap: 14px">
<div style="align-self: flex-start; padding: 6px 20px; background: #FFFDF6; border: 3px solid #1B1B1F; color: #1B1B1F; border-radius: 6px; font-size: 32px; font-weight: 800">{label}</div>
<div style="font-size: 42px; line-height: 1.34; font-weight: 500">{txt}</div></div>"""
s3=f"""<div style="position: absolute; left: 210px; right: 80px; top: 140px; display: flex; flex-direction: column; gap: 32px">
<div style="font-size: 76px; line-height: 1.05; {H}">KENAPA MITOSNYA {hl("KELIRU?")}</div>
{item("AYAM: TUMBUH CEPAT, TANPA SUNTIKAN","Ayam pedaging tumbuh cepat karena seleksi genetik puluhan tahun dan pakan yang terukur. Para ahli peternakan sudah berulang kali membantah kabar suntikan hormon.")}
{item("PUBERTAS: PENYEBABNYA BANYAK","Genetik keluarga, gizi yang lebih baik, dan berat badan. Saat cadangan lemak lebih banyak, aku melapor lebih keras.")}
<div style="font-size: 40px; line-height: 1.33; font-weight: 800; color: #B5483A; margin-top: 0px">Aku tidak menyuntikkan apa-apa. Aku hanya mengirim laporan.</div>
</div>"""

def step(n,t):
    return f"""<div style="display: flex; gap: 26px; align-items: flex-start">
<div style="flex: 0 0 72px; width: 72px; height: 72px; border-radius: 36px; background: #B5483A; border: 4px solid #1B1B1F; box-sizing: border-box; color: #FBF3DF; display: flex; align-items: center; justify-content: center; font-size: 40px; font-weight: 900">{n}</div>
<div style="flex: 1 1 0; min-width: 0; font-size: 40px; line-height: 1.34; font-weight: 600">{t}</div></div>"""
s4=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 40px">
<div style="font-size: 76px; line-height: 1.04; {H}">WAHAI {hl("GURU:")}</div>
{step(1,'<span style="font-weight: 900">Luruskan</span> mitos "ayam suntik" saat membahas sistem reproduksi, lewat mekanisme pubertas.')}
{step(2,'<span style="font-weight: 900">Siapkan</span> pembalut cadangan di UKS dan pastikan murid tahu harus ke mana bila haid datang di sekolah.')}
{step(3,'<span style="font-weight: 900">Hindari</span> komentar soal tubuh murid yang tumbuh lebih cepat; ejekan di usia ini sangat membekas.')}
<div style="margin-top: 10px">{scene("e4",e_calm(),"AKU LAPORAN,","BUKAN SUNTIKAN","Leptin tenang berkata: aku laporan, bukan suntikan",250)}</div>
</div>"""

def bul(t): return f'<div style="display: flex; gap: 22px"><span aria-hidden="true" style="flex: 0 0 18px; width: 18px; height: 18px; margin-top: 15px; background: #B5483A; border: 3px solid #1B1B1F; box-sizing: border-box; border-radius: 3px"></span><span>{t}</span></div>'
s5=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 40px">
<div style="font-size: 66px; line-height: 1.06; {H}">UNTUK {hl("AYAH DAN BUNDA:")}</div>
<div style="display: flex; flex-direction: column; gap: 34px; font-size: 40px; line-height: 1.3; font-weight: 700">
{bul("tidak perlu melarang ayam; ayam sumber protein yang murah dan baik")}
{bul("bicarakan haid sebelum datang, sekitar usia 9 sampai 10 tahun, dengan bahasa yang tenang")}
{bul("periksakan ke dokter bila tanda pubertas (payudara tumbuh) muncul sebelum usia 8 tahun pada anak perempuan atau sebelum 9 tahun pada anak laki-laki")}
</div>
<div style="margin-top: 20px">{scene("e5",e_worried(),"DIA BUTUH","PENJELASAN","Leptin berkata: yang dia butuhkan bukan larangan",250)}</div>
</div>"""

s6=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 44px">
<div style="font-size: 42px; line-height: 1.3; font-weight: 500">Aku bukan dari suntikan. Aku dari tubuh anakmu sendiri. Aku hanya melapor bahwa tubuhnya sudah punya cukup bekal untuk tumbuh dewasa.</div>
<div style="font-size: 58px; line-height: 1.06; {H}">YANG DIA BUTUHKAN BUKAN LARANGAN MAKAN AYAM. {hl("DIA BUTUH ORANG DEWASA YANG TENANG.")}</div>
<div style="font-size: 46px; font-weight: 800; color: #B5483A">Salam, Leptin.</div>
<div style="margin-top: 4px; display: flex; gap: 20px; align-items: center">
<div style="flex: 1 1 0; min-width: 0; border: 4px solid #1B1B1F; border-radius: 16px; padding: 30px 34px; background: #FFFDF6; display: flex; flex-direction: column; gap: 10px">
<div style="font-size: 42px; line-height: 1.2; font-weight: 900">Simpan, lalu kirim ke guru yang kamu kenal.</div>
</div>
<svg width="170" height="200" viewBox="0 20 200 240" role="img" aria-label="Leptin tersenyum lega" style="flex: 0 0 170px;margin-top:-30px">
<ellipse cx="100" cy="226" rx="50" ry="9" fill="#BCCADA"/>
{epi("e6",-18,6,0.62,e_happy())}
</svg>
</div></div>
<div style="position: absolute; left: 210px; right: 80px; bottom: 36px; font-size: 24px; line-height: 1.35; font-weight: 600; color: #6B6558">Ceritanya fiksi. Yang didukung bukti: leptin berperan sebagai sinyal izin pubertas; IMT lebih tinggi dikaitkan dengan pubertas lebih awal; ayam pedaging tumbuh cepat karena genetik dan pakan. Keterbatasan: penyebab pubertas lebih awal bersifat banyak faktor, dan peran zat pengganggu hormon dari lingkungan belum jelas.</div>
"""
import os
out=sys.argv[1]
os.makedirs(out,exist_ok=True)
for i,x in enumerate([s1,s2,s3,s4,s5,s6],1):
    open(f'{out}/slide{i}.html','w').write(page(i,x))

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

# ---- mascot override: Otot Masseter
def epi(cid,x,y,s,eyes):
    body='M250 120 C 360 110 392 220 380 300 C 368 390 310 420 250 418 C 190 420 132 390 120 300 C 108 220 140 130 250 120 Z'
    return f'''<g transform="translate({x} {y}) scale({s})"><g transform="translate(0 -40)">
<path d="{body}" fill="#8E3A32" transform="translate(8 8)"/>
<path d="{body}" fill="#D9695A" stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round"/>
<path d="M170 170 C 150 250 160 340 200 395 M330 170 C 350 250 340 340 300 395 M250 128 C 262 200 262 300 250 330" fill="none" stroke="#B5483A" stroke-width="10" stroke-linecap="round"/>
<path d="M175 180 C 165 215 165 245 172 270" fill="none" stroke="#F2A99C" stroke-width="16" stroke-linecap="round"/>
<g transform="translate(0 62)">{eyes}</g></g></g>'''
GIGI='<path d="M{x} {y} h120 v70 q0 30 -30 30 h-60 q-30 0 -30 -30 z" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="6" stroke-linejoin="round"/>'
cacing='''<ellipse cx="395" cy="318" rx="100" ry="12" fill="#BCCADA"/>
<path d="M330 250 C 350 150 390 290 410 190 C 420 150 450 170 460 140" fill="none" stroke="#1B1B1F" stroke-width="36" stroke-linecap="round"/>
<path d="M330 250 C 350 150 390 290 410 190 C 420 150 450 170 460 140" fill="none" stroke="#E7A6A0" stroke-width="24" stroke-linecap="round"/>
<circle cx="466" cy="136" r="5" fill="#1B1B1F"/>'''
gigi='''<ellipse cx="130" cy="318" rx="90" ry="12" fill="#BCCADA"/><g transform="translate(130 190) scale(1.15)"><path d="M-50,-60 C-50,-85 -20,-90 0,-78 C20,-90 50,-85 50,-60 C50,-20 38,10 34,45 C32,68 18,70 14,45 C10,20 -10,20 -14,45 C-18,70 -32,68 -34,45 C-38,10 -50,-20 -50,-60 Z" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="5.217391304347826" stroke-linejoin="round"/><path d="M-30 -62 C-34 -40 -30 -20 -26 -5" fill="none" stroke="#E4E8EC" stroke-width="6.9565217391304355" stroke-linecap="round"/></g>'''
pil='''<ellipse cx="660" cy="318" rx="80" ry="12" fill="#BCCADA"/>
<g transform="rotate(-35 660 195)"><rect x="610" y="165" width="100" height="60" rx="30" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="6"/>
<path d="M660 165 h20 a30 30 0 0 1 0 60 h-20 z" fill="#EDBE4E" stroke="#1B1B1F" stroke-width="6" stroke-linejoin="round"/></g>'''
s1=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 30px">
<div style="font-size: 68px; line-height: 1.04; font-weight: 900; font-variation-settings: 'opsz' 32; letter-spacing: -1.5px">ANAK YANG MENGGERTAKKAN GIGI SAAT TIDUR BELUM TENTU {hl("CACINGAN.")}</div>
<div style="font-size: 44px; line-height: 1.1; font-weight: 900; font-variation-settings: 'opsz' 32; color: #B5483A">DAN JANGAN BURU-BURU DIBERI OBAT CACING SAJA.</div>
<svg style="margin-top: 110px" width="790" height="350" viewBox="0 0 790 350" role="img" aria-label="Dua gigi beradu, seekor cacing, dan sebutir obat, masing-masing dicoret tanda larangan">
{gigi}{cacing}{pil}{ban(130,190,110)}{ban(395,190,110)}{ban(660,190,110)}
</svg>
</div>
<div style="position: absolute; left: 210px; right: 80px; bottom: 56px; font-size: 32px; font-weight: 700; color: #1B1B1F">Geser untuk tahu kenapa →</div>"""

s2=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 28px">
<div style="align-self: flex-start; padding: 10px 22px; border: 3px solid #1B1B1F; border-radius: 6px; background: #FFFDF6; font-size: 32px; line-height: 1.3; font-weight: 800">Namaku: Otot Masseter.<br>Julukanku: Si Pengunyah Terkuat.</div>
<div style="font-size: 58px; line-height: 1.07; {H}">KAMU MENGIRA BUNYI "KRETEK-KRETEK" ITU SUARA CACING.</div>
<div style="font-size: 58px; line-height: 1.07; {H}">{hl("ITU SUARAKU.")}</div>
<div style="font-size: 34px; line-height: 1.4; font-weight: 500">Aku otot di pipi yang menutup rahang saat kamu mengunyah. Kadang aku tetap bekerja saat pemilikku tidur.</div>
<svg width="790" height="340" viewBox="0 0 790 340" role="img" aria-label="Otot Masseter, tokoh otot pipi, tersenyum tenang di samping dua gigi">
<ellipse cx="200" cy="322" rx="130" ry="12" fill="#BCCADA"/><ellipse cx="610" cy="322" rx="110" ry="12" fill="#BCCADA"/>
{epi("e2",40,-8,0.8,e_calm())}
<g transform="translate(650 190) scale(1.3)"><path d="M-50,-60 C-50,-85 -20,-90 0,-78 C20,-90 50,-85 50,-60 C50,-20 38,10 34,45 C32,68 18,70 14,45 C10,20 -10,20 -14,45 C-18,70 -32,68 -34,45 C-38,10 -50,-20 -50,-60 Z" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="4.615384615384615" stroke-linejoin="round"/><path d="M-30 -62 C-34 -40 -30 -20 -26 -5" fill="none" stroke="#E4E8EC" stroke-width="6.153846153846153" stroke-linecap="round"/></g>
</svg>
</div>"""

def item(label,txt):
    return f'''<div style="display: flex; flex-direction: column; gap: 14px">
<div style="align-self: flex-start; padding: 6px 20px; background: #FFFDF6; border: 3px solid #1B1B1F; color: #1B1B1F; border-radius: 6px; font-size: 32px; font-weight: 800">{label}</div>
<div style="font-size: 38px; line-height: 1.34; font-weight: 500">{txt}</div></div>'''
s3=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 32px">
<div style="font-size: 70px; line-height: 1.05; {H}">KENAPA "CACINGAN" {hl("KELIRU?")}</div>
{item("OTAK SETENGAH TERBANGUN","Saat tidur, otak bisa &quot;setengah terbangun&quot; sebentar berkali-kali tanpa disadari. Pada sebagian anak, momen itu disertai kontraksi berirama dariku, lalu gigi beradu. Cukup umum, dan sering berkurang seiring usia.")}
{item("KAITAN DENGAN CACINGAN LEMAH","Bukti ilmiahnya lemah dan tidak konsisten. Yang lebih sering dibahas peneliti: pola tidur, stres atau cemas, dan pada sebagian anak gangguan napas saat tidur seperti mendengkur.")}
<div style="font-size: 34px; line-height: 1.35; font-weight: 800; color: #B5483A">Kalau hanya diberi obat cacing, penyebab yang mungkin sebenarnya bisa terlewat.</div>
</div>"""

def step(n,t):
    return f'''<div style="display: flex; gap: 26px; align-items: flex-start">
<div style="flex: 0 0 72px; width: 72px; height: 72px; border-radius: 36px; background: #B5483A; border: 4px solid #1B1B1F; box-sizing: border-box; color: #FBF3DF; display: flex; align-items: center; justify-content: center; font-size: 40px; font-weight: 900">{n}</div>
<div style="flex: 1 1 0; min-width: 0; font-size: 40px; line-height: 1.34; font-weight: 600">{t}</div></div>'''
s4=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 40px">
<div style="font-size: 70px; line-height: 1.04; {H}">WAHAI {hl("GURU:")}</div>
{step(1,'<span style="font-weight: 900">Hentikan ejekan "cacingan"</span> di kelas atau saat kemah.')}
{step(2,'<span style="font-weight: 900">Perhatikan murid</span> yang sering mengantuk, mendengkur, atau tampak cemas. Itu informasi berharga untuk orang tua.')}
{step(3,'<span style="font-weight: 900">Sampaikan ke orang tua</span> dengan bahasa netral, bukan label.')}
<div style="font-size: 34px; line-height: 1.4; font-weight: 700; color: #B5483A">Ini kondisi tidur, bukan soal kebersihan.</div>
<div style="margin-top: 20px">{scene("e4",e_calm(),"JANGAN TERTAWA","DENGARKAN AKU","Otot Masseter tenang berkata: jangan tertawa, dengarkan aku",230)}</div>
</div>"""

def bul(t): return f'<div style="display: flex; gap: 22px"><span aria-hidden="true" style="flex: 0 0 18px; width: 18px; height: 18px; margin-top: 17px; background: #B5483A; border: 3px solid #1B1B1F; box-sizing: border-box; border-radius: 3px"></span><span>{t}</span></div>'
s5=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 38px">
<div style="background: #B5483A; color: #FBF3DF; border-radius: 16px; padding: 36px 40px">
<div style="font-size: 54px; line-height: 1.06; {H}">OBAT CACING BERKALA TETAP BOLEH. TAPI JANGAN JADI <span style="white-space: nowrap">SATU-SATUNYA</span> PENJELASAN.</div>
</div>
<div style="font-size: 52px; line-height: 1.06; {H}">UNTUK {hl("AYAH DAN BUNDA:")}</div>
<div style="display: flex; flex-direction: column; gap: 22px; font-size: 40px; line-height: 1.25; font-weight: 700">
{bul("perhatikan: apakah anak mendengkur, sering terbangun, atau sedang tertekan?")}
{bul("periksakan ke dokter gigi bila gigi tampak aus, rahang nyeri, atau sakit kepala pagi")}
{bul("ke dokter bila mendengkur keras")}
</div>
<div style="margin-top: 10px">{scene("e5",e_worried(),"BUKAN CACING","BUKAN JOROK","Otot Masseter tampak cemas dan berkata: bukan cacing, bukan jorok",240)}</div>
</div>"""

s6=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 30px">
<div style="font-size: 40px; line-height: 1.3; font-weight: 500">Aku tidak sedang menggerogoti gigi anakmu dengan sengaja. Aku hanya otot kuat yang belum belajar beristirahat penuh.</div>
<div style="font-size: 62px; line-height: 1.06; {H}">DENGARKAN PESANKU, {hl("JANGAN MENERTAWAKAN SUARAKU.")}</div>
<div style="font-size: 44px; font-weight: 800; color: #B5483A">Salam, Otot Masseter.</div>
<div style="margin-top: 4px; display: flex; gap: 20px; align-items: center">
<div style="flex: 1 1 0; min-width: 0; border: 4px solid #1B1B1F; border-radius: 16px; padding: 22px 28px; background: #FFFDF6; display: flex; flex-direction: column; gap: 10px">
<div style="font-size: 36px; line-height: 1.2; font-weight: 900">Simpan, lalu kirim ke guru yang kamu kenal.</div>
</div>
<svg width="200" height="240" viewBox="0 0 200 240" role="img" aria-label="Otot Masseter tersenyum lega" style="flex: 0 0 200px">
<ellipse cx="100" cy="226" rx="70" ry="9" fill="#BCCADA"/>
{epi("e6",-34,-6,0.6,e_happy())}
</svg>
</div></div>
<div style="position: absolute; left: 210px; right: 80px; bottom: 40px; font-size: 25px; line-height: 1.35; font-weight: 600; color: #6B6558">Ceritanya fiksi, otot tidak berbicara. Nyata: bruksisme tidur cukup umum pada anak dan sering membaik seiring usia; kaitannya dengan cacingan tidak didukung bukti yang kuat. Pemeriksaan oleh dokter gigi atau dokter yang menentukan.</div>"""
import os
os.makedirs(out,exist_ok=True)
for i,s in enumerate([s1,s2,s3,s4,s5,s6],1):
    open(f'{out}/slide{i}.html','w').write(page(i,s))

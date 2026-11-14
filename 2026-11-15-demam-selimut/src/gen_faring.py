"""Jalur A · personifikasi + maskot · sistem desain v2 (Impeccable, 14 Nov 2026).
Pakai: salin file ini ke <folder>/src/, ganti isi daftar A (6 slide) dan maskot/ilustrasi bila tokohnya lain, lalu
  python3 gen_faring.py <outdir>     -> s1.html..s6.html
  node template/render_html.js <outdir> <outdir>   -> slide1..6.jpg (1080x1350)
Aturan sistem ada di PIPELINE.md bagian "Sistem desain v2".
Contoh lengkap: Leptin (2026-11-14). Maskot: flat 3 nada, outline tinta 7px, bayangan datar #BCCADA.
SOFT SELLING RPP (Senin/Rabu/Jumat): taruh RPP_LINE di bawah kartu CTA slide 6 (lihat contoh di bawah, tinggal aktifkan).
"""
import os, sys
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))

INK = "#1B1B1F"; GREY = "#5E594E"; RED = "#B5483A"; PAPER = "#FBF3DF"; CARD = "#FFFDF6"; HLC = "#FFE14D"

# ---------- ilustrasi ----------
INK = "#1B1B1F"

def ban(cx, cy, r):
    a = 0.7071 * r
    return f'<g fill="none" stroke-linecap="round"><circle cx="{cx}" cy="{cy}" r="{r}" stroke="#1B1B1F" stroke-width="30"/><line x1="{cx-a}" y1="{cy-a}" x2="{cx+a}" y2="{cy+a}" stroke="#1B1B1F" stroke-width="30"/><circle cx="{cx}" cy="{cy}" r="{r}" stroke="#B5483A" stroke-width="20"/><line x1="{cx-a}" y1="{cy-a}" x2="{cx+a}" y2="{cy+a}" stroke="#B5483A" stroke-width="20"/></g>'

def epi(x, y, s, eyes):
    return f'''<g transform="translate({x} {y}) scale({s})">
<circle cx="150" cy="240" r="100" fill="#9A6414" transform="translate(9 9)"/>
<circle cx="150" cy="240" r="100" fill="#F2B73D" stroke="#1B1B1F" stroke-width="7"/>
<path d="M 82 215 C 86 180 108 160 130 152" fill="none" stroke="#FFE9A8" stroke-width="12" stroke-linecap="round"/>
<g transform="translate(-108 -4)">{eyes}</g></g>'''

def _eyes(dy=0, brow=False):
    b = '<path d="M 205 165 L 238 177 M 305 165 L 272 177" fill="none" stroke="#1B1B1F" stroke-width="7" stroke-linecap="round"/>' if brow else ''
    return f'<circle cx="238" cy="220" r="25" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="5"/><circle cx="278" cy="220" r="25" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="5"/><circle cx="243" cy="{225+dy}" r="10" fill="#1B1B1F"/><circle cx="283" cy="{225+dy}" r="10" fill="#1B1B1F"/><circle cx="246" cy="{221+dy}" r="3" fill="#FFFDF6"/><circle cx="286" cy="{221+dy}" r="3" fill="#FFFDF6"/>{b}'

def e_calm(): return _eyes() + '<path d="M 240 282 Q 258 296 276 282" fill="none" stroke="#1B1B1F" stroke-width="6" stroke-linecap="round"/>'
def e_worried(): return _eyes(2, True) + '<path d="M 240 296 Q 258 278 276 296" fill="none" stroke="#1B1B1F" stroke-width="6" stroke-linecap="round"/>'
def e_happy(): return '<path d="M 218 228 Q 238 200 258 228 M 262 228 Q 282 200 302 228" fill="none" stroke="#1B1B1F" stroke-width="7" stroke-linecap="round"/><path d="M 236 276 Q 258 304 282 276" fill="none" stroke="#1B1B1F" stroke-width="7" stroke-linecap="round"/>'

drum = """<g stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"><path d="M 150 250 L 95 300" fill="none" stroke-width="16"/><circle cx="84" cy="300" r="12" fill="#FFFDF6"/><circle cx="104" cy="312" r="12" fill="#FFFDF6"/><path d="M 130 70 C 200 60 230 140 190 210 C 160 255 110 250 90 215 C 65 170 80 80 130 70 Z" fill="#D98B3A"/><path d="M 120 100 C 140 90 175 100 180 130" fill="none" stroke="#F4C27A" stroke-width="10"/></g>"""
syr = """<g stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"><rect x="95" y="90" width="70" height="150" rx="8" fill="#FFFDF6"/><rect x="108" y="150" width="44" height="82" fill="#F2B73D" stroke-width="0"/><rect x="95" y="90" width="70" height="150" rx="8" fill="none"/><path d="M 80 90 L 180 90 M 130 90 L 130 40 M 105 40 L 155 40" fill="none"/><path d="M 130 240 L 130 306" fill="none" stroke-width="6"/><path d="M 100 130 L 125 130 M 100 160 L 125 160 M 100 190 L 125 190" fill="none" stroke-width="5"/></g>"""

def ban_pair(w=790, h=350, shadow="#BCCADA"):
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 790 350" role="img" aria-label="Paha ayam dan jarum suntik dicoret">
<ellipse cx="260" cy="330" rx="110" ry="12" fill="{shadow}"/><ellipse cx="525" cy="330" rx="110" ry="12" fill="{shadow}"/>
<g transform="translate(130 0)">{drum}</g><g transform="translate(400 0)">{syr}</g>{ban(260,190,110)}{ban(525,190,110)}</svg>'''

def mascot(size, eyes, shadow="#BCCADA"):
    """Maskot sendiri dalam kotak persegi size x size."""
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 300 300" role="img" aria-label="Leptin">
<ellipse cx="150" cy="266" rx="105" ry="12" fill="{shadow}"/>{epi(0,-100,1,eyes)}</svg>'''

CSS = f"""
*{{box-sizing:border-box;margin:0}} body{{margin:0}}
.pg{{position:relative;width:1080px;height:1350px;overflow:hidden;background-color:{PAPER};
 background-image:repeating-linear-gradient(to bottom,transparent 0,transparent 71px,rgba(120,150,185,.16) 71px,rgba(120,150,185,.16) 73px);
 background-position:0 40px;font-family:'Inter',system-ui,sans-serif;color:{INK};-webkit-font-smoothing:antialiased}}
.pg.band{{background-color:{HLC};background-image:none}}
.margin{{position:absolute;left:120px;top:0;width:3px;height:1350px;background:{RED};opacity:.55}}
.band .margin{{background:{INK};opacity:.18}}
.hole{{position:absolute;left:40px;width:36px;height:36px;border-radius:18px;background:#E6DDC6}}
.band .hole{{background:#F0CF3A}}
.top{{position:absolute;left:176px;right:88px;top:64px;display:flex;justify-content:space-between;font-size:26px;font-weight:700;letter-spacing:-.01em}}
.top .h{{color:{RED}}} .top .n{{color:{GREY};font-variant-numeric:tabular-nums}}
.band .top .h{{color:{INK}}} .band .top .n{{color:{INK};opacity:.6}}
.body{{position:absolute;left:176px;right:88px;top:184px;bottom:150px;display:flex;flex-direction:column}}
.body>*{{flex-shrink:0}} .grow{{flex:1 1 auto}}
.foot{{position:absolute;left:176px;right:88px;bottom:62px;font-size:28px;font-weight:600;color:{GREY}}}
.note{{position:absolute;left:176px;right:88px;bottom:52px;font-size:23px;line-height:1.4;font-weight:500;color:{GREY}}}
/* skala tipe: 6 peran tetap */
.display{{font-size:96px;line-height:.98;font-weight:900;letter-spacing:-.035em;text-transform:uppercase;text-wrap:balance}}
.title{{font-size:68px;line-height:1.06;font-weight:800;letter-spacing:-.03em;text-wrap:balance}}
.lead{{font-size:44px;line-height:1.36;font-weight:500;letter-spacing:-.012em;text-wrap:pretty}}
.text{{font-size:38px;line-height:1.45;font-weight:500;letter-spacing:-.008em;text-wrap:pretty}}
.small{{font-size:32px;line-height:1.42;font-weight:500;color:{GREY};text-wrap:pretty}}
.label{{font-size:30px;line-height:1.2;font-weight:800;color:{RED};letter-spacing:-.005em}}
.red{{color:{RED}}} .grey{{color:{GREY}}} .nw{{white-space:nowrap}}
.hl{{background:linear-gradient(transparent 14%,{HLC} 14%,{HLC} 90%,transparent 90%);padding:0 .12em;margin:0 -.12em;
 -webkit-box-decoration-break:clone;box-decoration-break:clone}}
.g8{{height:8px}} .g16{{height:16px}} .g24{{height:24px}} .g32{{height:32px}} .g40{{height:40px}} .g56{{height:56px}} .g72{{height:72px}} .g96{{height:96px}}
.steps{{display:flex;flex-direction:column;gap:52px}}
.step{{display:grid;grid-template-columns:64px 1fr;column-gap:30px;align-items:start}}
.num{{width:64px;height:64px;border-radius:32px;background:{RED};color:{PAPER};display:flex;align-items:center;justify-content:center;
 font-size:34px;font-weight:800;font-variant-numeric:tabular-nums;margin-top:2px}}
.item{{display:flex;flex-direction:column;gap:12px}}
.rule{{height:2px;background:{INK};opacity:.10}}
.card{{background:{CARD};border-radius:28px;padding:40px 44px;box-shadow:0 1px 0 rgba(27,27,31,.06),0 18px 40px -12px rgba(27,27,31,.18)}}
.bubble{{position:relative;background:{CARD};border-radius:28px;padding:26px 34px;font-size:34px;line-height:1.2;font-weight:800;
 box-shadow:0 1px 0 rgba(27,27,31,.06),0 14px 30px -10px rgba(27,27,31,.18)}}
.bubble:before{{content:"";position:absolute;left:-18px;top:50%;margin-top:-14px;border:14px solid transparent;border-right:20px solid {CARD};border-left:0}}
.row{{display:flex;align-items:center;gap:28px}}
.dot{{flex:0 0 14px;width:14px;height:14px;border-radius:7px;background:{RED};margin-top:20px}}
.bul{{display:grid;grid-template-columns:14px 1fr;column-gap:26px}}
.rpp{{font-size:28px;line-height:1.4;font-weight:600;color:{GREY};text-wrap:pretty}} .rpp b{{color:{INK};font-weight:800}}
.quote{{font-size:64px;line-height:1.12;font-weight:800;letter-spacing:-.03em;text-wrap:balance}}
"""

def page(n, inner, foot="", band=False, bottom=150):
    holes = "".join(f'<div class="hole" style="top:{t}px"></div>' for t in (186, 648, 1110))
    return f'''<!doctype html><html lang="id"><head><meta charset="utf-8"><title>Slide {n}</title><style>{CSS}</style></head><body>
<div class="pg{' band' if band else ''}"><div class="margin"></div>{holes}
<div class="top"><span class="h">@ipadevpro <span style="color:#5E594E;font-weight:600">· {SERI}</span></span><span class="n">{n}/6</span></div>
<div class="body" style="bottom:{bottom}px">{inner}</div>{foot}</div></body></html>'''


SERI = 'Seri Jangan Dulu'   # nama seri tetap untuk semua carousel jalur A
hl = lambda t: f'<span class="hl">{t}</span>'
SWIPE_A = '<div class="foot">Geser untuk tahu kenapa →</div>'
SOFT_SELLING = False   # True pada hari Senin, Rabu, Jumat (WIB, tanggal tayang)
RPP_LINE = '<div class="g16"></div><div class="rpp">Guru yang waktunya habis di administrasi: <b>komentar RPP</b>, saya kirim link preview gratis lewat DM.</div>' if SOFT_SELLING else ''

# ===== Pembuluh Darah Kulit / Si Jendela Panas (2026-11-15, jalur A2 sore) =====
def ves(x, y, s, eyes):
    body = "M 70 170 C 70 150 85 140 110 140 L 190 140 C 215 140 230 150 230 170 L 230 310 C 230 330 215 340 190 340 L 110 340 C 85 340 70 330 70 310 Z"
    return f'''<g transform="translate({x} {y}) scale({s})">
<path d="{body}" fill="#9C3E33" transform="translate(9 9)"/>
<path d="{body}" fill="#E07A6A" stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round"/>
<path d="M 96 300 L 96 180 C 96 170 102 165 112 165" fill="none" stroke="#F6B9AE" stroke-width="12" stroke-linecap="round"/>
<path d="M 150 140 L 150 340 M 70 240 L 230 240" stroke="#1B1B1F" stroke-width="5" opacity=".18"/>
<g transform="translate(-108 -2)">{eyes}</g></g>'''

blanket = """<g stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
<path d="M 55 120 L 225 120 L 225 250 C 225 262 215 270 203 270 L 77 270 C 65 270 55 262 55 250 Z" fill="#6E8FC2"/>
<path d="M 55 120 L 225 120 L 225 160 L 55 160 Z" fill="#9DB6DE"/>
<path d="M 80 195 L 200 195 M 80 228 L 200 228" fill="none" stroke="#4A6A9E" stroke-width="9"/></g>"""

jacket = """<g stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
<path d="M 105 95 C 120 80 160 80 175 95 L 225 125 L 215 195 L 195 190 L 195 275 L 85 275 L 85 190 L 65 195 L 55 125 Z" fill="#7A9A5A"/>
<path d="M 105 95 C 115 125 165 125 175 95" fill="#A9C38A"/>
<path d="M 140 118 L 140 275" fill="none"/><path d="M 95 150 L 95 240" fill="none" stroke="#A9C38A" stroke-width="9"/></g>"""

def ban_pair(w=790, h=350, shadow="#BCCADA"):
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 790 350" role="img" aria-label="Selimut tebal dan jaket dicoret">
<ellipse cx="260" cy="330" rx="110" ry="12" fill="{shadow}"/><ellipse cx="525" cy="330" rx="110" ry="12" fill="{shadow}"/>
<g transform="translate(120 0)">{blanket}</g><g transform="translate(385 0)">{jacket}</g>{ban(260,190,110)}{ban(525,190,110)}</svg>'''

def mascot(size, eyes, shadow="#BCCADA"):
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 300 300" role="img" aria-label="Pembuluh darah kulit">
<ellipse cx="150" cy="266" rx="105" ry="12" fill="{shadow}"/>{ves(0,-90,1,eyes)}</svg>'''

SOFT_SELLING = False   # jalur A2 selalu tanpa soft selling
RPP_LINE = ''
A = []
A.append(page(1, f'''
<div class="title" style="font-size:72px">Anak yang demam jangan dibungkus {hl("selimut tebal")} supaya “keringatnya keluar”.</div>
<div class="g40"></div>
<div class="lead red" style="font-weight:700">Dan jangan dipakaikan jaket di kelas yang panas.</div>
<div class="grow"></div>
<div style="display:flex;justify-content:center">{ban_pair(760,337)}</div>''', SWIPE_A))
A.append(page(2, f'''
<div class="label">Namaku Pembuluh Darah Kulit, Si Jendela Panas.</div>
<div class="g24"></div>
<div class="display" style="font-size:80px">Kamu mengira mengeluarkan panasnya.</div>
<div class="g24"></div>
<div class="title">{hl("Sering kali kamu mengurungnya.")}</div>
<div class="g40"></div>
<div class="text">Tugasku membuang panas tubuh. Saat tubuh terlalu hangat, aku melebar di dekat permukaan kulit, supaya panas dari dalam bisa lepas ke udara.</div>
<div class="grow"></div>
<div class="row">{mascot(240, e_calm())}<div class="small" style="max-width:440px">Satu rahasia: aku hanya bisa bekerja kalau ada jalan keluar untuk panas itu.</div></div>'''))
A.append(page(3, f'''
<div class="display" style="font-size:84px">Kenapa caranya {hl("keliru?")}</div>
<div class="g56"></div>
<div class="item"><div class="label">Panas terperangkap di bawah kain tebal</div><div class="text">Keringat tidak bisa menguap dengan baik, padahal penguapan keringat itulah yang mendinginkan. Suhu tubuh anak bisa naik lebih tinggi lagi.</div></div>
<div class="g32"></div><div class="rule"></div><div class="g32"></div>
<div class="item"><div class="label">Keringat tidak membawa keluar “penyakit”</div><div class="text">Keringat hanya air dan garam. Anak makin lemas, makin haus, dan cairannya terkuras.</div></div>
<div class="grow" style="min-height:48px"></div>
<div class="lead red" style="font-weight:700">Seperti dapur panas yang semua jendelanya ditutup rapat: panasnya menumpuk.</div>'''))
A.append(page(4, f'''
<div class="display">Wahai {hl("guru:")}</div>
<div class="g56"></div>
<div class="steps">
<div class="step"><div class="num">1</div><div class="text"><b>Pindahkan</b> anak yang demam ke tempat sejuk, lalu longgarkan atau lepas pakaian tebalnya.</div></div>
<div class="step"><div class="num">2</div><div class="text"><b>Beri minum</b> sedikit-sedikit tapi sering.</div></div>
<div class="step"><div class="num">3</div><div class="text"><b>Hubungi</b> orang tua. Segera cari pertolongan bila anak sangat lemas, sulit dibangunkan, kejang, sesak, atau muncul bintik merah.</div></div>
</div>
<div class="grow"></div>
<div class="row">{mascot(200, e_calm())}<div class="bubble">Buka jendelaku,<br>bukan tutup.</div></div>'''))
A.append(page(5, f'''
<div class="display" style="font-size:88px">Untuk {hl("Ayah dan Bunda:")}</div>
<div class="g56"></div>
<div class="steps" style="gap:32px">
<div class="bul"><div class="dot"></div><div class="text">Pakaian tipis dan selimut tipis sudah cukup. Selimut tebal hanya saat menggigil, lalu dilepas.</div></div>
<div class="bul"><div class="dot"></div><div class="text">Cukupi minum. Obat penurun panas sesuai anjuran dokter atau aturan di kemasan.</div></div>
<div class="bul"><div class="dot"></div><div class="text" style="font-size:35px">Ke dokter bila demam lebih dari 2 sampai 3 hari, anak sangat lemas, kencing sedikit, atau ada tanda bahaya. Musim hujan, waspadai demam berdarah.</div></div>
</div>
<div class="grow"></div>
<div class="row">{mascot(190, e_worried())}<div class="bubble">Aku butuh<br>udara.</div></div>'''))
A.append(page(6, f'''
<div class="lead">Aku tidak butuh dibungkus. Aku butuh jendela yang terbuka: pakaian tipis, udara yang mengalir, dan air yang cukup.</div>
<div class="g56"></div>
<div class="title">Biarkan aku bekerja. {hl("Aku sudah melakukannya sejak anakmu lahir.")}</div>
<div class="g24"></div>
<div class="lead red" style="font-weight:700">Salam, Si Jendela Panas.</div>
<div class="grow"></div>
<div class="row" style="gap:20px"><div class="card" style="flex:1"><div class="lead" style="font-weight:800;font-size:40px;line-height:1.2">Simpan, kirim, lalu follow untuk mitos berikutnya.</div>{RPP_LINE}</div>{mascot(170, e_happy())}</div>''',
'<div class="note">Ceritanya fiksi. Yang didukung bukti: pakaian terlalu tebal menghambat pembuangan panas, dan keringat mendinginkan lewat penguapan, bukan dengan mengeluarkan penyakit. Batas: demam adalah respons tubuh melawan infeksi; yang perlu diperhatikan kondisi anak dan tanda bahaya. Bukan pengganti pemeriksaan dokter.</div>', bottom=250))


os.makedirs(OUT, exist_ok=True)
for i, s in enumerate(A, 1): open(os.path.join(OUT, f"s{i}.html"), "w").write(s)

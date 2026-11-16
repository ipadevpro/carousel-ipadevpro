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

# ===== Usus Besar / Si Penyerap Air (2026-11-16, jalur A pagi; thread diare dan teh pahit) =====
def colon(x, y, s, eyes):
    body = "M 60 200 C 60 150 95 128 150 128 C 205 128 240 150 240 200 L 240 290 C 240 325 215 340 180 340 L 120 340 C 85 340 60 325 60 290 Z"
    return f'''<g transform="translate({x} {y}) scale({s})">
<path d="{body}" fill="#B9614A" transform="translate(9 9)"/>
<path d="{body}" fill="#EE9A7E" stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round"/>
<path d="M 86 290 L 86 205 C 86 180 100 165 120 158" fill="none" stroke="#F9C6B4" stroke-width="12" stroke-linecap="round"/>
<path d="M 64 262 C 110 276 190 276 236 262 M 64 300 C 110 314 190 314 236 300" fill="none" stroke="#1B1B1F" stroke-width="5" opacity=".22"/>
<g transform="translate(-108 -6)">{eyes}</g></g>'''

tea = """<g stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
<path d="M 80 95 L 200 95 L 185 275 C 184 285 176 290 166 290 L 114 290 C 104 290 96 285 95 275 Z" fill="#FFFDF6"/>
<path d="M 86 140 L 194 140 L 185 275 C 184 285 176 290 166 290 L 114 290 C 104 290 96 285 95 275 Z" fill="#7A4A26"/>
<path d="M 108 160 L 114 260" fill="none" stroke="#A8703E" stroke-width="9"/>
<path d="M 125 70 C 115 55 135 45 125 30 M 155 70 C 145 55 165 45 155 30" fill="none" stroke-width="6"/></g>"""

tap = """<g stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
<rect x="40" y="110" width="40" height="70" rx="6" fill="#9FB3C8"/>
<path d="M 80 125 L 175 125 C 200 125 212 140 212 165 L 212 210 L 172 210 L 172 170 C 172 166 170 165 166 165 L 80 165 Z" fill="#C9D6E3"/>
<rect x="110" y="88" width="34" height="37" fill="#9FB3C8"/><rect x="92" y="72" width="70" height="20" rx="8" fill="#B5483A"/>
<path d="M 186 235 C 178 250 178 262 192 266 C 206 262 206 250 198 235 Z" fill="#7FB2E0"/></g>"""

def ban_pair(w=790, h=350, shadow="#BCCADA"):
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 790 350" role="img" aria-label="Teh pahit dan keran ditutup dicoret">
<ellipse cx="260" cy="330" rx="110" ry="12" fill="{shadow}"/><ellipse cx="525" cy="330" rx="110" ry="12" fill="{shadow}"/>
<g transform="translate(120 5)">{tea}</g><g transform="translate(400 20)">{tap}</g>{ban(260,190,110)}{ban(525,190,110)}</svg>'''

def mascot(size, eyes, shadow="#BCCADA"):
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 300 300" role="img" aria-label="Usus besar">
<ellipse cx="150" cy="266" rx="105" ry="12" fill="{shadow}"/>{colon(0,-90,1,eyes)}</svg>'''

SOFT_SELLING = False   # Senin: jalur A pagi tanpa soft selling
RPP_LINE = ''
A = []
A.append(page(1, f'''
<div class="title" style="font-size:72px">Anak yang diare jangan disuruh {hl("berhenti makan dan minum.")}</div>
<div class="g40"></div>
<div class="lead red" style="font-weight:700">Dan teh pahit bukan obatnya.</div>
<div class="grow"></div>
<div style="display:flex;justify-content:center">{ban_pair(760,337)}</div>''', SWIPE_A))
A.append(page(2, f'''
<div class="label">Namaku Usus Besar. Julukanku Si Penyerap Air.</div>
<div class="g24"></div>
<div class="display" style="font-size:80px">Kamu mengira aku perlu dikosongkan.</div>
<div class="g24"></div>
<div class="title">{hl("Sering kali aku butuh diisi.")}</div>
<div class="g40"></div>
<div class="text">Setiap hari aku menarik kembali air dan garam dari sisa makanan. Saat aku terganggu, air dan garam yang seharusnya kuserap ikut terbuang.</div>
<div class="grow"></div>
<div class="row">{mascot(240, e_calm())}<div class="small" style="max-width:440px">Yang hilang dari tubuhnya bukan cuma air. Tapi juga garam.</div></div>'''))
A.append(page(3, f'''
<div class="display" style="font-size:84px">Kenapa caranya {hl("keliru?")}</div>
<div class="g56"></div>
<div class="item"><div class="label">Menahan minum tidak menghentikan diarenya</div><div class="text">Tubuh justru kehilangan air dan garam lebih cepat daripada yang masuk. Pada anak, dehidrasi bisa memburuk lebih cepat daripada pada orang dewasa.</div></div>
<div class="g32"></div><div class="rule"></div><div class="g32"></div>
<div class="item"><div class="label">Teh pahit tidak mengganti garam</div><div class="text">Natrium dan kalium yang hilang tidak kembali lewat teh pahit. Tanpa makanan, sel-sel dindingku sulit memperbaiki diri.</div></div>
<div class="grow" style="min-height:48px"></div>
<div class="lead red" style="font-weight:700">Menutup keran tidak menambal ember yang bocor.</div>'''))
A.append(page(4, f'''
<div class="display">Wahai {hl("guru:")}</div>
<div class="g56"></div>
<div class="steps">
<div class="step"><div class="num">1</div><div class="text"><b>Izinkan</b> murid yang berkali-kali ke toilet karena diare. Jangan dimarahi, dan sediakan air minum.</div></div>
<div class="step"><div class="num">2</div><div class="text"><b>Hubungi</b> orang tua bila murid tampak pucat, lemas, atau pusing.</div></div>
<div class="step"><div class="num">3</div><div class="text"><b>Ajarkan</b> cuci tangan pakai sabun sebelum makan dan setelah dari toilet, terutama di kantin.</div></div>
</div>
<div class="grow"></div>
<div class="row">{mascot(200, e_calm())}<div class="bubble">Aku perlu diisi,<br>bukan dikosongkan.</div></div>'''))
A.append(page(5, f'''
<div class="display" style="font-size:88px">Untuk {hl("Ayah dan Bunda:")}</div>
<div class="g56"></div>
<div class="steps" style="gap:30px">
<div class="bul"><div class="dot"></div><div class="text">Beri oralit sedikit-sedikit tapi sering, pakai sendok atau gelas kecil. Tetap beri makan porsi kecil yang lembut.</div></div>
<div class="bul"><div class="dot"></div><div class="text">Teh pahit, kopi, atau minuman manis kemasan bukan pengganti oralit.</div></div>
<div class="bul"><div class="dot"></div><div class="text">Segera ke fasilitas kesehatan bila anak sangat lemas, tidak mau minum, tidak kencing berjam-jam, tinjanya berdarah, demam tinggi, atau muntah terus.</div></div>
</div>
<div class="grow"></div>
<div class="row">{mascot(180, e_worried())}<div class="bubble">Sedikit,<br>tapi sering.</div></div>'''))
S6 = 'style="font-size:36px"' if SOFT_SELLING else ''
T6 = 'style="font-size:54px"' if SOFT_SELLING else ''
A.append(page(6, f'''
<div class="lead" {S6}>Aku sedang sakit, bukan sedang minta dikosongkan. Beri aku cairan yang tepat, sedikit demi sedikit, dan aku akan kembali menyerap airnya.</div>
<div class="g56"></div>
<div class="title" {T6}>Yang dia butuhkan bukan teh pahit. {hl("Dia butuh oralit dan makanan lembut.")}</div>
<div class="g24"></div>
<div class="lead red" style="font-weight:700">Salam, Usus Besar.</div>
<div class="grow"></div>
<div class="row" style="gap:20px"><div class="card" style="flex:1"><div class="lead" style="font-weight:800;font-size:40px;line-height:1.2">Simpan, kirim, lalu follow untuk mitos berikutnya.</div>{RPP_LINE}</div>{mascot(170, e_happy())}</div>''',
'<div class="note">Ceritanya fiksi. Yang didukung bukti: oralit dan tetap makan dianjurkan untuk diare akut pada anak, termasuk oleh WHO; menahan makan dan minum tidak dianjurkan. Keterbatasan: penyebab diare bermacam-macam, sebagian perlu pemeriksaan dan obat dari dokter.</div>', bottom=250))


os.makedirs(OUT, exist_ok=True)
for i, s in enumerate(A, 1): open(os.path.join(OUT, f"s{i}.html"), "w").write(s)

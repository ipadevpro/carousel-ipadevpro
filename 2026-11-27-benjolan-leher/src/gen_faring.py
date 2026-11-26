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


# ===== Kelenjar Getah Bening / Si Pos Jaga (2026-11-27, jalur A2 sore: SOFT_SELLING False) =====
# Sumber: thread Threads 18027051164959202 (26 Nov, 6,7 ribu views, 5,7x). Maskot: kelenjar berbentuk kacang, ungu muda.
SOFT_SELLING = False
RPP_LINE = ''

def node(x, y, s, eyes):
    return f'''<g transform="translate({x} {y}) scale({s})">
<path d="M 60 230 C 50 160 110 130 160 150 C 190 162 200 150 222 146 C 262 140 280 190 266 240 C 252 300 200 330 150 326 C 96 322 66 282 60 230 Z" fill="#7A63A8" transform="translate(9 9)"/>
<path d="M 60 230 C 50 160 110 130 160 150 C 190 162 200 150 222 146 C 262 140 280 190 266 240 C 252 300 200 330 150 326 C 96 322 66 282 60 230 Z" fill="#B9A6E0" stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round"/>
<path d="M 82 226 C 82 196 100 174 126 168" fill="none" stroke="#E2D8F5" stroke-width="12" stroke-linecap="round"/>
<circle cx="230" cy="290" r="8" fill="#9C88CC"/><circle cx="96" cy="286" r="6" fill="#9C88CC"/>
<g transform="translate(-100 14)">{eyes}</g></g>'''

def mascot(size, eyes, shadow="#BCCADA"):
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 300 300" role="img" aria-label="Kelenjar getah bening berbentuk kacang ungu muda">
<ellipse cx="150" cy="282" rx="105" ry="12" fill="{shadow}"/>{node(0,-60,1,eyes)}</svg>'''

hand = """<g stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round" stroke-linecap="round" fill="#F3C9A0"><rect x="70" y="60" width="34" height="120" rx="17"/><rect x="108" y="44" width="34" height="136" rx="17"/><rect x="146" y="52" width="34" height="128" rx="17"/><rect x="184" y="72" width="32" height="110" rx="16"/><path d="M 66 150 L 220 150 L 220 220 Q 220 270 170 280 L 120 280 Q 66 274 60 220 Z"/><path d="M 66 190 Q 30 170 22 140 Q 18 124 34 124 Q 52 126 70 160" /><path d="M 90 230 Q 140 246 190 230" fill="none" stroke="#D9A57A" stroke-width="8"/></g>"""
onion = """<g stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"><path d="M 130 60 Q 136 90 150 104 Q 214 130 214 200 Q 214 270 130 276 Q 46 270 46 200 Q 46 130 110 104 Q 124 90 130 60 Z" fill="#B85C8A"/><path d="M 130 110 Q 92 150 96 210 Q 100 250 130 270" fill="none" stroke="#7E3A5E" stroke-width="7"/><path d="M 130 110 Q 168 150 164 210 Q 160 250 130 270" fill="none" stroke="#7E3A5E" stroke-width="7"/><path d="M 74 160 Q 80 136 102 124" fill="none" stroke="#E3A8C6" stroke-width="10"/><path d="M 116 290 L 112 304 M 130 292 L 130 308 M 144 290 L 148 304" fill="none" stroke-width="5"/></g>"""

def ban_pair(w=790, h=350, shadow="#BCCADA"):
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 790 350" role="img" aria-label="Tangan memijat dan bawang dicoret">
<ellipse cx="260" cy="330" rx="110" ry="12" fill="{shadow}"/><ellipse cx="525" cy="330" rx="110" ry="12" fill="{shadow}"/>
<g transform="translate(140 20) scale(0.92)">{hand}</g><g transform="translate(398 10) scale(0.98)">{onion}</g>{ban(260,190,110)}{ban(525,190,110)}</svg>'''

A = []
A.append(page(1, f'''
<div class="title" style="font-size:72px">Benjolan kecil di leher anak setelah dia pilek {hl("bukan otomatis tumor.")}</div>
<div class="g40"></div>
<div class="lead red" style="font-weight:700">Dan benjolannya jangan dipijat, diurut, atau ditempeli parutan bawang.</div>
<div class="grow"></div>
<div style="display:flex;justify-content:center">{ban_pair(760,337)}</div>''', SWIPE_A))
A.append(page(2, f'''
<div class="label">Namaku Kelenjar Getah Bening. Julukanku Si Pos Jaga.</div>
<div class="g24"></div>
<div class="display" style="font-size:84px">Kamu mengira aku musuh.</div>
<div class="g24"></div>
<div class="title">{hl("Aku sedang lembur.")}</div>
<div class="g40"></div>
<div class="text">Aku dan ratusan saudaraku tersebar di seluruh tubuh, banyak di leher, ketiak, dan lipat paha. Di dalamku sel-sel kekebalan berkumpul, menyaring cairan getah bening, dan bersiap melawan kuman.</div>
<div class="grow"></div>
<div class="row">{mascot(240, e_calm())}<div class="small" style="max-width:420px">Minggu lalu dia pilek. Kuman lewat, dan aku berjaga.</div></div>'''))
A.append(page(3, f'''
<div class="display" style="font-size:84px">Kenapa pijatan itu {hl("keliru?")}</div>
<div class="g56"></div>
<div class="item"><div class="label">Aku membesar karena sedang bekerja</div><div class="text">Sel kekebalan di dalamku memperbanyak diri untuk melawan kuman dari pilek dan radang tenggorokan. Itu sebabnya aku membesar dan sedikit nyeri.</div></div>
<div class="g32"></div><div class="rule"></div><div class="g32"></div>
<div class="item"><div class="label">Pijatan tidak membuatku kempes lebih cepat</div><div class="text">Memijatku justru bisa membuatku makin nyeri. Pada anak, pembesaran seperti ini sangat sering ditemukan dan biasanya mengecil dalam beberapa minggu.</div></div>
<div class="grow" style="min-height:48px"></div>
<div class="lead red" style="font-weight:700">Lampu pos jaga yang menyala terang tanda posnya sedang berjaga, bukan tanda posnya rusak.</div>'''))
A.append(page(4, f'''
<div class="display">Wahai {hl("guru:")}</div>
<div class="g56"></div>
<div class="steps">
<div class="step"><div class="num">1</div><div class="text"><b>Kenalkan aku</b> sebagai pos jaga saat pelajaran sistem imun, supaya murid tidak panik saat merabaku.</div></div>
<div class="step"><div class="num">2</div><div class="text"><b>Jangan menebak-nebak</b> penyakit murid dari benjolan di lehernya.</div></div>
<div class="step"><div class="num">3</div><div class="text"><b>Kabarkan ke orang tua</b> bila murid tampak sangat lemas, sering demam, atau berat badannya turun.</div></div>
</div>
<div class="grow"></div>
<div class="row">{mascot(200, e_calm())}<div class="bubble">Aku penjaga,<br>bukan penyakit.</div></div>'''))
A.append(page(5, f'''
<div class="display" style="font-size:88px">Untuk {hl("Ayah dan Bunda:")}</div>
<div class="g40"></div>
<div class="steps" style="gap:28px">
<div class="bul"><div class="dot"></div><div class="text">Benjolan kecil, kenyal, dan bisa digeser setelah pilek sering kali reaktif. Pantau dengan tenang.</div></div>
<div class="bul"><div class="dot"></div><div class="text">Jangan dipijat, diurut, atau ditempeli ramuan.</div></div>
<div class="bul"><div class="dot"></div><div class="text" style="font-size:34px">Periksakan ke dokter bila benjolan makin besar, keras, tidak bisa digeser, tidak mengecil setelah 2 sampai 4 minggu, kulitnya merah dan panas, atau disertai demam lama, keringat malam, atau berat badan turun.</div></div>
</div>
<div class="grow"></div>
<div class="row">{mascot(180, e_worried())}<div class="bubble">Pantau aku,<br>jangan pijat aku.</div></div>'''))
A.append(page(6, f'''
<div class="lead" style="font-size:40px">Aku bukan musuh yang tumbuh di leher anakmu. Aku penjaga yang sedang sibuk karena baru saja ada kuman lewat.</div>
<div class="g40"></div>
<div class="title" style="font-size:56px">Biarkan aku bekerja, pantau dengan tenang, {hl("dan tanyakan ke tenaga kesehatan bila ragu.")}</div>
<div class="g24"></div>
<div class="lead red" style="font-weight:700">Salam, Kelenjar Getah Bening.</div>
<div class="grow"></div>
<div class="row" style="gap:20px"><div class="card" style="flex:1"><div class="lead" style="font-weight:800;font-size:40px;line-height:1.2">Simpan, kirim, lalu follow untuk mitos berikutnya.</div>{RPP_LINE}</div>{mascot(170, e_happy())}</div>''',
'<div class="note">Ceritanya fiksi, dan kelenjar tidak berbicara. Yang didukung bukti: kelenjar getah bening leher pada anak sering membesar setelah infeksi dan biasanya mengecil sendiri. Keterbatasan: tidak ada satu patokan ukuran atau lama yang pasti normal; tanda bahaya di atas panduan umum, bukan pengganti pemeriksaan langsung.</div>', bottom=270))

os.makedirs(OUT, exist_ok=True)
for i, s in enumerate(A, 1): open(os.path.join(OUT, f"s{i}.html"), "w").write(s)

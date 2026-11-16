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

# ===== Estrogen / Si Pembuka Pintu Pubertas (2026-11-16, jalur A2 sore; thread keputihan sebelum haid pertama) =====
def estro(x, y, s, eyes):
    body = "M 150 120 C 185 120 200 138 215 150 C 245 160 250 200 245 225 C 262 255 250 300 215 315 C 195 340 105 340 85 315 C 50 300 38 255 55 225 C 50 200 55 160 85 150 C 100 138 115 120 150 120 Z"
    return f'''<g transform="translate({x} {y}) scale({s})">
<path d="{body}" fill="#8C5A9E" transform="translate(9 9)"/>
<path d="{body}" fill="#C99BD8" stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round"/>
<path d="M 80 280 C 72 250 74 215 92 190" fill="none" stroke="#E6CDEE" stroke-width="12" stroke-linecap="round"/>
<path d="M 150 122 C 150 100 150 92 158 80 M 158 92 C 172 74 196 76 200 84 C 186 98 168 98 158 92 Z" fill="#7FB27A" stroke="#1B1B1F" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
<g transform="translate(-108 2)">{eyes}</g></g>'''

sirih = """<g stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
<rect x="112" y="50" width="56" height="34" rx="6" fill="#FFFDF6"/>
<path d="M 100 84 L 180 84 C 205 84 215 100 215 125 L 215 270 C 215 283 205 290 192 290 L 88 290 C 75 290 65 283 65 270 L 65 125 C 65 100 75 84 100 84 Z" fill="#5E9A62"/>
<path d="M 140 150 C 175 165 180 215 140 245 C 100 215 105 165 140 150 Z" fill="#A6D29C"/><path d="M 140 160 L 140 238" fill="none" stroke-width="5"/>
<path d="M 85 120 L 85 250" fill="none" stroke="#8CC08E" stroke-width="9"/></g>"""

antis = """<g stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
<rect x="118" y="40" width="44" height="44" rx="6" fill="#B5483A"/>
<path d="M 110 84 L 170 84 L 170 110 C 205 120 215 140 215 165 L 215 272 C 215 284 206 290 194 290 L 86 290 C 74 290 65 284 65 272 L 65 165 C 65 140 75 120 110 110 Z" fill="#E9B44C"/>
<rect x="88" y="170" width="104" height="80" rx="10" fill="#FFFDF6"/><path d="M 140 185 L 140 235 M 115 210 L 165 210" fill="none" stroke="#B5483A" stroke-width="12"/></g>"""

def ban_pair(w=790, h=350, shadow="#BCCADA"):
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 790 350" role="img" aria-label="Sabun sirih dan cairan antiseptik dicoret">
<ellipse cx="260" cy="330" rx="110" ry="12" fill="{shadow}"/><ellipse cx="525" cy="330" rx="110" ry="12" fill="{shadow}"/>
<g transform="translate(120 5)">{sirih}</g><g transform="translate(385 5)">{antis}</g>{ban(260,190,110)}{ban(525,190,110)}</svg>'''

def mascot(size, eyes, shadow="#BCCADA"):
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 300 300" role="img" aria-label="Estrogen">
<ellipse cx="150" cy="266" rx="105" ry="12" fill="{shadow}"/>{estro(0,-80,1,eyes)}</svg>'''

SOFT_SELLING = False   # jalur A2 selalu tanpa soft selling
RPP_LINE = ''
A = []
A.append(page(1, f'''
<div class="title" style="font-size:72px">Remaja putri yang mulai {hl("keputihan")} sebelum haid pertama bukan anak yang jorok.</div>
<div class="g40"></div>
<div class="lead red" style="font-weight:700">Dan jangan disuruh membasuh bagian dalamnya dengan sabun sirih atau antiseptik.</div>
<div class="grow"></div>
<div style="display:flex;justify-content:center">{ban_pair(760,337)}</div>''', SWIPE_A))
A.append(page(2, f'''
<div class="label">Namaku Estrogen, Si Pembuka Pintu Pubertas.</div>
<div class="g24"></div>
<div class="display" style="font-size:80px">Kamu mengira itu kotoran.</div>
<div class="g24"></div>
<div class="title">{hl("Itu tanda aku mulai bekerja.")}</div>
<div class="g40"></div>
<div class="text">Aku hormon yang mulai banyak dibuat indung telur saat pubertas. Aku yang membuat payudara tumbuh, panggul melebar, dan kelak haid datang.</div>
<div class="grow"></div>
<div class="row">{mascot(240, e_calm())}<div class="small" style="max-width:440px">Beberapa bulan sampai sekitar setahun sebelum haid pertama, aku sering mengirim tanda kecil lebih dulu.</div></div>'''))
A.append(page(3, f'''
<div class="display" style="font-size:84px">Kenapa caranya {hl("keliru?")}</div>
<div class="g56"></div>
<div class="item"><div class="label">Cairan itu justru penjaga</div><div class="text">Keputihan normal adalah lendir yang membawa sel-sel lama keluar. Di sana hidup bakteri baik, terutama Lactobacillus, yang menjaga suasana tetap sedikit asam.</div></div>
<div class="g32"></div><div class="rule"></div><div class="g32"></div>
<div class="item"><div class="label">Sabun keras ikut mencuci penjaganya</div><div class="text">Saat bakteri baik tersingkir, jamur dan bakteri lain lebih mudah tumbuh. Yang muncul justru gatal dan perih.</div></div>
<div class="grow" style="min-height:48px"></div>
<div class="lead red" style="font-weight:700">Kamu tidak mencuci bola mata dengan sabun supaya “lebih bersih”.</div>'''))
A.append(page(4, f'''
<div class="display">Wahai {hl("guru:")}</div>
<div class="g56"></div>
<div class="steps">
<div class="step"><div class="num">1</div><div class="text"><b>Sebutkan</b> keputihan normal saat membahas pubertas, agar murid perempuan tidak merasa aneh atau kotor.</div></div>
<div class="step"><div class="num">2</div><div class="text"><b>Pastikan</b> toilet sekolah punya air bersih dan tempat sampah tertutup.</div></div>
<div class="step"><div class="num">3</div><div class="text"><b>Arahkan</b> murid yang mengeluh ke UKS atau guru BK yang ia percaya, tanpa membahasnya di depan kelas.</div></div>
</div>
<div class="grow"></div>
<div class="row">{mascot(200, e_calm())}<div class="bubble">Aku tanda tumbuh,<br>bukan tanda kotor.</div></div>'''))
A.append(page(5, f'''
<div class="display" style="font-size:88px">Untuk {hl("Ayah dan Bunda:")}</div>
<div class="g56"></div>
<div class="steps" style="gap:30px">
<div class="bul"><div class="dot"></div><div class="text">Jelaskan sejak awal: keputihan bening atau putih, tanpa gatal dan bau, adalah tanda pubertas yang normal.</div></div>
<div class="bul"><div class="dot"></div><div class="text">Cukup basuh bagian luar dengan air bersih, dari depan ke belakang, lalu keringkan. Pakai celana dalam katun.</div></div>
<div class="bul"><div class="dot"></div><div class="text">Periksakan bila warnanya kuning kehijauan, berbau busuk, sangat gatal, perih, atau ada nyeri perut bawah.</div></div>
</div>
<div class="grow"></div>
<div class="row">{mascot(180, e_worried())}<div class="bubble">Dia butuh<br>penjelasan.</div></div>'''))
S6 = ''
T6 = ''
A.append(page(6, f'''
<div class="lead">Aku datang lebih dulu sebelum haid, bukan untuk membuatnya malu, tapi untuk memberi tahu bahwa tubuhnya sedang tumbuh dengan baik.</div>
<div class="g56"></div>
<div class="title">Sambut aku dengan penjelasan, {hl("bukan dengan sabun paling keras di rumah.")}</div>
<div class="g24"></div>
<div class="lead red" style="font-weight:700">Salam, Estrogen.</div>
<div class="grow"></div>
<div class="row" style="gap:20px"><div class="card" style="flex:1"><div class="lead" style="font-weight:800;font-size:40px;line-height:1.2">Simpan, kirim, lalu follow untuk mitos berikutnya.</div>{RPP_LINE}</div>{mascot(170, e_happy())}</div>''',
'<div class="note">Ceritanya fiksi. Yang didukung bukti: keputihan fisiologis umum terjadi menjelang dan setelah haid pertama karena estrogen; pembilasan bagian dalam dengan sabun keras umumnya tidak dianjurkan. Keterbatasan: tidak setiap keputihan normal; perubahan warna, bau, atau rasa gatal perlu diperiksa tenaga kesehatan.</div>', bottom=250))


os.makedirs(OUT, exist_ok=True)
for i, s in enumerate(A, 1): open(os.path.join(OUT, f"s{i}.html"), "w").write(s)

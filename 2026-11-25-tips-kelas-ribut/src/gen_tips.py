"""Jalur C · tips & trik guru · sistem desain v2 (Impeccable).
Tayang Senin, Rabu, Jumat, Minggu pukul 20:13 WIB (bergantian dengan jalur B).
Pakai: salin ke <folder>/src/, ganti isi daftar S, lalu
  python3 gen_tips.py <outdir>  &&  node template/render_html.js <outdir> <outdir>
Struktur: (1) hook + janji jumlah trik / (2)-(4) satu trik per slide: nomor besar, nama trik, caranya, contoh kalimat atau langkah di kartu
/ (5) kesalahan yang sering terjadi ATAU trik bonus / (6) kartu CTA: simpan + "DM saya RPP" (otomatisasi Tebar mengirim link rpp.aiforteacher.id, khusus follower) + follow.
Aturan isi: trik harus praktis, bisa dicoba besok, tanpa angka/penelitian karangan, tanpa anekdot murid rekaan seolah nyata.
"""
import os, sys
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
SERI = 'Trik Kelas'

INK = "#1B1B1F"; GREY = "#5E594E"; RED = "#B5483A"; PAPER = "#FBF3DF"; CARD = "#FFFDF6"; HLC = "#FFE14D"

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
.ex{{background:{CARD};border-radius:24px;padding:30px 36px;box-shadow:0 1px 0 rgba(27,27,31,.06),0 14px 30px -12px rgba(27,27,31,.16)}}
.bignum{{width:96px;height:96px;border-radius:48px;background:{RED};color:{PAPER};display:flex;align-items:center;justify-content:center;font-size:52px;font-weight:900}}
.quote{{font-size:64px;line-height:1.12;font-weight:800;letter-spacing:-.03em;text-wrap:balance}}
"""

def page(n, inner, foot="", band=False, bottom=150):
    holes = "".join(f'<div class="hole" style="top:{t}px"></div>' for t in (186, 648, 1110))
    return f'''<!doctype html><html lang="id"><head><meta charset="utf-8"><title>Slide {n}</title><style>{CSS}</style></head><body>
<div class="pg{' band' if band else ''}"><div class="margin"></div>{holes}
<div class="top"><span class="h">@ipadevpro <span style="color:#5E594E;font-weight:600">· {SERI}</span></span><span class="n">{n}/6</span></div>
<div class="body" style="bottom:{bottom}px">{inner}</div>{foot}</div></body></html>'''

hl = lambda t: f'<span class="hl">{t}</span>'
SWIPE = '<div class="foot">Geser untuk tiga triknya →</div>'

def trik(n, nama, cara, contoh_label, contoh):
    return f'''
<div class="bignum">{n}</div>
<div class="g40"></div>
<div class="title" style="font-size:80px">{nama}</div>
<div class="g40"></div>
<div class="lead">{cara}</div>
<div class="grow" style="min-height:56px;max-height:160px"></div>
<div class="ex" style="padding:40px 44px"><div class="label">{contoh_label}</div><div class="g16"></div><div class="title" style="font-size:52px;line-height:1.14">{contoh}</div></div>'''

# ===== Kelas ribut setelah istirahat (2026-11-25, jalur C) =====
S = []
S.append(page(1, f'''
<div class="grow" style="max-height:120px"></div>
<div class="display" style="font-size:96px">Kelas ribut habis istirahat? {hl("Jangan adu suara.")}</div>
<div class="g56"></div>
<div class="lead" style="max-width:780px">Makin keras kita berteriak, makin keras kelas membalas. Tiga trik menenangkan kelas tanpa menaikkan suara, bisa dicoba besok setelah bel masuk.</div>''', SWIPE))
S.append(page(2, trik(1, "Mulai dengan berbisik.",
  "Berdiri di depan, tunggu sebentar, lalu bicara pelan kepada barisan terdekat. Murid yang penasaran akan diam supaya bisa ikut mendengar.",
  "Coba ucapkan pelan", "“Yang bisa dengar suara saya, sentuh hidungnya.”")))
S.append(page(3, trik(2, "Beri tugas tangan di menit pertama.",
  "Kelas tenang lebih cepat kalau tangan sudah sibuk. Tulis satu tugas singkat di papan sebelum bel, supaya murid langsung tahu harus mengerjakan apa.",
  "Tulis di papan", "“Gambar satu benda yang tadi kamu lihat saat istirahat, lalu beri satu label IPA.”")))
S.append(page(4, trik(3, "Pakai tanda yang sudah disepakati.",
  "Sepakati satu tanda bersama murid sejak awal: tangan terangkat, tepukan berirama, atau hitungan mundur dengan jari. Latih saat kelas sedang tenang.",
  "Contoh tepuk balas", "Guru tepuk dua kali, murid membalas tiga kali, lalu semua tangan di atas meja.")))
S.append(page(5, f'''
<div class="display">Yang sering {hl("terlewat:")}</div>
<div class="g56"></div>
<div class="lead">Tanda apa pun hanya bekerja kalau dipakai dengan cara yang sama setiap hari. Kalau hari ini tanda, besok teriakan, murid belajar menunggu teriakannya.</div>
<div class="g56"></div>
<div class="title" style="font-size:56px">Pilih satu trik saja, lalu pakai terus selama seminggu.</div>'''))
S.append(page(6, f'''
<div class="title">Simpan, lalu coba {hl("satu trik")} besok setelah bel masuk.</div>
<div class="g24"></div>
<div class="lead grey">Kirim ke rekan guru yang mengajar jam setelah istirahat. Follow @ipadevpro untuk trik kelas berikutnya.</div>
<div class="grow"></div>
<div class="card"><div class="lead" style="font-weight:800;font-size:40px;line-height:1.2">Mau menyiapkan kegiatan pembuka tanpa begadang?</div>
<div class="g16"></div><div class="small">DM saya kata <b style="color:#1B1B1F">RPP</b>, nanti saya kirim link preview gratis generator RPP, LKPD &amp; soal HOTS buatan saya.</div></div>'''))

os.makedirs(OUT, exist_ok=True)
for i, s in enumerate(S, 1): open(os.path.join(OUT, f"s{i}.html"), "w").write(s)

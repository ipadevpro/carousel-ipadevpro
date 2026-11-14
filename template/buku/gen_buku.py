"""Jalur B · renungan tipografi · sistem desain v2 (Impeccable, 14 Nov 2026).
Pakai: salin file ini ke <folder>/src/, ganti isi daftar S (6 slide), lalu
  python3 gen_buku.py <outdir>      -> s1.html..s6.html
  node template/render_html.js <outdir> <outdir>   -> slide1..6.jpg (1080x1350)
Aturan sistem ada di PIPELINE.md bagian "Sistem desain v2". Jangan mengubah CSS per slide kecuali ukuran display.
"""
import os, sys
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))

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
.quote{{font-size:64px;line-height:1.12;font-weight:800;letter-spacing:-.03em;text-wrap:balance}}
"""

def page(n, inner, foot="", band=False, bottom=150):
    holes = "".join(f'<div class="hole" style="top:{t}px"></div>' for t in (186, 648, 1110))
    return f'''<!doctype html><html lang="id"><head><meta charset="utf-8"><title>Slide {n}</title><style>{CSS}</style></head><body>
<div class="pg{' band' if band else ''}"><div class="margin"></div>{holes}
<div class="top"><span class="h">@ipadevpro</span><span class="n">{n}/6</span></div>
<div class="body" style="bottom:{bottom}px">{inner}</div>{foot}</div></body></html>'''

hl = lambda t: f'<span class="hl">{t}</span>'
SWIPE = '<div class="foot">Geser pelan-pelan →</div>'
NOTE = '<div class="note">Tulisan ini renungan, bukan kisah satu murid tertentu.</div>'
def item(label, text): return f'<div class="item"><div class="label">{label}</div><div class="text">{text}</div></div>'
def step(n, t, d): return f'<div class="step"><div class="num">{n}</div><div><div class="title" style="font-size:48px">{t}</div><div class="g8"></div><div class="small" style="font-size:36px">{d}</div></div></div>'

# ===== CONTOH LENGKAP: "Rapor tidak mencatat semuanya" (ganti isinya, pertahankan strukturnya) =====
S = []
# 1 hook: display kapital pendek (maks ~6 kata) + 1-2 kalimat konteks
S.append(page(1, f'''
<div class="grow" style="max-height:120px"></div>
<div class="display" style="font-size:112px">Rapor tidak mencatat {hl("semuanya.")}</div>
<div class="g56"></div>
<div class="lead" style="max-width:720px">Kamu pasti pernah melihatnya. Murid yang nilainya biasa saja, tapi hatinya besar.</div>''', SWIPE))
# 2 konteks + kalimat kunci kapital + satu frasa stabilo
S.append(page(2, f'''
<div class="lead">Mungkin dia yang mengambilkan penghapus temannya. Yang menyisakan bangku untuk anak baru. Yang bertanya, “Kamu sudah makan?”</div>
<div class="g96"></div>
<div class="display">Rapor tidak punya kolom untuk itu.</div>
<div class="g40"></div>
<div class="title">{hl("Tapi kebaikannya nyata.")}</div>'''))
# 3 edukasi: judul + 2 poin berlabel + kalimat penutup
S.append(page(3, f'''
<div class="display">Nilai mengukur {hl("sebagian.")}</div>
<div class="g56"></div>
{item("Nilai menjawab satu hal", "Seberapa jauh anak menguasai materi pada satu waktu. Itu penting, tapi bukan seluruh dirinya.")}
<div class="g32"></div><div class="rule"></div><div class="g32"></div>
{item("Kebaikan tidak ikut terhitung", "Kepedulian, kesabaran, dan keberanian membantu mungkin tidak punya kolom di rapor.")}
<div class="grow" style="min-height:48px"></div>
<div class="title" style="font-size:52px">Anak yang hatinya besar tetap perlu tahu bahwa itu berharga.</div>'''))
# 4 tiga hal kecil (bernomor karena urutan)
S.append(page(4, f'''
<div class="display">Tiga hal kecil yang {hl("bisa dicoba.")}</div>
<div class="g72"></div>
<div class="steps">
{step(1, "Sebut kebaikannya.", "Katakan apa yang kamu lihat: “Tadi kamu membantu temanmu.”")}
{step(2, "Tuliskan.", "Tambahkan satu kalimat tentang sikapnya di catatan wali kelas.")}
{step(3, "Beri kepercayaan.", "Minta ia memimpin hal kecil, seperti membagikan lembar kerja.")}
</div>'''))
# 5 PUNCAK: halaman kuning penuh (band=True). Tanpa stabilo di halaman ini (sudah kuning).
S.append(page(5, f'''
<div class="lead">Tidak perlu pidato panjang. Cukup satu kalimat:</div>
<div class="g40"></div>
<div class="display" style="font-size:132px">Aku melihatmu.</div>
<div class="grow"></div>
<div class="lead" style="opacity:.75">Lalu biarkan dia pulang membawa kalimat ini:</div>
<div class="g24"></div>
<div class="quote">“Guruku melihat kebaikanku.”</div>
<div class="g40"></div>''', band=True))
# 6 ajakan besok + kalimat menyentuh + kartu CTA buku
S.append(page(6, f'''
<div class="lead">Besok, perhatikan satu murid yang nilainya biasa saja. Cari satu hal baik yang ia lakukan. Lalu katakan padanya.</div>
<div class="g56"></div>
<div class="title">Mungkin itu pujian yang {hl("tidak tertulis")} di rapor mana pun.</div>
<div class="grow"></div>
<div class="card"><div class="lead" style="font-weight:800;font-size:40px;line-height:1.2">Simpan, lalu kirim ke satu guru yang kamu kenal.</div>
<div class="g16"></div><div class="small">Kisah murid yang tak terlihat seperti ini kutulis di buku <b style="color:{INK}">Kelas Ini Tidak Pernah Selesai</b>. Info bukunya ada di postingan tersemat di profil.</div></div>''', NOTE))

os.makedirs(OUT, exist_ok=True)
for i, s in enumerate(S, 1): open(os.path.join(OUT, f"s{i}.html"), "w").write(s)

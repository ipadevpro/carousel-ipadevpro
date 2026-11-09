import os
import sys
# usage: python3 gen_buku.py <outdir>
OUT=sys.argv[1] if len(sys.argv)>1 else os.path.dirname(os.path.abspath(__file__))
INK="#1B1B1F"; GREY="#5E594E"; RED="#B5483A"
HL="background: linear-gradient(transparent 12%, #FFE14D 12%, #FFE14D 92%, transparent 92%); padding: 0 6px; margin: 0 -6px; box-decoration-break: clone; -webkit-box-decoration-break: clone"
# type scale
DISPLAY=f"font-weight:900;letter-spacing:-2px;line-height:1.02;text-transform:uppercase"
HEAD=f"font-weight:900;letter-spacing:-1.2px;line-height:1.08"
BODY=f"font-size:44px;line-height:1.45;font-weight:500;color:{INK}"
LABEL=f"font-size:28px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:{RED}"

def page(n, inner, footer=""):
    holes="".join(f'<div style="position:absolute;left:52px;top:{t}px;width:40px;height:40px;border-radius:20px;background:#E3DAC3"></div>' for t in (180,640,1100))
    return f'''<!doctype html><html lang="id"><head><meta charset="utf-8"><title>Slide {n}</title><style>body{{margin:0}}</style></head><body>
<div style="position:relative;width:1080px;height:1350px;overflow:hidden;background-color:#FBF3DF;background-image:repeating-linear-gradient(to bottom,transparent 0,transparent 71px,rgba(120,150,185,0.18) 71px,rgba(120,150,185,0.18) 73px);background-position:0 40px;font-family:'Inter',system-ui,sans-serif;color:{INK}">
<div style="position:absolute;left:160px;top:0;width:3px;height:1350px;background:{RED};opacity:.75"></div>{holes}
<div style="position:absolute;left:210px;right:80px;top:60px;display:flex;justify-content:space-between;font-size:28px;font-weight:700"><span style="color:{RED}">@ipadevpro</span><span style="color:{GREY}">{n} / 6</span></div>
<div style="position:absolute;left:210px;right:90px;top:170px;bottom:150px;display:flex;flex-direction:column;justify-content:center">{inner}</div>
{footer}</div></body></html>'''

def gap(px): return f'<div style="height:{px}px;flex:0 0 {px}px"></div>'
def rule(): return f'<div style="height:3px;background:{INK};opacity:.12;margin:8px 0"></div>'
foot_swipe=f'<div style="position:absolute;left:210px;right:80px;bottom:60px;font-size:30px;font-weight:700;color:{GREY}">Geser pelan-pelan →</div>'
foot_note=f'<div style="position:absolute;left:210px;right:80px;bottom:56px;font-size:26px;line-height:1.35;font-weight:500;color:{GREY}">Tulisan ini renungan, bukan kisah satu murid tertentu.</div>'

S=[]
S.append(page(1, f"""
<div style="font-size:92px;{DISPLAY}">Namanya ada di daftar. <span style="{HL}">Perannya</span> belum ada.</div>
{gap(56)}
<div style="{BODY};font-size:46px;max-width:780px">Di setiap kelompok, mungkin ada satu anak yang suaranya paling pelan. Bisa jadi ia tidak malas. Ia belum tahu tempatnya di mana.</div>""", foot_swipe))
S.append(page(2, f"""
<div style="{BODY}">Tugas kelompok sudah dibagi rata di atas kertas.<br>Tapi anak yang pendiam bisa kebagian satu kalimat:<br>“Kamu ikut saja, ya.”</div>
{gap(64)}
<div style="font-size:92px;{DISPLAY}">Ikut saja bukan peran.</div>
{gap(32)}
<div style="font-size:64px;{HEAD}"><span style="{HL}">Itu hanya nama di daftar.</span></div>"""))
def item(num,label,text):
    return f"""<div style="display:flex;flex-direction:column;gap:14px"><div style="{LABEL}">{num} &nbsp;{label}</div><div style="{BODY}">{text}</div></div>"""
S.append(page(3, f"""
<div style="font-size:70px;{DISPLAY}">Pendiam belum tentu <span style="{HL}">tidak mau.</span></div>
{gap(56)}
{item("01","Diam bukan kosong","Bisa jadi ia sedang menimbang. Sebagian anak berpikir dulu sebelum bicara.")}
{gap(34)}{rule()}{gap(34)}
{item("02","Peran membuka pintu","Peran yang jelas memberi alasan untuk bersuara, tanpa harus berebut giliran.")}
{gap(56)}
<div style="font-size:52px;{HEAD}">Nama memberi tempat di daftar. Peran memberi tempat di kelompok.</div>"""))
def step(n,t,d):
    return f"""<div style="display:flex;gap:30px;align-items:flex-start">
<div style="flex:0 0 76px;width:76px;height:76px;border-radius:38px;background:{RED};color:#FBF3DF;display:flex;align-items:center;justify-content:center;font-size:38px;font-weight:900">{n}</div>
<div style="flex:1 1 0;min-width:0;display:flex;flex-direction:column;gap:8px;padding-top:6px"><div style="font-size:50px;{HEAD}">{t}</div><div style="{BODY};font-size:40px;color:{GREY}">{d}</div></div></div>"""
S.append(page(4, f"""
<div style="font-size:88px;{DISPLAY}">Tiga hal kecil yang <span style="{HL}">bisa dicoba.</span></div>
{gap(60)}
{step(1,"Beri peran bernama.","Penjaga waktu, pencatat, atau pembawa kesimpulan.")}
{gap(44)}
{step(2,"Cocokkan dengan caranya.","Anak yang suka menulis mungkin nyaman jadi pencatat.")}
{gap(44)}
{step(3,"Minta satu kalimat saja.","Cukup menyampaikan hasil kelompok, setelah diberi waktu menyiapkan.")}"""))
S.append(page(5, f"""
<div style="{BODY}">Kamu tidak perlu mengubah anak yang pendiam. Cukup satu hal:</div>
{gap(40)}
<div style="font-size:112px;{DISPLAY}">Beri ia tempat.</div>
{gap(64)}
<div style="{BODY};color:{GREY}">Semoga ia merasa kelompok ini butuh:</div>
{gap(28)}
<div style="border-left:10px solid {RED};padding:6px 0 6px 36px"><div style="font-size:66px;{HEAD}"><span style="{HL}">“Ada bagianku yang dipakai.”</span></div></div>"""))
S.append(page(6, f"""
<div style="{BODY}">Besok, sebelum kelompok mulai bekerja, tulis satu peran di samping setiap nama.</div>
{gap(48)}
<div style="font-size:64px;{HEAD}">Mungkin itu cara ia merasa <span style="{HL}"><span style="white-space:nowrap">dibutuhkan.</span></span></div>
{gap(72)}
<div style="border:4px solid {INK};border-radius:20px;padding:34px 38px;background:#FFFDF6;display:flex;flex-direction:column;gap:16px">
<div style="font-size:42px;{HEAD}">Simpan, lalu kirim ke satu guru yang kamu kenal.</div>
<div style="font-size:34px;line-height:1.4;font-weight:500;color:{GREY}">Kisah murid yang butuh dilihat kutulis di buku <b style="color:{INK}">Kelas Ini Tidak Pernah Selesai</b>. Link di bio.</div></div>""", foot_note))
for i,s in enumerate(S,1): open(os.path.join(OUT,f"s{i}.html"),"w").write(s)

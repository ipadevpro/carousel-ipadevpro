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
# 1 hook
S.append(page(1, f'''
<div style="font-size:96px;{DISPLAY}">Anak yang kamu cap nakal mungkin sedang <span style="{HL}">mencoba bicara.</span></div>
{gap(56)}
<div style="{BODY};font-size:46px;max-width:740px">Bukan dengan kata-kata. Dengan cara yang paling bisa ia lakukan.</div>''', foot_swipe))
# 2
S.append(page(2, f'''
<div style="{BODY}">Dia mengganggu teman.<br>Dia menyela saat kamu bicara.<br>Dia menantang.</div>
{gap(64)}
<div style="font-size:92px;{DISPLAY}">Perilakunya keras.</div>
{gap(32)}
<div style="font-size:64px;{HEAD}"><span style="{HL}">Tapi pesannya bisa jadi pelan.</span></div>'''))
# 3
def item(num,label,text):
    return f'''<div style="display:flex;flex-direction:column;gap:14px"><div style="{LABEL}">{num} &nbsp;{label}</div><div style="{BODY}">{text}</div></div>'''
S.append(page(3, f'''
<div style="font-size:88px;{DISPLAY}">Cap menutup <span style="{HL}">pertanyaan.</span></div>
{gap(60)}
{item("01","Cap menjawab terlalu cepat","Kata “nakal” terasa seperti jawaban. Padahal pertanyaan “kenapa” belum sempat ditanyakan.")}
{gap(36)}{rule()}{gap(36)}
{item("02","Didengar itu kebutuhan","Anak yang merasa tidak didengar mungkin mencari cara lain agar terlihat.")}
{gap(60)}
<div style="font-size:52px;{HEAD}">Perilaku perlu dibatasi. Anaknya perlu didengar.</div>'''))
# 4
def step(n,t,d):
    return f'''<div style="display:flex;gap:30px;align-items:flex-start">
<div style="flex:0 0 76px;width:76px;height:76px;border-radius:38px;background:{RED};color:#FBF3DF;display:flex;align-items:center;justify-content:center;font-size:38px;font-weight:900">{n}</div>
<div style="flex:1 1 0;min-width:0;display:flex;flex-direction:column;gap:8px;padding-top:6px"><div style="font-size:50px;{HEAD}">{t}</div><div style="{BODY};font-size:40px;color:{GREY}">{d}</div></div></div>'''
S.append(page(4, f'''
<div style="font-size:88px;{DISPLAY}">Tiga hal kecil yang <span style="{HL}">bisa dicoba.</span></div>
{gap(64)}
{step(1,"Batasi perilakunya.","Katakan apa yang tidak boleh, tanpa menyebut ia anak yang bagaimana.")}
{gap(48)}
{step(2,"Tanya berdua saja.","Di luar keramaian: “Tadi kenapa?” Lalu dengarkan sampai selesai.")}
{gap(48)}
{step(3,"Beri tugas kecil.","Peran yang jelas bisa lebih menenangkan daripada larangan.")}'''))
# 5
S.append(page(5, f'''
<div style="{BODY}">Sebelum menegur untuk kesekian kali, coba satu hal:</div>
{gap(40)}
<div style="font-size:120px;{DISPLAY}">Dengarkan dulu.</div>
{gap(64)}
<div style="{BODY};color:{GREY}">Lalu mungkin ia pulang membawa kalimat ini:</div>
{gap(28)}
<div style="border-left:10px solid {RED};padding:6px 0 6px 36px"><div style="font-size:72px;{HEAD}"><span style="{HL}">“Hari ini ada yang mau mendengarku.”</span></div></div>'''))
# 6
S.append(page(6, f'''
<div style="{BODY}">Besok, saat ada anak yang membuatmu ingin berkata “kamu nakal”, tarik napas sebentar. Ganti dengan satu pertanyaan.</div>
{gap(48)}
<div style="font-size:60px;{HEAD}">Mungkin itu <span style="{HL}"><span style="white-space:nowrap">pertama kalinya</span></span> ia ditanya, bukan dihakimi.</div>
{gap(72)}
<div style="border:4px solid {INK};border-radius:20px;padding:34px 38px;background:#FFFDF6;display:flex;flex-direction:column;gap:16px">
<div style="font-size:42px;{HEAD}">Simpan, lalu kirim ke satu guru yang kamu kenal.</div>
<div style="font-size:34px;line-height:1.4;font-weight:500;color:{GREY}">Kisah murid yang sulit dimengerti kutulis di buku <b style="color:{INK}">Kelas Ini Tidak Pernah Selesai</b>. Link di bio.</div></div>''', foot_note))
for i,s in enumerate(S,1): open(os.path.join(OUT,f"s{i}.html"),"w").write(s)

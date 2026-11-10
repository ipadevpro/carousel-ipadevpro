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
<div style="font-size:92px;{DISPLAY}">Ada anak yang nilainya <span style="{HL}">biasa saja.</span></div>
{gap(56)}
<div style="{BODY};font-size:46px;max-width:760px">Tapi ia sudah berusaha lebih keras dari biasanya. Apakah ada yang melihatnya?</div>''', foot_swipe))
# 2
S.append(page(2, f'''
<div style="{BODY}">Rapor memuat angka.<br>Angka mudah dilihat dan mudah dibandingkan.</div>
{gap(64)}
<div style="font-size:88px;{DISPLAY}">Usaha tidak punya kolom.</div>
{gap(32)}
<div style="font-size:64px;{HEAD}"><span style="{HL}">Jadi sering tidak tercatat.</span></div>'''))
# 3 education
def item(num,label,text):
    return f'''<div style="display:flex;flex-direction:column;gap:14px"><div style="{LABEL}">{num} &nbsp;{label}</div><div style="{BODY}">{text}</div></div>'''
S.append(page(3, f'''
<div style="font-size:84px;{DISPLAY}">Nilai menjawab <span style="{HL}">hasilnya.</span></div>
{gap(60)}
{item("01","Hasil","Nilai memberi tahu seberapa jauh anak sudah sampai hari ini.")}
{gap(36)}{rule()}{gap(36)}
{item("02","Usaha","Usaha bisa jadi satu-satunya hal yang sepenuhnya ada di tangan anak.")}
{gap(60)}
<div style="font-size:52px;{HEAD}">Anak yang terus mencoba perlu tahu bahwa itu terlihat.</div>'''))
# 4 actions
def step(n,t,d):
    return f'''<div style="display:flex;gap:30px;align-items:flex-start">
<div style="flex:0 0 76px;width:76px;height:76px;border-radius:38px;background:{RED};color:#FBF3DF;display:flex;align-items:center;justify-content:center;font-size:38px;font-weight:900">{n}</div>
<div style="flex:1 1 0;min-width:0;display:flex;flex-direction:column;gap:8px;padding-top:6px"><div style="font-size:50px;{HEAD}">{t}</div><div style="{BODY};font-size:40px;color:{GREY}">{d}</div></div></div>'''
S.append(page(4, f'''
<div style="font-size:88px;{DISPLAY}">Tiga hal kecil yang <span style="{HL}">bisa dicoba.</span></div>
{gap(64)}
{step(1,"Sebut yang ia kerjakan.","“Kamu coba tiga cara tadi, ya.” Bukan sekadar “bagus”.")}
{gap(48)}
{step(2,"Lihat perubahannya.","Bandingkan dengan dirinya minggu lalu, bukan dengan temannya.")}
{gap(48)}
{step(3,"Tulis satu kalimat.","Satu kalimat di pinggir kertas ulangan bisa dibaca berkali-kali.")}'''))
# 5 peak
S.append(page(5, f'''
<div style="{BODY}">Kamu tidak perlu menunggu nilai yang bagus. Cukup satu hal:</div>
{gap(40)}
<div style="font-size:112px;{DISPLAY}">Rayakan usahanya.</div>
{gap(64)}
<div style="{BODY};color:{GREY}">Mungkin itu yang membuatnya mau mencoba lagi besok:</div>
{gap(28)}
<div style="border-left:10px solid {RED};padding:6px 0 6px 36px"><div style="font-size:68px;{HEAD}"><span style="{HL}">“Usahaku ternyata dilihat.”</span></div></div>'''))
# 6 close + cta
S.append(page(6, f'''
<div style="{BODY}">Besok, saat membagikan hasil kerja murid, cari satu anak yang nilainya biasa. Lalu sebutkan satu hal yang ia usahakan.</div>
{gap(48)}
<div style="font-size:62px;{HEAD}">Bisa jadi itu <span style="{HL}">pujian pertama</span> yang ia dengar minggu ini.</div>
{gap(72)}
<div style="border:4px solid {INK};border-radius:20px;padding:34px 38px;background:#FFFDF6;display:flex;flex-direction:column;gap:16px">
<div style="font-size:42px;{HEAD}">Simpan, lalu kirim ke satu guru yang kamu kenal.</div>
<div style="font-size:34px;line-height:1.4;font-weight:500;color:{GREY}">Renungan tentang murid yang jarang terlihat kutulis di buku <b style="color:{INK}">Kelas Ini Tidak Pernah Selesai</b>. Link di bio.</div></div>''', foot_note))
for i,s in enumerate(S,1): open(os.path.join(OUT,f"s{i}.html"),"w").write(s)

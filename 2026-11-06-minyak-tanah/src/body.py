# ---- slide 1
botol='''<ellipse cx="130" cy="318" rx="90" ry="12" fill="#BCCADA"/>
<rect x="92" y="95" width="76" height="205" rx="22" fill="#DDEBF5" stroke="#1B1B1F" stroke-width="6"/>
<rect x="92" y="190" width="76" height="110" rx="20" fill="#EDBE4E" stroke="#1B1B1F" stroke-width="6"/>
<rect x="110" y="55" width="40" height="44" rx="6" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="6"/>
<rect x="104" y="40" width="52" height="24" rx="6" fill="#B5483A" stroke="#1B1B1F" stroke-width="6"/>
<rect x="104" y="120" width="12" height="60" rx="6" fill="#FFFDF6"/>'''
kelapa='''<ellipse cx="395" cy="318" rx="100" ry="12" fill="#BCCADA"/>
<circle cx="395" cy="195" r="100" fill="#8B6B4A" stroke="#1B1B1F" stroke-width="6"/>
<path d="M330 150 Q 395 90 460 150" fill="none" stroke="#6B5038" stroke-width="10" stroke-linecap="round"/>
<circle cx="372" cy="170" r="11" fill="#1B1B1F"/><circle cx="418" cy="170" r="11" fill="#1B1B1F"/><circle cx="395" cy="204" r="11" fill="#1B1B1F"/>
<path d="M325 240 Q 395 285 465 240" fill="none" stroke="#6B5038" stroke-width="10" stroke-linecap="round"/>'''
sendok='''<ellipse cx="660" cy="318" rx="80" ry="12" fill="#BCCADA"/>
<ellipse cx="660" cy="110" rx="52" ry="68" fill="#E4E8EC" stroke="#1B1B1F" stroke-width="6"/>
<rect x="644" y="170" width="32" height="140" rx="14" fill="#E4E8EC" stroke="#1B1B1F" stroke-width="6"/>
<ellipse cx="648" cy="100" rx="12" ry="34" fill="#FFFFFF" opacity="0.8"/>'''
s1=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 30px">
<div style="font-size: 68px; line-height: 1.04; font-weight: 900; font-variation-settings: 'opsz' 32; letter-spacing: -1.5px">ANAK YANG TERMINUM MINYAK TANAH DARI BOTOL AIR MINERAL JANGAN {hl("DIPANCING MUNTAH.")}</div>
<div style="font-size: 44px; line-height: 1.1; font-weight: 900; font-variation-settings: 'opsz' 32; color: #B5483A">DAN AIR KELAPA BUKAN PENAWARNYA.</div>
<svg style="margin-top: 50px" width="790" height="350" viewBox="0 0 790 350" role="img" aria-label="Botol air mineral berisi cairan kuning, kelapa, dan sendok, masing-masing dicoret tanda larangan">
{botol}{kelapa}{sendok}{ban(130,190,110)}{ban(395,190,110)}{ban(660,190,110)}
</svg>
</div>
<div style="position: absolute; left: 210px; right: 80px; bottom: 56px; font-size: 32px; font-weight: 700; color: #1B1B1F">Geser untuk tahu kenapa →</div>"""

# ---- slide 2
s2=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 28px">
<div style="align-self: flex-start; padding: 10px 22px; border: 3px solid #1B1B1F; border-radius: 6px; background: #FFFDF6; font-size: 32px; line-height: 1.3; font-weight: 800">Namaku: Minyak Tanah.<br>Julukanku: Si Licin Penyusup.</div>
<div style="font-size: 58px; line-height: 1.07; {H}">KAMU MENGIRA SEMUANYA HARUS DIMUNTAHKAN SEKARANG JUGA.</div>
<div style="font-size: 58px; line-height: 1.07; {H}">{hl("SAAT DIPAKSA MUNTAH, AKU NAIK LAGI KE TENGGOROKAN.")}</div>
<div style="font-size: 34px; line-height: 1.4; font-weight: 500">Aku cairan encer dan licin. Di situ aku mudah terhirup masuk ke saluran napas.</div>
<svg width="790" height="340" viewBox="0 0 790 340" role="img" aria-label="Minyak Tanah, tokoh tetesan kuning, berdiri di samping botol air mineral bekas">
<ellipse cx="200" cy="322" rx="130" ry="12" fill="#BCCADA"/><ellipse cx="610" cy="322" rx="110" ry="12" fill="#BCCADA"/>
{epi("e2",40,-8,0.8,e_calm())}
<g transform="translate(520 0) scale(1.1)"><rect x="40" y="95" width="76" height="205" rx="22" fill="#DDEBF5" stroke="#1B1B1F" stroke-width="6"/>
<rect x="40" y="190" width="76" height="110" rx="20" fill="#EDBE4E" stroke="#1B1B1F" stroke-width="6"/>
<rect x="58" y="55" width="40" height="44" rx="6" fill="#FFFDF6" stroke="#1B1B1F" stroke-width="6"/>
<rect x="52" y="40" width="52" height="24" rx="6" fill="#B5483A" stroke="#1B1B1F" stroke-width="6"/></g>
</svg>
</div>"""

def item(label,txt):
    return f'''<div style="display: flex; flex-direction: column; gap: 14px">
<div style="align-self: flex-start; padding: 6px 20px; background: #FFFDF6; border: 3px solid #1B1B1F; color: #1B1B1F; border-radius: 6px; font-size: 32px; font-weight: 800">{label}</div>
<div style="font-size: 40px; line-height: 1.34; font-weight: 500">{txt}</div></div>'''
# ---- slide 3
s3=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 34px">
<div style="font-size: 70px; line-height: 1.05; {H}">KENAPA MEMANCING MUNTAH {hl("KELIRU?")}</div>
{item("DI PARU-PARU AKU MENYEBAR TIPIS","Aku merusak lapisan yang membuat kantung udara tetap mengembang. Batuk setelah menelanku bisa jadi tanda aku sudah masuk ke saluran napas.")}
{item("AIR KELAPA TIDAK MENARIKKU KELUAR","Memaksa minum banyak justru bisa memicu muntah lagi.")}
<div style="font-size: 36px; line-height: 1.35; font-weight: 800; color: #B5483A">Gejalanya bisa memburuk dalam beberapa jam: batuk terus-menerus, napas cepat, sesak, demam, atau anak tampak lemas.</div>
{scene("e3",e_worried(),"JANGAN PANCING","AKU MUNTAH","Minyak Tanah tampak cemas dan berkata: jangan pancing aku muntah",230)}
</div>"""

def step(n,t):
    return f'''<div style="display: flex; gap: 26px; align-items: flex-start">
<div style="flex: 0 0 72px; width: 72px; height: 72px; border-radius: 36px; background: #B5483A; border: 4px solid #1B1B1F; box-sizing: border-box; color: #FBF3DF; display: flex; align-items: center; justify-content: center; font-size: 40px; font-weight: 900">{n}</div>
<div style="flex: 1 1 0; min-width: 0; font-size: 40px; line-height: 1.34; font-weight: 600">{t}</div></div>'''
# ---- slide 4
s4=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 40px">
<div style="font-size: 76px; line-height: 1.04; {H}">YANG {hl("BENAR")} DILAKUKAN</div>
{step(1,'<span style="font-weight: 900">Dudukkan anak tegak.</span>')}
{step(2,'<span style="font-weight: 900">Amankan botolnya</span> untuk ditunjukkan ke petugas kesehatan.')}
{step(3,'<span style="font-weight: 900">Segera bawa ke IGD terdekat,</span> walau anak terlihat baik-baik saja.')}
<div style="font-size: 34px; line-height: 1.4; font-weight: 700; color: #B5483A">Jangan paksa minum apa pun.</div>
<div style="margin-top: 70px">{scene("e4",e_calm(),"BAWA AKU","KE IGD","Minyak Tanah tenang berkata: bawa aku ke IGD",260)}</div>
</div>"""

def bul(t): return f'<div style="display: flex; gap: 22px"><span aria-hidden="true" style="flex: 0 0 18px; width: 18px; height: 18px; margin-top: 17px; background: #B5483A; border: 3px solid #1B1B1F; box-sizing: border-box; border-radius: 3px"></span><span>{t}</span></div>'
# ---- slide 5
s5=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 40px">
<div style="background: #B5483A; color: #FBF3DF; border-radius: 16px; padding: 36px 40px">
<div style="font-size: 56px; line-height: 1.06; {H}">JANGAN SIMPAN AKU DI BOTOL MINUMAN.</div>
</div>
<div style="font-size: 52px; line-height: 1.06; {H}">UNTUK {hl("GURU")} DI SEKOLAH:</div>
<div style="display: flex; flex-direction: column; gap: 22px; font-size: 42px; line-height: 1.25; font-weight: 700">
{bul("beri label jelas pada minyak tanah, tiner, dan bensin")}
{bul("simpan jauh dari jangkauan murid")}
{bul("bila tertelan, bawa anak dan wadahnya ke IGD")}
</div>
<div style="font-size: 36px; line-height: 1.35; font-weight: 800; color: #B5483A">Di rumah juga sama: simpan di wadah aslinya.</div>
<div style="margin-top: 20px">{scene("e5",e_worried(),"BOTOL MINUM","BUKAN RUMAHKU","Minyak Tanah tampak cemas dan berkata: botol minum bukan rumahku",260)}</div>
</div>"""

# ---- slide 6
s6=f"""<div style="position: absolute; left: 210px; right: 80px; top: 150px; display: flex; flex-direction: column; gap: 30px">
<div style="font-size: 40px; line-height: 1.3; font-weight: 500">Aku tidak berniat menyakiti. Aku hanya cairan yang salah tempat: botol minum, lalu paru-paru.</div>
<div style="font-size: 62px; line-height: 1.06; {H}">KALIAN BISA MENCEGAH KEDUANYA. {hl("CUKUP DENGAN BOTOL YANG TEPAT.")}</div>
<div style="font-size: 44px; font-weight: 800; color: #B5483A">Salam, Minyak Tanah.</div>
<div style="margin-top: 4px; display: flex; gap: 20px; align-items: center">
<div style="flex: 1 1 0; min-width: 0; border: 4px solid #1B1B1F; border-radius: 16px; padding: 22px 28px; background: #FFFDF6; display: flex; flex-direction: column; gap: 10px">
<div style="font-size: 36px; line-height: 1.2; font-weight: 900">Simpan, lalu kirim ke guru penjaga gudang sekolahmu.</div>

</div>
<svg width="200" height="240" viewBox="0 0 200 240" role="img" aria-label="Minyak Tanah tersenyum lega" style="flex: 0 0 200px">
<ellipse cx="100" cy="226" rx="70" ry="9" fill="#BCCADA"/>
{epi("e6",-34,-6,0.6,e_happy())}
</svg>
</div></div>
<div style="position: absolute; left: 210px; right: 80px; bottom: 40px; font-size: 25px; line-height: 1.35; font-weight: 600; color: #6B6558">Ceritanya fiksi, minyak tanah tidak berbicara. Nyata: memancing muntah setelah menelan hidrokarbon meningkatkan risiko aspirasi, dan air kelapa tidak terbukti sebagai penawar.</div>"""
import os
os.makedirs(out,exist_ok=True)
for i,s in enumerate([s1,s2,s3,s4,s5,s6],1):
    open(f'{out}/slide{i}.html','w').write(page(i,s))

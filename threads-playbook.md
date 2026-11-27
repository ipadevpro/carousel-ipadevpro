# Playbook Threads @ipadevpro

**Ini playbook utama (sumber tunggal) sejak 27 Nov 2026**, atas permintaan Devi supaya bisa diakses di semua sesi. Lokasi: repo GitHub `ipadevpro/carousel-ipadevpro`, file `threads-playbook.md` (branch `main`). Setiap sesi/tugas membaca file ini di awal, lalu menambah entri log dan commit + push ke `main` di akhir. Playbook lama di Project (`claude/threads-ipadevpro-playbook.md`) tidak dipakai lagi.
## Aset dan penjadwalan
- Akun Tebar Threads @ipadevpro: `fec1d1ef-eb77-41b4-9b22-76782bfc615b`.
- **Sejak 24 Nov 2026 semua penjadwalan Threads lewat Tebar**, bukan Buffer (Buffer kehilangan otorisasi ke Threads). Bila Tebar menolak, laporkan; jangan kembali ke Buffer.
- **Sejak 24 Nov 2026 thread terdiri dari 11 bagian** (1 postingan utama + 10 lanjutan), batas Tebar. Sebelumnya 13 bagian.
- Tebar `create_post`: `text` = bagian 1, `threads.thread` = array 10 string (bagian 2–11, bagian 1 tidak diulang). `scheduled_at` ISO +07:00, harus di masa depan.
- Slot harian: 07.00–16.00 WIB tiap jam bulat. Hook terkuat di 12.00 dan 13.00. Slot 16.00 = guru to guru. Jam yang sudah lewat digeser ke 17.00, 18.00, dst.
- Sebelum membuat postingan, cek Tebar `list_posts` status `scheduled` (limit 50) supaya tidak dobel. Postingan affiliate Shopee (menit :30), carousel IG/FB, dan akun sekolah bukan urusan tugas ini.
- Komentar organik = replies − 10 (thread 11 bagian) atau − 12 (thread 13 bagian sebelum 24 Nov).

## Struktur thread 11 bagian
1. Hook kapital: membalik label negatif, pernyataan keras, atau "PENGUMUMAN:".
2. "Namaku: … Julukanku: Si …" lalu perannya.
3. Adegan spesifik (jam, tempat) dengan anak tanpa nama, diikuti reaksi keliru orang dewasa dengan dialog (lelah/tidak tahu, bukan jahat).
4. Sudut pandang narator.
5. Konsekuensi/eskalasi, lalu perumpamaan "Bayangkan …".
6. Titik balik oleh orang dewasa tanpa nama (tanpa cameo guru IPA).
7. "Dalam sains, ini disebut … (…)", akurat; peneliti/tahun hanya bila yakin.
8. "Wahai Guru:" tiga poin "→".
9. "Ayah, Bunda:" tiga poin "→", termasuk kapan ke profesional.
10. Penutup hangat dari narator.
11. "Fakta vs dramatisasi:" (cerita fiksi, apa yang nyata, keterbatasan bukti).

Aturan: narator = organ, zat, mikroba, area otak, atau proses tubuh ("aku"). Tidak ada murid/guru bernama, bukan pengalaman nyata Devi. Maksimal 500 karakter per bagian (cek dengan python). Tidak memberi diagnosis atau saran medis spesifik.

## Soft selling dan jembatan
- Slot 16.00: Senin, Rabu, Jumat = soft selling huruf kecil "guru to guru" dengan ajakan "komentar RPP". Hari lain = pertanyaan ke sesama guru tanpa promosi, ditutup "drop di komen ya 😊". Variasikan sudutnya.
- P.S. RPP di akhir bagian 10 pada tepat 2 thread (topik paling dekat dengan beban kerja guru).
- Jembatan IG di akhir bagian 11 pada tepat 2 thread lain (slot 12.00 dan 13.00): "Versi carousel yang bisa disimpan ada di IG @ipadevpro (Seri Jangan Dulu)."
- Otomatisasi Tebar "Threads: komentar RPP" membalas komentar berisi "RPP" dengan link preview berpelacak.
- Fakta yang boleh dipakai: Devi yang membuat alatnya, ada preview gratis, ekspor ke Word, mencakup RPP/Modul Ajar, LKPD, soal HOTS. Dilarang: klaim tak terbukti, kesaksian karangan, harga/diskon, promosi di bagian 1–9 dan 11.

## Analisis pola (diperbarui 25 Nov 2026, data 5–24 Nov)
- **Pemenang terbesar** (x usual views): tersentak saat tertidur 277x (73,7 rb), haid lebih cepat bukan ayam suntik 112x (75,3 rb), ketindihan 81x, air direbus dua kali 77x, serumen/kotoran telinga 58x (47 rb), bergelantungan tidak menambah tinggi 51x, mi instan bukan lilin 47x, nasi sisa semalam 45x, gigitan lipan 42x, remaja lapar terus 38x (26 rb), tangan panas ulek cabai 31x.
- **Tiga kelompok topik yang paling sering meledak**: (1) tidur (hypnic jerk, ketindihan, tidur mata terbuka, suara memanggil); (2) mitos makanan/dapur dengan zat "tahan panas" atau "bukan racun" (air rebus dua kali, mi instan, nasi sisa, busa rebusan ayam); (3) pubertas dan tubuh yang tumbuh (haid, tinggi badan, lapar terus, serumen, canggung growth spurt).
- **Rumus hook terbaik**: label negatif pada tubuh anak dibalik ("BUKAN ANAK YANG JOROK/RAKUS/MANJA") + larangan cara rumahan yang keliru (cotton bud, diurut, pasta gigi) + situasi malu di depan keluarga/teman.
- **Yang lemah**: guru to guru tidak pernah lebih dari 1,6x (rata-rata 0,2–0,5x); soft selling rata-rata 343 views. Topik emosi/perilaku murid tanpa unsur tubuh yang jelas (merinding Indonesia Raya, tangan basah, tertawa saat ditegur) cenderung 0,5–0,6x.
- **Tren 24 Nov**: format 11 bagian stabil di 1,0–2,1x tetapi hampir 0 komentar organik. Belum ada yang meledak; perlu dipantau apakah lebih pendek memengaruhi diskusi.
- **Tren 26 Nov (update 27 Nov)**: format 11 bagian BISA meledak: Otot Masseter/gertak gigi "bukan cacingan" 130.394 views (110x, 314 share) dalam kurang dari sehari, rekor akun. Mengonfirmasi rumus tidur + mitos "cacingan" + dialog bentakan malam hari. Benjolan leher setelah pilek 5,7x (6,7 rb). Sisanya 0,9–2,1x. Hook "BAPAK, IBU GURU:" tetap lemah (0,5–1,0x).
- **Tren 27 Nov (update 28 Nov)**: Masseter terus tumbuh ke 168 rb (221x). Hari biasa tanpa outlier naik: semua thread 1,1–3,4x, rata-rata 1.553. Hook "ANAK YANG ... BUKAN ANAK YANG JOROK. DAN ... JANGAN [cara rumahan berbahaya]" kini konsisten jadi 2 teratas harian (kutu rambut, kutil, sebelumnya ngiler, kaki bau). PENGUMUMAN tentang sensasi sesaat (brain freeze, nanas) cenderung paling bawah. Soft selling dan P.S. RPP: 0 komentar RPP baru sejak 26 Nov.
- **Hari tanpa postingan** menurunkan views mingguan: 17, 22, 23 Nov kosong; views 7 hari turun 53% dibanding minggu sebelumnya.
- **Tren 25 Nov (hari kedua format 11 bagian)**: masih belum ada yang meledak; rentang 0,5–2,7x, rata-rata thread 1.019 views. Pemenang: hook "PENGUMUMAN:" tentang tubuh/makanan sehari-hari (hidung tersumbat bergantian 2,7x, tempe 1,7x). Hook "BAPAK, IBU GURU:" tentang emosi murid (wajah memerah) 0,6x; gigi hiu 0,5x. Komentar organik nyaris 0 (maks. 3). Dugaan: format 11 bagian atau hilangnya momentum setelah 2 hari kosong; pantau 3–5 hari lagi sebelum menyimpulkan.

## Narator/topik yang sudah dipakai (hindari mengulang)
5–24 Nov: pilek/antibiotik, gigi berlubang, haid keramas, ciki ngebul, radang tenggorokan, ketindihan, cacingan, tomcat, jengkolan, kesurupan massal, getah mangga, kedutan mata (2x), telinga berdenging (2x), mata juling, pandangan gelap, merinding, permen karet, lipan, hypnic jerk, kalajengking, mengigau, gundul, bintik putih kuku (2x), bunyi jari, mimpi gigi copot, night terror, patil lele, mandi malam, tidur mata terbuka, nyamuk, growing pains, kail pancing, mata minus/wortel, biji jambu, linglung magrib, sunburn, gula hiperaktif, suara memanggil, mandi setelah olahraga, murid menguap (2x), jerawat (2x), kehujanan, jamur liar, ulek cabai, berenang setelah makan, bangun jam tiga, memar, air dingin setelah lari, kaporit, bergelantungan, getah talas, seblak, sosok gelap, mi instan, keramik ambeien, déjà vu, bayam, ponsel dekat bantal, kopi, angkat beban, micin, haid dini, semangka, jarum pentul, air rebus dua kali, nasi sisa (2x), ayam dicuci, udang + vitamin C, gorengan + air dingin, beras plastik, ginekomastia, botol di mobil, keputihan, aturan lima detik, jelantah, telur cokelat, panci aluminium, telur + madu, ikan cacingan, haid es, microwave, jari keriput, air semalam, es batu, pusar, madu kristal, ceker, bawang merah demam, haid tak teratur, tidur setelah makan, kangkung, pingsan upacara, bau ketiak, susu UHT, suara pecah, kerokan, kresek hitam, mimisan, cegukan, kesemutan, solanin kentang, cincin hijau telur, bersin cahaya, canggung growth spurt, melatonin, keseleo, blank saat dipanggil, begadang, telur mengapung, tertawa ditegur, apel cokelat, Osgood-Schlatter, roti berjamur, payudara tumbuh, menatap ke atas, iris bawang, kulit susu, kerupuk melempem, merinding lagu, lapar remaja, tumit Sever, stretch mark, perut Senin, pisang bintik, busa rebusan, serumen, pare pahit, remaja nekat, telapak basah, mood remaja, anak laki-laki menangis, izin toilet, tas berat, kacamata minus, gigi kuning, luka bubuk kopi, sariawan, ketombe, kaki bau.
25 Nov: konka (siklus nasal), Rhizopus (tempe), gigi seri dewasa (gigi hiu), korteks prefrontal (sleepwalking), pembuluh darah pipi (blushing), neutrofil (bisul/telur), histamin (tongkol/skombroid), vasopresin (ngompol), adenoid (mendengkur).
26 Nov: bromelain (lidah perih nanas), kelenjar ludah (ngiler), kompleks motorik migrasi (perut bunyi di kelas), melanosit (uban remaja), tuba Eustachius (telinga budeg karyawisata), lempeng pertumbuhan kaki (sepatu cepat sempit), bakteri usus besar (kentut di kelas), otot masseter (gertak gigi/bruksisme), kelenjar getah bening (benjolan leher setelah pilek).
27 Nov: kasein (susu + jeruk), HPV kulit (kutil/kodok), Streptococcus mutans (ulat gigi; catatan: topik gigi berlubang sudah pernah dipakai sebelum 25 Nov, narator berbeda), memori kerja (doorway effect), saraf trigeminal (brain freeze), kutu rambut (pedikulosis), kelenjar kelopak mata (bintitan/hordeolum), sistem vestibular (mabuk perjalanan), otot siliaris (mata pegal layar).
28 Nov: folikel rambut (rontok/telogen), beta-karoten (karotenemia/telapak kuning), bakteri anaerob lidah (bau mulut pagi), serat otot (DOMS/pegal class meeting), otot betis (kram malam), tungau Sarcoptes (skabies/kudis santri), Malassezia (panu), adenovirus (konjungtivitis/belekan), kuku jempol kaki (cantengan/kuku tumbuh ke dalam).

## Log harian

### 28 Nov 2026 (Sabtu)
- Followers Threads 76.336 (−28 dalam 7 hari; −10 dari 26 Nov).
- 20–27 Nov: 60 postingan, rata-rata 5.236 views (median 1.061); thread rata-rata 5.782 (median 1.137); guru to guru 323. Views akun 7 hari 656 rb (+72% vs minggu sebelumnya menurut Tebar, didorong Otot Masseter). Klik akun 7 hari: 9.
- Top 3 (7 hari, x usual): Otot Masseter/gertak gigi 168.269 (221x, 98 komentar organik, 71 repost); serumen 47.123 (58x); remaja lapar terus 26.094 (37,8x). Benjolan leher naik ke 7.131 (9,4x).
- Kemarin (27 Nov), thread rata-rata 1.553 views (naik dari 1.019 pada 25 Nov). Top 3: kutu rambut "bukan jorok, jangan minyak tanah" 2.584 (3,4x, 9 komentar organik); kutil "bukan karena kodok" 2.434 (3,2x, 3 komentar); otot siliaris/mata pegal HP 1.632 (2,1x). Bottom 3: brain freeze (PENGUMUMAN) 825 (1,1x); ulat gigi 1.040 (1,4x); muntah di bus 1.240 (1,6x). Semua thread kemarin ≥1,1x, tidak ada yang di bawah usual.
- Soft selling 7 hari (20, 25, 27 Nov): rata-rata 338 views, 0 komentar RPP baru; guru to guru pertanyaan (21, 24, 26 Nov) rata-rata 308; thread 5.782.
- Otomatisasi komentar RPP: total 7 terpicu, 7 terkirim, 0 klik (tidak ada yang baru sejak 26 Nov 20.32 WIB).
- Hari tanpa postingan (7 hari): 22 dan 23 Nov.
- Pelajaran: label "jorok" + larangan cara rumahan yang berbahaya (minyak tanah) + mitos penyebab ("karena kodok") konsisten paling tinggi di hari tanpa outlier; hook PENGUMUMAN tentang sensasi sesaat (brain freeze) paling rendah. P.S. RPP di bagian 10 belum menghasilkan satu pun komentar RPP dalam 4 hari; ajakan mungkin terlalu jauh di bawah. Hari ini 4 thread pola pemenang: kudis santri, panu, belekan (ASI), cantengan (silet).
- Postingan terjadwal (Tebar):
  - 07.00 Folikel Rambut, rontok saat disisir bukan karena keramas (PENGUMUMAN)
  - 08.00 Beta-karoten, telapak kuning karena pepaya/wortel vs sakit kuning (PENGUMUMAN)
  - 09.00 Bakteri Anaerob Lidah, bau mulut pagi bukan jorok, jangan dikerik sendok
  - 10.00 Serat Otot, pegal setelah class meeting bukan asam laktat (DOMS) (**P.S. RPP**)
  - 11.00 Otot Betis, kram malam bukan kurang darah, jangan ditusuk peniti
  - 12.00 Tungau Sarcoptes, kudis santri bukan jorok/tanda betah, jangan minyak tanah (**jembatan IG**)
  - 13.00 Malassezia, panu bukan jorok, jangan lengkuas/minyak tanah (**jembatan IG**)
  - 14.00 Adenovirus, belekan tidak menular lewat tatapan, jangan tetes ASI (**P.S. RPP**)
  - 15.00 Kuku Jempol Kaki, cantengan bukan jorok, jangan dicungkil silet
  - 16.00 Guru to guru (Sabtu, tanpa promosi): pertanyaan murid paling tak terduga

### 27 Nov 2026 (Jumat)
- Followers Threads 76.345 (−22 dalam 7 hari; +8 dari kemarin).
- 19–26 Nov: 60 postingan, rata-rata 4.510 views (median 913); thread rata-rata 4.981 (median 1.000); guru to guru rata-rata 276. Views akun 7 hari 656 rb (−48% vs minggu sebelumnya menurut Tebar).
- Top 3 (7 hari, x usual): Otot Masseter/gertak gigi 130.394 (110,5x, 54 komentar organik, metrik masih berjalan); serumen 47.108 (58,1x); remaja lapar terus 26.086 (37,8x).
- Bottom 3 thread (7 hari): gigi hiu 462 (0,4x); merinding Indonesia Raya 365 (0,5x); kerupuk melempem 369 (0,5x).
- Soft selling (20 Nov 265, 25 Nov 328) rata-rata sekitar 297 vs guru to guru pertanyaan sekitar 265 vs thread 4.981.
- Otomatisasi komentar RPP: total 7 terpicu, 7 terkirim, 0 klik (terakhir 26 Nov sekitar 20.32 WIB). Klik akun Threads 7 hari: 32.
- Hari tanpa postingan: 22 dan 23 Nov.
- Pelajaran: format 11 bagian tidak menghalangi viral; yang menentukan tetap hook. Tidur + mitos "cacingan" + reaksi orang tua di kamar malam hari = outlier terbesar sejauh ini. Hari ini 4 thread pola pemenang memakai label "jorok/lemah" + larangan cara rumahan berbahaya (minyak tanah, sundut obat nyamuk, pencet, duduk di atas koran).
- Postingan terjadwal (Tebar):
  - 07.00 Kasein, susu setelah jeruk bukan racun (PENGUMUMAN)
  - 08.00 HPV jenis kulit, kutil bukan karena kodok
  - 09.00 Streptococcus mutans, gigi berlubang bukan ulat gigi
  - 10.00 Memori Kerja, lupa setelah masuk kamar (doorway effect) (**P.S. RPP**)
  - 11.00 Saraf Trigeminal, brain freeze es serut (PENGUMUMAN)
  - 12.00 Kutu Rambut, bukan jorok, jangan minyak tanah (**jembatan IG**)
  - 13.00 Kelenjar Kelopak Mata, bintitan bukan karena mengintip (**jembatan IG**)
  - 14.00 Sistem Vestibular, muntah di bus study tour
  - 15.00 Otot Siliaris, mata pegal karena HP bukan radiasi (**P.S. RPP**)
  - 16.00 Soft selling guru to guru (Jumat): malam sebelum supervisi
- Catatan: mulai hari ini playbook pindah resmi ke repo ini (lihat header).

### 26 Nov 2026 (Kamis)
- Followers Threads 76.336 (−7 dari kemarin; −43 dalam 7 hari).
- 18–25 Nov: 60 postingan, rata-rata 2.260 views; thread biasa rata-rata 2.480, median 877. Views akun 7 hari 381 rb (−46% vs minggu sebelumnya).
- Top 3 (7 hari, x usual): serumen 47.082 (58,1x); remaja lapar terus 26.074 (37,8x); busa rebusan ayam 6.195 (8,4x). Top 3 kemarin (25 Nov): konka/hidung tersumbat bergantian 2.282 (2,7x, 3 komentar organik); Rhizopus/tempe 1.446 (1,7x); adenoid/mendengkur 1.248 (1,5x).
- Bottom 3 kemarin (non guru to guru): gigi hiu 451 (0,5x); wajah memerah dipanggil ke depan 526 (0,6x, berisi P.S. RPP); ngompol 563 (0,7x). Rata-rata thread 25 Nov 1.019 views, median 747.
- Soft selling 25 Nov (Hari Guru) 249 views, 2 balasan; rata-rata guru to guru/soft selling 7 hari 281 vs thread 2.480.
- Otomatisasi komentar RPP: total 5 terpicu, 5 terkirim, 0 klik (1 baru pada 25 Nov sekitar 17.32 WIB). Klik akun Threads 7 hari: 30, semuanya 18–20 Nov.
- Hari tanpa postingan dalam 7 hari: 22 dan 23 Nov; 24 Nov mulai pukul 09.00.
- Pelajaran: dua hari format 11 bagian belum ada yang di atas 3x. Hook "PENGUMUMAN:" tubuh/dapur sehari-hari lebih stabil daripada hook "BAPAK, IBU GURU:" soal emosi murid. Hari ini dicoba lebih banyak label "jorok/cacingan" + larangan cara rumahan (ngiler, kentut, gertak gigi) dan pubertas (sepatu sempit, uban).
- Postingan terjadwal (Tebar):
  - 07.00 Bromelain, lidah perih setelah makan nanas (PENGUMUMAN)
  - 08.00 Kelenjar Ludah, ngiler bukan cacingan
  - 09.00 Kompleks Motorik Migrasi, perut bunyi saat kelas hening (**P.S. RPP**)
  - 10.00 Melanosit, uban remaja jangan dicabuti
  - 11.00 Tuba Eustachius, telinga budeg di bus karyawisata (**P.S. RPP**)
  - 12.00 Lempeng Pertumbuhan Kaki, sepatu cepat sempit saat pubertas (**jembatan IG**)
  - 13.00 Bakteri Usus Besar, kentut di kelas (**jembatan IG**)
  - 14.00 Otot Masseter, gertak gigi saat tidur bukan cacingan
  - 15.00 Kelenjar Getah Bening, benjolan leher setelah pilek
  - 16.00 Guru to guru (Kamis, tanpa promosi): materi paling susah bikin murid "klik"
- Catatan: alat Projects tetap tidak tersedia; playbook asli di Project tidak bisa dibaca/diperbarui, yang diperbarui salinan repo ini.

### 25 Nov 2026 (Rabu, Hari Guru Nasional)
- Followers Threads 76.343 (−51 dalam 7 hari, sekitar −7/hari).
- Rata-rata views 17–24 Nov: 2.500 per postingan (50 postingan); thread biasa rata-rata 2.746, median 884.
- Top 3: serumen/kotoran telinga 47.039 (58,3x, 21 komentar organik); remaja lapar terus 26.055 (37,9x, 61 komentar organik); busa rebusan ayam 6.193 (8,4x).
- Bottom 3 (non guru to guru): kerupuk melempem 360; merinding Indonesia Raya 362; telapak tangan basah dan telinga berdenging sound system ±420.
- Soft selling (18 Nov soal HOTS 427, 20 Nov LKPD 258) rata-rata 343 vs thread biasa 2.746. Guru to guru tanpa promosi rata-rata 241.
- Otomatisasi komentar RPP: 4 terpicu, 4 terkirim, 0 klik (tidak ada yang baru sejak 19 Nov).
- Hari tanpa postingan: 17, 22, 23 Nov.
- Pelajaran: thread 24 Nov (pertama dengan 11 bagian) stabil 1,0–2,1x tetapi 0 komentar organik; pemenang tetap label negatif dibalik + larangan cara rumahan + pubertas/tidur/mitos makanan.
- Postingan terjadwal (Tebar):
  - 07.00 Konka, hidung tersumbat bergantian (siklus nasal)
  - 08.00 Rhizopus, bulu putih tempe
  - 09.00 Gigi Seri Dewasa, gigi hiu (persistensi gigi susu)
  - 10.00 Korteks Prefrontal, berjalan saat tidur
  - 11.00 Pembuluh Darah Pipi, murid wajah memerah (**P.S. RPP**)
  - 12.00 Neutrofil, bisul bukan karena telur (**jembatan IG**)
  - 13.00 Histamin, gatal setelah makan tongkol (**jembatan IG**)
  - 14.00 Vasopresin, mengompol bukan karena main api
  - 15.00 Adenoid, anak mendengkur keras (**P.S. RPP**)
  - 16.00 Soft selling guru to guru edisi Hari Guru (Rabu)

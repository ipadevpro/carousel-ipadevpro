# Playbook Threads @ipadevpro

Salinan kerja playbook Threads di repo ini. Dibuat 25 Nov 2026 karena playbook asli di Project (`claude/threads-ipadevpro-playbook.md`) tidak bisa diakses oleh tugas harian (alat Projects tidak tersedia). Bila alat Projects kembali tersedia, samakan isi kedua file.

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
- **Hari tanpa postingan** menurunkan views mingguan: 17, 22, 23 Nov kosong; views 7 hari turun 53% dibanding minggu sebelumnya.

## Narator/topik yang sudah dipakai (hindari mengulang)
5–24 Nov: pilek/antibiotik, gigi berlubang, haid keramas, ciki ngebul, radang tenggorokan, ketindihan, cacingan, tomcat, jengkolan, kesurupan massal, getah mangga, kedutan mata (2x), telinga berdenging (2x), mata juling, pandangan gelap, merinding, permen karet, lipan, hypnic jerk, kalajengking, mengigau, gundul, bintik putih kuku (2x), bunyi jari, mimpi gigi copot, night terror, patil lele, mandi malam, tidur mata terbuka, nyamuk, growing pains, kail pancing, mata minus/wortel, biji jambu, linglung magrib, sunburn, gula hiperaktif, suara memanggil, mandi setelah olahraga, murid menguap (2x), jerawat (2x), kehujanan, jamur liar, ulek cabai, berenang setelah makan, bangun jam tiga, memar, air dingin setelah lari, kaporit, bergelantungan, getah talas, seblak, sosok gelap, mi instan, keramik ambeien, déjà vu, bayam, ponsel dekat bantal, kopi, angkat beban, micin, haid dini, semangka, jarum pentul, air rebus dua kali, nasi sisa (2x), ayam dicuci, udang + vitamin C, gorengan + air dingin, beras plastik, ginekomastia, botol di mobil, keputihan, aturan lima detik, jelantah, telur cokelat, panci aluminium, telur + madu, ikan cacingan, haid es, microwave, jari keriput, air semalam, es batu, pusar, madu kristal, ceker, bawang merah demam, haid tak teratur, tidur setelah makan, kangkung, pingsan upacara, bau ketiak, susu UHT, suara pecah, kerokan, kresek hitam, mimisan, cegukan, kesemutan, solanin kentang, cincin hijau telur, bersin cahaya, canggung growth spurt, melatonin, keseleo, blank saat dipanggil, begadang, telur mengapung, tertawa ditegur, apel cokelat, Osgood-Schlatter, roti berjamur, payudara tumbuh, menatap ke atas, iris bawang, kulit susu, kerupuk melempem, merinding lagu, lapar remaja, tumit Sever, stretch mark, perut Senin, pisang bintik, busa rebusan, serumen, pare pahit, remaja nekat, telapak basah, mood remaja, anak laki-laki menangis, izin toilet, tas berat, kacamata minus, gigi kuning, luka bubuk kopi, sariawan, ketombe, kaki bau.
25 Nov: konka (siklus nasal), Rhizopus (tempe), gigi seri dewasa (gigi hiu), korteks prefrontal (sleepwalking), pembuluh darah pipi (blushing), neutrofil (bisul/telur), histamin (tongkol/skombroid), vasopresin (ngompol), adenoid (mendengkur).

## Log harian

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

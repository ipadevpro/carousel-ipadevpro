# Pipeline harian: 2 carousel Instagram @ipadevpro

## Aset
- Buffer org id: 682887c330d408bb78641b35
- Channel Threads: 68288862f49c987a953a2e25
- Channel Instagram: 6ae81d63e29c69a171334a3d (business, direct publishing)
- Repo ini publik. URL gambar untuk Buffer: https://raw.githubusercontent.com/ipadevpro/carousel-ipadevpro/main/<folder>/slideN.jpg
- Zona waktu: Asia/Jakarta. Font Inter terpasang lokal (Google Fonts diblokir). Playwright sudah terpasang.

## Jadwal tayang (pakai mode customScheduled, BUKAN antrean) · berlaku sejak 15 Nov 2026
- Jalur A (pagi): 06:47 WIB, thread personifikasi dengan views tertinggi yang belum dipakai.
- Jalur A2 (sore): 15:47 WIB, thread personifikasi terbaik berikutnya (format A, template sama).
- Malam 20:13 WIB: Jalur C (tips & trik guru) pada Senin, Rabu, Jumat, Minggu; Jalur B (renungan) pada Selasa, Kamis, Sabtu.
- Soft selling RPP: Jalur C selalu (kartu CTA "DM saya RPP"); Jalur A pagi SOFT_SELLING = True hanya Selasa, Kamis, Sabtu (hari tanpa jalur C). Jalur A2 dan B tanpa promosi produk.
Sebelum membuat post, cek log.json: kalau tanggal+jalur (A, A2, B, C) sudah ada, lewati jalur tersebut.

## Jalur A: personifikasi edukasi (konversi thread viral)
- Sumber: post Threads terkirim (list_posts channel Threads, includeMetrics, telusuri beberapa halaman; get_post untuk isi thread penuh). Pilih format personifikasi (organ/penyakit/benda bercerita, "JANGAN ... DAN JANGAN ...", suara orang pertama) dengan views tertinggi yang belum ada di log.json.
- Gaya: sistem desain v2 (lihat bagian "Sistem desain v2"). Salin template/faring/gen_faring.py ke <folder>/src/, ganti isi daftar A (contoh lengkap: Leptin) dan maskot/ilustrasi bila tokohnya lain (flat 3 nada, outline tinta 7px, bayangan datar #BCCADA). Nama seri tetap "Seri Jangan Dulu" (bar atas). Kartu CTA slide 6 sudah memuat ajakan follow. Set SOFT_SELLING = True hanya untuk jalur A pagi pada Selasa/Kamis/Sabtu (RPP_LINE otomatis masuk ke kartu CTA slide 6).
- Render: python3 gen_faring.py <outdir> lalu node template/render_html.js <outdir> <outdir>
- 6 slide: hook larangan + ilustrasi dicoret + "Geser untuk tahu kenapa" / tokoh memperkenalkan diri + "kamu mengira... sering kali..." / kenapa keliru / yang benar (3 langkah) / tanda bahaya atau aturan kunci kedua / penutup suara tokoh + ajakan simpan dan kirim + catatan kaki fiksi untuk topik kesehatan.
- Hanya klaim yang ada di thread. Tidak menambah saran medis baru.

## Jalur B: renungan suara langsung, relevan dengan buku "Kelas Ini Tidak Pernah Selesai"
- Topik: ambil topik [ ] berikutnya dari topics-buku.md (boleh menulis topik baru yang setema bila habis), lalu tandai [x] + tanggal.
- TANPA karakter/maskot. Hanya tipografi. TANPA kutipan atau cerita ulang dari buku. TANPA anekdot murid rekaan seolah nyata.
- Gaya: sistem desain v2. Salin template/buku/gen_buku.py (contoh lengkap "Rapor tidak mencatat semuanya"), ganti isi daftar S, jalankan: python3 gen_buku.py <outdir> lalu node template/render_html.js <outdir> <outdir>.
- Slide 5 (puncak emosi) WAJIB halaman kuning penuh: page(5, ..., band=True), tanpa stabilo di halaman itu.
- Alur 6 slide: (1) hook menunjuk pembaca langsung + 1-2 kalimat konteks + "Geser pelan-pelan" / (2) konteks pendek lalu kalimat kunci kapital + penekanan stabilo / (3) edukasi: judul + 2 poin berlabel bata + kalimat penutup / (4) tiga hal kecil yang bisa dicoba / (5) puncak emosi, halaman kuning: satu kalimat display besar + kutipan tebal (tanpa garis merah) / (6) ajakan besok pagi + kalimat penutup menyentuh + kotak CTA "Simpan, lalu kirim ke satu guru yang kamu kenal." dan "Kisah murid ... kutulis di buku Kelas Ini Tidak Pernah Selesai. Link di bio." + catatan kaki "Tulisan ini renungan, bukan kisah satu murid tertentu."
- Caption: renungan singkat 3-5 kalimat, tiga hal kecil, ajakan simpan dan kirim, satu kalimat soft selling buku + "link di bio", 10 hashtag (#guru #guruindonesia #pendidikan #refleksiguru #muridku #kelasinitidakpernahselesai #bukuguru #gurupenggerak #parenting #ipadevpro).

## Jalur C: tips & trik guru (Senin, Rabu, Jumat, Minggu 20:13)
- Topik: ambil topik [ ] berikutnya dari topics-tips.md, tandai [x] + tanggal.
- Gaya: template/tips/gen_tips.py (contoh lengkap "Murid diam bukan berarti paham"), seri "Trik Kelas". Struktur: hook + janji jumlah trik / tiga slide trik (nomor besar, nama trik, caranya, kartu contoh) / kesalahan yang sering terlewat atau trik bonus / CTA: simpan + coba besok + follow + kartu "DM saya kata RPP".
- Otomatisasi Tebar "DM kata kunci" mengirim link rpp.aiforteacher.id ke yang DM kata RPP, LKPD, atau MODUL (khusus follower; yang belum follow diminta follow dulu). Jangan menyebut kata kunci lain di slide.
- Caption: 2-3 kalimat pengantar, tiga trik dalam satu baris masing-masing, ajakan simpan dan kirim ke rekan guru, "DM saya kata RPP untuk link preview gratis generator RPP, LKPD & soal HOTS", 10 hashtag (#guru #guruindonesia #tipsguru #triksmengajar #modulajar #rpp #lkpd #kurikulummerdeka #pendidikan #ipadevpro).
- Isi: praktis, bisa dicoba besok, tanpa angka/penelitian karangan, tanpa anekdot murid rekaan.

## Putaran umpan balik harian (Tebar)
- Akun Instagram di Tebar: @ipadevpro, account_id af1f1f5a-80e0-4117-8e1d-bb5d0c4572c7.
- Setiap hari: get_account_insights (days 7) untuk followers, views, reach, saves, shares, profile_links_taps; get_post_performance (days 14) untuk "kali lipat views biasa" dan follows per post; list_automations untuk statistik otomatisasi RPP (terpicu, terkirim, klik link).
- followers.md: tambah satu baris per hari (tanggal, followers, perubahan, views 7 hari, follows dari post kemarin, klik link otomatisasi).
- KPI utama: follows per 1.000 views per post dan klik link ke rpp.aiforteacher.id. Pilih thread jalur A/A2 yang polanya mirip pemenang (topik, jenis larangan, situasi sekolah/rumah) dan catat pelajarannya di results.md.

## Sistem desain v2 (berlaku sejak 15 Nov 2026, dasar: skill Impeccable)
Prinsip: dunia "buku tulis guru" dipertahankan (kertas bergaris, garis margin bata, lubang, Inter, stabilo, palet sama). Yang dikunci adalah sistemnya.
- Contoh tampilan: template/contoh/jalur-a.jpg, jalur-b.jpg, jalur-c.jpg. Jangan menyimpang dari CSS di gen_faring.py / gen_buku.py / gen_tips.py; yang boleh diubah per slide hanya ukuran .display/.title saat teks terlalu panjang.
- Bingkai: konten mulai x=176, kanan 88; judul selalu mulai di y=184 (top-aligned, TIDAK dipusatkan vertikal). Footer geser/catatan di bawah.
- Enam peran tipe saja: display 96px 900 KAPITAL (hanya kalimat pendek, maks sekitar 6 kata) / title 68px 800 huruf kalimat / lead 44px 500 / text 38px 500 / small 32px abu / label 30px 800 bata huruf kalimat. Kalimat hook yang panjang memakai .title, bukan kapital.
- Satu frasa stabilo per slide (kecuali slide kuning). Warna bata hanya untuk label, nomor langkah, dan satu kalimat penegas.
- Ritme spasi: kelas g8 sampai g96; rapat di dalam kelompok, longgar antar kelompok. Elemen anak .body tidak boleh menyusut (flex-shrink 0); bila konten tidak muat, perkecil teks atau potong kalimat, jangan menghapus jarak.
- DILARANG: kotak label berbingkai tebal, label kecil dekoratif di atas judul (eyebrow; perkenalan tokoh di slide 2 jalur A boleh karena itu isi), border-left tebal untuk kutipan, bayangan keras tanpa blur, bingkai hitam tebal pada kartu, nomor 01/02 bila urutan tidak penting.
- Kartu CTA: latar #FFFDF6, radius 28, bayangan lembut (sudah ada di kelas .card).
- Langkah bernomor memakai lingkaran bata .num (hanya bila urutan berarti); daftar biasa memakai titik .dot.

## Aturan isi (antislop, kedua jalur)
- Tidak mengarang angka, persentase, atau studi.
- Tanpa tanda pisah panjang (em dash), tanpa panah dekoratif (kecuali isyarat geser slide 1), tanpa pil/eyebrow dekoratif, tanpa ikon kilau.
- Palet: krem #FBF3DF, tinta #1B1B1F, abu hangat, bata #B5483A, stabilo #FFE14D.
- Periksa SETIAP JPG dengan Read: teks meluap, tumpang tindih (terutama kartu CTA vs catatan kaki di slide 6), kata terputus, ruang kosong besar, judul tidak di posisi y=184. Perbaiki sebelum push.

## Alur tugas harian (jalan 05:13 WIB)
1. Baca log.json, results.md, topics-buku.md.
2. Kerjakan jalur A lalu jalur B (lewati yang sudah ada di log untuk tanggal hari ini).
3. Simpan tiap carousel di folder YYYY-MM-DD-slug/ (JPG + src/), commit, push ke main.
4. Tunggu sekitar 3 menit, cek tiap URL raw (curl -I harus 200).
5. create_post ke channel Instagram: mode customScheduled, dueAt sesuai jadwal di atas (+07:00), schedulingType automatic, metadata.instagram {type: post, shouldShareToFeed: true}, 6 aset gambar dengan altText, caption + 10 hashtag. Jika jam tayang sudah lewat, pakai slot +2 jam dari sekarang.
6. Perbarui log.json (id post Buffer, jalur, tanggal) dan topics-buku.md.
7. results.md: untuk carousel yang sudah tayang >= 24 jam, ambil metrik IG (list_posts channel IG, includeMetrics) dan, untuk jalur A, views thread sumber; isi barisnya.
8. followers.md: jika ada tool yang menampilkan jumlah followers IG (cek get_channel / metrik Buffer), tambahkan satu baris harian beserta konten yang tayang kemarin. Jika tidak tersedia, tulis 'menunggu angka dari Devi' dan sebutkan di ringkasan akhir.
9. Reels: post video di channel Instagram yang dibuat di luar pipeline ini (Reels mitos/fakta sains, biasanya tayang sekitar 12:00 dan 19:00 WIB). JANGAN diubah atau dihapus. Untuk Reels yang sudah tayang >= 24 jam dan belum tercatat, ambil metriknya (list_posts channel IG, includeMetrics) dan tambahkan baris di tabel Reels di results.md.
10. Setiap Senin: tulis "Ringkasan mingguan" di results.md: rata-rata reach, saves, shares, dan komentar per format (Reels, Carousel A, Carousel B) selama 7 hari terakhir, 3 konten terbaik, perubahan followers dari followers.md, dan satu rekomendasi format mana yang diperbanyak.
11. Commit dan push. Jangan menghapus atau mengubah post yang sudah ada di Buffer.

# Pipeline harian: 2 carousel Instagram @ipadevpro

## Aset
- Buffer org id: 682887c330d408bb78641b35
- Channel Threads: 68288862f49c987a953a2e25
- Channel Instagram: 6ae81d63e29c69a171334a3d (business, direct publishing)
- Repo ini publik. URL gambar untuk Buffer: https://raw.githubusercontent.com/ipadevpro/carousel-ipadevpro/main/<folder>/slideN.jpg
- Zona waktu: Asia/Jakarta. Font Inter terpasang lokal (Google Fonts diblokir). Playwright sudah terpasang.

## Jadwal tayang (pakai mode customScheduled, BUKAN antrean)
- Jalur A: 06:47 WIB hari yang sama
- Jalur B: 20:13 WIB hari yang sama
Sebelum membuat post, cek log.json: kalau tanggal+jalur itu sudah ada, lewati jalur tersebut.

## Jalur A: personifikasi edukasi (konversi thread viral)
- Sumber: post Threads terkirim (list_posts channel Threads, includeMetrics, telusuri beberapa halaman; get_post untuk isi thread penuh). Pilih format personifikasi (organ/penyakit/benda bercerita, "JANGAN ... DAN JANGAN ...", suara orang pertama) dengan views tertinggi yang belum ada di log.json.
- Gaya: template/faring (6 file .dc.html). Kertas buku tulis, maskot tokoh narator (flat 3 nada, outline tinta, bayangan datar #BCCADA).
- Render: node template/render.js <dir berisi Main.dc.html + Slide2..6.dc.html> <outdir>
- 6 slide: hook larangan + ilustrasi dicoret + "Geser untuk tahu kenapa" / tokoh memperkenalkan diri + "kamu mengira... sering kali..." / kenapa keliru / yang benar (3 langkah) / tanda bahaya atau aturan kunci kedua / penutup suara tokoh + ajakan simpan dan kirim + catatan kaki fiksi untuk topik kesehatan.
- Hanya klaim yang ada di thread. Tidak menambah saran medis baru.

## Jalur B: renungan suara langsung, relevan dengan buku "Kelas Ini Tidak Pernah Selesai"
- Topik: ambil topik [ ] berikutnya dari topics-buku.md (boleh menulis topik baru yang setema bila habis), lalu tandai [x] + tanggal.
- TANPA karakter/maskot. Hanya tipografi. TANPA kutipan atau cerita ulang dari buku. TANPA anekdot murid rekaan seolah nyata.
- Gaya: template/buku/gen_buku.py (contoh lengkap "Anak di barisan depan"). Salin, ganti isi daftar slide S, jalankan: python3 gen_buku.py <outdir> lalu node template/render_html.js <outdir> <outdir>.
- Hierarki tipe (wajib): DISPLAY kapital 84-120px hanya untuk satu kalimat pendek per slide; HEAD 50-72px huruf biasa tebal untuk penekanan; BODY 40-46px huruf biasa; LABEL 28px merah kapital bernomor; satu frasa stabilo kuning per slide; kata berhubung dibungkus white-space:nowrap.
- Alur 6 slide: (1) hook menunjuk pembaca langsung + 1-2 kalimat konteks + "Geser pelan-pelan" / (2) konteks pendek lalu kalimat kunci kapital + penekanan stabilo / (3) edukasi: judul + 2 poin bernomor + kalimat penutup / (4) tiga hal kecil yang bisa dicoba / (5) puncak emosi: satu perintah kapital besar + kutipan bergaris merah / (6) ajakan besok pagi + kalimat penutup menyentuh + kotak CTA "Simpan, lalu kirim ke satu guru yang kamu kenal." dan "Kisah murid ... kutulis di buku Kelas Ini Tidak Pernah Selesai. Link di bio." + catatan kaki "Tulisan ini renungan, bukan kisah satu murid tertentu."
- Caption: renungan singkat 3-5 kalimat, tiga hal kecil, ajakan simpan dan kirim, satu kalimat soft selling buku + "link di bio", 10 hashtag (#guru #guruindonesia #pendidikan #refleksiguru #muridku #kelasinitidakpernahselesai #bukuguru #gurupenggerak #parenting #ipadevpro).

## Aturan isi (antislop, kedua jalur)
- Tidak mengarang angka, persentase, atau studi.
- Tanpa tanda pisah panjang (em dash), tanpa panah dekoratif (kecuali isyarat geser slide 1), tanpa pil/eyebrow dekoratif, tanpa ikon kilau.
- Palet: krem #FBF3DF, tinta #1B1B1F, abu hangat, bata #B5483A, stabilo #FFE14D.
- Periksa SETIAP JPG dengan Read: teks meluap, tumpang tindih, kata terputus, ruang kosong besar. Perbaiki sebelum push.

## Alur tugas harian (jalan 05:13 WIB)
1. Baca log.json, results.md, topics-buku.md.
2. Kerjakan jalur A lalu jalur B (lewati yang sudah ada di log untuk tanggal hari ini).
3. Simpan tiap carousel di folder YYYY-MM-DD-slug/ (JPG + src/), commit, push ke main.
4. Tunggu sekitar 3 menit, cek tiap URL raw (curl -I harus 200).
5. create_post ke channel Instagram: mode customScheduled, dueAt sesuai jadwal di atas (+07:00), schedulingType automatic, metadata.instagram {type: post, shouldShareToFeed: true}, 6 aset gambar dengan altText, caption + 10 hashtag. Jika jam tayang sudah lewat, pakai slot +2 jam dari sekarang.
6. Perbarui log.json (id post Buffer, jalur, tanggal) dan topics-buku.md.
7. results.md: untuk carousel yang sudah tayang >= 24 jam, ambil metrik IG (list_posts channel IG, includeMetrics) dan, untuk jalur A, views thread sumber; isi barisnya.
8. Commit dan push. Jangan menghapus atau mengubah post yang sudah ada di Buffer.

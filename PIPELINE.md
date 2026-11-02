# Pipeline harian: thread personifikasi Threads -> carousel Instagram @ipadevpro

## Aset
- Buffer org id: 682887c330d408bb78641b35
- Channel Threads: 68288862f49c987a953a2e25
- Channel Instagram: 6ae81d63e29c69a171334a3d (business, direct publishing)
- Repo ini publik. URL gambar untuk Buffer: https://raw.githubusercontent.com/ipadevpro/carousel-ipadevpro/main/<folder>/slideN.jpg
- Zona waktu: Asia/Jakarta. Font Inter terpasang lokal di sandbox (Google Fonts diblokir).

## Gaya visual (jangan diubah)
Kertas buku tulis 1080x1350: krem #FBF3DF, garis biru rgba(120,150,185,.35) tiap 72px, margin bata #B5483A di x=160, tiga lubang binder, tinta #1B1B1F, abu hangat #6B6558, bata #B5483A, stabilo kuning #FFE14D untuk satu frasa kunci per slide. Inter Black huruf kapital untuk judul. Maskot = tokoh yang bercerita di thread (flat 3 nada, outline tinta tebal, bayangan datar #BCCADA).
Referensi lengkap: folder template/faring (6 file .dc.html). Salin lalu ganti teks dan ilustrasi SVG.

## 6 slide
1. Hook: larangan utama (dari baris pertama thread) + ilustrasi dicoret + "Geser untuk tahu kenapa" (satu-satunya panah).
2. Tokoh memperkenalkan diri + kalimat 'kamu mengira... sering kali...' + ilustrasi tokoh.
3. Kenapa kebiasaan itu keliru (2 blok teks + ikon).
4. Yang benar dilakukan (3 langkah bernomor).
5. Tanda bahaya / kapan ke dokter atau IGD, atau aturan kunci kedua.
6. Penutup suara tokoh + ajakan simpan dan kirim ke grup WA guru dan wali murid + catatan kaki "Ceritanya fiksi... tidak menggantikan pemeriksaan dokter" (untuk topik kesehatan).

## Aturan isi (antislop)
- Hanya klaim yang ada di thread sumber. Dilarang mengarang angka, persentase, nama studi.
- Tanpa tanda pisah panjang (em dash), tanpa panah dekoratif, tanpa pil/eyebrow dekoratif, tanpa ikon kilau.
- Palet maksimal: netral + bata + kuning stabilo.
- Satu ide per slide, teks min 34px (catatan kaki min 26px).
- Topik kesehatan/keselamatan: tidak menambah saran medis baru di luar thread.

## Render
node template/render.js <dir berisi Main.dc.html + Slide2..6.dc.html> <outdir>   (hasil slide1..6.jpg, quality 92)
Cek tiap JPG dengan Read untuk teks yang meluap atau tumpang tindih sebelum push.

## Alur tugas harian
1. Baca log.json (thread yang sudah dikonversi) dan results.md.
2. Pilih thread: ambil post Threads sent (list_posts includeMetrics, halaman berurutan) berformat personifikasi (tokoh organ/penyakit/benda bercerita, "JANGAN ... DAN JANGAN ...", suara orang pertama), views tertinggi yang belum ada di log.json.
3. Buat 6 slide, render, periksa, simpan di folder YYYY-MM-DD-slug/ (JPG + src/), commit, push ke main.
4. Tunggu sekitar 3 menit, cek URL raw (curl -I harus 200), lalu create_post ke channel Instagram: mode addToQueue, schedulingType automatic, metadata.instagram {type: post, shouldShareToFeed: true}, 6 asset gambar dengan altText, caption + 10 hashtag. Caption: ringkasan thread, langkah benar, ajakan simpan dan kirim, catatan fiksi untuk topik kesehatan.
5. Perbarui log.json. Isi results.md untuk carousel yang sudah tayang >= 24 jam: ambil metrik IG (list_posts channel IG, includeMetrics) dan views thread sumber (get_post), tulis satu baris.
6. Commit dan push.

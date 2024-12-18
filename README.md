PENGELOMPOKAN MAHASISWA BERDASARKAN PARTISIPASI DI KEGIATAN SOSIAL DAN ORGANISASI DENGAN K-MEANS CLUSTERING UNTUK PENINGKATAN PROGRAM PENGEMBANGAN SOFT SKILLS DAN KEPEMIMPINAN.

Proyek ini adalah aplikasi berbasis web yang bertujuan untuk mengelompokkan mahasiswa berdasarkan tingkat partisipasi sosial dan organisasinya menggunakan algoritma K-Means Clustering. Aplikasi ini memungkinkan pengguna untuk mengunggah file CSV berisi data mahasiswa, kemudian memproses data tersebut untuk menghasilkan klaster yang menggambarkan kategori partisipasi masing-masing mahasiswa. Selain itu, hasil pengelompokan divisualisasikan secara interaktif menggunakan teknik Principal Component Analysis (PCA).

-> Fitur Utama
1. Unggah File CSV
Pengguna dapat mengunggah file CSV yang mengandung data partisipasi mahasiswa. File tersebut harus memiliki dua kolom utama:
Partisipasi_Sosial
Partisipasi_Organisasi

2. Pra-pemrosesan Data
Data pada kolom Partisipasi_Sosial dan Partisipasi_Organisasi distandarisasi menggunakan StandardScaler agar memiliki distribusi yang seragam.

3. Pengelompokan (Clustering)
Data diproses menggunakan algoritma K-Means Clustering dengan jumlah klaster optimal yang disetel ke 3. Setiap klaster diberi kategori berikut:
Pasif
Sedang
Aktif

4. Visualisasi Data
Data hasil klaster direduksi dimensinya menjadi dua menggunakan PCA. Hasil pengelompokan divisualisasikan dalam bentuk scatter plot, dengan warna berbeda untuk setiap kategori.

5. Tampilan Hasil
Tabel data yang telah dikelompokkan ditampilkan di halaman hasil.
Scatter plot visualisasi klaster ditampilkan langsung di halaman web.

Cara Kerja
1. Unggah Data
Pengguna mengunggah file CSV melalui antarmuka web.

2. Proses Data
Data divalidasi untuk memastikan kolom yang dibutuhkan ada.
Algoritma K-Means digunakan untuk melakukan pengelompokan.

3. Tampilkan Hasil
Hasil klasterisasi ditampilkan dalam tabel.
Scatter plot hasil pengelompokan divisualisasikan untuk mempermudah analisis.


-> Teknologi yang Digunakan
Python: Bahasa pemrograman utama.
Flask: Framework untuk pengembangan aplikasi web.
Pandas dan NumPy: Untuk manipulasi dan analisis data.
Scikit-learn: Untuk algoritma K-Means dan PCA.
Matplotlib dan Seaborn: Untuk visualisasi data.
HTML & CSS: Untuk antarmuka pengguna.


-> Cara Menjalankan Aplikasi
Pastikan Anda telah menginstal Python 3 dan pustaka berikut:
pip install flask pandas numpy scikit-learn matplotlib seaborn

Jalankan aplikasi dengan perintah:
python app.py

-> Struktur File
app.py: File utama aplikasi.
templates/index.html: Halaman awal untuk mengunggah file.
templates/hasil.html: Halaman hasil yang menampilkan tabel dan plot.

-> Lisensi
Kelompok 7 Pengenalan Pola
Nama Anggota Kelompok :
1. Nadzare Kafah Alfatiha (H1D023014)
2. Haniel Wijanarko (H1D023052)
3. Ananda Arsya Sabili (H1D023053)
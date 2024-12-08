PENGELOMPOKAN MAHASISWA BERDASARKAN PARTISIPASI DI KEGIATAN SOSIAL DAN ORGANISASI DENGAN K-MEANS CLUSTERING UNTUK PENINGKATAN PROGRAM PENGEMBANGAN SOFT SKILLS DAN KEPEMIMPINAN.

Proyek ini menggunakan algoritma K-Means Clustering untuk mengelompokkan mahasiswa berdasarkan dua fitur utama: Partisipasi Sosial dan Partisipasi Organisasi. Program ini memungkinkan pengguna untuk menginput data mahasiswa secara manual atau melalui file CSV, melakukan preprocessing, dan akhirnya mengelompokkan mahasiswa dalam kategori berdasarkan skor partisipasi mereka. Visualisasi dan analisis klaster juga disediakan untuk membantu memahami hasilnya.

Teknologi yang Digunakan
Python: Bahasa pemrograman utama.
Pandas: Untuk manipulasi data.
NumPy: Untuk komputasi numerik.
Matplotlib & Seaborn: Untuk visualisasi data.
Scikit-learn: Untuk algoritma K-Means dan StandardScaler.
Fitur
Input Data:

Input data dapat dilakukan melalui file CSV atau input manual.
Format CSV yang diperlukan harus memiliki kolom: Mahasiswa, Partisipasi_Sosial, Partisipasi_Organisasi.
Preprocessing Data:

Data partisipasi sosial dan organisasi akan distandarisasi agar sesuai untuk algoritma K-Means.
Metode Elbow:

Menentukan jumlah klaster yang optimal menggunakan Metode Elbow untuk membantu memilih jumlah klaster yang tepat.
K-Means Clustering:

Mahasiswa akan dikelompokkan ke dalam klaster berdasarkan partisipasi sosial dan organisasi.
Kategorisasi Klaster:

Setiap klaster akan diberikan kategori: Pasif, Sedang, dan Aktif.
Visualisasi:

Hasil klaster akan divisualisasikan dalam plot 2D menggunakan PCA (Principal Component Analysis).
Bar chart untuk menunjukkan rata-rata tingkat partisipasi per kategori.
Simpan Hasil:

Hasil pengelompokan mahasiswa beserta kategori disimpan dalam file CSV.
Cara Penggunaan
Persiapkan Data: Anda dapat memilih untuk mengimpor data melalui dua cara:

File CSV: Pastikan file CSV memiliki kolom Mahasiswa, Partisipasi_Sosial, dan Partisipasi_Organisasi.
Input Manual: Anda dapat memasukkan data mahasiswa secara langsung.
Jalankan Program: Setelah mempersiapkan data, jalankan program dengan memilih salah satu opsi input. Program ini akan melakukan pengelompokan data dan menampilkan hasil klaster.

Hasil: Hasil pengelompokan akan disimpan dalam file hasil_pengelompokan_mahasiswa.csv.

Instalasi
Untuk menjalankan proyek ini, pastikan Anda memiliki Python versi 3.x terinstal, serta pustaka yang diperlukan. Anda dapat menginstalnya dengan mengikuti langkah-langkah di bawah ini:

Clone Repository (Jika Ada):

bash
Copy code
git clone <url-repository>
cd <folder-proyek>
Buat Virtual Environment:

bash
Copy code
python -m venv env
Aktifkan Virtual Environment:

Di Windows:
bash
Copy code
.\env\Scripts\activate
Di macOS/Linux:
bash
Copy code
source env/bin/activate
Install Dependensi: Anda dapat menginstal dependensi yang diperlukan dengan menjalankan:

bash
Copy code
pip install -r requirements.txt
Struktur Proyek
bash
Copy code
.
├── main.py              # Program utama
├── data.csv             # Dataset input (contoh file)
├── hasil_pengelompokan_mahasiswa.csv  # Hasil pengelompokan
├── .gitignore           # File Git ignore
├── README.md            # Dokumentasi proyek
env                       # Virtual environment
Kontribusi
Jika Anda ingin berkontribusi pada proyek ini, silakan buat fork repository ini dan ajukan pull request. Pastikan untuk mengikuti pedoman pengkodean yang baik dan menyertakan penjelasan untuk setiap perubahan yang dilakukan.

Lisensi
Proyek ini dilisensikan di bawah kelompok pengenalan pola.

Penjelasan:
Bagian Pengenalan memberikan gambaran umum tentang proyek dan tujuannya.
Fitur menjelaskan berbagai fitur yang ada dalam program, seperti input data, proses pengelompokan, dan visualisasi.
Instruksi Penggunaan memberikan petunjuk langkah demi langkah agar pengguna dapat menjalankan program.
Instalasi berisi cara mengatur lingkungan dan menginstal dependensi yang diperlukan.
Struktur Proyek memberikan gambaran tentang struktur file dan folder dalam proyek.

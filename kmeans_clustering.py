import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import seaborn as sns

# 1. Input Data dari File CSV
def buat_data_dari_file(nama_file):
    try:
        df = pd.read_csv(nama_file)
        if 'Mahasiswa' in df.columns and 'Partisipasi_Sosial' in df.columns and 'Partisipasi_Organisasi' in df.columns:
            return df
        else:
            raise ValueError("Kolom yang diperlukan ('Mahasiswa', 'Partisipasi_Sosial', 'Partisipasi_Organisasi') tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file: {e}")
        exit()

# 2. Input Data Secara Manual
def input_data_manual():
    print("Masukkan data mahasiswa (ketik 'selesai' untuk berhenti):")
    data = {'Mahasiswa': [], 'Partisipasi_Sosial': [], 'Partisipasi_Organisasi': []}
    while True:
        nama = input("Nama Mahasiswa: ")
        if nama.lower() == 'selesai':
            break
        try:
            sosial = int(input("Skor Partisipasi Sosial (0-100): "))
            organisasi = int(input("Skor Partisipasi Organisasi (0-100): "))
            if 0 <= sosial <= 100 and 0 <= organisasi <= 100:
                data['Mahasiswa'].append(nama)
                data['Partisipasi_Sosial'].append(sosial)
                data['Partisipasi_Organisasi'].append(organisasi)
            else:
                print("Skor harus antara 0 hingga 100. Coba lagi.")
        except ValueError:
            print("Input harus berupa angka. Coba lagi.")

    return pd.DataFrame(data)

# 3. Preprocessing Data
def pra_proses_data(df):
    scaler = StandardScaler()
    fitur = ['Partisipasi_Sosial', 'Partisipasi_Organisasi']
    fitur_skala = scaler.fit_transform(df[fitur])
    return fitur_skala, fitur

# 4. Metode Elbow untuk Menentukan Jumlah Klaster Optimal
def metode_elbow(data):
    n_samples = data.shape[0]
    max_clusters = min(10, n_samples)  # Pastikan maksimum klaster <= jumlah data
    inertia = []
    for k in range(1, max_clusters):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data)
        inertia.append(kmeans.inertia_)

    plt.figure(figsize=(8, 5))
    plt.plot(range(1, max_clusters), inertia, marker='o', linestyle='--')
    plt.title('Metode Elbow untuk Menentukan Jumlah Klaster Optimal')
    plt.xlabel('Jumlah Klaster (k)')
    plt.ylabel('Inersia')
    plt.grid(True)
    plt.show()

# 5. Terapkan K-Means Clustering
def terapkan_kmeans(data, jumlah_klaster):
    kmeans = KMeans(n_clusters=jumlah_klaster, random_state=42)
    klaster = kmeans.fit_predict(data)
    return kmeans, klaster

# 6. Kategorisasi Klaster
def kategorisasi_klaster(df):
    kategori = {0: "Pasif", 1: "Sedang", 2: "Aktif"}
    rata_rata_klaster = df.groupby('Klaster')[['Partisipasi_Sosial', 'Partisipasi_Organisasi']].mean()
    rata_rata_klaster = rata_rata_klaster.sort_values(by=['Partisipasi_Sosial', 'Partisipasi_Organisasi'])
    mapping = {old: kategori[i] for i, old in enumerate(rata_rata_klaster.index)}
    df['Kategori'] = df['Klaster'].map(mapping)
    return df

# 7. Visualisasi Klaster
def visualisasi_klaster(df, data, klaster, kmeans, fitur):
    df['Klaster'] = klaster
    pca = PCA(n_components=2)
    data_reduksi = pca.fit_transform(data)

    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        x=data_reduksi[:, 0], y=data_reduksi[:, 1],
        hue=df['Kategori'], palette='Set2', s=100
    )
    plt.title('Pengelompokan Mahasiswa Berdasarkan Partisipasi')
    plt.xlabel('Komponen PCA 1')
    plt.ylabel('Komponen PCA 2')
    plt.legend(title='Kategori')
    plt.grid(True)
    plt.show()

    rata_rata_klaster = df.groupby('Kategori')[fitur].mean()
    rata_rata_klaster.plot(kind='bar', figsize=(10, 6), colormap='viridis')
    plt.title('Rata-rata Tingkat Partisipasi Per Kategori')
    plt.ylabel('Skor Rata-rata')
    plt.xlabel('Kategori')
    plt.grid(axis='y')
    plt.show()

# 8. Simpan Hasil ke CSV
def simpan_hasil_csv(df, nama_file):
    df.to_csv(nama_file, index=False)
    print(f"Hasil pengelompokan disimpan dalam file: {nama_file}")

# 9. Main Execution
def main():
    print("Pilih sumber data:")
    print("1. Input dari file CSV")
    print("2. Input data manual")
    pilihan = input("Masukkan pilihan (1/2): ")

    if pilihan == '1':
        nama_file = input("Masukkan nama file CSV (dengan ekstensi): ")
        df = buat_data_dari_file(nama_file)
    elif pilihan == '2':
        df = input_data_manual()
    else:
        print("Pilihan tidak valid.")
        return

    print("\nContoh Data:")
    print(df.head())

    data, fitur = pra_proses_data(df)
    print("\nMenentukan Jumlah Klaster Optimal Menggunakan Metode Elbow...")
    metode_elbow(data)

    print("\nMelakukan Pengelompokan K-Means...")
    jumlah_klaster_optimal = 3
    kmeans, klaster = terapkan_kmeans(data, jumlah_klaster_optimal)

    df['Klaster'] = klaster
    df = kategorisasi_klaster(df)

    print("\nVisualisasi Klaster...")
    visualisasi_klaster(df, data, klaster, kmeans, fitur)

    print("\nHasil Pengelompokan dengan Kategori:")
    print(df[['Mahasiswa', 'Partisipasi_Sosial', 'Partisipasi_Organisasi', 'Kategori']].head())
    simpan_hasil_csv(df, 'hasil_pengelompokan_mahasiswa.csv')

if __name__ == "__main__":
    main()

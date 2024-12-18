from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

app = Flask(__name__)

# Fungsi Helper untuk Clustering
def pra_proses_data(df):
    scaler = StandardScaler()
    fitur = ['Partisipasi_Sosial', 'Partisipasi_Organisasi']
    fitur_skala = scaler.fit_transform(df[fitur])
    return fitur_skala, fitur

def terapkan_kmeans(data, jumlah_klaster):
    kmeans = KMeans(n_clusters=jumlah_klaster, random_state=42)
    klaster = kmeans.fit_predict(data)
    return kmeans, klaster

def kategorisasi_klaster(df):
    kategori = {0: "Pasif", 1: "Sedang", 2: "Aktif"}
    rata_rata_klaster = df.groupby('Klaster')[['Partisipasi_Sosial', 'Partisipasi_Organisasi']].mean()
    rata_rata_klaster = rata_rata_klaster.sort_values(by=['Partisipasi_Sosial', 'Partisipasi_Organisasi'])
    mapping = {old: kategori[i] for i, old in enumerate(rata_rata_klaster.index)}
    df['Kategori'] = df['Klaster'].map(mapping)
    return df

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files['file']
        if file:
            try:
                # Baca file CSV
                df = pd.read_csv(file)
                # Validasi kolom yang dibutuhkan
                if not {'Partisipasi_Sosial', 'Partisipasi_Organisasi'}.issubset(df.columns):
                    return "File CSV harus memiliki kolom 'Partisipasi_Sosial' dan 'Partisipasi_Organisasi'."

                # Preprocessing dan K-Means
                data, fitur = pra_proses_data(df)
                jumlah_klaster_optimal = 3
                kmeans, klaster = terapkan_kmeans(data, jumlah_klaster_optimal)

                # Tambahkan hasil klaster ke DataFrame
                df['Klaster'] = klaster
                df = kategorisasi_klaster(df)

                # Visualisasi dengan PCA
                pca = PCA(n_components=2)
                data_reduksi = pca.fit_transform(data)
                df['PCA1'] = data_reduksi[:, 0]
                df['PCA2'] = data_reduksi[:, 1]

                # Plot Visualisasi
                plt.figure(figsize=(8, 6))
                sns.scatterplot(
                    x='PCA1', y='PCA2', hue='Kategori', data=df,
                    palette='Set2', s=100
                )
                plt.title('Pengelompokan Mahasiswa Berdasarkan Partisipasi')
                plt.grid(True)

                # Simpan plot ke buffer
                img = io.BytesIO()
                plt.savefig(img, format='png', bbox_inches='tight')
                img.seek(0)
                plot_url = base64.b64encode(img.getvalue()).decode()

                # Tampilkan hasil
                return render_template("hasil.html",
                                       tables=[df.to_html(classes='table table-striped table-bordered', escape=False, index=False)],
                                       plot_url=plot_url)

            except Exception as e:
                return f"Terjadi kesalahan: {e}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

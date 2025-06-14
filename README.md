# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institute adalah sebuah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan memiliki reputasi baik dalam menghasilkan lulusan berkualitas. Namun, seperti banyak institusi pendidikan lainnya, Jaya Jaya Institute menghadapi tantangan terkait tingkat dropout mahasiswa yang cukup tinggi.

Institusi ini memiliki berbagai program studi dan menerima mahasiswa dari berbagai latar belakang demografis dan akademis. Dengan semakin kompetitifnya dunia pendidikan tinggi, penting bagi institusi untuk dapat mengidentifikasi mahasiswa yang berisiko dropout sejak dini agar dapat memberikan intervensi yang tepat.

### Permasalahan Bisnis

1. **Tingkat Dropout yang Tinggi**:  
   Berdasarkan data historis, terdapat sejumlah signifikan mahasiswa yang tidak menyelesaikan pendidikan mereka (dropout), yang berdampak pada:

   - Penurunan revenue institusi
   - Reputasi institusi di mata publik
   - Pemborosan sumber daya pendidikan

2. **Kurangnya Sistem Early Warning**:  
   Institusi belum memiliki sistem yang dapat memprediksi mahasiswa mana yang berisiko dropout, sehingga intervensi hanya dilakukan secara reaktif.

3. **Pengelolaan Sumber Daya yang Tidak Optimal**:  
   Tanpa prediksi yang akurat, institusi kesulitan dalam:

   - Alokasi bimbingan akademik
   - Penyediaan program bantuan keuangan
   - Perencanaan kapasitas kelas

4. **Analisis Faktor Risiko**:  
   Belum ada pemahaman mendalam tentang faktor-faktor apa saja yang paling berpengaruh terhadap keputusan mahasiswa untuk dropout.

### Cakupan Proyek

Proyek ini mencakup:

1. **Analisis Data Mahasiswa**:  
   Menganalisis data historis mahasiswa termasuk data demografis, akademis, dan finansial
2. **Pengembangan Model Prediktif**:  
   Membangun model machine learning untuk memprediksi status kelulusan mahasiswa (Graduate, Enrolled, Dropout)
3. **Pembuatan Dashboard Bisnis**:  
   Mengembangkan dashboard interaktif untuk monitoring performa akademik dan identifikasi pola
4. **Sistem Prediksi Real-time**:  
   Mengimplementasikan aplikasi web untuk prediksi status mahasiswa secara real-time
5. **Analisis Faktor Risiko**:  
   Mengidentifikasi faktor-faktor utama yang mempengaruhi tingkat dropout
6. **Rekomendasi Strategis**:  
   Memberikan rekomendasi action items untuk mengurangi tingkat dropout

### Persiapan

**Sumber data**: [Dataset Mahasiswa Jaya Jaya Institute](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)

**Setup environment**:

```bash
# Install dependencies
pip install -r requirements.txt

# Clone repository
git clone https://github.com/f2rra/bpds-dropout/tree/main
cd bpds-dropout

# Jalankan aplikasi Streamlit
streamlit run app.py
```

## Business Dashboard

Dashboard bisnis telah dikembangkan untuk memberikan insights mendalam tentang performa mahasiswa Jaya Jaya Institute. Dashboard ini menampilkan:

### Key Metrics:

- **Distribusi Status Mahasiswa**: Visualisasi jumlah mahasiswa berdasarkan status (Graduate: 2,209, Enrolled: 794, Dropout: 1,421)
- **Persentase Status**: Breakdown persentase dari total populasi mahasiswa

### Performa Akademik:

- **Analisis SKS Semester 1 & 2**: Distribusi jumlah SKS yang diambil dan lulus berdasarkan status mahasiswa
- **Distribusi Nilai**: Pola sebaran nilai akademik untuk setiap semester
- **Tren Performa**: Analisis tren nilai admission dan kualifikasi sebelumnya

### Status Finansial:

- **Analisis Pembayaran**: Proporsi mahasiswa yang tepat waktu vs terlambat dalam pembayaran
- **Status Beasiswa**: Distribusi penerima dan non-penerima beasiswa
- **Analisis Hutang**: Profil mahasiswa yang memiliki hutang vs tidak

### Profil Mahasiswa:

- **Distribusi Usia**: Sebaran usia mahasiswa saat enrollment
- **Analisis Gender**: Proporsi mahasiswa berdasarkan gender
- **Status Displacement**: Analisis mahasiswa pindahan
- **Mode Aplikasi**: Distribusi berdasarkan cara pendaftaran

Dashboard dapat diakses melalui localhost sebagai berikut.

1. Buka terminal dan jalankan docker compose

```bash
docker compose up -d
```

2. Buka browser dan akses

```bash
https://localhost:3000
```

3. Jika dimintai login, masukkan email dan password berikut.

- email: root@mail.com
- password: root123

## Menjalankan Sistem Machine Learning

Sistem machine learning dapat dijalankan melalui aplikasi web berbasis Streamlit yang user-friendly:

### Cara Menjalankan:

```bash
# Pastikan semua dependencies terinstall
pip install -r requirements.txt

# Jalankan aplikasi
streamlit run app.py
```

### Akses Prototype:

Aplikasi dapat diakses secara lokal setelah menjalankan command di atas atau kunjungi link berikut.

- [Aplikasi Prediksi Status Mahasiswa](https://student-status-predictions-jayajaya-institute.streamlit.app/)

### Fitur Aplikasi:

1. **Input Interface**: Sidebar dengan berbagai input fields:

   - Usia saat pendaftaran
   - Nilai pendaftaran dan kualifikasi sebelumnya
   - Data akademik semester 1 & 2 (SKS dan nilai)
   - Status finansial (pembayaran, beasiswa, hutang)
   - Data demografis (gender, status pindahan)

2. **Prediksi Real-time**:

   - Model akan memprediksi status mahasiswa (Graduate/Dropout/Enrolled)
   - Menampilkan probabilitas untuk setiap kelas
   - Visualisasi probabilitas dalam bentuk bar chart

3. **Interpretasi Hasil**:
   - Status prediksi dengan color coding (hijau untuk Graduate, merah untuk Dropout, biru untuk Enrolled)
   - Tingkat kepercayaan model untuk setiap prediksi
   - Tabel probabilitas yang mudah dipahami

## Conclusion

Proyek ini berhasil mengembangkan sistem prediksi status kelulusan mahasiswa yang dapat membantu Jaya Jaya Institute dalam:

1. **Identifikasi Dini Mahasiswa Berisiko**: Model machine learning dapat memprediksi mahasiswa yang berpotensi dropout dengan akurasi yang baik, memungkinkan intervensi dini.

2. **Pemahaman Faktor Risiko**: Analisis menunjukkan bahwa faktor-faktor seperti performa akademik semester awal, status finansial, dan karakteristik demografis memiliki pengaruh signifikan terhadap kelulusan.

3. **Dashboard Monitoring**: Business dashboard memberikan visibility real-time terhadap kondisi mahasiswa dan membantu dalam pengambilan keputusan strategis.

4. **Sistem Prediksi Terintegrasi**: Aplikasi web memungkinkan staff akademik untuk melakukan prediksi dengan mudah dan cepat.

### Rekomendasi Action Items

Berdasarkan hasil analisis dan model yang dikembangkan, berikut adalah rekomendasi action items untuk Jaya Jaya Institute:

- **Program Bimbingan Akademik Tertarget**: Fokuskan program bimbingan pada mahasiswa dengan performa semester 1-2 yang rendah, karena ini merupakan indikator kuat risiko dropout

- **Optimalisasi Program Bantuan Keuangan**: Prioritaskan bantuan keuangan untuk mahasiswa yang menunggak pembayaran, karena status finansial berkorelasi kuat dengan tingkat dropout

- **Intervensi Khusus Mahasiswa Pindahan**: Berikan program orientasi dan support khusus untuk mahasiswa pindahan yang menunjukkan risiko dropout lebih tinggi

- **Monitoring Berkala**: Lakukan evaluasi bulanan menggunakan dashboard untuk mengidentifikasi tren dan pola baru yang muncul

- **Program Remedial Akademik**: Buat program remedial khusus untuk mahasiswa dengan SKS lulus rendah pada semester awal

- **Analisis Mode Pendaftaran**: Evaluasi dan optimalkan proses rekrutment berdasarkan application mode yang menunjukkan tingkat keberhasilan lebih tinggi

- **Program Mentoring Peer**: Kembangkan program mentoring di mana mahasiswa senior membimbing mahasiswa junior yang berisiko

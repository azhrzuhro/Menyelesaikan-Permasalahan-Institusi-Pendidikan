# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut, sebuah institusi pendidikan tinggi yang telah berdiri kokoh sejak tahun 2000, telah menorehkan prestasi dengan mencetak lulusan-lulusan unggulan di berbagai bidang. Reputasinya yang kuat menjadikannya pilihan utama bagi banyak calon mahasiswa yang ingin meraih masa depan gemilang.

Namun di balik pencapaian tersebut, terdapat tantangan besar yang tak bisa diabaikan fenomena tingginya angka dropout mahasiswa. Masalah ini bukan sekadar angka statistik; ia mencerminkan hambatan yang lebih dalam dalam sistem pendidikan, mulai dari proses seleksi, metode pembelajaran, hingga dukungan akademik yang mungkin belum optimal.

Tingginya tingkat dropout menjadi alarm serius bagi institusi, karena tidak hanya berdampak pada angka kelulusan, tetapi juga berpengaruh langsung terhadap citra dan daya tarik Jaya Jaya Institut di mata calon mahasiswa baru. Tantangan ini menuntut perhatian strategis dan solusi yang berbasis data agar setiap mahasiswa memiliki peluang yang lebih besar untuk menyelesaikan pendidikannya dengan sukses.


### Permasalahan Bisnis
1. Bagaimana memprediksi apakah seorang mahasiswa akan mengalami dropout atau tidak?

2. Faktor-faktor apa yang paling signifikan dalam mempengaruhi keputusan mahasiswa untuk dropout?

3. Apakah karakteristik sosial-ekonomi dan latar belakang pendidikan memiliki hubungan dengan performa akademik mahasiswa?

4. Apakah performa akademik semester awal dapat digunakan sebagai indikator kuat untuk memprediksi keberhasilan studi mahasiswa?

### Cakupan Proyek
Proyek ini akan mencakup hal-hal berikut:

- Eksplorasi data dan pemahaman karakteristik mahasiswa.

- Pra-pemrosesan dan transformasi data untuk keperluan machine learning.

- Membangun model klasifikasi untuk memprediksi dropout dan keberhasilan akademik.

- Visualisasi data dalam bentuk dashboard interaktif untuk mendukung keputusan manajemen.

- Pengujian dan validasi sistem machine learning sebagai prototype

### Persiapan
Sumber data: dataset yang digunakan merupakan dataset [Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

* Setup environment:
  ```
    conda activate proyek-akhir-penerapan-ds
  ```
* Install requirements: 
  ```
    pip install -r requirements.txt
  ```
* Setup metabase:
  ```
    docker pull metabase/metabase:v0.46.4
    docker run -p 3000:3000 --name metabase metabase/metabase
  ```
    Akses metabase pada http://localhost:3000/setup dan lakukan setup.

* Setup database (supabase):

  - Buat akun dan login https://supabase.com/dashboard/sign-in.
  - Buat new project
  - Copy URI pada database setting
  - Kirim dataset menggunakan sqlalchemy 
  ```python
  from sqlalchemy import create_engine

  URL = "DATABASE_URL"

  engine = create_engine(URL)
  df.to_sql('dataset', engine)
  ```
## Business Dashboard
1. Memantau Tingkat Dropout Secara Proaktif
Visualisasi berupa diagram donat menyajikan distribusi mahasiswa berdasarkan status: Graduated (49.9%), Dropout (32.1%), dan Enrolled (17.9%).

Tampilan ini memungkinkan institusi untuk secara cepat mendeteksi adanya kenaikan atau penurunan jumlah dropout, sehingga tindakan preventif dapat segera diambil.

2. Menganalisis Hubungan Faktor Akademik dan Ekonomi Terhadap Dropout
Nilai penerimaan (admission grade) menunjukkan bahwa mahasiswa dengan nilai masuk yang lebih rendah cenderung lebih berisiko mengalami dropout.

Rata-rata nilai semester 1 dan semester 2 mahasiswa yang dropout lebih rendah dibandingkan mahasiswa yang lulus, memperkuat pentingnya pemantauan performa akademik di awal masa studi.

3. Evaluasi Dampak Kondisi Keuangan dan Beasiswa
Visualisasi berdasarkan status pembayaran biaya kuliah menunjukkan bahwa keterlambatan atau ketidakmampuan membayar berkorelasi dengan status dropout.

Mahasiswa penerima beasiswa memiliki peluang kelulusan lebih tinggi dibandingkan yang tidak menerima, mengindikasikan bahwa bantuan finansial efektif dalam menekan angka dropout.

4. Dukungan Kebijakan yang Lebih Baik
Dengan melihat kombinasi faktor akademik dan non-akademik, dashboard ini menjadi alat bantu penting untuk mendesain program intervensi seperti mentoring, konseling, atau dukungan finansial yang lebih personal dan tepat sasaran.

## Menjalankan Sistem Machine Learning
Untuk menjalankan prototype machine learning yang telah dibuat, terdapat dua cara: menjalankannya secara lokal atau mengaksesnya melalui tautan Streamlit. Berikut adalah langkah-langkah yang perlu dilakukan jika ingin menjalankan prototype secara lokal:

1. Buka terminal pada virtual environment yang telah diaktifkan sebelumnya.

2. Pastikan direktori saat ini berada di folder yang berisi semua berkas yang dibutuhkan, terutama berkas app.py. Jika belum berada di direktori tersebut, gunakan perintah berikut:

  ```
    cd path/to/destination/directory
  ```
3. Setelah berada di direktori yang benar, jalankan perintah berikut:

  ```
    streamlit run app.py
  ```
4. Setelah aplikasi berhasil dijalankan, masukkan data yang sesuai kemudian klik tombol Predict untuk mengetahui status mahasiswa tersebut (apakah berisiko dropout atau tidak).

Jika ingin menjalankan aplikasi secara online, Anda dapat mengaksesnya melalui tautan berikut:
[Jaya Jaya Institut App](https://menyelesaikan-permasalahan-institusi-pendidikan-2nrbycsjcd3mla.streamlit.app/)

## Conclusion
Proyek ini dirancang untuk menjawab beberapa permasalahan utama yang dihadapi oleh Jaya Jaya Institut terkait tingginya tingkat dropout mahasiswa. Berdasarkan hasil eksplorasi data, pemodelan machine learning, dan pengujian sistem, berikut adalah kesimpulan dari proyek ini:

1. Bagaimana cara mengidentifikasi mahasiswa yang berpotensi mengalami dropout sejak dini?

Dengan membangun model prediktif berbasis algoritma Random Forest, Jaya Jaya Institut kini dapat mengidentifikasi mahasiswa yang memiliki risiko tinggi untuk mengalami dropout sejak semester awal. Model ini menggunakan berbagai fitur seperti nilai akademik, status sosial ekonomi, dan latar belakang pendidikan untuk memprediksi risiko dropout secara akurat.

2. Faktor-faktor apa saja yang paling berpengaruh terhadap keputusan mahasiswa untuk dropout?

Berdasarkan analisis eksploratif dan evaluasi feature importance, ditemukan bahwa beberapa faktor yang paling berpengaruh adalah:
- Nilai semester awal, yang mencerminkan kemampuan awal akademik mahasiswa.
- Status beasiswa dan status ekonomi, seperti apakah mahasiswa berasal dari keluarga berpenghasilan rendah atau merupakan penerima bantuan.
- Mahasiswa yang menunjukkan performa akademik rendah di semester awal atau berasal dari latar belakang ekonomi kurang mendukung memiliki   kecenderungan lebih tinggi untuk dropout.

3. Apakah performa akademik semester awal merupakan indikator kuat keberhasilan studi?

Hasil analisis menunjukkan bahwa performa akademik pada semester pertama, khususnya IPK, merupakan indikator yang sangat signifikan. Mahasiswa dengan nilai rendah cenderung lebih rentan terhadap tekanan akademik di semester berikutnya, dan memiliki kemungkinan dropout lebih tinggi.

4. Apakah latar belakang sosial-ekonomi dan pendidikan memengaruhi performa mahasiswa?

Ya, ditemukan bahwa faktor-faktor seperti jenis pekerjaan orang tua, status penerima beasiswa, dan asal sekolah turut memengaruhi performa akademik. Mahasiswa dari latar belakang kurang mampu atau yang tidak mendapatkan dukungan akademik dari sekolah sebelumnya cenderung menunjukkan performa lebih rendah di tahun-tahun awal perkuliahan.

### Rekomendasi Action Items
beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

1. Implementasi Sistem Prediksi Dropout Secara Berkala

Gunakan model machine learning untuk secara rutin mengidentifikasi mahasiswa yang berisiko tinggi dropout, sehingga institusi dapat melakukan intervensi dini yang lebih terarah dan efektif.

2. Penguatan Program Pendampingan Akademik (Academic Mentoring)

Buat program bimbingan belajar atau pendampingan dari dosen/pembimbing akademik bagi mahasiswa dengan risiko tinggi dropout 
berdasarkan hasil prediksi.

3. Berikan Intervensi Awal Berdasarkan Performa Akademik Semester Pertama 

Lakukan pemantauan ketat terhadap performa akademik di semester awal dan berikan bantuan khusus bagi mahasiswa yang menunjukkan penurunan prestasi, seperti program remedial atau konseling belajar


Username: root@mail.com
Password: root123

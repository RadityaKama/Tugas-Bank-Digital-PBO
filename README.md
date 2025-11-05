# Studi Kasus Bank Digital
Kode ini merupakan implementasi sederhana dari kelas Python yang merepresentasikan akun nasabah di sebuah bank fiktif bernama Bank Cerdas Nusantara (BCN). Sistem ini menangani fitur dasar seperti pencatatan saldo, transaksi menabung dan belanja, serta pengelolaan poin reward yang dapat ditukar dengan hadiah.

# Gambaran Umum
Kelas Nasabah menyimpan data penting terkait seorang nasabah, yaitu nama, nomor rekening, saldo, poin reward, dan riwayat transaksi secara lengkap. Dengan menggunakan prinsip enkapsulasi, saldo disimpan secara privat agar tidak mudah diakses dan dimodifikasi secara sembarangan, sedangkan poin reward dan riwayat transaksi diproteksi untuk manajemen internal kelas.

# Cara Kerja dan Fitur Utama
Ketika objek Nasabah dibuat, ia langsung menyapa nasabah dengan pesan selamat datang dan secara otomatis mencatat transaksi pembukaan akun dengan saldo awal yang diberikan.

### Pencatatan Waktu dan Transaksi
Fungsi internal waktu() mengembalikan timestamp saat ini dalam format YYYY-MM-DD HH:MM:SS, yang kemudian digunakan oleh fungsi catat_transaksi() untuk merekam setiap aktivitas ke dalam daftar riwayat transaksi. Transaksi dicatat lengkap dengan waktu, jenis aktivitas, nominal uang, keterangan, serta saldo dan poin setelah transaksi tersebut.

### Manajemen Saldo
Saldo nasabah dikelola dengan metode getter (get_saldo()) dan setter (set_saldo()) yang menjamin saldo tidak pernah menjadi negatif. Jika ada upaya mengubah saldo menjadi nilai negatif, sistem akan menolak dan menampilkan pesan error.

### Informasi Nasabah
Metode tampilkan_info() menyajikan ringkasan data nasabah yang terdiri dari nama, nomor rekening, saldo saat ini, dan poin reward terkumpul. Fungsi ini memanggil fungsi cek_saldo() dan cek_poin() untuk menampilkan data tersebut dengan format yang mudah dibaca.

### Transaksi Menabung
Metode menabung(jumlah) menerima input nominal setoran. Ia menambah saldo dengan nominal tersebut dan memberikan cashback 1% dari jumlah setoran secara otomatis sebagai bonus. Kedua aktivitas ini dicatat dalam riwayat transaksi dengan keterangan masing-masing.

### Transaksi Belanja
Metode belanja(jumlah, deskripsi) digunakan untuk pengeluaran atau pembelanjaan. Sebelum saldo dikurangi, sistem memastikan saldo cukup. Jika cukup, saldo dikurangi dan nasabah mendapatkan poin reward, dimana setiap Rp10.000 pengeluaran bernilai 1 poin. Transaksi ini juga dicatat secara detail.

### Penukaran Poin Reward
Nasabah dapat menukarkan poin reward dengan hadiah tertentu melalui metode redeem_poin(pilihan_hadiah). Ada beberapa pilihan hadiah dengan syarat poin berbeda, mulai dari voucher belanja hingga saldo bonus dan produk eksklusif. Sistem memvalidasi kecukupan poin dan memperbarui poin serta saldo (jika berlaku) saat penukaran berhasil.

### Riwayat Transaksi Lengkap
Metode generate_riwayat_transaksi() menampilkan seluruh catatan transaksi nasabah secara kronologis, mulai dari setoran awal, menabung, cashback, belanja, hingga redeem poin. Setiap transaksi ditampilkan dengan waktu, jenis, nominal perubahan saldo, serta saldo dan poin akhir setelah transaksi tersebut.

### Alur Program dan Contoh Penggunaan
Pada bagian bawah kode, dibuat objek nasabah bernama "Raditya Kama Cahaydewa" dengan nomor rekening dan saldo awal besar sebagai simulasi akun elit. Setelah itu, berbagai aktivitas dijalankan, seperti menabung, beberapa kali belanja dengan deskripsi berbeda, menabung ulang, menukarkan poin untuk hadiah, dan akhirnya mencetak riwayat transaksi lengkap.

Kunci Implementasi
  1. Enkapsulasi Saldo: saldo disimpan sebagai atribut privat (__saldo) untuk melindungi integritas data.
  2. Catatan Riwayat: semua transaksi dicatat secara rinci, membuat sistem ini layak dikembangkan untuk fitur laporan dan audit.
  3. Poin Reward: integrasi poin sebagai insentif menambah nilai pada sistem tabungan konvensional.
  4. Validasi Input: jumlah yang dimasukkan untuk menabung atau belanja harus positif, dan saldo harus cukup untuk pengeluaran.
  5. Timestamp Otomatis: pencatatan waktu menggunakan waktu komputer saat transaksi terjadi, meningkatkan akurasi data.

### Teknologi dan Struktur Data
Kode menggunakan modul standar datetime untuk waktu transaksi dan fitur dasar kelas di Python tanpa ketergantungan eksternal. Semua data disimpan dalam memori objek dan dicatat dalam list transaksi yang bisa dikembangkan lebih lanjut untuk penyimpanan permanen (misalnya ke file atau database).

### Kesimpulan
Kelas Nasabah ini merupakan contoh implementasi model data nasabah bank yang komprehensif dengan fitur tabungan, pembelanjaan, reward, dan pelacakan transaksi secara real-time. Dengan desain modular dan penggunaan prinsip OOP seperti enkapsulasi dan metode, kode ini siap menjadi dasar untuk aplikasi perbankan digital yang lebih lengkap di masa depan.

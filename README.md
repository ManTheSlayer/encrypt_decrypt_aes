# Aplikasi Enkripsi dan Dekripsi AES

Aplikasi ini adalah contoh implementasi enkripsi dan dekripsi menggunakan algoritma AES (Advanced Encryption Standard) dengan bahasa pemrograman Python. Aplikasi ini memiliki antarmuka grafis (GUI) yang dibuat menggunakan library Tkinter.

## Fitur

- Enkripsi pesan menggunakan algoritma AES
- Dekripsi pesan yang telah dienkripsi
- Antarmuka grafis (GUI) yang mudah digunakan
- Dapat dijalankan di sistem operasi Windows, macOS, dan Linux

## Cara Menggunakan

1. Install library yang diperlukan dengan menjalankan perintah:
   ```bash
   pip install cryptography
   pip install tkinter
   ```
2. Buat file baru dengan nama `aplikasi.py` dan salin kode aplikasi ke dalam file tersebut.
3. Jalankan aplikasi dengan perintah:
   ```bash
   python aplikasi.py
   ```
4. Gunakan aplikasi:
   - Pilih tombol **"Enkripsi Pesan"** untuk mengenkripsi pesan.
     - Masukkan kunci dan pesan yang ingin dienkripsi.
     - Klik tombol **"Enkripsi"** untuk mendapatkan hasil enkripsi.
   - Pilih tombol **"Dekripsi Pesan"** untuk mendekripsi pesan.
     - Masukkan kunci dan pesan terenkripsi yang ingin didekripsi.
     - Klik tombol **"Dekripsi"** untuk mendapatkan hasil dekripsi.

## Kode Aplikasi

Kode aplikasi dapat ditemukan di file `aplikasi.py`. Kode ini menggunakan:
- Library `cryptography` untuk melakukan enkripsi dan dekripsi.
- Library `tkinter` untuk membuat antarmuka grafis.

## Lisensi

Aplikasi ini dilisensikan di bawah lisensi MIT. Anda dapat menggunakan, memodifikasi, dan mendistribusikan aplikasi ini secara bebas.

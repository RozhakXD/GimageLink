# GimageLink
![GimageLink](https://github.com/user-attachments/assets/aa1b0215-5416-4646-88c6-5579d3279c39)

**GimageLink** adalah alat yang memungkinkan Anda untuk mencari link yang terkait dengan gambar melalui pencarian Google Lens dan pencarian gambar terbalik Google. Alat ini memudahkan Anda menemukan kecocokan gambar secara langsung hanya dengan satu gambar!

## Fitur
- **Konversi Gambar ke Link**: Mengubah gambar menjadi link pencarian yang cocok.
- **Pencarian Tepat Sasaran**: Mencari gambar dengan tingkat kecocokan tinggi melalui Google Lens dan reverse image search.
- **Tampilan Dinamis**: Pilih tampilan rapi dengan modul Rich atau output standar untuk memudahkan salin tautan.
- **Dukungan Format Gambar**: Mendukung berbagai format gambar seperti JPG, PNG, dan lainnya.

## Persyaratan
- Paket Python:
    - `requests_toolbelt`
    - `requests`
    - `rich`
- Python 3.x

## Instalasi
1. Clone Repository
    ```bash
    git clone https://github.com/RozhakXD/GimageLink.git
    cd GimageLink
    ```
3. Install Dependencies
    ```bash
    pip install requests rich requests_toolbelt
    ```
4. Jalankan Program
   ```bash
   python Run.py
   ```

## Cara Menggunakan
1. Pastikan Anda memiliki gambar yang ingin dicari dalam direktori yang benar.
2. Masukkan path gambar sesuai dengan petunjuk, contoh: `Temp/Image.jpg`.
3. Pilih apakah Anda ingin menggunakan tampilan dengan modul Rich atau tampilan standar.
4. Hasil akan ditampilkan sebagai daftar link yang cocok berdasarkan pencarian gambar di Google.

## Contoh Penggunaan
Setelah menjalankan program, Anda akan diminta untuk memasukkan path gambar, misalnya:

```markdown
> Temp/Image.jpg
```

Kemudian program akan mencari kecocokan gambar di Google, dan menampilkan hasilnya dalam format yang dipilih.

## Masalah yang Diketahui
- **Gambar Tidak Ditemukan**: Jika gambar tidak memberikan hasil pencarian yang cocok, pastikan file gambar ada di direktori yang benar.
- **Kecocokan Tidak Akurat**: Kadang, hasil pencarian mungkin tidak akurat jika gambar memiliki kualitas rendah atau elemen yang tidak mudah dikenali oleh algoritma Google.
- **Tautan Tidak Bisa Disalin**: Jika menggunakan tampilan Rich, pastikan Anda menggunakan output standar jika ingin mudah menyalin tautan.

Jika Anda menemukan bug lainnya, harap laporkan melalui Issues.

## Tangkapan Layar
![FunPic_20240922](https://github.com/user-attachments/assets/073b152d-f17f-4ae3-b4c4-45b42d5200ab)

## Dukungan
Jika Anda merasa program ini bermanfaat, Anda dapat mendukung pengembangan lebih lanjut melalui donasi. Terima kasih atas dukungannya!

- [Trakteer](https://trakteer.id/rozhak_official/tip)
- [PayPal](https://paypal.me/rozhak9)

## Kontribusi
Kontribusi sangat diterima! Silakan fork repository ini dan ajukan pull request jika Anda memiliki perbaikan atau fitur baru.

## Lisensi
Proyek ini dilisensikan di bawah [MIT License](https://github.com/RozhakXD/GimageLink?tab=MIT-1-ov-file).

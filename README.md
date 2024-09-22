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
Setelah menjalankan program, masukkan path gambar yang ingin dicari, misalnya:

```markdown
> Temp/Image.jpg
```

Kemudian program akan segera mencari kecocokan gambar di Google dan menampilkan hasilnya sesuai format yang Anda pilih.

## Masalah yang Diketahui
- **Gambar Tidak Ditemukan**: Pastikan file gambar ada di direktori yang benar jika tidak ada hasil pencarian.
- **Tautan Sulit Disalin**: Jika Anda menggunakan tampilan Rich, pertimbangkan untuk beralih ke output standar agar lebih mudah menyalin tautan yang dihasilkan.
- **Kecocokan Tidak Akurat**: Hasil pencarian mungkin kurang tepat jika gambar memiliki kualitas rendah atau mengandung elemen yang sulit dikenali oleh algoritma Google.

Jika Anda menemukan bug lainnya, harap laporkan melalui Issues.

## Tangkapan Layar
![FunPic_20240922](https://github.com/user-attachments/assets/073b152d-f17f-4ae3-b4c4-45b42d5200ab)

## Dukungan
Jika merasa program ini bermanfaat, Anda bisa membantu pengembangannya melalui donasi. Setiap dukungan sangat berarti! Terima kasih!

- [Trakteer](https://trakteer.id/rozhak_official/tip)
- [PayPal](https://paypal.me/rozhak9)

## Kontribusi
Kontribusi sangat diterima! Silakan fork repository ini dan ajukan pull request jika Anda memiliki perbaikan atau fitur baru.

## Lisensi
Proyek ini dilisensikan di bawah [MIT License](https://github.com/RozhakXD/GimageLink?tab=MIT-1-ov-file).

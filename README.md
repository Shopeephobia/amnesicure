# Amnesicure - An Unorthodox Flashcard Web App

Super COOL Flashcard App will be coming soon!

[![codecov](https://codecov.io/gh/Shopeephobia/amnesicure/branch/main/graph/badge.svg?token=UCJZWUT2ZM)](https://codecov.io/gh/Shopeephobia/amnesicure)

---

> Proyek ini dibuat untuk memenuhi tugas kelompok pada mata kuliah Rekayasa Perangkat Lunak (CSCM603125)
> yang diselenggarakan oleh Fakultas Ilmu Komputer, Universitas Indonesia pada Semester Gasal, Tahun Ajaran 2022/2023.

## 👨‍💻 Pengembang Aplikasi 👩‍💻

Proyek ini dibuat oleh kelompok [Sophophobia]() yang beranggotakan sebagai berikut.

- 2006596232 - Akbar Maliki Haqoni Jati
- 2006527481 - Muhammad Athallah
- 2006473844 - Muhammad Kenshin Himura Mahmuddin
- 2006526812 - Stefanus Ndaru Wedhatama
- 2006535716 - Teuku Faiz Aryasena

Kelompok [Sophophobia]() dibimbing oleh Kak Azka Fitria selaku asisten dosen dan Bu Iis Solichah selaku dosen pengampu mata kuliah Rekayasa Perangkat Lunak.

## Instruksi Penggunaan

### Pengembangan Lokal (Docker)

1. Masuk ke dalam direktori yang sudah di-*clone* dan jalankan perintah berikut
   untuk menyalakan memulai aplikasinya.

   ```shell
   docker build --tag amnesicure .
   docker run --publish 8000:8000 amnesicure
   ```
2. Buka localhost:8000 untuk melihat aplikasinya

### Pengembangan Lokal

Apabila kamu ingin menggunakan repositori ini sebagai repositori awalan yang nantinya akan kamu modifikasi, ikuti langkah-langkah berikut.

1. Buka laman GitHub repositori templat kode, lalu klik tombol "**Use this template**"
   untuk membuat salinan repositori ke dalam akun GitHub milikmu.

2. Buka laman GitHub repositori yang dibuat dari templat, lalu gunakan perintah
   `git clone` untuk menyalin repositorinya ke suatu lokasi di dalam sistem
   berkas (*filesystem*) komputermu.

   ```shell
   git clone <URL ke repositori di GitHub> <path ke suatu lokasi di filesystem>
   ```

3. Masuk ke dalam repositori yang sudah di-*clone* dan jalankan perintah berikut
   untuk menyalakan *virtual environment*.

   ```shell
   python -m venv env
   ```

4. Nyalakan *virtual environment* dengan perintah berikut.

   ```shell
   # Windows
   .\env\Scripts\activate
   # Linux/Unix, e.g. Ubuntu, MacOS
   source env/bin/activate
   ```

5. Instal *dependencies* yang dibutuhkan untuk menjalankan aplikasi dengan perintah berikut.

   ```shell
   pip install -r requirements.txt
   ```

6. Jalankan aplikasi Django menggunakan server pengembangan yang berjalan secara lokal.

   ```shell
   python manage.py runserver
   ```

7. Bukalah `http://localhost:8000` pada browser favoritmu untuk melihat apakah aplikasi sudah berjalan dengan benar.

[Sophophobia]: https://github.com/Shopeephobia

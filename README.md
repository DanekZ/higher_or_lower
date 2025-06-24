# 🔼 Higher or Lower Game – Python CLI Project

Sebuah permainan terminal sederhana berbasis Python, di mana pemain diminta menebak siapa yang memiliki jumlah followers lebih banyak di Instagram!

---

## 🎮 Gameplay Singkat

- Dua akun selebriti atau brand ditampilkan secara acak.
- Pemain memilih mana yang memiliki lebih banyak followers (A atau B).
- Jika benar, permainan lanjut dan skor bertambah.
- Jika salah, game over.
- Pemain bisa memilih untuk bermain lagi atau keluar.

---

## 🧠 Fitur yang Diimplementasikan

✅ Modularisasi kode (`main.py`, `utilities.py`, `art.py`)  
✅ Validasi input dari user (`A/B`, `y/n`)  
✅ Penanganan perulangan permainan (replay)  
✅ Menampilkan skor saat ini dan akhir  
✅ Tampilan teks ASCII sederhana (`logo`, `vs`, `thanks`)  

---

## 🗂️ Struktur File

higher-or-lower/
│
├── main.py # Alur utama permainan
├── utilities.py # Kumpulan fungsi pendukung (logika, validasi, data)
├── art.py # Variabel string ASCII art seperti logo dan ucapan
└── data.py # (opsional) Data followers (jika kamu pisah dari util)


---

## 📦 Library yang Digunakan

Semua fungsi menggunakan Python built-in:
- `random` untuk pengambilan data acak
- `input()`, `print()`, `while`, `if` untuk kontrol alur dasar

---

## ▶️ Cara Menjalankan

Pastikan kamu sudah punya Python terinstal (Python 3.x).

```bash
python main.py

🙌 Kontribusi
Project ini dibuat sebagai latihan logika dan kontrol alur program.
Jika kamu punya ide pengembangan (misalnya leaderboard, GUI, atau Web version), feel free to fork or pull request!

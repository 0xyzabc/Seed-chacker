🔐 Seed Phrase Permutation Checker

Script ini digunakan untuk memeriksa semua kemungkinan kombinasi (permutasi) dari 12 kata seed phrase (BIP39) dan mengidentifikasi mana yang merupakan seed phrase yang valid.

Script ini sangat berguna jika Anda mengetahui semua kata dalam seed phrase tetapi tidak tahu urutan yang benar.
🚨 Peringatan

    Jangan pernah gunakan seed phrase asli Anda dengan script pihak ketiga jika tidak yakin dengan keamanannya. Pastikan script ini dijalankan secara lokal dan offline.

📁 Struktur File

    seed-words.txt
    Berisi 12 kata (satu per baris) yang merupakan kandidat seed phrase.

    check_seeds.py
    Script utama yang memeriksa setiap permutasi dan memverifikasi apakah itu seed phrase yang valid.

🧪 Cara Menggunakan

    Pasang dependensi

pip install mnemonic

Siapkan file seed-words.txt

Contoh isi:

mimic
ripple
gravity
legend
lunar
jungle
pudding
circle
lunch
snack
element
vendor

Jalankan script

    python check_seeds.py

    Script akan:

        Mengambil semua permutasi dari 12 kata tersebut (12! = 479.001.600 kemungkinan).

        Memeriksa validitas setiap permutasi menggunakan pustaka mnemonic.

        Menampilkan seed yang valid jika ditemukan.

🛠️ Fitur

    Validasi seed phrase berdasarkan standar BIP39 (menggunakan library mnemonic dari trezor).

    Menampilkan progress setiap 100.000 permutasi yang diperiksa.

    Mendukung pengecekan offline.

💡 Catatan

    Jumlah total permutasi dari 12 kata adalah 479 juta. Proses ini sangat berat dan memakan waktu, kecuali Anda mengurangi jumlah kata atau mempersempit ruang pencarian (misalnya dengan mengunci kata di posisi tertentu).

    Jika Anda mengetahui sebagian urutan seed phrase, Anda dapat mengunci kata tertentu seperti ini:

    for perm in permutations(known_words[1:]):  # Kunci kata pertama
        phrase = "ripple " + " ".join(perm)

⚖️ Lisensi

Script ini bersifat open-source dan diberikan apa adanya. Penggunaan sepenuhnya tanggung jawab pengguna.
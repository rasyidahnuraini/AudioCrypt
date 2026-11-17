
from crypto_engine import encrypt_audio, decrypt_audio

# Membuat file audio contoh untuk pengujian
with open("contoh.txt", "wb") as file:
    file.write(b"Ini adalah data audio untuk pengujian AudioCrypt.")

# Enkripsi
encrypt_audio("contoh.txt", "contoh.acrypt", "password123")
print("Enkripsi berhasil!")

# Dekripsi
decrypt_audio("contoh.acrypt", "hasil_dekripsi.txt", "password123")
print("Dekripsi berhasil!")

# Memeriksa hasil
with open("contoh.txt", "rb") as file:
    data_asli = file.read()

with open("hasil_dekripsi.txt", "rb") as file:
    data_dekripsi = file.read()

if data_asli == data_dekripsi:
    print("Pengujian berhasil! Data sama persis.")
else:
    print("Pengujian gagal! Data berbeda.")

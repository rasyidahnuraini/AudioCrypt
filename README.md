# 🔐 AudioCrypt
### Audio File Encryption and Decryption Application

## 🇮🇩 Bahasa Indonesia

### Tentang Proyek
AudioCrypt adalah aplikasi desktop berbasis Python yang digunakan untuk mengamankan file audio melalui proses enkripsi dan dekripsi menggunakan algoritma AES-256-GCM.

Pengguna dapat melindungi file audio menggunakan password. File yang telah dienkripsi tidak dapat diputar secara langsung dan hanya bisa dikembalikan ke bentuk aslinya melalui proses dekripsi dengan password yang sama.

### Fitur
- Enkripsi file audio menggunakan AES-256-GCM.
- Dekripsi file audio menggunakan password.
- Password-based key derivation menggunakan PBKDF2-HMAC-SHA256.
- Antarmuka grafis (GUI) menggunakan Tkinter.
- Mendukung file WAV dan MP3.
- Menyimpan file terenkripsi dengan ekstensi `.acrypt`.

### Teknologi
- Python 3
- Tkinter
- Cryptography Library
- AES-256-GCM
- PBKDF2-HMAC-SHA256

### Tujuan
Proyek ini dibuat sebagai implementasi pembelajaran kriptografi menggunakan Python untuk menjaga keamanan dan kerahasiaan file audio.

---

## 🇬🇧 English

### About the Project
AudioCrypt is a Python-based desktop application designed to secure audio files through encryption and decryption using the AES-256-GCM algorithm.

Users can protect their audio files with a password. Encrypted files cannot be played directly and must be decrypted using the same password to restore the original audio.

### Features
- Audio file encryption using AES-256-GCM.
- Audio file decryption using a password.
- Password-based key derivation using PBKDF2-HMAC-SHA256.
- Graphical User Interface (GUI) using Tkinter.
- Supports WAV and MP3 files.
- Saves encrypted files with the `.acrypt` extension.

### Technologies Used
- Python 3
- Tkinter
- Cryptography Library
- AES-256-GCM
- PBKDF2-HMAC-SHA256

### Project Purpose
This project was developed as a practical implementation of cryptography using Python to protect the security and confidentiality of audio files.

---

## Installation and Usage

Clone the repository:

```bash
git clone https://github.com/your-username/AudioCrypt.git
cd AudioCrypt
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

## Important Note
Always remember your password. Without the correct password, encrypted files cannot be decrypted.

---

**Developed as a Python Cryptography Project.**

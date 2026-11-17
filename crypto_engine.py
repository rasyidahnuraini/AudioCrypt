
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes


# Konfigurasi enkripsi
KEY_LENGTH = 32
SALT_LENGTH = 16
NONCE_LENGTH = 12
ITERATIONS = 600_000
MAGIC = b"ACRYPT01"


def derive_key(password, salt):
    """Mengubah password menjadi kunci enkripsi."""
    if not password:
        raise ValueError("Password tidak boleh kosong.")

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_LENGTH,
        salt=salt,
        iterations=ITERATIONS,
    )

    return kdf.derive(password.encode("utf-8"))


def encrypt_audio(input_path, output_path, password):
    """Mengenkripsi file audio menggunakan AES-256-GCM."""
    with open(input_path, "rb") as file:
        audio_data = file.read()

    salt = os.urandom(SALT_LENGTH)
    nonce = os.urandom(NONCE_LENGTH)

    key = derive_key(password, salt)
    aesgcm = AESGCM(key)

    header = MAGIC + salt + nonce
    encrypted_data = aesgcm.encrypt(nonce, audio_data, header)

    with open(output_path, "wb") as file:
        file.write(header + encrypted_data)


def decrypt_audio(input_path, output_path, password):
    """Mendekripsi file audio menggunakan AES-256-GCM."""
    with open(input_path, "rb") as file:
        encrypted_file = file.read()

    header_length = len(MAGIC) + SALT_LENGTH + NONCE_LENGTH

    if len(encrypted_file) < header_length + 16:
        raise ValueError("File terenkripsi tidak valid.")

    magic = encrypted_file[:len(MAGIC)]

    if magic != MAGIC:
        raise ValueError("Format file tidak dikenali.")

    salt_start = len(MAGIC)
    salt_end = salt_start + SALT_LENGTH

    salt = encrypted_file[salt_start:salt_end]
    nonce = encrypted_file[salt_end:header_length]
    header = encrypted_file[:header_length]
    encrypted_data = encrypted_file[header_length:]

    key = derive_key(password, salt)
    aesgcm = AESGCM(key)

    decrypted_data = aesgcm.decrypt(
        nonce,
        encrypted_data,
        header
    )

    with open(output_path, "wb") as file:
        file.write(decrypted_data)


import os
import tkinter as tk
from tkinter import filedialog, messagebox
from crypto_engine import encrypt_audio, decrypt_audio

# Membuat folder hasil secara otomatis
os.makedirs("encrypted", exist_ok=True)
os.makedirs("decrypted", exist_ok=True)

selected_file = None


def choose_file():
    global selected_file

    file_path = filedialog.askopenfilename(
        title="Pilih File Audio",
        filetypes=[
            ("File Audio dan Terenkripsi", "*.wav *.mp3 *.acrypt"),
            ("Semua File", "*.*")
        ]
    )

    if file_path:
        selected_file = file_path
        file_label.config(text=os.path.basename(file_path))


def encrypt_process():
    if not selected_file:
        messagebox.showwarning("Peringatan", "Pilih file audio terlebih dahulu.")
        return

    password = password_entry.get()

    if not password:
        messagebox.showwarning("Peringatan", "Masukkan password terlebih dahulu.")
        return

    filename = os.path.basename(selected_file)
    output_path = os.path.join("encrypted", filename + ".acrypt")

    try:
        encrypt_audio(selected_file, output_path, password)
        messagebox.showinfo(
            "Berhasil",
            f"File berhasil dienkripsi!\n\nLokasi: {output_path}"
        )
        status_label.config(text="Status: Enkripsi berhasil")

    except Exception as error:
        messagebox.showerror("Gagal", str(error))


def decrypt_process():
    if not selected_file:
        messagebox.showwarning("Peringatan", "Pilih file terenkripsi terlebih dahulu.")
        return

    password = password_entry.get()

    if not password:
        messagebox.showwarning("Peringatan", "Masukkan password terlebih dahulu.")
        return

    if not selected_file.lower().endswith(".acrypt"):
        messagebox.showwarning(
            "Format tidak sesuai",
            "Pilih file dengan ekstensi .acrypt untuk dekripsi."
        )
        return

    filename = os.path.basename(selected_file)[:-7]
    output_path = os.path.join("decrypted", filename)

    try:
        decrypt_audio(selected_file, output_path, password)
        messagebox.showinfo(
            "Berhasil",
            f"File berhasil didekripsi!\n\nLokasi: {output_path}"
        )
        status_label.config(text="Status: Dekripsi berhasil")

    except Exception:
        status_label.config(text="Status: Dekripsi gagal")
        messagebox.showerror(
            "Dekripsi Gagal",
            "Password salah atau file terenkripsi rusak."
        )


# Membuat jendela aplikasi
root = tk.Tk()
root.title("AudioCrypt - Audio Encryption")
root.geometry("500x430")
root.resizable(False, False)
root.configure(bg="#eaf3ff")

# Judul
title_label = tk.Label(
    root,
    text="AudioCrypt",
    font=("Arial", 25, "bold"),
    bg="#eaf3ff",
    fg="#24558a"
)
title_label.pack(pady=(25, 5))

subtitle_label = tk.Label(
    root,
    text="Secure Your Audio Files with AES-256",
    font=("Arial", 10),
    bg="#eaf3ff",
    fg="#52677e"
)
subtitle_label.pack(pady=(0, 20))

# Tombol pilih file
choose_button = tk.Button(
    root,
    text="Pilih File Audio",
    command=choose_file,
    font=("Arial", 11),
    bg="#3978b9",
    fg="white",
    width=20,
    relief="flat"
)
choose_button.pack(pady=5)

file_label = tk.Label(
    root,
    text="Belum ada file dipilih",
    font=("Arial", 9),
    bg="#eaf3ff",
    fg="#52677e"
)
file_label.pack(pady=8)

# Password
password_label = tk.Label(
    root,
    text="Password",
    font=("Arial", 10, "bold"),
    bg="#eaf3ff",
    fg="#24558a"
)
password_label.pack(pady=(15, 5))

password_entry = tk.Entry(
    root,
    show="*",
    font=("Arial", 12),
    width=30
)
password_entry.pack(pady=5)

# Tombol enkripsi
encrypt_button = tk.Button(
    root,
    text="ENKRIPSI AUDIO",
    command=encrypt_process,
    font=("Arial", 11, "bold"),
    bg="#3978b9",
    fg="white",
    width=25,
    relief="flat"
)
encrypt_button.pack(pady=(20, 8))

# Tombol dekripsi
decrypt_button = tk.Button(
    root,
    text="DEKRIPSI AUDIO",
    command=decrypt_process,
    font=("Arial", 11, "bold"),
    bg="#527c9f",
    fg="white",
    width=25,
    relief="flat"
)
decrypt_button.pack(pady=5)

# Status
status_label = tk.Label(
    root,
    text="Status: Menunggu proses",
    font=("Arial", 9),
    bg="#eaf3ff",
    fg="#52677e"
)
status_label.pack(pady=20)

root.mainloop()

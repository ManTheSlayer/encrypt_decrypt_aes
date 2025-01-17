from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode, urlsafe_b64decode
import os
import tkinter as tk
from tkinter import messagebox, scrolledtext

# Fungsi untuk menghasilkan kunci dari key

def generate_key(key, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(key.encode())

# Fungsi untuk mengenkripsi pesan
def encrypt_message(key, plaintext):
    salt = os.urandom(16)  # Salt acak
    derived_key = generate_key(key, salt)
    iv = os.urandom(16)  # Vector inisialisasi acak
    cipher = Cipher(algorithms.AES(derived_key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
    # Gabungkan salt, iv, dan ciphertext untuk penyimpanan
    return urlsafe_b64encode(salt + iv + ciphertext).decode()

# Fungsi untuk mendekripsi pesan
def decrypt_message(key, encrypted_data):
    data = urlsafe_b64decode(encrypted_data.encode())
    salt, iv, ciphertext = data[:16], data[16:32], data[32:]
    derived_key = generate_key(key, salt)
    cipher = Cipher(algorithms.AES(derived_key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext.decode()

# Fungsi untuk menampilkan menu Enkripsi
def show_encrypt_menu():
    clear_frame()
    tk.Label(frame, text="Enkripsi Pesan", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

    tk.Label(frame, text="Key:", font=("Arial", 12), bg="#f0f0f0").pack(anchor="w")
    key_entry = tk.Entry(frame, width=30, font=("Arial", 12))
    key_entry.pack(pady=5)

    tk.Label(frame, text="Pesan:", font=("Arial", 12), bg="#f0f0f0").pack(anchor="w")
    plaintext_entry = tk.Text(frame, height=5, width=50, font=("Arial", 12))
    plaintext_entry.pack(pady=5)

    def encrypt_action():
        key = key_entry.get()
        plaintext = plaintext_entry.get("1.0", tk.END).strip()
        if not key or not plaintext:
            messagebox.showwarning("Peringatan", "Key dan pesan tidak boleh kosong.")
            return
        try:
            encrypted = encrypt_message(key, plaintext)
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, encrypted)
            messagebox.showinfo("Sukses", "Pesan berhasil dienkripsi!")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal mengenkripsi: {e}")

    tk.Button(frame, text="Enkripsi", command=encrypt_action, width=20, bg="#4CAF50", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
    tk.Button(frame, text="Kembali ke Menu Utama", command=show_main_menu, width=20, bg="#2196F3", fg="white", font=("Arial", 12, "bold")).pack(pady=5)

# Fungsi untuk menampilkan menu Dekripsi
def show_decrypt_menu():
    clear_frame()
    tk.Label(frame, text="Dekripsi Pesan", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

    tk.Label(frame, text="Key:", font=("Arial", 12), bg="#f0f0f0").pack(anchor="w")
    key_entry = tk.Entry(frame, width=30, font=("Arial", 12))
    key_entry.pack(pady=5)

    tk.Label(frame, text="Pesan Terenkripsi:", font=("Arial", 12), bg="#f0f0f0").pack(anchor="w")
    encrypted_entry = tk.Text(frame, height=5, width=50, font=("Arial", 12))
    encrypted_entry.pack(pady=5)

    def decrypt_action():
        key = key_entry.get()
        encrypted_data = encrypted_entry.get("1.0", tk.END).strip()
        if not key or not encrypted_data:
            messagebox.showwarning("Peringatan", "Key dan pesan tidak boleh kosong.")
            return
        try:
            decrypted = decrypt_message(key, encrypted_data)
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, decrypted)
            messagebox.showinfo("Sukses", "Pesan berhasil didekripsi!")
        except Exception as e:
            messagebox.showerror("Error", "Key atau data salah. Gagal mendekripsi.")

    tk.Button(frame, text="Dekripsi", command=decrypt_action, width=20, bg="#4CAF50", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
    tk.Button(frame, text="Kembali ke Menu Utama", command=show_main_menu, width=20, bg="#2196F3", fg="white", font=("Arial", 12, "bold")).pack(pady=5)

# Fungsi untuk membersihkan frame
def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()

# Fungsi untuk menampilkan menu utama
def show_main_menu():
    clear_frame()
    tk.Label(frame, text="AES Encryption/Decryption", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=20)
    tk.Button(frame, text="Enkripsi Pesan", command=show_encrypt_menu, width=20, bg="#4CAF50", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
    tk.Button(frame, text="Dekripsi Pesan", command=show_decrypt_menu, width=20, bg="#4CAF50", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

# GUI Utama
root = tk.Tk()
root.title("Aplikasi Enkripsi dan Dekripsi AES")
root.geometry("600x500")  # Ukuran jendela lebih besar

# Warna latar belakang aplikasi
root.config(bg="#f0f0f0")

frame = tk.Frame(root, padx=10, pady=10, bg="#f0f0f0")
frame.pack(fill="both", expand=True)

# Area hasil
result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10, font=("Arial", 12))
result_text.pack(pady=10)

# Tampilkan menu utama
show_main_menu()

# Jalankan aplikasi
root.mainloop()

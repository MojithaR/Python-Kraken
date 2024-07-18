# otp_gui_enhanced_fixed.py

import tkinter as tk
from tkinter import messagebox, ttk
import random

def generate_random_key(length):
    """Generate a random key of specified length."""
    key = []
    for _ in range(length):
        key.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    return ''.join(key)

def encrypt(plaintext, key):
    """Encrypt the plaintext using the key."""
    ciphertext = []
    for i in range(len(plaintext)):
        p_char = plaintext[i]
        k_char = key[i]
        if p_char.isalpha():
            # XOR operation
            c_char = chr(((ord(p_char) - 65) ^ (ord(k_char) - 65)) % 26 + 65)
        else:
            # Non-alphabetic characters remain unchanged
            c_char = p_char
        ciphertext.append(c_char)
    return ''.join(ciphertext)

def decrypt(ciphertext, key):
    """Decrypt the ciphertext using the key."""
    plaintext = []
    for i in range(len(ciphertext)):
        c_char = ciphertext[i]
        k_char = key[i]
        if c_char.isalpha():
            # XOR operation
            p_char = chr(((ord(c_char) - 65) ^ (ord(k_char) - 65)) % 26 + 65)
        else:
            # Non-alphabetic characters remain unchanged
            p_char = c_char
        plaintext.append(p_char)
    return ''.join(plaintext)

def encrypt_message():
    plaintext = plaintext_entry.get().upper()
    key_length = len(plaintext)
    key = generate_random_key(key_length)
    key_label.config(text=f"Random Key: {key}")
    
    encrypted_message = encrypt(plaintext, key)
    encrypted_text.delete(1.0, tk.END)
    encrypted_text.insert(tk.END, encrypted_message)

def decrypt_message():
    ciphertext = encrypted_text.get(1.0, tk.END).strip()
    key = key_label.cget("text").split(": ")[1]
    
    if not ciphertext:
        messagebox.showerror("Error", "No ciphertext to decrypt.")
        return
    
    try:
        decrypted_message = decrypt(ciphertext, key)
        decrypted_text.delete(1.0, tk.END)
        decrypted_text.insert(tk.END, decrypted_message)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear_entries():
    plaintext_entry.delete(0, tk.END)
    key_label.config(text="Random Key: ")
    encrypted_text.delete(1.0, tk.END)
    decrypted_text.delete(1.0, tk.END)

# Create the main window
root = tk.Tk()
root.title("One-Time Pad Encryption")
root.geometry("500x300")
root.configure(bg="#f0f0f0")

# Create and place the plaintext entry field
tk.Label(root, text="Enter plaintext:", bg="#f0f0f0", fg="#333333").place(x=20, y=20)
plaintext_entry = tk.Entry(root, width=50)
plaintext_entry.place(x=140, y=20)

# Create the Encrypt button
encrypt_button = ttk.Button(root, text="Encrypt", command=encrypt_message)
encrypt_button.place(x=400, y=20)

# Create the key label
key_label = tk.Label(root, text="Random Key: ", bg="#f0f0f0", fg="#333333")
key_label.place(x=20, y=50)

# Create and place the encrypted text display area
tk.Label(root, text="Encrypted Message:", bg="#f0f0f0", fg="#333333").place(x=20, y=90)
encrypted_text = tk.Text(root, height=5, width=50)
encrypted_text.place(x=20, y=120)

# Create the Decrypt button
decrypt_button = ttk.Button(root, text="Decrypt", command=decrypt_message)
decrypt_button.place(x=400, y=220)

# Create and place the decrypted text display area
tk.Label(root, text="Decrypted Message:", bg="#f0f0f0", fg="#333333").place(x=20, y=220)
decrypted_text = tk.Text(root, height=5, width=50)
decrypted_text.place(x=20, y=250)

# Create the Clear button
clear_button = ttk.Button(root, text="Clear Entries", command=clear_entries)
clear_button.place(x=220, y=200)

# Start the main event loop
root.mainloop()

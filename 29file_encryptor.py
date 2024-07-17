# file_encryptor.py
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import os
import base64

def generate_key(password, salt):
    """
    Generates a key from the given password and salt using PBKDF2HMAC.

    Parameters:
    password (str): The password.
    salt (bytes): The salt.

    Returns:
    bytes: The generated key.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return key

def encrypt_file(file_path, password):
    """
    Encrypts a file using AES encryption.

    Parameters:
    file_path (str): The path of the file to encrypt.
    password (str): The password for encryption.

    Returns:
    None
    """
    salt = os.urandom(16)
    key = generate_key(password, salt)
    iv = os.urandom(16)

    with open(file_path, 'rb') as f:
        data = f.read()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    with open(file_path + '.enc', 'wb') as f:
        f.write(salt + iv + encrypted_data)

    print(f"File '{file_path}' encrypted successfully.")

def decrypt_file(file_path, password):
    """
    Decrypts a file using AES encryption.

    Parameters:
    file_path (str): The path of the file to decrypt.
    password (str): The password for decryption.

    Returns:
    None
    """
    with open(file_path, 'rb') as f:
        salt = f.read(16)
        iv = f.read(16)
        encrypted_data = f.read()

    key = generate_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()

    original_file_path = file_path.replace('.enc', '.dec')
    with open(original_file_path, 'wb') as f:
        f.write(data)

    print(f"File '{file_path}' decrypted successfully.")

def main():
    """
    Main function to execute the file encryption/decryption script.
    """
    choice = input("Do you want to (e)ncrypt or (d)ecrypt a file? ")
    if choice.lower() == 'e':
        file_path = input("Enter the path of the file to encrypt: ")
        password = input("Enter the password: ")
        encrypt_file(file_path, password)
    elif choice.lower() == 'd':
        file_path = input("Enter the path of the file to decrypt: ")
        password = input("Enter the password: ")
        decrypt_file(file_path, password)
    else:
        print("Invalid choice. Please select 'e' for encrypt or 'd' for decrypt.")

if __name__ == "__main__":
    main()

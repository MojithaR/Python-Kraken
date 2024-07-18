from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

def encrypt_message(message, key):
    """
    Encrypts a message using AES encryption in CBC mode.

    Args:
    - message (str): The message to encrypt.
    - key (bytes): The AES encryption key (must be 16, 24, or 32 bytes long).

    Returns:
    - bytes: The encrypted message data.
    - bytes: The initialization vector (IV) used for encryption.
    """
    # Convert message to bytes
    message_bytes = message.encode('utf-8')

    # Generate an initialization vector (IV)
    iv = os.urandom(16)

    # Pad the message to be a multiple of 16 bytes (AES block size)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(message_bytes) + padder.finalize()

    # Create an AES cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    
    # Encrypt the data
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    return encrypted_data, iv

def decrypt_message(encrypted_data, iv, key):
    """
    Decrypts an AES encrypted message.

    Args:
    - encrypted_data (bytes): The encrypted message data.
    - iv (bytes): The initialization vector (IV) used for encryption.
    - key (bytes): The AES encryption key (must be 16, 24, or 32 bytes long).

    Returns:
    - str: The decrypted message.
    """
    # Create an AES cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    
    # Decrypt the data
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Unpad the decrypted data
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    # Convert bytes back to string
    decrypted_message = unpadded_data.decode('utf-8')

    return decrypted_message

if __name__ == "__main__":
    # Get user input for message and key
    message = input("Enter the message to encrypt: ")
    key = input("Enter the encryption key (must be 16, 24, or 32 bytes long): ").encode('utf-8')

    # Encrypt the message
    encrypted_data, iv = encrypt_message(message, key)
    print("Encrypted Data:", encrypted_data.hex())

    # Decrypt the encrypted message
    decrypted_message = decrypt_message(encrypted_data, iv, key)
    print("Decrypted Message:", decrypted_message)

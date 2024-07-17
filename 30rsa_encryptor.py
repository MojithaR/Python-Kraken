# rsa_encryptor.py
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
import os

def generate_keys():
    """
    Generates a pair of RSA keys (public and private) and saves them to files.

    Returns:
    None
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Save the private key
    with open("private_key.pem", "wb") as f:
        f.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )
        )

    # Save the public key
    with open("public_key.pem", "wb") as f:
        f.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )

    print("RSA key pair generated and saved to 'private_key.pem' and 'public_key.pem'.")

def encrypt_file(file_path, public_key_path):
    """
    Encrypts a file using the RSA public key.

    Parameters:
    file_path (str): The path of the file to encrypt.
    public_key_path (str): The path of the public key file.

    Returns:
    None
    """
    # Load the public key
    with open(public_key_path, "rb") as f:
        public_key = serialization.load_pem_public_key(
            f.read(),
            backend=default_backend()
        )

    # Read the file data
    with open(file_path, "rb") as f:
        data = f.read()

    # Encrypt the data
    encrypted_data = public_key.encrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Save the encrypted data
    with open(file_path + '.enc', 'wb') as f:
        f.write(encrypted_data)

    print(f"File '{file_path}' encrypted successfully.")

def decrypt_file(file_path, private_key_path):
    """
    Decrypts a file using the RSA private key.

    Parameters:
    file_path (str): The path of the file to decrypt.
    private_key_path (str): The path of the private key file.

    Returns:
    None
    """
    # Load the private key
    with open(private_key_path, "rb") as f:
        private_key = serialization.load_pem_private_key(
            f.read(),
            password=None,
            backend=default_backend()
        )

    # Read the encrypted data
    with open(file_path, "rb") as f:
        encrypted_data = f.read()

    # Decrypt the data
    decrypted_data = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Save the decrypted data
    original_file_path = file_path.replace('.enc', '.dec')
    with open(original_file_path, 'wb') as f:
        f.write(decrypted_data)

    print(f"File '{file_path}' decrypted successfully.")

def main():
    """
    Main function to execute the file encryption/decryption script.
    """
    choice = input("Do you want to (g)enerate keys, (e)ncrypt a file, or (d)ecrypt a file? ")
    if choice.lower() == 'g':
        generate_keys()
    elif choice.lower() == 'e':
        file_path = input("Enter the path of the file to encrypt: ")
        public_key_path = input("Enter the path of the public key file: ")
        encrypt_file(file_path, public_key_path)
    elif choice.lower() == 'd':
        file_path = input("Enter the path of the file to decrypt: ")
        private_key_path = input("Enter the path of the private key file: ")
        decrypt_file(file_path, private_key_path)
    else:
        print("Invalid choice. Please select 'g' to generate keys, 'e' to encrypt a file, or 'd' to decrypt a file.")

if __name__ == "__main__":
    main()

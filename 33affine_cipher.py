# affine_cipher.py

import string

def gcd(a, b):
    """
    Computes the greatest common divisor (GCD) of two numbers.

    Parameters:
    a (int): First number.
    b (int): Second number.

    Returns:
    int: GCD of a and b.
    """
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    """
    Computes the modular multiplicative inverse of a number under modulo m.

    Parameters:
    a (int): The number for which inverse is to be found.
    m (int): The modulo value.

    Returns:
    int: Modular inverse of a under modulo m.
    """
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def clean_text(text):
    """
    Cleans the text by removing non-alphabetic characters and converting to uppercase.

    Parameters:
    text (str): The text to clean.

    Returns:
    str: The cleaned text containing only uppercase alphabetic characters.
    """
    cleaned_text = []
    for char in text:
        if char.isalpha():
            cleaned_text.append(char.upper())
    return ''.join(cleaned_text)

def affine_encrypt(plaintext, a, b):
    """
    Encrypts the plaintext using the Affine Cipher.

    Parameters:
    plaintext (str): The plaintext message to encrypt.
    a (int): The first key for encryption. Should be coprime with the alphabet size (26).
    b (int): The second key for encryption.

    Returns:
    str: The encrypted ciphertext.
    """
    plaintext = clean_text(plaintext)
    ciphertext = []
    for char in plaintext:
        if char.isalpha():
            encrypted_char = chr(((ord(char) - 65) * a + b) % 26 + 65)
            ciphertext.append(encrypted_char)
    return ''.join(ciphertext)

def affine_decrypt(ciphertext, a, b):
    """
    Decrypts the ciphertext using the Affine Cipher.

    Parameters:
    ciphertext (str): The ciphertext message to decrypt.
    a (int): The first key for decryption. Should be coprime with the alphabet size (26).
    b (int): The second key for decryption.

    Returns:
    str: The decrypted plaintext.
    """
    m = 26  # Modulo size of the alphabet
    inv_a = mod_inverse(a, m)
    plaintext = []
    for char in ciphertext:
        if char.isalpha():
            decrypted_char = chr((inv_a * (ord(char) - 65 - b)) % 26 + 65)
            plaintext.append(decrypted_char)
    return ''.join(plaintext)

def main():
    """
    Main function to execute Affine Cipher encryption and decryption.
    """
    try:
        plaintext = input("Enter the plaintext message: ")
        key_a = int(input("Enter the first key (a): "))
        key_b = int(input("Enter the second key (b): "))

        # Check if key_a is coprime with 26
        if gcd(key_a, 26) != 1:
            raise ValueError("The first key (a) must be coprime with 26.")

        encrypted_message = affine_encrypt(plaintext, key_a, key_b)
        decrypted_message = affine_decrypt(encrypted_message, key_a, key_b)

        print(f"Plaintext: {plaintext}")
        print(f"Key (a): {key_a}")
        print(f"Key (b): {key_b}")
        print(f"Encrypted message: {encrypted_message}")
        print(f"Decrypted message: {decrypted_message}")

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()

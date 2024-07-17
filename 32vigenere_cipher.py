# vigenere_cipher.py

import string

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

def extend_keyword(keyword, length):
    """
    Extends the keyword to match the length of the text to encrypt/decrypt.

    Parameters:
    keyword (str): The keyword to extend.
    length (int): The desired length of the extended keyword.

    Returns:
    str: The extended keyword.
    """
    if not keyword:
        raise ValueError("Keyword must contain alphabetic characters.")
    
    repeated_keyword = (keyword * (length // len(keyword))) + keyword[:length % len(keyword)]
    return repeated_keyword.upper()

def vigenere_encrypt(plaintext, keyword):
    """
    Encrypts the plaintext using the Vigenère Cipher.

    Parameters:
    plaintext (str): The plaintext message to encrypt.
    keyword (str): The keyword used for encryption.

    Returns:
    str: The encrypted ciphertext.
    """
    plaintext = clean_text(plaintext)
    keyword = clean_text(keyword)
    extended_keyword = extend_keyword(keyword, len(plaintext))
    
    ciphertext = []
    for i in range(len(plaintext)):
        shift = ord(extended_keyword[i]) - 65  # A=0, B=1, ..., Z=25
        shifted_char = chr((ord(plaintext[i]) - 65 + shift) % 26 + 65)
        ciphertext.append(shifted_char)
    
    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext, keyword):
    """
    Decrypts the ciphertext using the Vigenère Cipher.

    Parameters:
    ciphertext (str): The ciphertext message to decrypt.
    keyword (str): The keyword used for decryption.

    Returns:
    str: The decrypted plaintext.
    """
    ciphertext = clean_text(ciphertext)
    keyword = clean_text(keyword)
    extended_keyword = extend_keyword(keyword, len(ciphertext))
    
    plaintext = []
    for i in range(len(ciphertext)):
        shift = ord(extended_keyword[i]) - 65  # A=0, B=1, ..., Z=25
        shifted_char = chr((ord(ciphertext[i]) - 65 - shift) % 26 + 65)
        plaintext.append(shifted_char)
    
    return ''.join(plaintext)

def main():
    """
    Main function to execute Vigenère Cipher encryption and decryption.
    """
    try:
        plaintext = input("Enter the plaintext message: ")
        keyword = input("Enter the keyword: ")

        encrypted_message = vigenere_encrypt(plaintext, keyword)
        decrypted_message = vigenere_decrypt(encrypted_message, keyword)

        print(f"Plaintext: {plaintext}")
        print(f"Keyword: {keyword}")
        print(f"Encrypted message: {encrypted_message}")
        print(f"Decrypted message: {decrypted_message}")

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()

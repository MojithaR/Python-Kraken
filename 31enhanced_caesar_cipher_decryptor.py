# enhanced_caesar_cipher_decryptor.py
import string
import collections

def load_dictionary():
    """
    Loads a dictionary of English words for reference.

    Returns:
    set: A set containing English words.
    """
    with open('english_words.txt', 'r') as file:
        english_words = set(word.strip().lower() for word in file)
    return english_words

def caesar_decrypt(ciphertext, shift):
    """
    Decrypts the given text using the Caesar Cipher.

    Parameters:
    ciphertext (str): The text to decrypt.
    shift (int): The number of positions the characters were shifted.

    Returns:
    str: The decrypted text.
    """
    decrypted_text = []
    for char in ciphertext:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            decrypted_text.append(chr((ord(char) - shift_amount - shift) % 26 + shift_amount))
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

def analyze_cipher_text(ciphertext):
    """
    Analyzes the cipher text to find the most common letters.

    Parameters:
    ciphertext (str): The cipher text to analyze.

    Returns:
    list: A list of tuples containing (character, count) sorted by count in descending order.
    """
    counter = collections.Counter(char.lower() for char in ciphertext if char.isalpha())
    sorted_chars = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    return sorted_chars

def decrypt_with_frequency_analysis(ciphertext, possible_shifts):
    """
    Decrypts the cipher text using frequency analysis and outputs all possible plaintexts.

    Parameters:
    ciphertext (str): The cipher text to decrypt.
    possible_shifts (int): The number of possible shifts to consider.

    Returns:
    list: A list of tuples containing (plaintext, original_mapping).
    """
    english_words = load_dictionary()
    decrypted_texts = []

    for shift in range(possible_shifts):
        plaintext = caesar_decrypt(ciphertext, shift)
        decrypted_texts.append((plaintext, create_mapping(ciphertext, plaintext)))

    return decrypted_texts

def create_mapping(ciphertext, plaintext):
    """
    Creates a mapping between the original characters and their decrypted counterparts.

    Parameters:
    ciphertext (str): The original cipher text.
    plaintext (str): The decrypted plaintext.

    Returns:
    dict: A dictionary mapping each original character to its decrypted counterpart.
    """
    mapping = {}
    for orig_char, decrypted_char in zip(ciphertext, plaintext):
        if orig_char.isalpha():
            mapping[orig_char] = decrypted_char
    return mapping

def main():
    """
    Main function to execute the Caesar Cipher decryption with frequency analysis.
    """
    ciphertext = input("Enter the cipher text to decrypt: ").strip()

    # Analyze the cipher text to find common letters
    sorted_chars = analyze_cipher_text(ciphertext)
    most_common_letters = ''.join(char for char, count in sorted_chars)[:5]

    print(f"Most common letters in cipher text: {most_common_letters}")

    # Decrypt using frequency analysis
    possible_shifts = 26
    decrypted_texts = decrypt_with_frequency_analysis(ciphertext, possible_shifts)

    # Save all possible decrypted outcomes to a text file
    with open('decrypted_results.txt', 'w') as file:
        for index, (plaintext, mapping) in enumerate(decrypted_texts):
            file.write(f"Attempt {index + 1} (Shift: {index}): {plaintext}\n")
            file.write("Mapping:\n")
            for orig_char, decrypted_char in mapping.items():
                file.write(f"{orig_char} ==> {decrypted_char}\n")
            file.write("\n")

    print(f"All possible decrypted outcomes saved to 'decrypted_results.txt'.")

if __name__ == "__main__":
    main()

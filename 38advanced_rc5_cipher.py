import struct

def left_rotate(value, shift, word_size):
    """Perform a left rotate operation on a value."""
    return ((value << shift) | (value >> (word_size - shift))) & ((1 << word_size) - 1)

def right_rotate(value, shift, word_size):
    """Perform a right rotate operation on a value."""
    return ((value >> shift) | (value << (word_size - shift))) & ((1 << word_size) - 1)

def pad_plaintext(plaintext, block_size):
    """Pad plaintext to make its length a multiple of block_size."""
    padding_length = block_size - (len(plaintext) % block_size)
    if padding_length == 0:
        padding_length = block_size  # Pad a full block if plaintext length is a multiple of block_size
    padded_text = plaintext + bytes([padding_length] * padding_length)
    return padded_text

def unpad_plaintext(padded_text):
    """Remove padding from padded plaintext."""
    padding_length = padded_text[-1]
    return padded_text[:-padding_length]

def rc5_key_schedule(key, word_size, rounds):
    """Generate RC5 key schedule."""
    # Constants for RC5
    P = 0xb7e15163
    Q = 0x9e3779b9

    # Key expansion
    key_words = (len(key) + (word_size - 1)) // word_size
    L = list(struct.unpack(f">{key_words}I", key.ljust(key_words * 4, b'\0')))
    T = (2 * (rounds + 1)) * [0]
    
    T[0] = P
    for i in range(1, 2 * (rounds + 1)):
        T[i] = (T[i - 1] + Q) & ((1 << word_size) - 1)
    
    A = B = 0
    j = 0
    for s in range(3 * max(key_words, 2 * (rounds + 1))):
        A = T[j] = left_rotate((T[j] + A + B), 3, word_size)
        B = L[i % key_words] = left_rotate((L[i % key_words] + A + B), (A + B) % word_size, word_size)
        i = (i + 1) % key_words
        j = (j + 1) % (2 * (rounds + 1))
    
    return T

def rc5_encrypt_block(plaintext, key, word_size=32, rounds=12):
    """Encrypt a block of plaintext using RC5 algorithm."""
    block_size = len(plaintext)
    assert block_size == 8, "Block size must be 8 bytes for RC5-32/12"

    # Generate subkeys
    subkeys = rc5_key_schedule(key, word_size, rounds)

    # Convert plaintext to integers
    A, B = struct.unpack(">II", plaintext)

    # Encryption rounds
    A = (A + subkeys[0]) & ((1 << word_size) - 1)
    B = (B + subkeys[1]) & ((1 << word_size) - 1)
    for i in range(1, rounds + 1):
        A = (left_rotate((A ^ B), B, word_size) + subkeys[2 * i]) & ((1 << word_size) - 1)
        B = (left_rotate((B ^ A), A, word_size) + subkeys[2 * i + 1]) & ((1 << word_size) - 1)
    
    # Pack encrypted integers back into bytes
    ciphertext = struct.pack(">II", A, B)
    return ciphertext

def rc5_decrypt_block(ciphertext, key, word_size=32, rounds=12):
    """Decrypt a block of ciphertext using RC5 algorithm."""
    block_size = len(ciphertext)
    assert block_size == 8, "Block size must be 8 bytes for RC5-32/12"

    # Generate subkeys
    subkeys = rc5_key_schedule(key, word_size, rounds)

    # Convert ciphertext to integers
    A, B = struct.unpack(">II", ciphertext)

    # Decryption rounds
    for i in range(rounds, 0, -1):
        B = right_rotate((B - subkeys[2 * i + 1]) & ((1 << word_size) - 1), A, word_size) ^ A
        A = right_rotate((A - subkeys[2 * i]) & ((1 << word_size) - 1), B, word_size) ^ B
    
    A = (A - subkeys[0]) & ((1 << word_size) - 1)
    B = (B - subkeys[1]) & ((1 << word_size) - 1)

    # Pack decrypted integers back into bytes
    plaintext = struct.pack(">II", A, B)
    return plaintext

# Example usage:
if __name__ == "__main__":
    plaintext = b"Hello123"  # Example plaintext
    key = b"mysecretkey"     # Example key

    # Encryption
    encrypted = rc5_encrypt_block(pad_plaintext(plaintext, 8), key)
    print("Encrypted:", encrypted.hex())

    # Decryption
    decrypted = unpad_plaintext(rc5_decrypt_block(encrypted, key))
    print("Decrypted:", decrypted.decode('utf-8'))

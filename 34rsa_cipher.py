# rsa_cipher.py

import random
from sympy import isprime, mod_inverse

def generate_prime_candidate(length):
    """
    Generate an odd integer randomly.
    """
    p = random.getrandbits(length)
    # Apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p

def generate_prime_number(length=1024):
    """
    Generate a prime number.
    """
    p = 4
    # Keep generating while the primality test fail
    while not isprime(p):
        p = generate_prime_candidate(length)
    return p

def generate_keys(bit_length=1024):
    """
    Generate RSA public and private keys.
    """
    p = generate_prime_number(bit_length)
    q = generate_prime_number(bit_length)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randrange(1, phi)
    # Ensure e and phi(n) are coprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    
    d = mod_inverse(e, phi)
    
    # Public key (e, n) and Private key (d, n)
    return ((e, n), (d, n))

def gcd(a, b):
    """
    Compute the greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return a

def encrypt(public_key, plaintext):
    """
    Encrypt the plaintext using the public key.
    """
    e, n = public_key
    cipher = [(pow(ord(char), e, n)) for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
    """
    Decrypt the ciphertext using the private key.
    """
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)

def main():
    """
    Main function to execute RSA encryption and decryption.
    """
    bit_length = int(input("Enter the bit length for prime numbers (e.g., 1024): "))
    
    public_key, private_key = generate_keys(bit_length)
    
    print("Public key:", public_key)
    print("Private key:", private_key)
    
    plaintext = input("Enter the plaintext message: ")
    
    encrypted_message = encrypt(public_key, plaintext)
    decrypted_message = decrypt(private_key, encrypted_message)
    
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted message: {encrypted_message}")
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()

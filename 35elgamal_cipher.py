# elgamal_cipher.py

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
    Generate ElGamal public and private keys.
    """
    p = generate_prime_number(bit_length)
    g = random.randint(2, p - 1)
    x = random.randint(1, p - 2)
    y = pow(g, x, p)
    
    # Public key (p, g, y) and Private key (x)
    return ((p, g, y), x)

def encrypt(public_key, plaintext):
    """
    Encrypt the plaintext using the public key.
    """
    p, g, y = public_key
    k = random.randint(1, p - 2)
    a = pow(g, k, p)
    b = [(ord(char) * pow(y, k, p)) % p for char in plaintext]
    return (a, b)

def decrypt(private_key, public_key, ciphertext):
    """
    Decrypt the ciphertext using the private key.
    """
    a, b = ciphertext
    p, g, y = public_key
    x = private_key
    s = pow(a, x, p)
    plain = [chr((char * mod_inverse(s, p)) % p) for char in b]
    return ''.join(plain)

def main():
    """
    Main function to execute ElGamal encryption and decryption.
    """
    bit_length = int(input("Enter the bit length for prime numbers (e.g., 1024): "))
    
    public_key, private_key = generate_keys(bit_length)
    
    print("Public key:", public_key)
    print("Private key:", private_key)
    
    while True:
        choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? (E/D): ").upper()
        
        if choice == 'E':
            plaintext = input("Enter the plaintext message: ")
            encrypted_message = encrypt(public_key, plaintext)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == 'D':
            a = int(input("Enter the 'a' component of the ciphertext: "))
            b = input("Enter the 'b' component of the ciphertext (comma separated): ")
            b = [int(char) for char in b.split(',')]
            ciphertext = (a, b)
            decrypted_message = decrypt(private_key, public_key, ciphertext)
            print(f"Decrypted message: {decrypted_message}")
        else:
            print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")
        
        another = input("Would you like to perform another operation? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()

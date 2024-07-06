# Password_Generator.py

import random
import string

def generate_password(length, include_digits=True, include_punctuation=True):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_punctuation:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    print("Generated password:", generate_password(length))

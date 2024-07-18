import hashlib
import os

def calculate_file_hash(file_path, hash_algorithm='sha256'):
    """
    Calculates the hash value of a file using a specified hash algorithm.

    Args:
    - file_path (str): Path to the file.
    - hash_algorithm (str): Hash algorithm to use (default is 'sha256').

    Returns:
    - str: Hexadecimal representation of the file's hash value.
    """
    hash_func = hashlib.new(hash_algorithm)

    with open(file_path, 'rb') as file:
        while True:
            data = file.read(8192)  # Read file in chunks of 8192 bytes
            if not data:
                break
            hash_func.update(data)

    return hash_func.hexdigest()

def check_integrity(original_hash, file_path, hash_algorithm='sha256'):
    """
    Checks the integrity of a file by comparing its hash value with the original hash.

    Args:
    - original_hash (str): Original hash value to compare against.
    - file_path (str): Path to the file to check.
    - hash_algorithm (str): Hash algorithm used (default is 'sha256').

    Returns:
    - bool: True if the file's hash matches the original hash, False otherwise.
    """
    current_hash = calculate_file_hash(file_path, hash_algorithm)
    return original_hash == current_hash

if __name__ == "__main__":
    print("=== File Integrity Checker ===")

    while True:
        file_path = input("Enter the path to the file: ").strip()
        if os.path.isfile(file_path):
            break
        else:
            print(f"Error: '{file_path}' is not a valid file. Please enter a valid file path.")

    hash_algorithm = input("Enter the hash algorithm (default is 'sha256'): ").strip().lower() or 'sha256'

    if hash_algorithm not in hashlib.algorithms_available:
        print(f"Error: Hash algorithm '{hash_algorithm}' is not available.")
        exit()

    original_hash = calculate_file_hash(file_path, hash_algorithm)
    print(f"\nOriginal Hash ({hash_algorithm}):")
    print(original_hash)

    try:
        with open(file_path, 'r+b') as file:
            file.seek(0)
            file.write(b'1')
    except IOError as e:
        print(f"Error: {e}")
        exit()

    print("\nSimulating file modification...")

    is_integrity_intact = check_integrity(original_hash, file_path, hash_algorithm)
    if is_integrity_intact:
        print("\nFile integrity is intact.")
    else:
        print("\nFile integrity check failed. File may have been modified.")

# diffie_hellman_gui.py

import tkinter as tk
from tkinter import messagebox
import random
from time import sleep
from sympy import isprime, mod_inverse

def generate_prime_candidate(length):
    """Generate an odd integer randomly."""
    p = random.getrandbits(length)
    # Apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p

def generate_prime_number(length=1024):
    """Generate a prime number."""
    p = 4
    while not isprime(p):
        p = generate_prime_candidate(length)
    return p

def generate_keys(prime, base):
    """Generate private and public keys."""
    private_key = random.randint(2, prime - 2)
    public_key = pow(base, private_key, prime)
    return private_key, public_key

def generate_shared_secret(prime, private_key, other_public_key):
    """Generate a shared secret."""
    return pow(other_public_key, private_key, prime)

def simulate_key_exchange(bit_length, delay, text_widget):
    prime = generate_prime_number(bit_length)
    base = random.randint(2, prime - 2)

    text_widget.insert(tk.END, f"Generated parameters:\nPrime number (p): {prime}\nBase (g): {base}\n\n")
    text_widget.update()
    sleep(delay)

    # Alice generates her keys
    alice_private_key, alice_public_key = generate_keys(prime, base)
    text_widget.insert(tk.END, "Alice's keys:\n")
    text_widget.insert(tk.END, f"  Private key: {alice_private_key}\n")
    text_widget.insert(tk.END, f"  Public key: {alice_public_key}\n\n")
    text_widget.update()
    sleep(delay)

    # Bob generates his keys
    bob_private_key, bob_public_key = generate_keys(prime, base)
    text_widget.insert(tk.END, "Bob's keys:\n")
    text_widget.insert(tk.END, f"  Private key: {bob_private_key}\n")
    text_widget.insert(tk.END, f"  Public key: {bob_public_key}\n\n")
    text_widget.update()
    sleep(delay)

    # Generate shared secrets
    alice_shared_secret = generate_shared_secret(prime, alice_private_key, bob_public_key)
    bob_shared_secret = generate_shared_secret(prime, bob_private_key, alice_public_key)
    
    text_widget.insert(tk.END, f"Alice's shared secret: {alice_shared_secret}\n")
    text_widget.insert(tk.END, f"Bob's shared secret: {bob_shared_secret}\n\n")
    text_widget.update()
    sleep(delay)

    if alice_shared_secret == bob_shared_secret:
        text_widget.insert(tk.END, "Success! The shared secrets match.\n")
    else:
        text_widget.insert(tk.END, "Error! The shared secrets do not match. Something went wrong.\n")
    
    text_widget.update()

def start_simulation():
    try:
        bit_length = int(bit_length_entry.get())
        delay = float(delay_entry.get())
        if bit_length < 2:
            raise ValueError("Bit length must be greater than 1.")
    except ValueError as e:
        messagebox.showerror("Invalid input", str(e))
        return

    text_widget.delete(1.0, tk.END)
    simulate_key_exchange(bit_length, delay, text_widget)

# Create the main window
root = tk.Tk()
root.title("Diffie-Hellman Key Exchange Simulation")

# Create and place the bit length input field
tk.Label(root, text="Bit length for prime numbers (e.g., 1024):").pack()
bit_length_entry = tk.Entry(root)
bit_length_entry.pack()

# Create and place the delay input field
tk.Label(root, text="Time delay between steps (seconds):").pack()
delay_entry = tk.Entry(root)
delay_entry.pack()

# Create and place the start button
start_button = tk.Button(root, text="Start Simulation", command=start_simulation)
start_button.pack()

# Create and place the text widget for displaying output
text_widget = tk.Text(root, height=20, width=80)
text_widget.pack()

# Start the main event loop
root.mainloop()

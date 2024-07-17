# advanced_password_strength_checker.py
import re
import tkinter as tk
from tkinter import messagebox
from collections import Counter

# List of common passwords (expand this list as needed)
common_passwords = [
    "123456", "password", "123456789", "12345678", "12345", 
    "1234567", "1234567890", "qwerty", "abc123", "password1"
]

# Load a dictionary of common words
with open("dictionary.txt") as f:
    common_words = set(word.strip().lower() for word in f)

def check_password_strength(password):
    """
    Checks the strength of a given password and provides feedback.

    Parameters:
    password (str): The password to check.

    Returns:
    str: A message indicating the strength of the password.
    """
    feedback = []

    # Length check
    if len(password) < 8:
        feedback.append("Password must be at least 8 characters long.")
    
    # Uppercase and lowercase letters
    if not re.search(r'[A-Z]', password):
        feedback.append("Password must contain at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        feedback.append("Password must contain at least one lowercase letter.")
    
    # Digits and special characters
    if not re.search(r'[0-9]', password):
        feedback.append("Password must contain at least one digit.")
    if not re.search(r'[@$!%*?&#]', password):
        feedback.append("Password must contain at least one special character (@$!%*?&#).")
    
    # Common passwords check
    if password in common_passwords:
        feedback.append("Password is too common.")
    
    # Consecutive identical characters
    if re.search(r'(.)\1{2,}', password):
        feedback.append("Password must not contain three or more consecutive identical characters.")
    
    # Sequential characters
    if re.search(r'(012|123|234|345|456|567|678|789|890|qwerty|asdf|zxcv|qwertyuiop)', password.lower()):
        feedback.append("Password must not contain sequential characters (e.g., '123', 'abc').")
    
    # Dictionary words
    words = re.findall(r'[a-zA-Z]+', password)
    for word in words:
        if word.lower() in common_words:
            feedback.append(f"Password contains a common dictionary word: {word}")
    
    # Calculate strength
    if not feedback:
        return "Password is strong.", feedback
    elif len(feedback) <= 2:
        return "Password is moderate.", feedback
    else:
        return "Password is weak.", feedback

def on_check_password():
    """
    Handler function for the 'Check Password' button click.
    """
    password = password_entry.get()
    strength, feedback = check_password_strength(password)
    messagebox.showinfo("Password Strength", f"{strength}\n\n" + "\n".join(feedback))

# GUI setup
root = tk.Tk()
root.title("Advanced Password Strength Checker")

tk.Label(root, text="Enter Password:").pack(pady=10)
password_entry = tk.Entry(root, show='*', width=40)
password_entry.pack(pady=10)

check_button = tk.Button(root, text="Check Password", command=on_check_password)
check_button.pack(pady=20)

root.mainloop()

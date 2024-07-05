# Advanced_Double_Encryption_GUI.py

import base64
from tkinter import *
from tkinter import ttk

# Caesar Cipher function for the first encryption
def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():  # Check if the character is alphabetic
            shifted = ord(char) + shift  # Shift the character by the specified amount
            if char.islower():  # Handle lowercase letters
                if shifted > ord('z'):  # Wrap around if shifted beyond 'z'
                    shifted -= 26
                elif shifted < ord('a'):  # Wrap around if shifted before 'a'
                    shifted += 26
            elif char.isupper():  # Handle uppercase letters
                if shifted > ord('Z'):  # Wrap around if shifted beyond 'Z'
                    shifted -= 26
                elif shifted < ord('A'):  # Wrap around if shifted before 'A'
                    shifted += 26
            result.append(chr(shifted))  # Append the shifted character to the result list
        else:
            result.append(char)  # Append non-alphabetic characters unchanged
    return ''.join(result)  # Return the encrypted or decrypted text as a string

# Function to perform double encryption
def double_encrypt():
    input_text = input_field.get("1.0", END).strip()  # Get input text from the input field
    
    # First encryption: Caesar Cipher with shift of 3
    encrypted_text1 = caesar_cipher(input_text, 3)
    
    # Second encryption: Base64 encoding
    encoded_text = base64.b64encode(encrypted_text1.encode()).decode()
    
    output_field.config(state=NORMAL)  # Enable the output field to insert text
    output_field.delete("1.0", END)  # Clear the output field
    output_field.insert("1.0", encoded_text)  # Insert the encoded text into the output field
    output_field.config(state=DISABLED)  # Disable the output field to make it read-only

# Function to perform double decryption
def double_decrypt():
    input_text = input_field.get("1.0", END).strip()  # Get input text from the input field
    
    # First decryption: Base64 decoding
    decoded_text = base64.b64decode(input_text.encode()).decode()
    
    # Second decryption: Caesar Cipher with shift of -3 (inverse of encryption)
    decrypted_text2 = caesar_cipher(decoded_text, -3)
    
    output_field.config(state=NORMAL)  # Enable the output field to insert text
    output_field.delete("1.0", END)  # Clear the output field
    output_field.insert("1.0", decrypted_text2)  # Insert the decoded text into the output field
    output_field.config(state=DISABLED)  # Disable the output field to make it read-only

# Set up the main application window
root = Tk()  # Create the main window
root.title("Double Encryption GUI")  # Set the window title

# Create style for ttk widgets
style = ttk.Style()
style.configure('TButton', padding=(10, 5), font='Helvetica 12')

# Input field
input_label = Label(root, text="Input Text", font='Helvetica 14 bold')
input_label.pack(pady=10)  # Pack the input label with padding
input_field = Text(root, height=5, width=60, font='Helvetica 12')
input_field.pack()  # Pack the input text field

# Buttons frame
buttons_frame = Frame(root)  # Create a frame for buttons
buttons_frame.pack(pady=20)  # Pack the frame with padding

# Encrypt button
encrypt_button = ttk.Button(buttons_frame, text="Encrypt", command=double_encrypt)
encrypt_button.grid(row=0, column=0, padx=10)  # Place the Encrypt button in the frame

# Decrypt button
decrypt_button = ttk.Button(buttons_frame, text="Decrypt", command=double_decrypt)
decrypt_button.grid(row=0, column=1, padx=10)  # Place the Decrypt button in the frame

# Output field
output_label = Label(root, text="Output Text", font='Helvetica 14 bold')
output_label.pack(pady=10)  # Pack the output label with padding
output_field = Text(root, height=5, width=60, font='Helvetica 12', state=DISABLED)
output_field.pack()  # Pack the output text field

# Start the main loop to run the application
root.mainloop()

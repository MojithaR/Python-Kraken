# Basic_Crypto.py

# Import the necessary libraries
import base64  # For base64 encoding and decoding
from tkinter import *  # For GUI components

# Function to encode the input text to Base64
def encode_text():
    # Get the input text from the input field
    input_text = input_field.get("1.0", END).strip()
    # Encode the input text to Base64
    encoded_text = base64.b64encode(input_text.encode()).decode()
    # Enable the output field to insert text
    output_field.config(state=NORMAL)
    # Clear the output field
    output_field.delete("1.0", END)
    # Insert the encoded text into the output field
    output_field.insert("1.0", encoded_text)
    # Disable the output field to make it read-only
    output_field.config(state=DISABLED)

# Function to decode the Base64 input text back to normal text
def decode_text():
    # Get the input text from the input field
    input_text = input_field.get("1.0", END).strip()
    try:
        # Decode the input text from Base64
        decoded_text = base64.b64decode(input_text.encode()).decode()
        # Enable the output field to insert text
        output_field.config(state=NORMAL)
        # Clear the output field
        output_field.delete("1.0", END)
        # Insert the decoded text into the output field
        output_field.insert("1.0", decoded_text)
        # Disable the output field to make it read-only
        output_field.config(state=DISABLED)
    except Exception as e:
        # If an error occurs, show an error message in the output field
        output_field.config(state=NORMAL)
        output_field.delete("1.0", END)
        output_field.insert("1.0", "Error: Invalid Base64 string")
        output_field.config(state=DISABLED)

# Set up the main application window
root = Tk()  # Create the main window
root.title("Base64 Encoder and Decoder")  # Set the window title

# Create and pack the input field label
input_label = Label(root, text="Input Text")
input_label.pack()

# Create and pack the input field (multi-line text widget)
input_field = Text(root, height=5, width=50)
input_field.pack()

# Create and pack the encode button
encode_button = Button(root, text="Encode", command=encode_text)
encode_button.pack(pady=5)

# Create and pack the decode button
decode_button = Button(root, text="Decode", command=decode_text)
decode_button.pack(pady=5)

# Create and pack the output field label
output_label = Label(root, text="Output Text")
output_label.pack()

# Create and pack the output field (multi-line text widget, read-only)
output_field = Text(root, height=5, width=50, state=DISABLED)
output_field.pack()

# Start the main loop to run the application
root.mainloop()

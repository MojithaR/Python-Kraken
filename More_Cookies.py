#!/usr/bin/python3
import requests
import base64

# Create a session
s = requests.Session()

# Make a GET request to the target URL
s.get("http://mercury.picoctf.net:43275/")

# Get the value of the cookie named "auth_name"
cookie = s.cookies["auth_name"]
print(cookie)

# Decode the base64 encoded cookie
unb64 = base64.b64decode(cookie)
print(unb64)

# Decode the base64 encoded data again to reveal the original bytes
unb64b = base64.b64decode(unb64)

# Iterate through each bit position
for i in range(0, 128):
    # Calculate the byte position
    pos = i // 8

    # Perform a bit flip at the current position
    guessdec = (
        unb64b[0:pos] +
        ((unb64b[pos] ^ (1 << (i % 8))).to_bytes(1, 'big')) +
        unb64b[pos + 1:]
    )

    # Encode the modified bytes using base64
    guessenc1 = base64.b64encode(guessdec)

    # Further encode the modified bytes twice using base64
    guess = base64.b64encode(base64.b64encode(guessdec)).decode()

    # Make a GET request with the modified cookie
    r = requests.get("http://mercury.picoctf.net:43275/", cookies={"auth_name": guess})

    # Check if the response contains "pico"
    if "pico" in r.text:
        print(r.text)  # Print the response if "pico" is found

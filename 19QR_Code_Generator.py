# QR_Code_Generator.py

import qrcode

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)

if __name__ == "__main__":
    data = input("Enter data for QR code: ")
    filename = input("Enter filename to save QR code (e.g., qrcode.png): ")
    generate_qr_code(data, filename)
    print(f"QR code saved as {filename}")

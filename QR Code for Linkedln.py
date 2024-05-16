#QR Code in Image format

import qrcode  # Import the qrcode library for generating QR codes

data = "https://www.linkedin.com/in/vishaalgautam/"  # URL to be encoded in the QR code

# Generate QR code
qr = qrcode.QRCode(version=1, box_size=9, border=3)  # Create a QRCode instance with specified version, box size, and border
qr.add_data(data)  # Add the data to be encoded to the QRCode instance
qr.make(fit=True)  # Generate the QR code, adjusting the size to fit the data if necessary

# Create an image from the QR Code instance
img = qr.make_image(fill_color="Yellow", back_color="Black")  # Generate an image of the QR code with specified fill and background color

# Display the image
img.show()  # Show the generated QR code image


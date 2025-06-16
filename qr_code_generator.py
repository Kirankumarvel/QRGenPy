# QR Code Generator using Python
import qrcode

# Data to be encoded
data = "https://kirankumarvel.wordpress.com/"

# Create QR code image
img = qrcode.make(data)

# Save the QR code image
img.save("qr.png")

print("QR Code generated and saved as 'qr.png'")

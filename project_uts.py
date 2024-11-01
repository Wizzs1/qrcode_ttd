import qrcode
import barcode
from barcode.writer import ImageWriter
from PIL import Image

# URL pendek hasil dari layanan URL shortener
short_url = "https://ibb.co.com/bzNzV6C"

# Membuat QR code dengan URL pendek
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(short_url)
qr.make(fit=True)

qr_img = qr.make_image(fill='black', back_color='white')
qr_img.save("qrcode_gambar.png")
print("QR code berhasil dibuat dan disimpan sebagai 'qrcode_gambar.png'")

# Membuat Barcode dengan URL pendek menggunakan Code128
options = {'write_text': False}  # Disable the text below the barcode
ean = barcode.get('code128', short_url, writer=ImageWriter())
barcode_img = ean.save("barcode_gambar", options=options)
print("Barcode berhasil dibuat dan disimpan sebagai 'barcode_gambar.png'")

# Menampilkan QR code dan Barcode
qr_img.show()
barcode_img = Image.open("barcode_gambar.png")
barcode_img.show()

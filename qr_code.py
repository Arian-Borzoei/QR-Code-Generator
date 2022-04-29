# [Dev - Arian]

from importlib_metadata import version
import qrcode

data = "Push The Information you Want To Create The QR Code for"

qr = qrcode.QRCode(
    version=1 ,box_size=10 ,border=5)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(
    fill_Color = "black",
    back_Color = "white")

img.save("qrCode.png")
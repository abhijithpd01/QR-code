import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("GEC IDUKKI,PIN:685603")
qr.png("mycode.png",scale=8)

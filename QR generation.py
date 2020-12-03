import pyqrcode
qr = pyqrcode.create("GEC IDUKKI,PIN:685603")
qr.png("mycode.png",scale=8)

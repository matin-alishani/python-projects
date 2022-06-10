import qrcode
x = "hello world"
qr = qrcode.make(x)
qr.save(r"C:\Users\A\Desktop\python\qr.png")


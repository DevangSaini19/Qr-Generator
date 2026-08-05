import qrcode

data = "Learning Data Structures And Algorithms"

qr = qrcode.make(data)

qr.save("qrcode.png")

print("Qr Code Generated Successfully")
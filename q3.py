import qrcode
qr=qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

data="https://youtu.be/It57Mjm09pk"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="green")
img.save('text.png')
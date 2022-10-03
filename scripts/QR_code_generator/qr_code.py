import qrcode

link = input("Paste Your URL Here: ")
img = qrcode.make(link)
name_img = input("Name of img: ")
img.save(name_img)

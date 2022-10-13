from PIL import Image

img  = Image.open(r"testpic.jpg") 

pix = img.load()
w , h = img.size

for i in range(w):
    for j in range(h):   
        RGB_tuple = pix[i,j]
        AVG = int((int(RGB_tuple[0]) + int(RGB_tuple[1]) + int(RGB_tuple[2])) / 3)
        pix[i,j] = (AVG, AVG, AVG)
img.save('testpic_grayscaled.png')
from PIL import Image

img_1 = Image.open(r'image1.jpg')
img_2 = Image.open(r'image2.jpg')
img_3 = Image.open(r'image3.jpeg')
img_4 = Image.open(r'image4.jpg')
img_5 = Image.open(r'image5.png')
img_6 = Image.open(r'image6.png')

im_1 = img_1.convert('RGB')
im_2 = img_2.convert('RGB')
im_3 = img_3.convert('RGB')
im_4 = img_4.convert('RGB')
im_5 = img_5.convert('RGB')
im_6 = img_6.convert('RGB')

imlist = [im_2, im_3, im_4,im_5,im_6]

im_1.save(r'listimg.pdf', save_all=True, append_images=imlist)
from PIL import Image
# Make sure to add the paths of Images 
im1 = Image.open(r'path where the JPG is stored\file name.jpg')
im1.save(r'path where the PNG will be stored\new file name.png')

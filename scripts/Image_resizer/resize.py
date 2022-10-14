from PIL import Image as img 
import os

file_name = input("Enter anpe of file: ")
name , ext = file_name.split('.')
pic = img.open((os.path.join(os.path.dirname(os.path.abspath(__file__)),file_name)))

ht, wt= input("Enter dimenstions(eg: 1024x720): ").split('x')
dim = int(ht), int(wt)
img_resize = pic.resize(dim)
img_resize.save((os.path.join(os.path.dirname(os.path.abspath(__file__)),f'{name}_resized.{ext}')))
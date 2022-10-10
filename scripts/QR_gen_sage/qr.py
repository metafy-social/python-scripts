import pyqrcode 
from pyqrcode import QRCode 
  
# @author https://github.com/theadeyemiolayinka

s = input('Enter your URL:\n>')
f = input('Enter preferred file name (without extension):\n>')
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file
url.svg(f+'.png', scale = 8) 

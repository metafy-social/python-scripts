from email.mime import image
import urllib.request
import os

#You can replace the replace the urls links according to your needs
urls = [
    'https://images.unsplash.com/photo-1664552399245-8ee5fa8eddd2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=685&q=80',

    'https://images.unsplash.com/photo-1664519803504-a8ed329d9381?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=735&q=80',

    'https://images.unsplash.com/photo-1664361859625-07f20702b6c2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1074&q=80'

]

# This function will create a images folder to save our images
def downloadImage(image_urls):
    crtFileLocation =  os.getcwd()
    os.makedirs('Images')
    
    for x in range(0, len(image_urls)):
      filename =  'image_' +  str(x) + '.png'
      print(f'downloading {x+1} out of {len(image_urls)} images')
      urllib.request.urlretrieve(image_urls[x], os.path.join(crtFileLocation, 'Images', filename))

downloadImage(urls)


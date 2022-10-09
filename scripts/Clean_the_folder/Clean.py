import os
folder_location = 'C:\\Users\\user\\Downloads\\demo'

os.chdir(folder_location)
list_of_files = os.listdir()

images = [content for content in list_of_files if content.endswith(('.png','.jpg','.jpeg'))] 

for index, image in  enumerate(images):
    os.rename(image,f'{index}.png')


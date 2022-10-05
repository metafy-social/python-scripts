from PIL import Image
from PIL.ExifTags import TAGS
import sys

arg = sys.argv[1]
if arg == "":
    print("Please give a valid image path")
    quit()

image = Image.open(arg)
exifdata = image.getexif()
 
if len(exifdata) <= 0:
    print("No metadata found for this image")
    quit()

for tag_id in exifdata:
      
    tagname = TAGS.get(tag_id, tag_id)
    value = exifdata.get(tag_id)

    print(f"{tagname:25}: {value}")

import os
from PIL import Image


def tiff_to_jpeg():
    path = os.getcwd()
    for root, dirs, files in os.walk(path):
        for name in files:
            if os.path.splitext(os.path.join(root, name))[1].lower() == ".tiff":
                outfile = os.path.splitext(os.path.join(root, name))[0] + ".jpg"
                im = Image.open(os.path.join(root, name)).convert('RGB')
                im.thumbnail(im.size)
                im.save(outfile, "JPEG", quality=90)
    print('.tiff file(s) are converted to .jpeg')


def tiff_to_png():

    path = os.getcwd()
    for root, dirs, files in os.walk(path):
        for name in files:
            if os.path.splitext(os.path.join(root, name))[1].lower() == ".tiff":
                outfile = os.path.splitext(os.path.join(root, name))[0] + ".png"
                im = Image.open(os.path.join(root, name)).convert('RGB')
                im.thumbnail(im.size)
                im.save(outfile, "PNG", quality=90)
    print('.tiff file(s) are converted to .png')

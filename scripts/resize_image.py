# import argparse
# import sys
# import cv2
# import os

# parser = argparse.ArgumentParser()
# parser.add_argument("--src", metavar="source",
#                     help="Source folder of the Image files")
# parser.add_argument("--dest", metavar="destinantion",
#                     help="Destination folder of the Image files (Default: Source folder)")
# parser.add_argument("--size", metavar="size", nargs='+', type=int,
#                     help="Size of the new image(Width Height)")
# parser.add_argument("--ext", metavar="extension", nargs='+',
#                     help="""Extensions of files to be resized (Default: jpg png).
#                          Supported extensions - Extensions Supported by OpenCV.""")
# args = parser.parse_args()


# def resize_image(img, size):
#     """Resize the image to given size
#     params:
#         img - array of image pixels
#         size - tuple => (Width, Height)
#     """

#     return cv2.resize(img, size, interpolation=cv2.INTER_AREA)


# def load_images(src, ext, size):
#     """Resize the images in given source folder
#     and save to the destinantion folder
#     params:
#         src - Source folder
#         ext - Extensions of images to be
#     """

#     cd = os.getcwd()
#     os.chdir(src)
#     files_ls = os.listdir()
#     files = [file for file in files_ls if ((len(file.split('.')) > 1)
#              and (file.split('.')[1].lower() in ext))]
#     res_imgs = []
#     for file in files:
#         img = cv2.imread(file)
#         res_imgs.append((file, resize_image(img, size)))
#         print("\nResizing Image:", src + file)

#     return res_imgs, cd


# def save_images(cd, imgs, src, dest):
#     """Save the images to the destination folder
#     params:
#         cd - Working Directory where program resides
#         imgs - list of Tuples => (image name, image)
#         src - Source of the image files
#         dest - destinantion folder of the image
#     """
#     os.chdir(cd)
#     os.chdir(dest)
#     for img in imgs:
#         cv2.imwrite(img[0], img[1])
#         print("\nSaving Image:", src + img[0],
#               "To", dest + img[0])


# if args.src == None:
#     sys.exit("Path source Folder Missing")


# if args.dest == None:
#     args.dest = args.src


# if args.size == None:
#     sys.exit("New image size missing.")


# if args.ext == None:
#     args.ext = ['jpg', 'png']


# imgs, cd = load_images(args.src, args.ext, tuple(args.size))
# save_images(cd, imgs, args.src, args.dest)


import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("D:\image.jpg", 1)
# Loading the image

half = cv2.resize(image, (0, 0), fx=0.1, fy=0.1)
bigger = cv2.resize(image, (1050, 1610))

stretch_near = cv2.resize(image, (780, 540),
                          interpolation=cv2.INTER_NEAREST)


Titles = ["Original", "Half", "Bigger", "Interpolation Nearest"]
images = [image, half, bigger, stretch_near]
count = 4

for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i])

plt.show()

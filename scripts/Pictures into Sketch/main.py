from turtle import done
import cv2
img = input("Enter the name of image with file extension name that is in the same directory")
image = cv2.imread(img)
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)
blur = cv2.GaussianBlur(invert, (21,21),0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)

cv2.imwrite("sketch.png", sketch)
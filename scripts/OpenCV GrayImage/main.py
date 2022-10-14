import cv2

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    
    blurImage = cv.GaussianBlur(img,(5,5),0)
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayimage", grayImg)
    cv2.imshow("Blur", blurImage)
    cv2.imshow("image",img)
    cv2.waitKey(10)

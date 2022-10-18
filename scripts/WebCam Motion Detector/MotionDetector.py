import cv2,time,pandas
from datetime import datetime

first_frame = None
status_list = [None, None]
time = []
df = pandas.DataFrame(columns=["Start", "End"])

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    status = 0
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    grey = cv2.GaussianBlur(grey, (21, 21), 0)  #blurring for accuracy

    if first_frame is None:     #capturing the background or the initial frame
        first_frame = grey
        continue

    delta_frame = cv2.absdiff(first_frame, grey)    #to 

    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    #returns a tuple and converts the moving pixels to white

    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)

    for cont in cnts:
        if cv2.contourArea(cont) < 10000:  #excluding negligble objects
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(cont)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3,)
    status_list.append(status)

    status_list = status_list[-2:] 

    if status_list[-1] == 1 and status_list[-2] == 0:
        time.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        time.append(datetime.now())
    cv2.imshow("captured", grey)
    cv2.imshow("delta", delta_frame)
    cv2.imshow("Threshold", thresh_frame)
    cv2.imshow("color frame", frame)
    
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        if status == 1:
            time.append(datetime.now())
        break
    print(status)

print(status_list)
print(time)

for i in range(0, len(time), 2):
    df = df.append({"Start" : time[i], "End": time[i+1]}, ignore_index=True)

df.to_csv("Times.csv")



video.release()
cv2.destroyAllWindows()
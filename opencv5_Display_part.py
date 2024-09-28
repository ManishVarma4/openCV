import cv2
import numpy as np
img = cv2.VideoCapture(0)
while(True):
    ret,frame = img.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90,50,50])
    upper_blue = np.array([130,255,255])
    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("FRAME", res)
    cv2.imshow("mask", mask)

    if cv2.waitKey(1)== ord('q'):
        break
img.release()
cv2.destroyAllWindows()

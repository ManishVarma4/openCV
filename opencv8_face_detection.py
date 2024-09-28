import cv2
import numpy as np
img = cv2.VideoCapture(0)
face = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

while(True):
    ret, frame = img.read()
    gar= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gar,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),5)
        roi_gray = gar[y:y+w,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        eyes = eye.detectMultiScale(roi_gray,1.3,5)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),5)
    cv2.imshow("FRAME",frame)
    if cv2.waitKey(1)==ord('q'):
        break
img.release()
cv2.destroyAllWindows()
import cv2
img = cv2.VideoCapture(0)
while(True):
    ret,frame = img.read()
    width = int(img.get(3))
    height = int(img.get(4))
    cv2.line(frame,(0,0),(width,height),(255,255,76),10)
    cv2.line(frame,(0,height),(width,0),(2,255,76),10)
    cv2.rectangle(frame,(100,100),(200,200),(0,0,0),-1)
    cv2.circle(frame,(400,400),90,(56,78,200),-1)
    font = cv2.FONT_ITALIC
    cv2.putText(frame,'He still likes Honey!!',(width//2,height-50),font,0.5,(0,0,0),2)
    cv2.imshow("FRAME", frame)
    if cv2.waitKey(1)== ord('q'):
        break
img.release()
cv2.destroyAllWindows()
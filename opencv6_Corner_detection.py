import numpy as np
import cv2
img = cv2.imread('Screenshot 2024-09-03 145945.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
corners =cv2.goodFeaturesToTrack(gray,100,0.01,10)
corners= np.intp(corners)
# print(corners)
for cor in corners:
    x,y = cor.ravel()
    cv2.circle(img,(x,y),5,(255,0,0),-1)
for i in range(len(corners)):
    for j in range(i+1,len(corners)):
        co1 = tuple(corners[i][0])
        co2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x),np.random.randint(0,255,size=3)))
        cv2.line(img,co1,co2,color,1)
cv2.imshow("IMG",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

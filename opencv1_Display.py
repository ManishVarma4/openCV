import cv2
img = cv2.imread("Nitro_Wallpaper_03_3840x2400.jpg",1)
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite('new.jpg',img)
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

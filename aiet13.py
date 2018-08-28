import cv2
img=cv2.imread('flower.jpg')
img_HSV=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow('HSV image',img_HSV)
cv2.imshow('Hue Channel',img_HSV[:,0,0])
cv2.imshow('Saturation',img_HSV[1,:,1])
cv2.imshow('Value Channel',img_HSV[2,2,:])
cv2.waitKey(0)
cv2.destroyAllWindows()

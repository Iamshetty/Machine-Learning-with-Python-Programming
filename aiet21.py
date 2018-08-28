import cv2
import numpy as np
img=cv2.imread("flower.jpg")
height,width=img.shape[:2]
rot_matrix=cv2.getRotationMatrix2D((width/4,height/4),70,0.7)
rot_img=cv2.warpAffine(img,rot_matrix,(width,height))


cv2.imshow('Original image',img)
cv2.imshow('Rotation image',rot_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
img=cv2.imread("flower.jpg",0)
height,width=img.shape

sobel_x=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobel_y=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
cv2.imshow('Original',img)
cv2.waitKey(0)
cv2.imshow('Sobel x image',sobel_x)
cv2.waitKey(0)
cv2.imshow('y image',sobel_y)
cv2.waitKey(0)

s_or=cv2.bitwise_or(sobel_x,sobel_y)
cv2.imshow('Sobel or image',s_or)
cv2.waitKey(0)

laplacian=cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow('Laplacian',laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as pd
img=cv2.imread('flower.jpg')
height,width=img.shape[:2]
s_r,s_c=int(height*.00),int(width*.00)
e_r,e_c=int(height*.50),int(width*.50)

s_r1,s_c1=int(height*.50),int(width*.50)
e_r1,e_c1=int(height*1.0),int(width*1.0)






cropped=img[s_r:e_r,s_c:e_c]
cropped1=img[s_r1:e_r1,s_c1:e_c1]
#cropped2=img[s_r2:e_r2,s_c2:e_c2]

cv2.imshow('Og',img)
cv2.waitKey(0)

cv2.imshow('Cropped',cropped)
cv2.waitKey(0)

cv2.imshow('Cropped1',cropped1)
cv2.waitKey(0)
'''cv2.imshow('Cropped2',cropped2)
cv2.waitKey(0)'''


cv2.destroyAllWindows()

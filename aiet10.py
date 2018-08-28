import cv2
import matplotlib.pyplot as plt
#import numpy as np

img=cv2.imread("flower.jpg")
cv2.imshow("Hello World",img)
'''titles=['Flower', 'Red channel', 'Green channel', 'Blue channel']
cmaps = [None, plt.Reds_r, plt.cm.Greens_r, plt.cm.Blues_r]'''

red_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  
cv2.imshow('Grayscale',red_img)
#cv2.imshow(cmap=cmaps)
'''cv2.imshow('Redscale',cmaps)
cv2.imshow('Greenscale',cmaps)
cv2.imshow('Bluescale',cmaps)'''


cv2.waitKey(0)
cv2.destroyAllWindows()

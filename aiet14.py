import cv2
import numpy as np

img = np.zeros([512,512,3],np.uint8)
img+=255
cv2.imshow('White Rectangle Color',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

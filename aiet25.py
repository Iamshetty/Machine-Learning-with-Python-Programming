import cv2 as cv
import numpy as np

img = cv.imread("flower.jpg")

height, width = img.shape[:2]

start_row, start_col = int(height*.00), int(width*.00)
end_row, end_col = int(height*.50), int(width*.50)
cropped1 = img[start_row:end_row, start_col:end_col]

start_row, start_col = int(height*.00), int(width*.50)
end_row, end_col = int(height*.50), int(width*1.0)
cropped2 = img[start_row:end_row, start_col:end_col]

start_row, start_col = int(height*.50), int(width*.00)
end_row, end_col = int(height*1.0), int(width*.50)
cropped3 = img[start_row:end_row, start_col:end_col]

start_row, start_col = int(height*.50), int(width*.50)
end_row, end_col = int(height*1.0), int(width*1.0)
cropped4 = img[start_row:end_row, start_col:end_col]

cv.imshow('Original Image', img)
cv.waitKey(0)
cv.imshow('Cropped Image 1', cropped1)
cv.waitKey(0)
cv.imshow('Cropped Image 2', cropped2)
cv.waitKey(0)
cv.imshow('Cropped Image 3', cropped3)
cv.waitKey(0)
cv.imshow('Cropped Image 4', cropped4)
cv.waitKey(0)

cv.destroyAllWindows()

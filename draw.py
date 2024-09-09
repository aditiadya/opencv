import cv2 as cv
import numpy as np

# dummy image(blank image)
blank = np.zeros((500, 500, 3), dtype = 'uint8')
cv.imshow('Blank', blank)

# 1) paint the image a certain color

# paint whole iamge of a certain color
# blank[:] = 0,255,0
# cv.imshow('Green', blank)

# paint some dimension of the image with a certain color
blank[200:300, 300:400] = 0,255,0
cv.imshow('Green', blank)

# 2) draw a rectangle
cv.rectangle(blank, (0,0),(250,250), (0, 255, 0), thickness=2)
# cv.rectangle(blank, (0,0),(250,250), (0, 255, 0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

cv.waitKey(0)
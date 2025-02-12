import cv2 as cv

img = cv.imread('k1.pgm')
cv.imshow('read_', img)
cv.waitKey(0)
cv.destroyAllWindows()

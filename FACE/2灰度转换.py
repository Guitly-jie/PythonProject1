import cv2 as cv
img =cv.imread('k1.jpg')
#灰度转换
gray1_img =cv.cvtColor(img,cv.COLOR_RGB2BGR)
gray2_img =cv.cvtColor(img,cv.COLOR_RGB2YCrCb)


cv.imshow('gray1',gray1_img)
cv.imshow('gray2',gray2_img)
cv.imshow('read',img)

cv.imwrite('gray1.jpg',gray1_img)
cv.imwrite('gray2.jpg',gray2_img)
cv.waitKey(0)
cv.destroyAllWindows()

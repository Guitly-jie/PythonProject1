import cv2 as cv
img=cv.imread('k1.pgm')
x,y,w,h=100,100,100,100
cv.rectangle(img,(x,y,x+w,x+y),color=(255,0,0),thickness=10)

a,b,r=100,100,100
cv.circle(img,center=(a,b),radius=r,color=(0,0,255),thickness=5)
#显示图片
cv.imshow('rectangle_img',img)
cv.waitKey(0)
cv.destroyAllWindows()
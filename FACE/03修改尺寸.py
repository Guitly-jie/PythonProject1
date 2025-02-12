import cv2 as cv
img=cv.imread('k1.pgm')
resize_img=cv.resize(img,dsize=(2000,2400))

cv.imshow('resize_img',resize_img)

cv.imwrite('re.jpg',resize_img)

print("原来图片的形状",img.shape)
print("后来图片的形状",resize_img.shape)
while True:
    if ord("F")==cv.waitKey(0):
        break
cv.destroyAllWindows()

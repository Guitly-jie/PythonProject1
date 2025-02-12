import cv2 as cv
def face_detect_demo():
    # 转换为灰度图像
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # 加载特征数据
    face_detector = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # 检测人脸
    faces = face_detector.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=4)
    for x, y, w, h in faces:
        print(x,y,w,h)
        cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 255, 255), thickness=2)
        cv.circle(img,center=(x+w//2,y+h//2),radius=w//2,color=(0,255,255),thickness=2)
    # 显示结果
    cv.imshow('result', img)

img = cv.imread('k3.jpg')
face_detect_demo()

# 等待按键并关闭窗口
cv.waitKey(0)
cv.destroyAllWindows()
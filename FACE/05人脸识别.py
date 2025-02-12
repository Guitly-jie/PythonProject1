import cv2 as cv


# 人脸检测函数
def face_detect_demo():
    # 转换为灰度图像
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # 加载特征数据
    face_detector = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # 检测人脸
    faces = face_detector.detectMultiScale(gray)
    for x, y, w, h in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 255, 255), thickness=4)
    # 显示结果
    cv.imshow('result', img)

# 加载图像
img = cv.imread('k1.pgm')
if img is None:
    print("Error: 图像文件未找到或无法加载！")
    exit()

# 调用人脸检测函数
face_detect_demo()

# 等待按键并关闭窗口
cv.waitKey(0)
cv.destroyAllWindows()
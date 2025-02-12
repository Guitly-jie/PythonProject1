import cv2 as cv


def face_detect_demo(img):
    # 转换为灰度图像
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # 加载特征数据
    face_detector = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # 检测人脸
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4)
    for x, y, w, h in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 255, 255), thickness=2)
        cv.circle(img, center=(x + w // 2, y + h // 2), radius=w // 2, color=(0, 255, 255), thickness=2)
    # 显示结果


cap = cv.VideoCapture('video.mp4')
while True:
    flag, frame = cap.read()
    print('flag:', flag, 'frame.shape:', frame.shape)
    if not flag:
        break
    face_detect_demo(frame)
    if ord('F') == cv.waitKey(0):
        break
cv.destroyAllWindows()
cap.release()

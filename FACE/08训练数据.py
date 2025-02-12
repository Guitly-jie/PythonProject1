import os
import cv2
import sys
from PIL import Image
import numpy as np

def getImageAndLabels(path):
    facesSamples = []
    ids = []
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades +
                                          'haarcascade_frontalface_default.xml')
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img, 'uint8')
        faces = face_detector.detectMultiScale(img_numpy)
        id = int(os.path.split(imagePath)[1].split('.')[0])
        for x, y, w, h in faces:
            facesSamples.append(img_numpy[y:y + h, x:x + w])
            ids.append(id)
    return facesSamples, ids


if __name__ == '__main__':
    path = './data/jm/'
    faces, ids = getImageAndLabels(path)
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, np.array(ids))
    recognizer.write('train/trainer.yml')

import cv2
import numpy as np

def findBallons(img):

    bboxs = []
    img = cropImage(img, 0.1)
    img = preProcess(img)
    img = findContours(img)

    return img 


def cropImage(img, cropVal):
    h, w, c = img.shape
    img = img[100:h, 0:w]
    return img

def preProcess(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (5, 5), 5, 0)
    img = cv2.Canny(img, 50, 100)
    Kernel = np.ones((5, 5), np.unit8)
    img = cv2.dialte(img, kernel)

    return img

def findContours(img):

    h, w, c = img.shape
    imgContours = np.zeroes((w, h), np.unit8)
    contours, hierarchy = cv2.findContours(img, cv2.RETER_EXTERNAL, cv2.CHAIN_APPROX_SIMP)
    cv2.drawContours(img, contours, -1, (255, 0, 255), 2)

    # for cnt in contours:
    #     pass

    for i, cnt in enumerate(contours):
        area = cv2.contourArea(cnt)
        print(area)
        if area > 30000 and area < 250000:
            cv2.drawContours(imgContours, contours, i, (255, 0, 255), 2)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(imgContours, (x,y), (x+w, y+h), (0,255,0), 2)


    return imgContours


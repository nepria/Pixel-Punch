import cv2
from FindingBallons import*

img = cv2.imread("./test.jpg")

imgBallons = findBallons(img)
img = detectHit(img, bboxs)

imgBallons = cv2.resize(img, (0,0), None, 0.5, 0.5)

cv2.imshow("Output", imgBallons)
cv2.waitKey(0)
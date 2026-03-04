import cv2 as cv
import numpy as np

img = cv.imread("C://Users//Emmanuel//pictures//img//frutas.png")
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

rojoInf = np.array([0,150,100])
rojoSup = np.array([6,255,255])

mask = cv.inRange(hsv, rojoInf, rojoSup)
imgs= cv.bitwise_and(img, img, mask=mask)
cv.imshow("Mascara Binaria", mask)
cv.imshow("Resultado",imgs)
cv.waitKey(0)
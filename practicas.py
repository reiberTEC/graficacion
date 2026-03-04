import cv2 as cv
import numpy as np

def resize(img, scale=0.7):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    return cv.resize(img, (width, height))


img = cv.imread('C://Users//Emmanuel//pictures//img//frutas.png')

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

rojoInf = np.array([0, 150, 100])
rojoSup = np.array([6, 255, 255])

rojoInf2 = np.array([170, 150, 100])
rojoSup2 = np.array([180, 255, 255])

mask_rojo1 = cv.inRange(hsv, rojoInf, rojoSup)
mask_rojo2 = cv.inRange(hsv, rojoInf2, rojoSup2)

mask_rojo = mask_rojo1 +mask_rojo2
rojo = cv.bitwise_and(img, img, mask=mask_rojo)

verdeInf = np.array([40, 150, 100])
verdeSup = np.array([80, 255, 255])

mask_verde = cv.inRange(hsv, verdeInf, verdeSup)

verde = cv.bitwise_and(img, img, mask=mask_verde)

amainf = np.array([20, 100, 100])
amasup = np.array([35, 255, 255])

mask_amarillo = cv.inRange(hsv, amainf, amasup)
amarillo = cv.bitwise_and(img, img, mask=mask_amarillo)

cv.imshow("Original", resize(img))
cv.imshow("Rojo", resize(rojo))
cv.imshow("Verde", resize(verde))
cv.imshow("Amarillo", resize(amarillo))


cv.waitKey(0)
cv.destroyAllWindows()

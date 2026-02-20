import cv2 as cv
import numpy as np

img = cv.imread('C://Users//Emmanuel//pictures//img//frutas.png')

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#limite 1
rojoInf = np.array([0, 150, 100])
rojoSup = np.array([6, 255, 255])
#limite 2
rojoInf2 = np.array([170, 150, 100])
rojoSup2 = np.array([180, 255, 255])

mask_rojo1 = cv.inRange(hsv, rojoInf, rojoSup)
mask_rojo2 = cv.inRange(hsv, rojoInf2, rojoSup2)
mask_rojo = mask_rojo1 + mask_rojo2

amarilloInf = np.array([20, 150, 100])
amarilloSup = np.array([30, 255, 255])
mask_amarillo = cv.inRange(hsv, amarilloInf, amarilloSup)

verdeInf = np.array([40, 150, 100])
verdeSup = np.array([80, 255, 255])
mask_verde = cv.inRange(hsv, verdeInf, verdeSup)
panel = np.ones((5,5), np.uint8) 
#amarillo
limpia_amarillo = cv.morphologyEx(mask_amarillo, cv.MORPH_OPEN, panel)
limpia_amarillo = cv.morphologyEx(limpia_amarillo, cv.MORPH_CLOSE, panel)
contornos_amarillo, _ = cv.findContours(
    limpia_amarillo,
    cv.RETR_EXTERNAL,       
    cv.CHAIN_APPROX_SIMPLE
)
areas_amarillo = []
contador_amarillo = 0
AREA_MIN_AMARILLO = 500
for c in contornos_amarillo:
    area = cv.contourArea(c)
    if area > AREA_MIN_AMARILLO:
        contador_amarillo += 1
        areas_amarillo.append(area)

print("frutas amarillas:", contador_amarillo)

 

 # verde
limpia_verde = cv.morphologyEx(mask_verde, cv.MORPH_OPEN, panel)
limpia_verde = cv.morphologyEx(limpia_verde, cv.MORPH_CLOSE, panel)
contornos_verde, _ = cv.findContours(
    limpia_verde,
    cv.RETR_EXTERNAL,       
    cv.CHAIN_APPROX_SIMPLE
)
areas_verde = []
contador_verde = 0
AREA_MIN_VERDE = 1000
for c in contornos_verde:
    area = cv.contourArea(c)
    if area > AREA_MIN_VERDE:
        contador_verde += 1
        areas_verde.append(area)

print("frutas verdes:", contador_verde)

# rojas

limpia = cv.morphologyEx(mask_rojo, cv.MORPH_OPEN, panel)
limpia = cv.morphologyEx(limpia, cv.MORPH_CLOSE, panel)
contornos, _ = cv.findContours(
    limpia,
    cv.RETR_EXTERNAL,       
    cv.CHAIN_APPROX_SIMPLE
)


areas = []
contador = 0
AREA_MIN = 500   

for c in contornos:
    area = cv.contourArea(c)
    if area > AREA_MIN:
        contador += 1
        areas.append(area)


print("frutas rojas", contador)


rojo = cv.bitwise_and(img, img, mask=limpia)
cv.imshow("Original", img)
cv.imshow("Mask Rojo", limpia)
cv.imshow("Rojo", rojo)
cv.imshow("Mask Amarillo", limpia_amarillo)
cv.imshow("Mask Verde", limpia_verde)


cv.waitKey(0)
cv.destroyAllWindows()


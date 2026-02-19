import cv2 as cv
import numpy as np

img = cv.imread('C://Users//Emmanuel//pictures//img//frutas.png')

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#primer limite
rojoInf = np.array([0, 150, 100])
rojoSup = np.array([6, 255, 255])
#segundo limite
rojoInf2 = np.array([170, 150, 100])
rojoSup2 = np.array([180, 255, 255])

mask_rojo1 = cv.inRange(hsv, rojoInf, rojoSup)
mask_rojo2 = cv.inRange(hsv, rojoInf2, rojoSup2)
mask_rojo = mask_rojo1 + mask_rojo2

# Limpieza 
panel = np.ones((5,5), np.uint8)
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


print("Número total de regiones conectadas válidas:", contador)

for i, a in enumerate(areas):
    print(f"Fruta {i+1}: Área aproximada = {int(a)} píxeles")

# (Visualización opcional, NO parte del análisis)
rojo = cv.bitwise_and(img, img, mask=limpia)

cv.imshow("Mask Rojo", limpia)
cv.imshow("Rojo", rojo)

cv.waitKey(0)
cv.destroyAllWindows()


import cv2 as cv
import numpy as np

# Leer imagen
img = cv.imread('C://Users//Emmanuel//pictures//img//frutas.png')

# Convertir a HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# ================= ROJO =================
rojoInf = np.array([0, 150, 100])
rojoSup = np.array([6, 255, 255])

rojoInf2 = np.array([170, 150, 100])
rojoSup2 = np.array([180, 255, 255])

mask_rojo1 = cv.inRange(hsv, rojoInf, rojoSup)
mask_rojo2 = cv.inRange(hsv, rojoInf2, rojoSup2)

# Unir las dos máscaras del rojo
mask_rojo = cv.bitwise_or(mask_rojo1, mask_rojo2)

# Aplicar máscara del rojo
rojo = cv.bitwise_and(img, img, mask=mask_rojo)

# ================= VERDE =================
verdeInf = np.array([40, 150, 100])
verdeSup = np.array([80, 255, 255])

mask_verde = cv.inRange(hsv, verdeInf, verdeSup)

# Aplicar máscara del verde
verde = cv.bitwise_and(img, img, mask=mask_verde)

# ================= MOSTRAR =================
cv.imshow('Original', img)
cv.imshow('Rojo', rojo)
cv.imshow('Verde', verde)

cv.waitKey(0)
cv.destroyAllWindows()

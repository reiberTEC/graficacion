import cv2 as cv
import numpy as np

img = cv.imread('C:\\Users\\Emmanuel\\Desktop\\Documentos\\Programacion\\tareasGraficacion\\tareasGraficacion\\misiones\\vehiculo.jpg')

# Obtener tamaño real de la imagen
x, y, c = img.shape

# Crear imagen vacía con los mismos canales
img2 = np.zeros((x, y, 3), dtype=np.uint8)

dx, dy = 300, 200

for i in range(x):
    for j in range(y):

        new_i = i + dy
        new_j = j + dx

        if 0 <= new_i < x and 0 <= new_j < y:
            img2[new_i, new_j] = img[i, j]


#---------------------------------------------------------
M = np.float32([
    [1, 0, dx],
    [0, 1, dy]
])


open = cv.warpAffine(img, M, (img.shape[1], img.shape[0]))

#cv.imshow('img', img)
cv.imshow('Metodo RAW', img2)
cv.imshow("Metodo openCV", open)

cv.waitKey(0)
cv.destroyAllWindows()




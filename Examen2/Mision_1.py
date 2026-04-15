import cv2
import numpy as np


img = cv2.imread("C:\\Users\\Emmanuel\\Downloads\\m1_oscura.png", cv2.IMREAD_GRAYSCALE)
# con for

h, w = img.shape

img_int = img.astype(np.int32)

recuperado = np.zeros((h, w), dtype=np.int32)

# Paso A: multiplicar por 50
for y in range(h):
    for x in range(w):
        recuperado[y, x] = img_int[y, x] * 50


recuperado = np.clip(recuperado, 0, 255).astype(np.uint8)

cv2.imwrite("m1_recuperado_x50.png", recuperado)

# RAW
recuperado2 = recuperado.astype(np.int32)
for y in range(h):
    for x in range(w):
        recuperado2[y, x] = recuperado2[y, x] + 20

recuperado2 = np.clip(recuperado2, 0, 255).astype(np.uint8)

cv2.imwrite("m1_recuperado_x50_mas20.png", recuperado2)
cv2.imwrite("m1_vec_x50.png", vec)





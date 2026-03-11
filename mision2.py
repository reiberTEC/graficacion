import cv2 as cv
import numpy as np
import math

img = cv.imread('C:\\Users\\Emmanuel\\Desktop\\Documentos\\Programacion\\tareasGraficacion\\tareasGraficacion\\misiones\\qr_rotado.jpg', 0)


h, w = 500,500

img_rotada = np.zeros((h, w), dtype=np.uint8)

cx, cy = w // 2, h // 2

angulo = 45

theta = math.radians(angulo)

for i in range(h):
    for j in range(w):

        
        x = j - cx
        y = i - cy

        
        new_x = int(x * math.cos(theta) - y * math.sin(theta))
        new_y = int(x * math.sin(theta) + y * math.cos(theta))

        
        new_j = new_x + cx
        new_i = new_y + cy

        if 0 <= new_i < h and 0 <= new_j < w:
            img_rotada[new_i, new_j] = img[i, j]

cv.imshow("QR Original", img)
cv.imshow("img2", img_rotada)
cv.waitKey(0)
cv.destroyAllWindows()

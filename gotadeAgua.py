import cv2
import numpy as np
import math

# Tamaño ventana
ancho = 600
alto = 600

# Centro
cx = ancho // 2
cy = alto // 2

# Parámetros
amplitud = 20
frecuencia = 0.2
tiempo = 0

while True:
    img = np.zeros((alto, ancho, 3),np.uint8)

    for x in range(ancho):
        for y in range(alto):

            # Distancia al centro
            r = math.sqrt((x - cx)**2 + (y - cy)**2)

            # Onda radial
            z = amplitud * math.sin(frecuencia * r - tiempo)

            # Convertimos a intensidad
            color = int(127 + z * 5)

            # Limitamos valores
            color = max(0, min(255, color))

            img[y, x] = (color, color, 255)

    cv2.imshow("Gota en el agua", img)

    tiempo += 0.3

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
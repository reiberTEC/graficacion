import cv2
import numpy as np
import math

# Tamaño de la ventana
ancho = 800
alto = 400

# Parámetros de la onda
amplitud = 50
frecuencia = 0.20
fase = 0.1

while True:
    # Imagen negra
    img = np.zeros((alto, ancho, 3), dtype=np.uint8)

    # Centro vertical
    centro_y = alto // 2

    # Dibujar la onda seno punto a punto
    for x in range(ancho):
        y = int(centro_y + amplitud * math.sin(frecuencia * x + fase))
        cv2.circle(img, (x, y), 1, (0, 255, 0), -1)

    # Mostrar imagen
    cv2.imshow("Onda Seno Animada", img)

    # Incrementar fase para animar
    fase += 0.1

    # Salir con ESC
    if cv2.waitKey(30) == 27:
        break

cv2.destroyAllWindows()
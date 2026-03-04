import cv2 as cv
import numpy as np

# Crear ventana
width = 500
height = 500

# Posición inicial pelota
x = 250
y = 250
radio = 10

# Velocidad horizontal
vx = 5

while True:

    # Fondo blanco
    img = np.ones((height, width, 3), np.uint8) * 255

    # ---- MOVER PELOTA ----
    x = x + vx

    # ---- DETECTAR COLISIÓN ----
    # Paleta izquierda en x = 10
    if x - radio <= 15:
        vx = -vx

    # Paleta derecha en x = 490
    if x + radio >= 485:
        vx = -vx

    # ---- DIBUJAR PALLETAS ----
    cv.line(img, (10,100), (10,300), (0,0,0), 5)
    cv.line(img, (490,100), (490,300), (0,0,0), 5)

    # ---- DIBUJAR PELOTA ----
    cv.circle(img, (x,y), radio, (0,0,0), -1)

    # Mostrar
    cv.imshow("Ping Pong Simple", img)

    # Espera y salir con ESC
    key = cv.waitKey(20)
    if key == 27:
        break

cv.destroyAllWindows()
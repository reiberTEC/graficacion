import cv2
import numpy as np
import math

img = np.zeros((600, 600, 3), dtype=np.uint8)

cx, cy = 300, 300
r = 100
k = 10
vueltas = 6
alpha = math.radians(55) 
theta = 0
while theta <= vueltas * 2 * math.pi:

    # Coordenadas 3D originales
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    z = k * theta

    # Rotación alrededor del eje X
    y_rot = y * math.cos(alpha) - z * math.sin(alpha)
    z_rot = y * math.sin(alpha) + z * math.cos(alpha)

    # Proyección simple a 2D (ignoramos z_rot para perspectiva)
    px = int(cx + x)
    py = int(cy + y_rot)

    if 0 <= px < 600 and 0 <= py < 600:
        img[py, px] = (0, 255, 0)

    theta += 0.01

    cv2.imshow("Helice Inclinada", img)
    cv2.waitKey(1)
    
    
cv2.destroyAllWindows()
import cv2 as cv
import numpy as np
import math
cx, cy = 250, 250
r=100
img = np.ones((500,500), np.uint8)

for theta in range(0, 360):
        rad = math.radians(theta)
        x = int(cx + r * math.cos(rad))
        y = int(cy + r * math.sin(rad))
        img[y, x] = (0, 255, 0)





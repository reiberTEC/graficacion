import cv2 as cv 
import numpy as np

img = np.ones((400,400),np.uint8)*255
img[50:100, 100:130]=0
img[50:100, 200:230] = 0 

h, k = 165, 210   # centro
r = 100           # radio

for y in range(400):
    for x in range(400):
        if (x - h)**2 + (y - k)**2 <= r**2:
            img[y, x] = 0


cv.imshow("imagen",img)
cv.waitKey(0)
cv.destroyAllWindows

""""
img[50:100, 100:130]=0
img[50:100, 200:230] = 0

img[120:180, 70:320] = 0
"""
import cv2 as cv
import numpy as np 

img = np.ones((500,500), np.uint8)*255
#(imagen,punto de inicio, punto final, color del rectangulo en BGR, y si esta relleno o no ) 
cv.rectangle(img, (10,10), (200,100), (34,56,100), 1)
cv.rectangle(img, (49,49), (251,151), (0 ,0 ,0), 1)

cv.rectangle(img, (50,50), (250, 149), (255,255,255), -1)
cv.line(img, (10,10), (49,49), (23, 244, 144), 1)
cv.line(img, (210,210), (300,199), (23, 244, 144), 1)

#cv.circle(img, (255,255), 1, (23, 43, 144), -1 )
#cv.line(img, (255,255), (200,100), (23, 244, 144), 4)
"""
for i in range(400):
    cv.circle(img, (i,i), i , (255, 0, 0), -1 )
    cv.rectangle(img, (10+i,10), (200,100), (34,56,100), -1)

    cv.imshow('img', img)
    #img = np.ones((500,500,3), np.uint8)*150 
"""

cv.waitKey(30)
    




cv.imshow('img', img)
cv.waitKey(0)
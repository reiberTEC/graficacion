""""
import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    ret, img= cap.read()
    r,g,b = cv.split(img)
    cv.imshow('videor', img)
    cv.imshow('videog', r)
    cv.imshow('videob', g)
    cv.imshow('video', b)
    k = cv.waitKey(1)
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()
"""

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
ret, img= cap.read()
x,y,z = img.shape
fondo = np.zeros((x,y), np.uint8)
#cv.imshow('fondo', fondo)
while True:
    if(ret):
        r,g,b = cv.split(img)
        
        mr = cv.merge([fondo,fondo,r])
        mg = cv.merge([fondo,g,fondo])
        mb = cv.merge([b,fondo,fondo])
        
        nv= cv.merge([b,g,r])
        #cv.imshow('videor', img)
        cv.imshow('videog', mr)
        cv.imshow('videob', mg)
        cv.imshow('video', mb)
        cv.imshow('video', nv)
    else:
        print("No se pudo abrir la cámara")
        break
    k = cv.waitKey(1)
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()





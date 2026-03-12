import cv2 as cv
import numpy as np
import math
'''
 #--------------------MISION 1------------------------------------------------------------------------------------------------------------------------------------------------------
img = cv.imread('C:\\Users\\Emmanuel\\Desktop\\Documentos\\Programacion\\tareasGraficacion\\tareasGraficacion\\misiones\\m1_oscura.png',0)    
alto, ancho = img.shape
imgNueva = np.zeros((alto, ancho), dtype=np.uint8)
#---------------MODO RAW----------------------------------------------------------------------------------------------------------------------------------
for i in range(alto):
    for j in range(ancho):
        a = img[i][j] * 50
        a = np.clip(a, 0, 255)
        imgNueva[i][j] = a
#---------------MODO openCV----------------------------------------------------------------------------------------------------------------------------------
ocv = img * 50
ocv = np.clip(ocv, 0, 255).astype(np.uint8)


cv.imshow("openCV", ocv)
cv.imshow("RAW", imgNueva)
cv.waitKey(0)
cv.destroyAllWindows()
'''
mitad1 = cv.imread('C:\\Users\\Emmanuel\\Desktop\\Documentos\\Programacion\\tareasGraficacion\\tareasGraficacion\\misiones\\m2_mitad1.png',0)
mitad2 = cv.imread('C:\\Users\\Emmanuel\\Desktop\\Documentos\\Programacion\\tareasGraficacion\\tareasGraficacion\\misiones\\m2_mitad2.png',0)

lienzo = np.zeros((400,400), dtype=np.uint8)

h1, w1 = mitad1.shape
h2, w2 = mitad2.shape


# ----------------------
# TRASLACION MANUAL
# ----------------------

tx = -50
ty = -50

trasladada = np.zeros((h1,w1), dtype=np.uint8)

for i in range(h1):
    for j in range(w1):

        new_x = j + tx
        new_y = i + ty

        if 0 <= new_x < w1 and 0 <= new_y < h1:
            trasladada[new_y,new_x] = mitad1[i,j]

# colocar mitad1
lienzo[0:h1,0:w1] = trasladada


# ----------------------
# ROTACION MANUAL
# ----------------------

rotated_img = np.zeros((h2,w2), dtype=np.uint8)

cx = w2 // 2
cy = h2 // 2

angle = 180
theta = math.radians(angle)

for i in range(h2):
    for j in range(w2):

        new_x = int((j - cx)*math.cos(theta) - (i - cy)*math.sin(theta) + cx)
        new_y = int((j - cx)*math.sin(theta) + (i - cy)*math.cos(theta) + cy)

        if 0 <= new_x < w2 and 0 <= new_y < h2:
            rotated_img[new_y,new_x] = mitad2[i,j]

# colocar mitad2
lienzo[200:200+h2,0:w2] = rotated_img



cv.imshow("mitad1", lienzo)
#cv.imshow("mitad1", mitad1)
#cv.imshow("mitad2", mitad2)
cv.waitKey(0)
cv.destroyAllWindows()


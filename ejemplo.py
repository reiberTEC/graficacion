import cv2 as cv 
import numpy as np


# Crear una imagen en negro de 400x400 píxeles
#es una matriz de unos y lo puedo multiplicar por algun valor de 1 al 255
img2 = np.ones((400,400), np.uint8)*150

# Cargar una imagen desde un archivo
imagen = cv.imread('C:\\Users\\Emmanuel\\Desktop\\ejemplo.jpg', 1)
#con esto se carga las caracteristicas de la imagen, como el numero de filas, columnas y canales
print(imagen.shape)

#esta es de la imagen cargada
cv.imshow('img', imagen)
#esta es de la imagen de 400x400
cv.imshow('img2', img2 )

cv.waitKey(0)

cv.destroyAllWindows()
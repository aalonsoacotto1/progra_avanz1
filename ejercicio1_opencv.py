import cv2
import numpy as np 

#leer imagen de folder en opencv
img = cv2.imread('img1.jpg')
#mostrar imagen en pantalla python opencv
cv2.imshow('Mostrar Imagen OPENCV', img)

#COLOR SPACES
# ACTUAL RGB(BGR)
# PASAR A HSV
# 0 0 0 ... 0 0 8
color_bajo = (1, 190, 200)
color_alto = (18, 255, 255)

# VERDES
# AMARILLOS
# ROJOS

imagen_salida = img.copy()
imagen_salida_rgb = cv2.cvtColor(imagen_salida, cv2.COLOR_BGR2RGB)
imagen_salida_hsv = cv2.cvtColor(imagen_salida_rgb, cv2.COLOR_RGB2HSV)
mascara = cv2.inRange(imagen_salida_hsv, color_bajo, color_alto)
resultado = cv2.bitwise_and(imagen_salida, imagen_salida, mask=mascara)
cv2.imshow('PROCESADO POR OPENCV', mascara)

cv2.waitKey(0)
cv2.destroyAllWindows()
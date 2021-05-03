import cv2
import numpy as np 

imagen = cv2.imread('img1.jpg')

cv2.imshow("IMAGEN", imagen)

hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

alto = np.array([125, 250, 210])
bajo = np.array([95, 200, 140])

mascara = cv2.inRange(hsv, bajo, alto)
cv2.imshow("Mascara", mascara)

cv2.waitKey(0)
cv2.destroyAllWindows()
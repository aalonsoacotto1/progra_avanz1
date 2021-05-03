import cv2
import numpy as np 

image = cv2.imread('img_tarea.png')
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("IMG", image)

circulos = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)

if circulos is not None:
	circulos = np.round(circulos[0, :]).astype("int")
	for (x, y, r) in circulos:
		cv2.circle(output, (x, y), r, (0, 255, 0), 4)
		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

	cv2.imshow("SALIDA", output)
	cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows()
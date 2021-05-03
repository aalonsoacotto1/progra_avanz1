# importing the module
import cv2
import numpy as np

light_color = 0
dark_color = 0

# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):

	global light_color, dark_color

	# checking for left mouse clicks
	if event == cv2.EVENT_RBUTTONDOWN:
		print("***** BOTON DERECHO *****")
		print(x, ' ', y)
		font = cv2.FONT_HERSHEY_SIMPLEX
		b = img[y, x, 0]
		g = img[y, x, 1]
		r = img[y, x, 2]
		print("R:{}".format(r))
		print("G:{}".format(g))
		print("B:{}".format(b))
		color_arr = np.uint8([[[b,g,r ]]])  
		color_hsv = cv2.cvtColor(color_arr, cv2.COLOR_BGR2HSV)
		dark_color = color_hsv 
		print("HSV COLOR ALTO: {}".format(color_hsv))

		output = img.copy()

		output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
		hsv_output = cv2.cvtColor(output, cv2.COLOR_RGB2HSV)
		mask = cv2.inRange(hsv_output, light_color, dark_color)
		result = cv2.bitwise_and(output, output, mask=mask)

		cv2.imshow("OpenCV Image Processing", result)

	# checking for right mouse clicks	
	if event==cv2.EVENT_LBUTTONDOWN:
		print("***** BOTON IZQUIERDO *****")
		print(x, ' ', y)
		font = cv2.FONT_HERSHEY_SIMPLEX
		b = img[y, x, 0]
		g = img[y, x, 1]
		r = img[y, x, 2]
		print("R:{}".format(r))
		print("G:{}".format(g))
		print("B:{}".format(b))
		color_arr = np.uint8([[[b,g,r ]]])  
		color_hsv = cv2.cvtColor(color_arr, cv2.COLOR_BGR2HSV)
		light_color = color_hsv 
		print("HSV COLOR BAJO: {}".format(color_hsv))


# driver function
if __name__=="__main__":

	# reading the image
	img = cv2.imread('img1.jpg', 1)

	# displaying the image
	cv2.imshow('image', img)

	# setting mouse hadler for the image
	# and calling the click_event() function
	cv2.setMouseCallback('image', click_event)

	# wait for a key to be pressed to exit
	cv2.waitKey(0)

	# close the window
	cv2.destroyAllWindows()

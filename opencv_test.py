import cv2

image = cv2.imread('img1.jpg')

# Extracting the height and width of an image
h, w = image.shape[:2]
# Displaying the height and width
print("Height = {},  Width = {}".format(h, w))

output = image.copy()

output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
hsv_output = cv2.cvtColor(output, cv2.COLOR_RGB2HSV)
light_orange = (1, 190, 200)
dark_orange = (18, 255, 255)
mask = cv2.inRange(hsv_output, light_orange, dark_orange)
result = cv2.bitwise_and(output, output, mask=mask)
  
# Using the rectangle() function to create a rectangle.
#rectangle = cv2.rectangle(output, (50, 50), (100, 100), (0, 0, 0), 2)

cv2.imshow("OpenCV Image Reading", image)
cv2.imshow("OpenCV Image Processing", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
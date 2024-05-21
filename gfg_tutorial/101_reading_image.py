# Importing the OpenCV library
import cv2
# Reading the image using imread() function
image = cv2.imread('../img/road.jpg')
# print(cv2.__version__)


# # Extracting the height and width of an image
# h, w = image.shape[:2]
# # Displaying the height and width
# print("Height = {}, Width = {}".format(h, w))
#
#
# # OpenCV arranges the channels in BGR order. So the 0th value will correspond to the Blue pixel and not the Red.
# # Extracting RGB values.
# # Here we have randomly chosen a pixel
# # by passing in 100, 100 for height and width.
# (B, G, R) = image[100, 200]
#
# # Displaying the pixel values
# print("R = {}, G = {}, B = {}".format(R, G, B))
#
# # We can also pass the channel to extract
# # the value for a specific channel
# B = image[100, 200, 0]
# print("B = {}".format(B))
#
#
# # We will calculate the region of interest
# # by slicing the pixels of the image
# # a rectangular area from pixel coordinates (100, 200) (top-left corner) to (499, 699) (bottom-right corner, non-inclusive).
# roi = image[100 : 500, 200 : 700]
# cv2.imshow("ROI", roi)
# # waits for a key press before closing the window.
# cv2.waitKey(0)
#
# # resize() function takes 2 parameters,
# # the image and the dimensions
# resize = cv2.resize(image, (500, 500))
# cv2.imshow("Resized Image", resize)
# cv2.waitKey(0)
#
#
# # Calculating the ratio
# ratio = 800 / w
# # Creating a tuple containing width and height
# dim = (800, int(h * ratio))
# # Resizing the image
# resize_aspect = cv2.resize(image, dim)
# cv2.imshow("Resized Image", resize_aspect)
# cv2.waitKey(0)
#
#
# We can draw a rectangle on the image using rectangle() method. It takes in 5 arguments:
# Image
# width and height of the rectangle itself
# Top-left corner co-ordinates
# Color (in BGR format)
# Line width

# We are copying the original image
output = image.copy()

# Adjust rectangle coordinates based on your image dimensions
rectangle = cv2.rectangle(output, (500, 600), (200, 200), (255, 0, 0), 2)  # Blue rectangle with thickness 2

# Adding the text using putText() function
# using the putText() method of OpenCV module. It takes in 7 arguments:
# Image
# Text to be displayed
# Bottom-left corner co-ordinates, from where the text should start
# Font
# Font size
# Color (BGR format)
# Line width
text = cv2.putText(output, 'OpenCV Demo', (200, 550),
                cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 2)

# Display the image with the rectangle
cv2.imshow("Image with Rectangle", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
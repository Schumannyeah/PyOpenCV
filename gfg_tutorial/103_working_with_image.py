#import cv2, numpy and matplotlib libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("../img/cherry.jpg")
#Displaying image using plt.imshow() method
# See the difference in colors of images read by cv2 and matplotlib library.
# Because cv2 uses BGR color format and matplotlib uses RGB color format.
plt.imshow(img)

#hold the window
plt.waitforbuttonpress()
plt.close('all')

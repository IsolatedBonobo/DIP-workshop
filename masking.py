import cv2 as cv
import numpy as np 

# masking of a image 
img = cv.imread("MaskImage.jpg")
cv.imshow("image", img)
# converting image color into hsv 

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# bounding yellow color reigon 
lower_yellow = np.array([15, 50, 180])
upper_yellow = np.array([40, 255, 255])

# creating mask of it 
mask = cv.inRange(hsv, lower_yellow, upper_yellow)


result = cv.bitwise_and(img, img, mask=mask)

cv.imshow("Result", result)
cv.waitKey(0)


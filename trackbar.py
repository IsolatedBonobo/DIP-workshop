import cv2 as cv 
import numpy as np
# cv.namedWindow('window)name')
# cv.crateTrackbar('track_bar name', 'window name; , start value, maxvalue, onChangeFunction)

# cv.getTrackbarPos('trackbarName', 'window name')

def Onchange(a):
    pass

img = np.zeros((512, 512, 3), np.uint8)

cv.namedWindow("window1")
cv.resizeWindow("window1", 600, 50)

cv.createTrackbar("trackbar1", "window1", 0, 255, Onchange)
cv.createTrackbar("trackbar2", "window1", 0, 255, Onchange)
cv.createTrackbar("trackbar3", "window1", 0, 255, Onchange)

while True:
    value = cv.getTrackbarPos("trackbar1", "window1")
    value2 = cv.getTrackbarPos("trackbar2", "window1")
    value3 = cv.getTrackbarPos("trackbar3", "window1")
    print(value, value2, value3)
    img [:]= [value, value2, value3]
    cv.imshow("window1", img)
    if cv.waitKey(1) == 27:
        break
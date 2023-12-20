import cv2 as cv
import numpy as np 

# cv2.line(img, start, end, color, thickness)

img = np.zeros((512, 512, 3), np.uint8)

cv.line(img, (0,0), (511, 511),(0, 255, 0), 3 )
# cv.waitKey(0)
font = cv.FONT_HERSHEY_SIMPLEX

cv.putText(img, "OpenCV", (150, 255), font, 2, (0, 255, 0), 4)
# cirles in opencv
# cv2.cirle(img, center, radius, color, thickness)

# img2 = np.zeros((512, 512, 3), np.uint8)
cv.circle(img, (255,255), 180,(255, 255, 0), 3 )
# cv.waitKey(0)


# rectangle cv2.rectangle(img, top_left, bottom_right, color, thcikness)

# img3 = np.zeros((512, 512, 3), np.uint8)
cv.rectangle(img, (100,100), (400, 400),(255, 255, 0), 3 )

cv.imshow("line",img)
# cv.imshow("circle",img)
# cv.imshow("rectangle",img)
cv.waitKey(0)


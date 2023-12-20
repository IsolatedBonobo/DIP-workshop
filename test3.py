import cv2 

image = cv2.imread(".\8.jpg", cv2.IMREAD_GRAYSCALE)
# image = cv2.imread(".\8.jpg", cv2.IMREAD_UNCHANGED)

cv2.imshow("Tanjuro Kanado", image )

cv2.waitKey(50)
# cv2.destroyAllWindows()
cv2.imwrite('out8_gray.jpg', image)




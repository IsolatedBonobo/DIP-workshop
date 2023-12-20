import cv2 

img_path = ".\9.jpg"

img = cv2.imread(img_path)

print(img)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

img = cv2.imread("RedColor.png")

# print(img.shape)
# print(img.size)
# print(img.dtype)

# cv2.imshow("original", img)
# px = img[100, 100]
# print(px)

# img[100, 100] = [255, 0, 0]
# img[100:200, 300:400] = [255, 0, 0];
# print(img)
# cv2.imshow("original", img)
# cv2.waitKey(0)


# this is to import text at required coordinates 

# font = cv2.FONT_HERSHEY_SIMPLEX
# white = (255, 255, 255)
# cv2.putText(img, "Red color Image", (100, 100),font,4, white,4)
# cv2.imshow("updated", img)
# cv2.waitKey(0)


# img = cv2.imread("FerrariImage.jpg")
# croppedimage = img[0:600, 0:600]
# cv2.imshow("original image", croppedimage)
# cv2.waitKey(0)

# combimnig two image (addition)
# img1 = cv2.imread('Add1.jpg')
# img2 = cv2.imread('Add2.jpg')
# cv2.imshow("img1", img1)
# cv2.imshow("img2", img2)
# weightedsum = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

# cv2.imshow("weighted image is", weightedsum)

# if cv2.waitKey(0) & 0xff == 27:
#     cv2.destroyAllWindows()

# subtraction of image 
# img1 = cv2.imread('Add1.jpg')
# img2 = cv2.imread('Add2.jpg')
# cv2.imshow("img1", img1)
# cv2.imshow("img2", img2)
# weightedsum = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

# cv2.imshow("weighted image is", weightedsum)

# if cv2.waitKey(0) & 0xff == 27:
#     cv2.destroyAllWindows()

image1 = cv2.imread("Bit1.png")
image2 = cv2.imread("Bit2.png")

dest_and = cv2.bitwise_and(image2, image1, mask = None)
dest_or = cv2.bitwise_or(image2, image1, mask = None)
dest_xor = cv2.bitwise_xor(image2, image1, mask = None)
cv2.imshow("bit wise", dest_and)

cv2.imshow("bit wise", dest_or)

cv2.imshow("bit wise", dest_xor)
cv2.waitKey(0)

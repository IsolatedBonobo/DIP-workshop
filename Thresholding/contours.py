import cv2
import numpy as np

def nothing(x):
    pass

def createTrackbar():
    cv2.namedWindow("thresholding")
    cv2.createTrackbar("Hl","thresholding", 0, 255, nothing)
    cv2.createTrackbar("Sl","thresholding", 0, 255, nothing)
    cv2.createTrackbar("Vl","thresholding", 0, 255, nothing)
    cv2.createTrackbar("Hu","thresholding", 0, 255, nothing)
    cv2.createTrackbar("Su","thresholding", 0, 255, nothing)
    cv2.createTrackbar("Vu","thresholding", 0, 255, nothing)
    
    # Resize the window to a smaller size (e.g., 400x300 pixels)
    cv2.resizeWindow("thresholding", 350, 100)

# Load the image
img = cv2.imread('Thresholding\WhatsApp Image 2023-09-17 at 11.42.44.jpeg')

# Function to find and draw centroids on the image
def find_and_draw_centroids(img, contours):
    for contour in contours:
        # Calculate the moments of the contour
        M = cv2.moments(contour)
        
        if M["m00"] != 0:
            # Calculate the centroid coordinates
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            
            # Draw a circle at the centroid
            cv2.circle(img, (cX, cY), 5, (0, 0, 255), -1)  # Red circle
        
    return img

# Check if the image was loaded successfully
if img is None:
    print("Error: Image not loaded.")
else:
    createTrackbar()

    while True:
        Hl = cv2.getTrackbarPos("Hl", "thresholding")
        Sl = cv2.getTrackbarPos("Sl", "thresholding")
        Vl = cv2.getTrackbarPos("Vl", "thresholding")
        Hu = cv2.getTrackbarPos("Hu", "thresholding")
        Su = cv2.getTrackbarPos("Su", "thresholding")
        Vu = cv2.getTrackbarPos("Vu", "thresholding")

        u = np.array([Hu, Su, Vu])
        l = np.array([Hl, Sl, Vl])

        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        thresh_img = cv2.inRange(img_hsv, l, u)

        cv2.imshow("thresh_image", thresh_img)

        image_copy = img.copy()


        contours, _ = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        print(contours)

        # Find and draw centroids
        image_with_centroids = find_and_draw_centroids(image_copy, contours)
        

        cv2.drawContours(image_copy, contours, -1, (255, 0, 255), 1)
        cv2.imshow("originalimage", image_copy)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cv2.destroyAllWindows()
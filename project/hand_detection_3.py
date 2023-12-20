import cv2
import numpy as np
from utils.hand_detection import HandDetection
from utils.Ball import Ball
from utils.collision import collision
from utils.constants import WIDTH, HEIGHT, ball_radius, PADDLE_WIDTH, PADDLE_HEIGHT, WHITE, speed_increment

# Initialize video capture
vid = cv2.VideoCapture(0)
# Create an instance of HandDetection
hand_detection = HandDetection()

class Paddle:
    def _init_(self, x, y, width, height, paddle_color):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.paddle_color = paddle_color
        self.width = width
        self.height = height

    def draw(self, frame):
        cv2.rectangle(
            frame,
            (int(self.x - self.width // 2), int(HEIGHT - self.height)),
            (int(self.x + self.width // 2), int(HEIGHT)),
            self.paddle_color,
            -1,
        )

    def move(self, frame, centroid_x):
        self.x = centroid_x

        if self.x - self.width//2 < 0:
            self.x = self.width//2
        if self.x + self.width//2 > WIDTH:
            self.x = WIDTH - self.width//2
        # self.draw(frame)

    def reset(self):
        self.x = self. original_x
        self.y = self.original_y

def masking(img):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 33, 81])
    upper = np.array([42, 193, 140])
    mask = cv2.inRange(imgHSV, lower, upper)
    return mask
# Function to draw pieces in the main function
def draw_pieces(frame, paddle, ball):
    paddle.draw(frame)
    ball.draw(frame)

def main():
    paddle = Paddle(WIDTH//2, HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT, WHITE)
    ball = Ball(WIDTH//2, HEIGHT//2, ball_radius, 5, WHITE)
    while vid.isOpened():
        _, frame = vid.read()
        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, (WIDTH, HEIGHT))
        mask = masking(frame)
        threshImg = hand_detection.threshold(mask)
        mask_cleaned = hand_detection.clean_image(threshImg)
        contours = hand_detection.find_contours(mask_cleaned)
        frame = cv2.drawContours(frame, contours, -1, (255, 0, 0), 2)
        max_cntr = hand_detection.max_contour(contours)
        (centroid_x, centroid_y) = hand_detection.centroid(max_cntr)
        frame = cv2.circle(frame, (centroid_x, centroid_y), 5, (255, 255, 0),
                           -1)
        paddle.move(frame, centroid_x)
        draw_pieces(frame, paddle, ball)

        cv2.imshow('Hand Gesture Slider', frame)

        key = cv2.waitKey(10)

        if key == ord('q'):
            break

    # Release the video capture and close all OpenCV windows
    vid.release()
    cv2.destroyAllWindows()


if _name_ == '__main__':
    main()
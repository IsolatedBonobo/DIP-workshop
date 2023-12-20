import cv2 as cv
video_reader = cv.VideoCapture(0)

while True:
    success, frame  = video_reader.read()
    if not success :
        break

    cv.imshow("My Video", frame)
    key = cv.waitKey(1)

    if key == ord('q') or key == ord('Q'):
        break

video_reader.release()
cv.destroyAllWindows()

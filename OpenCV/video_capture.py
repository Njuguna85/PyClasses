import cv2
import time

video = cv2.VideoCapture(0)
# 0 is the index of my webcam
number_of_frames = 1
while True:
    number_of_frames = number_of_frames+1
    check, frame = video.read()
    #   check is a boolean field and frame is the first
    #   image captured
    print(check)
    print(frame)

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Capturing", gray_frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print(number_of_frames)
video.release()

cv2.destroyAllWindows()

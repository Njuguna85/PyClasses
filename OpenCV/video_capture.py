import cv2
import time

video = cv2.VideoCapture(0)
# 0 is the index of my webcam

check, frame = video.read()

print(check)
print(frame)

time.sleep(3)
# pausing the capture for 5 seconds before releasing it

cv2.imshow("Capturing", frame)
cv2.waitKey(0)
video.release()

cv2.destroyAllWindows()

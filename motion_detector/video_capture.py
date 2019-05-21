import cv2
from datetime import datetime
import pandas

first_frame = None
status_list = [None, None]
#   set the first item  and second one to be none
time_stamp = []
df = pandas.DataFrame(columns=["Start", "End"])

video = cv2.VideoCapture(0)
# 0 is the index of my webcam
while True:

    check, frame = video.read()
    #   check is a boolean field and frame is the first
    #   image captured

    status = 0
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #   converting to a gray image
    gray_frame = cv2.GaussianBlur(gray_frame, (9, 9), 0)
    #   applying gaussian blur inorder to remove noise to
    #   the image and thus improve accuracy
    #   (9,9) tuple is the parameters of blurreness
    #   0 is the standard deviation

    if first_frame is None:
        first_frame = gray_frame
        continue
        #   continue will cause the loop to go back to the start
        #   of the loop and will thus cause it not to  conitue
        #   with the rest of the code
        #   This is effective as the next iteration will have the
        #   first_frame already occupied and not none

    delta_frame = cv2.absdiff(first_frame, gray_frame)

    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    #   30 is the threshold limit
    #   255 is the color we assign to values that are more than 30  (white color)
    #   we use THRESH_BINARY method
    #   we then access the second value of the tuple

    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (cnts, _) = cv2.findContours(thresh_frame.copy(),
                                 cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1

        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    status_list.append(status)

    if status_list[-1] == 1 and status_list[-2] == 0:
        time_stamp.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        time_stamp.append(datetime.now())

    cv2.imshow("Gray Frame", gray_frame)
    cv2.imshow("Delta frame", delta_frame)
    cv2.imshow("Thresh Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)
    #   1 milisecond
    if key == ord('q'):
        #   once we press the q key it will break
        if status == 1:
            time_stamp.append(datetime.now())
        break


print(time_stamp)


for i in range(0, len(time_stamp), 2):
    df = df.append(
        {"Start": time_stamp[i], "End": time_stamp[i+1]}, ignore_index=True)
# the above loop will loop over 2 two step time_stamps
# we append two successive time_stamps to the dataframe and set the ignore_index to true
# remember that the status is 0 when the background has no
# object in motion and is 1 when there is an object thus those two time_stamps are recorded as done earlier

df.to_csv("Time_Stamp.csv")

video.release()

cv2.destroyAllWindows()

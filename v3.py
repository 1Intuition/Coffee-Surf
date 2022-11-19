from imutils.video import VideoStream
from imutils.video import FPS
import argparse
import imutils
import time
import cv2
from datetime import datetime, time
import numpy as np
import time as time2




HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# ap = argparse.ArgumentParser()
# ap.add_argument("-v", "--video", help="path to the video file")
# ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
# ap.add_argument("-t", "--tracker", type=str, default="csrt", help="OpenCV object tracker type")
# args = vars(ap.parse_args())




def detect(frame):
    bounding_box_coordinates, weights = HOGCV.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.03)

    person = 1
    for x, y, w, h in bounding_box_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f'person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        person += 1

    cv2.putText(frame, 'Status : Detecting ', (40, 40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.putText(frame, f'Total Persons : {person - 1}', (40, 70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.imshow('preview', frame)
    return frame


if __name__ == "__main__":

    cv2.namedWindow("preview")
    video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if video.isOpened():  # try to get the first frame
        rval, frame = video.read()
    else:
        rval = False

    while rval:
        # cv2.imshow("preview", frame)
        detect(frame)
        rval, frame = video.read()
        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            break

    video.release()
    cv2.destroyWindow("preview")
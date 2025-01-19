import cv2 as cv
import numpy as np
from util import get_limits
from PIL import Image


purple = [128, 0, 128] # yellow in BGR colorspace

cap = cv.VideoCapture(0)
# opens web-cam
while True:
    ret, frame = cap.read()
    hsvImage = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    purple_hsv = cv.cvtColor(np.uint8([[purple]]), cv.COLOR_BGR2HSV)[0][0]
    lowerLimit, upperLimit = get_limits(color=purple_hsv)

    lowerLimit, upperLimit = get_limits(color=purple)
    mask = cv.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask) # converting opencv image which is in the form of a numpy array to pillow

    bbox = mask_.getbbox()
    print(bbox)

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
        cv.putText(frame, "Purple Object", (x1, y1 - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv.imshow('Frame', frame)

    if cv.waitKey(1) & 0xFF==ord('l'):
        break

cap.release()
cv.destroyAllWindows()

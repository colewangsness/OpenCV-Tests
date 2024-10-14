#This code example is tuned to United States sized 12oz soda can. Project was built using a logitech C920 webcam in well-lit office environment.

import cv2
import cv2 as cv
import numpy as np

delay = 1
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) #CAP_DSHOW Flag required for Windows

while True:
    ret, frame = cap.read()
    img = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    img = cv2.medianBlur(img, 5)
    cimg = frame

    circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT_ALT, 1.5, 150,param1=300, param2=0.9, minRadius=80, maxRadius=95)
    # Tuned Math: Gradient ALT Mode measuring perfectness of circles, DP set to 1.5, param2 = 90%

    #debug
    #cv2.imshow('Video Feed', img)
    #key = cv2.waitKey(1)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            counter = (int(circles.size/3))
            # draw the outer circle
            cv.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
            center = (i[0], i[1])
            cv2.putText(cimg, "Soda Can", center, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            if counter > 2 and counter < 4:
                cv2.putText(cimg, "Ship It!", (250,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            elif counter > 3:
                cv2.putText(cimg, "TOO MANY!", (250, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            elif counter < 3:
                cv2.putText(cimg, "Not Enough!", (250, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (105, 105, 105), 2)
    else:
        cv2.putText(cimg, "No Objects Present", (200,200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Video Feed', cimg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

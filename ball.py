import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
prevCircle = None
dist = lambda x1,x2,y1,y2: (x1-x2)**2 + (y1-y2)**2

while True:
    ret, frame = cap.read()
    if not ret: break;

    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blurFrame = cv.GaussianBlur(grayFrame, (17,17), 0)

    circles = cv.HoughCircles(blurFrame, cv.HOUGH_GRADIENT, 1.2, 400,
                              param1=100, param2=40, minRadius=50, maxRadius=150)

    if circles is not None:
        circles = np.uint16(np.around(circles))

        for circle in circles[0, :]:
            print(circle)
            cv.circle(frame, (circle[0], circle[1]), 1, (0,100,100), 3)
            cv.circle(frame, (circle[0], circle[1]), circle[2], (255,0,255), 3)

    cv.imshow("circles", frame)

    if cv.waitKey(1) & 0xFF == ord('q'): break;

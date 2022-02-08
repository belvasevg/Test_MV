import cv2 as cv
import numpy as np
n = 0;
cap = cv.VideoCapture(0)
while(1):
    _, frame = cap.read()
    cv.imshow('frame', frame)
    k = cv.waitKey(5) & 0xFF
    if k == ord("s"):
        path = "Cubick_test2_%d.jpg" % n  # Уникальное имя для каждого кадра
        cv.imwrite(path, frame)
        n += 1
    if k == 27:
        break



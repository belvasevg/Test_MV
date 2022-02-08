import cv2 as cv
import numpy as np

img = cv.imread('mask\All_Bukva_Blue0(11).jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
kernel3 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
closing_ellipse = cv.morphologyEx(gray, cv.MORPH_CLOSE, kernel3)
ret, thresh = cv.threshold(closing_ellipse,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

# sure background area
#kernel4 = np.ones((3, 3), np.uint8)
kernel1 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (2, 4))
sure_bg = cv.dilate(thresh,kernel1,iterations=3)
# Finding sure foreground area
dist_transform = cv.distanceTransform(thresh,cv.DIST_L2,5)

cv.imshow("Display frame", thresh)
k = cv.waitKey (0)

if k == ord("s"):
    cv.imwrite("mask\All_Bukva_Blue0(11).jpg", thresh)
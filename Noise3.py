import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('photos\Cubick1111_1.jpg')
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

ret1, sure_fg1 = cv.threshold(dist_transform,0.183*dist_transform.max(),255,0)
ret2, sure_fg2 = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)
# Finding unknown region
sure_fg1 = np.uint8(sure_fg1)
sure_fg2 = np.uint8(sure_fg2)

unknown1 = cv.subtract(sure_bg,sure_fg1)
unknown2 = cv.subtract(sure_bg,sure_fg2)


ret1, markers1 = cv.connectedComponents(sure_fg1)
ret2, markers2 = cv.connectedComponents(sure_fg2)
# Add one to all labels so that sure background is not 0, but 1
markers1 = markers1+1
markers2 = markers2+1
# Now, mark the region of unknown with zero
markers1[unknown1==255] = 0
markers2[unknown2==255] = 0
markers = cv.watershed(img,markers2)

n = img.shape[0]
m = img.shape[1]
# img[markers == -1] = [255,0,0]
for i in range(n):
    for j in range(m):
        if markers[i, j] != -1:
            gray[i, j] = 0

        if markers[i, j] == -1:
            gray[i, j] = 255

contours, hierarchy = cv.findContours(gray, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img,contours,3,(0,0,255),2)
plt.subplot(111),plt.imshow(img,cmap = 'gray')
plt.show()
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from Noise2 import contours

cnt = contours[2]
img = cv.imread('Cubick1111_1.jpg')

#  правильный прямоугольник по крайним точкам
# epsilon = 0.1*cv.arcLength(cnt,True)
# approx = cv.approxPolyDP(cnt,epsilon,True)
# x1, y1 = approx[0,0,0], approx[0,0,1]
# x2, y2 = approx[2,0,0], approx[2,0,1]
# cv.rectangle (img, (x1,y1), (x2,y2), (0,255,0), 3)

#Прямоугольник по контуру
# rect = cv.minAreaRect(cnt)
# box = cv.boxPoints(rect)
# box = np.int0(box)
# cv.drawContours(img,[box],0,(0,0,255),2)


plt.subplot(111),plt.imshow(img,cmap = 'gray')
plt.show()
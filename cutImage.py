import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from Noise2 import contours

cnt = contours[2]
img = cv.imread('Cubick1111_1.jpg')

#Прямоугольник по контуру
rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = np.int0(box)

min_x = min(box[:,0])
max_x = max(box[:,0])
min_y = min(box[:,1])
max_y = max(box[:,1])

cut = img[min_y:max_y,min_x:max_x]

plt.subplot(111),plt.imshow(cut,cmap = 'gray')
plt.show()

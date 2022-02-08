import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Cubick4_2.jpg', 0)

kernel1 = cv.getStructuringElement(cv.MORPH_CROSS, (8, 9))
closing_cross = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel1)
kernel2 = cv.getStructuringElement(cv.MORPH_RECT, (8, 10))
closing_rect = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel2)
kernel3 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (11, 11))
closing_ellipse = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel3)
kernel4 = np.ones((5, 5), np.uint8)
closing_cubic = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel4)

edges1 = cv.Canny(closing_cross, 50, 200)
edges2 = cv.Canny(closing_rect, 50, 200)
edges3 = cv.Canny(closing_ellipse, 50, 200)
edges4 = cv.Canny(closing_cubic, 50, 20)

plt.subplot(221),plt.imshow(edges1,cmap = 'gray')
plt.title('Cross Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(edges2,cmap = 'gray')
plt.title('Rect Image'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(edges3,cmap = 'gray')
plt.title('Ellipse Image'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(edges4,cmap = 'gray')
plt.title('Cubic Image'), plt.xticks([]), plt.yticks([])
plt.show()
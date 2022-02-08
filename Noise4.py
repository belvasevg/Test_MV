import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Cubick4_6.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#удаление шума
kernel3 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (11, 11))
closing_ellipse = cv.morphologyEx(gray, cv.MORPH_CLOSE, kernel3)

# Бинаризация Оцу
#ret, thresh = cv.threshold(closing_ellipse,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
edges3 = cv.Canny(closing_ellipse, 50, 200)
# sure background area
kernel1 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (2, 4))
sure_bg = cv.dilate(edges3,kernel1,iterations=1)

#Нахождение контуров
contours, hierarchy = cv.findContours(sure_bg, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


#Рисование нужных контуров
# for i in range(3,len(contours)- 1):
#     img = cv.drawContours(img, contours,i, (255, 0, 0), 3)
img = cv.drawContours (img, contours, 3, (255,0,0), 3)
img = cv.drawContours(img, contours, 4, (255, 0, 0), 3)
#img = cv.drawContours(img, contours, -1, (255, 0, 0), 3)


plt.subplot(111),plt.imshow(img ,cmap = 'gray')
plt.show()
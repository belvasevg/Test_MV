import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Cubick1111_1.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#удаление шума
kernel3 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
closing_ellipse = cv.morphologyEx(gray, cv.MORPH_CLOSE, kernel3)

# Бинаризация Оцу
ret, thresh = cv.threshold(closing_ellipse,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

# sure background area
kernel1 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (2, 4))
sure_bg = cv.dilate(thresh,kernel1,iterations=3)

#Нахождение контуров
contours, hierarchy = cv.findContours(sure_bg, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#print(contours)
#Рисование нужных контуров
print(contours)
img = cv.drawContours (img, contours, 3, (255,0,0), 3)
img = cv.drawContours (img, contours, 2, (255,0,0), 3)
#img = cv.drawContours (img, contours, -1, (255,0,0), 3)

plt.subplot(111),plt.imshow(img,cmap = 'gray')
plt.show()


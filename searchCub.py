import numpy as np
import math
import matplotlib.pyplot as plt
import cv2 as cv
from Noise2 import contours

cnt = contours[2]
img = cv.imread('Cubick1111_1.jpg')
print(contours[1])
rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = np.int0(box)
e_min = 10000
e_min_index = -1
for i in range(box.shape[0]):
    l1_y = math.sqrt(abs((box[0,0]- box[1,0])**2 + (box[0,1]- box[1,1])**2))
    l2_y = math.sqrt(abs((box[3, 0] - box[2, 0]) ** 2 + (box[3, 1] - box[2, 1]) ** 2))
    l3_x = math.sqrt(abs((box[0, 0] - box[3, 0]) ** 2 + (box[0, 1] - box[3, 1]) ** 2))
    l4_x = math.sqrt(abs((box[1, 0] - box[2, 0]) ** 2 + (box[1, 1] - box[2, 1]) ** 2))
    e_x = (l3_x - l4_x)**2
    e_y = (l1_y - l2_y)**2
    e = (e_x - e_y)**2
    if(e_min > e) or (e_min == 10000):
        e_min = e
        e_min_index = i

print(e_min_index)
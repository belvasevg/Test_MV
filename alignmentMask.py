import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

name = ['mask\All_Bukva_Black0(1).jpg', 'mask\All_Bukva_Black0(2).jpg', 'mask\All_Bukva_Blue0(1).jpg',
        'mask\All_Bukva_Blue0(2).jpg', 'mask\All_Bukva_Blue0(3).jpg', 'mask\All_Bukva_Blue0(4).jpg',
        'mask\All_Bukva_Blue0(5).jpg', 'mask\All_Bukva_Blue0(6).jpg', 'mask\All_Bukva_Blue0(7).jpg',
        'mask\All_Bukva_Blue0(8).jpg', 'mask\All_Bukva_Blue0(9).jpg', 'mask\All_Bukva_Blue0(10).jpg',
        'mask\All_Bukva_Blue0(11).jpg','mask\All_Bukva_Green0(1).jpg', 'mask\All_Bukva_Green0(2).jpg',
        'mask\All_Bukva_Green0(3).jpg','mask\All_Bukva_Green0(4).jpg', 'mask\All_Bukva_Green0(5).jpg',
        'mask\All_Bukva_Green0(6).jpg','mask\All_Bukva_Green0(7).jpg', 'mask\All_Bukva_Green0(8).jpg',
        'mask\All_Bukva_Green0(9).jpg','mask\All_Bukva_Green0(10).jpg', 'mask\All_Bukva_Red0(1).jpg',
        'mask\All_Bukva_Red0(2).jpg', 'mask\All_Bukva_Red0(3).jpg', 'mask\All_Bukva_Red0(4).jpg',
        'mask\All_Bukva_Red0(5).jpg', 'mask\All_Bukva_Red0(6).jpg', 'mask\All_Bukva_Red0(7).jpg',
        'mask\All_Bukva_Red0(8).jpg', 'mask\All_Bukva_Red0(9).jpg', 'mask\All_Bukva_Red0(10).jpg']

# i = 12
# img = cv.imread(name[i])
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# print(gray.shape)
# plt.subplot(111),plt.imshow(gray,cmap = 'gray')
# plt.show()

# gray = np.delete(gray,(0), axis=0)
# gray = np.delete(gray,(0), axis=1)
#
# r = np.zeros((4,99),dtype=np.uint8)
# c = np.zeros((100,1),dtype=np.uint8)
# gray = np.append(gray,r,axis =0)
# gray = np.append(gray,c,axis=1)
# print(gray.shape)
#
# cv.imshow("Display frame", gray)
# k = cv.waitKey (0)
#
# if k == ord("s"):
#     cv.imwrite(name[i], gray)

# x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# x = np.delete(x, (0,1), axis=0)
# r = np.zeros((1,3),dtype=np.int32)
# c = np.zeros((4,1),dtype=np.int32)
# x = np.append(x,r,axis =0)
# x = np.append(x,c,axis=1)
# print(x)
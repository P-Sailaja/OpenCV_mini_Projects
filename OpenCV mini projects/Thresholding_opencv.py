#---------------------Thresholding------------------------
'''
Use to extract selected Data from the image by using pixels Values.
Also use to manage pixels and divide all values in two parts
'''
import cv2
import numpy as np

img = cv2.imread("E:\\Data\\Pic2.jpg",0)
img = cv2.resize(img, (300,300))
'''
cv2.imshow("data", img)


#th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
#th2 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV)
th3 = cv2.threshold(img, 50, 255, cv2.THRESH_TRUNC)
#th4 = cv2.threshold(img, 50, 255, cv2.THRESH_TOZERO)
#th5 = cv2.threshold(img ,50, 255, cv2.THRESH_TOZERO_INV)

#cv2.imshow("1 - THRESH_BINARY", th1)
#cv2.imshow("2 - THRESH_BINARY_INV", th2)
cv2.imshow("3 - THRESH_TRUNC", th3)
#cv2.imshow("4 - THRESH_TOZERO", th4)
#cv2.imshow("5 - THRESH_TOZERO_INV", th5)
'''
th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2);

cv2.imshow("Image", img)
cv2.imshow("THRESH_BINARY", th1)
cv2.imshow("ADAPTIVE_THRESH_MEAN_C", th2)
cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", th3)

cv2.waitKey(0)
cv2.destroyAllWindows()

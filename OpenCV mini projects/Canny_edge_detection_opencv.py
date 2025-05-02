#Canny Edge Detection using OpenCV
#Canny Edge Detection is a popular edge detection approach.

#It use multi-stage algorithm to detect a edges.
#It was developed by John F. Canny in 1986.
#This approach combine with 5 steps.
#  1 - Noise reduction (gauss)
#  2 - Gradien calculation
#  3 - Non-maximum suppresson, 
#  4 - Double Threshold
#  5 - Edge Tracking by Hysteresis

import cv2 as c
import numpy as np
'''
#Load image into gray scale
img = cv2.imread("E:\\Data\\Pic1.jpg")
img = cv2.resize(img, (400,400))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


canny = cv2.Canny(img_gray, 20, 150)

cv2.imshow("Original", img)
cv2.imshow("Gray", img_gray)
cv2.imshow("Canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

#Load image into gray scale
img = c.imread("E:\\Data\\Pic1.jpg")
img = c.resize(img, (400,400))
img_gray = c.cvtColor(img,c.COLOR_BGR2GRAY)

def nothing(x):
    pass

c.namedWindow("Canny")
c.createTrackbar("Threshold","Canny", 0, 255, nothing)

while True:
    a = c.getTrackbarPos("Threshold","Canny")
    print(a)
    res = c.Canny(img_gray,a,255)
    c.imshow("Canny", res)
    if c.waitKey(1) & 0xFF == 27:
        break
c.destroyAllWindows()

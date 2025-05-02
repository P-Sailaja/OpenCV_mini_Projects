import  cv2
import numpy as np

#load the image into gray
img = cv2.imread("E:\\Data\\Pic2.jpg")
img = cv2.resize(img, (500,500))

#There are two types of image pyramids-
# 1. Gaussian pyramid  2. Laplacian pyramids

#Gaussian Pyramid have 2 functions
#  1-- cv2.pyrUp()
#  2-- cv2.pyrDown()
'''
#pyrDown......
pd1 = cv2.pyrDown(img)
pd2 = cv2.pyrDown(pd1)

#pyrUp..........
#if we pyrUp any pyrdown image both are not equal 
pu1 =  cv2.pyrUp(pd2) --- blur

cv2.imshow("Original",img)
cv2.imshow("pd1", pd1)
cv2.imshow("pd2", pd2)
cv2.imshow("pul", pu1)
'''

img1 = img.copy()
data = [img1]

for i in range(4):
    img1 = cv2.pyrDown(img1)
    data.append(img1)
    cv2.imshow("result" + str(i), img1)
    
cv2.imshow("Original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

####IMAGE GRADIENT
'''
It isj a dirational change in the color or intensity in an image.
It is most important part to find information from image.
Like finding edges within theimages.
There are various methods to find image gradient.
These are - Laplacian Derivatives, SobelX and SobelY.
All these functions have diff. mathematical approach to get result.
All load image in the gray scale
'''
import cv2 as c
import numpy as np

#Load image into gray scale.
img = c.imread("E:\\Data\\Pic4.jpg")
img = c.resize(img, (400,300))
img_gray = c.cvtColor(img, c.COLOR_BGR2GRAY)


#Laplacian Derivative --- It calculate laplace derivate
#parameter (img, data_type for -ve , ksize)

lap = c.Laplacian(img_gray, c.CV_64F, ksize= 3)
lap = np.uint8(np.absolute(lap))

#Sobel operation - is a joint gaussian smoothing plus differetiation
#operation, so it is more resistent to noise
#This is use for x and y both parameter (img, type for -ve val, x= 1, y=0, ksize)
#SobelX focus on vertical lines
#Sobel Y focus on horizontal lines
sobelX = c.Sobel(img_gray, c.CV_64F, 1,0,ksize = 3)# 1 means x direction
sobelY = c.Sobel(img_gray, c.CV_64F,0,1,ksize = 3)# 1 means y directions

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

#finally combine sobelX and sobelY together
sobelcombine = c. bitwise_or(sobelX,sobelY)


c.imshow("Original ",img)
c.imshow("gray ",img_gray)
c.imshow("Lap", lap)
c.imshow("SobelX", sobelX)
c.imshow("SobelY", sobelY)
c.imshow("Combines image", sobelcombine)
c.waitKey(0)
c.destroyAllWindows()
               

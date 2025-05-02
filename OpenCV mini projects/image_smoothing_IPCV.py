'''
* Image smoothing or blluring is most common used operation in image processing.
* It is use to remive noise from the images.
* There are so many filter which is use for smoothing the image.
* There are LOW passfilter (LPS) which use to remove noise from the images.
* There are high pass filter which use to detect and finding edges in an image.

* we discuss abouot various filters--like, homogeneous, blur(averaging),median, bilateral.
'''
import cv2 as c
import numpy as np

img = c.imread("E:\\Data\\eye.jpg",0)

img = c.resize(img, (300,400))

#c.imshow("Eye",img)

kernel = np.ones((4,4),np.float32)/16

#FILTER number ---------1
'''
This filter work like, eacah output poxel is the mean of its kernel neighbour
It is aka homogeneous filter in this all pixel contribute with equal weight.
Kernel is a small shape or matrix which we apply on image.
In this filter kernel is [(1/kernel(h,w)*kernel)]'''
h_filter = c.filter2D(img,-1,kernel)# -1 is desired depth
#c.imshow("homogeneous ", h_filter)

#FILTER number ------------2
#blur method or averaging
#takes the avg of all the pixels underkernek area and replaces the central element with this average.
blur = c.blur(img, (5,5))
#c.imshow("blur ", blur)

#FILTER number -----------3
#Gaussian filter Here it using different weight kernek,in row as well as
#means side values are small then centre. IT manage distance b/w value of

gau = c.GaussianBlur(img,(5,5),0)
#c.imshow("gau blur",gau)

#FILTER number -------------4
#Median filter --- computes the median of all the pixels under the kernel window and the
#central pixel is replaced with this median value.
#This is highly effective in removing salt - and-pepper noise.
#Here kernel size must be add except one.
med = c.medianBlur(img,5) # odd value #1 as default
#c.imshow("median filter", med)

#BILATERAL filter ---- is highly effective at noise removal while preserving the edges.
#It work like gaussian filter but more focus on edges
#It is slow as compare eith the other filters
#Argument (img, neighbour_pixel_diameter, sigma_color, sigma_space)
bi_f = c.bilateralFilter(img, 9,75,75)#50- 100
#c.imshow("bi_f", bi_f)
                          
#now plot all the images on graph
titles = ["Original_image","home", "Blur", "gauss", "med", "bi_f"]
images = [img, h_filter,blur, gau,med,bi_f]

#if you want then plot it
from matplotlib import pyplot as plt
for i in range(6):
    plt.subplot(2,3,i+1),
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
          

c.waitKey(0)
c.destroyAllWindows()

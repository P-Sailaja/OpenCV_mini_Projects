import cv2 as c
import numpy as np
'''
img = c.imread("E:\\Data\\variety_colored_balls.webp",0)

img = c.resize(img, (400,250))

c.imshow("Balls",img)

c.waitKey(0)
c.destroyAllWindows()
'''

img = c.imread("E:\\Data\\variety_colored_balls.webp",0)

img = c.resize(img, (400,250))
_,mask = c.threshold(img,207,255,c.THRESH_BINARY_INV)
#------------------erosion----------------------
kernel = np.ones((5,5), np.uint8) # 5x5 kernal with full of ones.
e = c.erode(mask,kernel)
#-----------------------dilation-----------------
kernel = np.ones((5,5), np.uint8) #kernel with full of threes
d = c.dilate(mask,kernel) #iterations = 2(optional parameters) iterations
c.imshow("dilate", d)

# if you want then plot it
import matplotlib.pyplot as plt
titles = ['img', 'mask','erosion','dilation']
images = [img,mask, e, d]
for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

'''
c.imshow("img", img)
c.imshow("kernel", kernel)
c.imshow("mask",mask)
#c.imshow("erosion", e)
'''

 
c.waitKey(0)
c.destroyAllWindows()
 
               

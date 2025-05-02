import cv2 as c
import numpy as np

img = c.imread("E:\\Data\\variety_colored_balls.webp",0)
img = c.resize(img, (400,250))
_,mask = c.threshold(img,207,255,c.THRESH_BINARY_INV)

c.imshow("img", img)

c.imshow("mask",mask)


kernel = np.ones((5,5), np.uint8)
o = c.morphologyEx(mask, c.MORPH_OPEN, kernel) # optional parametrs iterations =2
c.imshow("Opening", o)
kernel = np.ones((4,4), np.uint8)
s = c.morphologyEx(mask, c.MORPH_CLOSE, kernel)
c.imshow("Closing", s)

#--------options-------------
x1 = c.morphologyEx(mask,c.MORPH_TOPHAT,kernel) # diff b/w mask & opening
x2 = c.morphologyEx(mask, c.MORPH_GRADIENT,kernel)#diff b/w dilation & erosion
x3 = c.morphologyEx(mask, c.MORPH_BLACKHAT,kernel)

c.imshow("kernel", kernel)
c.imshow("x1",x1)
c.imshow("x2",x2)
c.imshow("x3",x3)

c.waitKey(0)
c.destroyAllWindows()

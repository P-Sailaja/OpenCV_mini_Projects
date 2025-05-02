#Extracting object from the image and place on another image
#Random figure ROI or Background Subtraction.

import cv2 as c
import numpy as np

#Load twi images
img1 = c.imread("E:\\Data\\iron_man.jpg")
img2 = c.imread("E:\\Data\\katthi.jpg")

img1 = c.resize(img1, (1024,650))
img2 = c.resize(img2, (600,650))

#I want to fix image 2 data into img1
r,c,ch = img2.shape
print(r,c,ch)

roi = img1[0:r,0:c]

#now creating mask for img2
img_gry = c.cvtColor(img2, c.COLOR_BGR2GRAY)

#create mask using threshold
-, mask = c.threshold(img_gry, 50, 255, c.THRESH_BINARY)

#remove bg
mask_inv = c.bitwise_not(mask)

#put mask into roi
img1_bg = c.bitwise_and(roi, roi, mask = mask_inv)

#Take only region of figure from irginal image.
img2_fg = c.bitwise_and(img2, img2, mask = mask)

#put img in ROI and modify the main image
res = c.add(img1_bg,img2_fg)

'''
c.imshow("Iron man", img1)
c.imshow("Strom",img2)
c.imshow("RoI",roi)
'''

c.imshow(" Step -1 gry == ", img_gry)
c.imshow(" Step -2 Mask === ", mask)
c.imshow(" Step -3 Mask_inv", mask_inv)
c.imshow(" Step -4 Mask fg", img2_bg)
c.imshow(" Step -5 Mask fg", img2_fg)
c.imshow(" Step -6 Result", res)

final = img1

final[0:r,0:c] = res #final output
c.imshow("Step 7 == Final ", final)

c.waitKey(0)
c.destroyAllWindows()

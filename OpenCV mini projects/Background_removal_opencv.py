#GrabCut Algorithm with the help of this algorithm we easily
#cutoff any foreground object from image or video.
#It works like a rectangle portion mark on the image and area outise the raactangle is treat as a extract part
#so this algo remove it completely.
#Gaussian mixture model help to achieve the target.

import numpy as np
import cv2

img = cv2.imread('E:\\Data\\Pic4.jpg')
img = cv2.resize(img, (500,500))
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel= np.zeros((1,65), np.float64)*255
fgdModel = np.zeros((1,65), np.float64)*255

#parameter(img, mask,rect, bgmodel, fgmodel, iter, method)
rect = (134,150,660,730)
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2)|(mask == 0), 0, 1).astype('uint8')
img = img*mask2[:,:, np.newaxis]

cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

#cv2.copyMakeBorder() function
#It take parameters like(img, border_width*4, bordertype, val_brdr)
#border width = top, bottom, right, left

img = cv2.imread("E:\\Data\\Pic2.jpg")
img = cv2.resize(img, (500,600))

#creating image border
brdr = cv2.copyMakeBorder(img, 20, 20, 5, 5,
                          cv2.BORDER_CONSTANT,
                          value =[255,0,255])

cv2.imshow("result", brdr)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

img1 = cv2.imread("E:\\Data\\Pic2.jpg")
img1 = cv2.resize(img1, (500,700))
img2 = cv2.imread("E:\\Data\\Pic4.jpg")
img2 = cv2.resize(img2, (500,700))


#numpy addition. In this, we get module b/w value.
#result = img2+img1

#result1 = cv2.add(img1, img2)

result2 = cv2.addWeighted(img1, 0.3, img2, 0.7,0)

#cv2.imshow("result==",result)
#cv2.imshow("result==", result1)
cv2.imshow("result ==", result2)

cv2.waitKey(0)
cv2.destroyAllWindows()
 

#Drawing functions in opencv

import numpy as np
import cv2 as c

img = c.imread("E:\\Data\\Pic2.jpg")
img = c.resize(img, (500,400))

#Here line accepts - (img, starting,ending, color, thickness)
img = c.line(img, (0,0), (200,200), (203, 173, 174),8) #color format BGR

c.imshow("result",img)
c.waitKey(0)
c.destroyAllWindows()

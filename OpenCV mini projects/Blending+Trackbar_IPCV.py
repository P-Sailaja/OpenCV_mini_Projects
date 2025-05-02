import cv2
import numpy as np

img1 = cv2.imread("E:\\Data\\Pic2.jpg")
img1 = cv2.resize(img1, (500,700))
img2 = cv2.imread("E:\\Data\\Pic4.jpg")
img2 = cv2.resize(img2, (500,700))

#cv2.imshow(image1)
#cv2.imshow()

def blend(x):
    pass

img = np.zeros((300,400,3),np.uint8)
cv2.namedWindow("win")# create trackbar windows

cv2.createTrackbar('alpha', 'win', 1, 100, blend)
switch= "0:OFF\n1:ON"
cv2.createTrackbar(switch,"win", 0, 1, blend)


while True:
    s = cv2.getTrackbarPos(switch, 'win')
    a = cv2.getTrackbarPos("alpha","win")
    n = float(a/100)
    print(n)

    if s == 0:
        dst = img[:]
    else:
        dst = cv2.addWeighted(img1,i-n,img2,n,0)
        cv2.putText(dst, str(a),(20, 50), cv2.FONT_ITALIC,
                    2, (0,125,255), 2)
        cv.imshow('dst',dst)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cv2.waitKey(0)
cv2.destroyAllWindows()
        



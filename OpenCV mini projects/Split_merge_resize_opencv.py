import cv2
import numpy as np

#Read the image

img = cv2.imread("E:\\Data\\Pic4.jpg")
img= cv2.resize(img, (100,100))
cv2.imshow("result", img)

print("Shape ==", img.shape)
print("no.of pixels ==", img.size)
print("datatype ==", img.dtype)
print("ImageType ==", type(img))

#Split - returns # channel of your image which is blue, green, red
img = cv2.imread("E:\\Data\\Pic4.jpg")
img= cv2.resize(img, (200,200))
b,g,r = cv2.split(img)
cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)

#Merge -
mr1 = cv2.merge((r,g,b))
cv2.imshow("rgb",mr1)
mr2 = cv2.merge((g,b,r))
cv2.imshow("gbr", mr2)
mr3 = cv2.merge((b,r,g))
cv2.imshow("brg", mr2)

#working on pixel color values-----
img = c.imread("E:\\Data\\Pic2.jpg")
img = cv2.resize(img, (500,300))
cv2.imshow("picture", img)
print("Shape ==", img.shape)
print("no.of pixels ==", img.size)
print("datatype ==", img.dtype)
print("ImageType ==", type(img))

px = img[520,580] #store coordinate in variable
print("The pixel of that co-ordinates ==",px)

blue = img[520,580,0]
print("The pixel having blue color ===" , blue)

grn = img[520,580,1]
print("The pixel having blue color ===" , grn)

red = img[520,580,2]
print("The pixel having blue color ===" , red)




cv2.waitKey()
cv2.destroyAllWindows()


cv2.waitKey(0)
cv2.destroyAllWindows()

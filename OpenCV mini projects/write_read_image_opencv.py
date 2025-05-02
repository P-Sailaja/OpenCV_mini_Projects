import cv2 #opencv use as cv2 in python
#this function is used to read the image from location
img1= cv2.imread('E:\\Data\\Pic1.jpg',1)

img1=cv2.resize(img1,(500,500))#width, height
cv2.imshow("Colored Image", img1)#It accept two parameters 1) - Name of screen,2)


img2= cv2.imread('E:\\Data\\Pic1.jpg',0)

img2=cv2.resize(img2,(500,500))#width, height
cv2.imshow("Gray Image", img2)#It accept two parameters 1) - Name of screen,2)
print("Image in gray scale==\n",img2)


img3= cv2.imread('E:\\Data\\Pic1.jpg',-1)

img3=cv2.resize(img3,(500,500))#width, height
cv2.imshow("Invert Image", img3)#It accept two parameters 1) - Name of screen,2)

k = cv2.waitKey(0) & 0xFF  #Here parameter inside waitKey handle the life duration of an image
if k== ord("q"):
    cv2.destroyAllWindows()
elif k== ord("s"):
    cv2.imwrite("output.png",img1) #It accept name of image and data
    cv2.destroyAllWindows()

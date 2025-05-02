import cv2
'''
img1 = cv2.imread("E:\\Data\\Pic2.jpg",1)
img1 = cv2.resize(img1, (500,700))
cv2.imshow("Original",img1)

img2 = cv2.imread("E:\\Data\\Pic2.jpg",0) # -1 unchanged
img2 = cv2.resize(img2, (500,700))
cv2.imshow("Gray",img2)


cv2.waitKey()
cv2.destroyAllWindows()

'''
# Image conversion project colored image into grayscale.

#path = input("Enter the path and name of an image === ")
#print("You Enter this ===", path)

#Now read the image
img = cv2.imread("E:\\Data\\Pic2.jpg",1)
img = cv2.resize(img, (500,700))
img = cv2.flip(img,-1) #0,1,-1
cv2.imshow("Converted Image",img)

cv2.waitKey(0) #to wait for a key event,
cv2.destroyAllWindows() #to destroy all windows,
#cv2.imwrite('imagename.png', img)

'''
k = cv2.waitKey(0)
if k == ord("s"):
    cv2.imwrite("E:\\Data\\output.jpg",img)
else:
    cv2.destroyAllWindows()
'''


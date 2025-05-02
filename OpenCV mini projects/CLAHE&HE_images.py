import cv2 as c
import numpy as np

image = c. imread("E:\Data\Pic4.jpg")
image_bw = c.cvtColor(image, c.COLOR_BGR2GRAY)

#The deaclaration of CLAHE
#clipLimit --> Threshold for contrast limiting
clahe = c.createCLAHE(clipLimit = 5)
final_img = clahe.apply(image_bw)

normal_hist = c.equalizeHist(image_bw)
#Ordinary thresholding the same image
#_, ordinary_img = c.threshold(image_bw,155,255,c/THRESH_BINARY)

#showing all the three images
c.imshow("ordinary", image)
c.imshow("CLAHE image", final_img)
c.imshow("HE image", normal_hist)
c.waitKey(5000)

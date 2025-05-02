#Contours - helps in shape detection,analyzation and Recognition
'''
Contours can be explained simply as a curve joining all the continuous points
(along the boundary), having same color or intensity.

The contours are a useful tool for shape analysis and object detection and recognition

For better accuracy, use binary images and also apply edge detection before

Finding.......

findContour function manipulate original image so copy it before proceeding.
findContour is like finding white object from black background.
so you must turn image in white and background is black.

We have to find and draw contours as per the requirement.
'''

import cv2
import numpy as np

img = cv2.imread("E:\\Data\\Pic1.jpg")
img = cv2.resize(img, (300,300))
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img1, 20, 255, 0) # for red 127=70 for blue 127=20
#findContour(img, contour_retrieval_mode, method)
cnts,hier = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#Here cnts =list of contours, and each contour is an array with x, y coordinates
#hier variable called hierarchy and it contain image information.
print("No.of contours =",cnts,"Total conours =",len(cnts))
print("Hierarchy",hier)

#drawcontour (img, cnts, id of contour, color, thickness, )#Here if we draw all
#contour just pass -1
#Draw the contours
'''
img = cv2.drawContours(img,cnts, 10, (176,10,15),4) #(25,100,15)= green border
#-------------------------------- -1/5/. ----------------------
#Output......
cv2.imshow("contours", img)
cv2.imshow("gray" , img1)
cv2.imshow("thresh", thresh)
'''
#Draw contours
area1 =[]
#loop over the contours
for c in cnts:
    #compute the center of the contour
    #an image moment is a certain particular weighted average(moment)
    M = cv2.moments(c)
    print("M ==", M)
    cX = int(M['m10'] / M['m00'])
    cY = int(M['m01'] / M['m00'])
    #find area of contour
    area = cv2.contourArea(c)
    area1.append(area)


    #contour  Approxx - it is use to approx shape with less number of vertices
    epsilon = 0.1*cv2.arcLength(c,True)# arc length take contour and return
    data = cv2.approxPolyDP(c, epsilon,True)
    #convexhull is used to provide proper contours convexity.

    hull = cv2.convexHull(data)

    x,y,w,h = cv2.boundingRect(hull)
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (125, 10, 20), 5)
    
    #draw the contour and center of the shape on the image
    cv2.drawContours(img, [c], -1,(0,255,0),2)
    cv2.circle(img, (cX, cY), 7, (255,255,255), -1)
    cv2.putText(img, "center", (cX - 20,cY - 20), cv2.FONT_HERSHEY_SIMPLEX,0.5,
                (255,255,255),2)
    
#Output......
cv2.imshow("contours", img)
cv2.imshow("gray" , img1)
cv2.imshow("thresh", thresh)










cv2.waitKey(0)
cv2.destroyAllWindows()

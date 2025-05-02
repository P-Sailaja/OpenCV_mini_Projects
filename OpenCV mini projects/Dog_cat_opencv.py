#Cat face detection using har cascade

import cv2
import numpy
face = cv2.CAscadeClassifier(" ")

image = cv2.imread("E:\\Data\\dogcat.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Parameters(img, scale_factor[reduce image size], min_neighbour)
faces = face.detectMultiScale(gray,1.1,1) # for faces

for (x,y,w,h) in faces:
    image = cv2.rectangle(image,(x,y), (x+w,y+h), (127, 0, 205), 3)

image = cv2.resize(image,(500,500))
cv2.imshow("Sailaja", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

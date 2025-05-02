import cv2 as c
import numpy as np

wCam, hCam = 640,480
cap = c.VideoCapture(0,c.CAP_DSHOW)
cap.set(3,wCam)
cap.set(4,hCam)

success, img1 = cap.read()
success, img2 = cap.read()

while cap.isOpened():
    diff = c.absdiff(img1, img2)
    gray = c.cvtColor(diff, c.COLOR_BGR2GRAY)
    blur = c.GaussianBlur(gray, (5,5), 0)
    _, thresh = c.threshold(blur, 20, 255, c.THRESH_BINARY)
    dilated = c.dilate(thresh, None, iterations=3)
    contours, _ = c.findContours(dilated, c.RETR_TREE, c.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x,y,w,h) = c.boundingRect(contour)

        if c.contourArea(contour) < 900:
            continue
        c.rectangle(img1, (x,y), (x+w, y+h), (0,255,0), 2)
        c.putText(img1, "status: {}".format('Movement'),(10,20),
                  c.FONT_HERSHEY_SIMPLEX,1, (0,0,255), 3)
    #c.drawContours(img1, contours, -1,(0,255,0),2)

    c.imshow("Inter", img1)
    img1 = img2
    success, img2 = cap.read()

    if c.waitKey(40) == 72:
        break

c.destroyAllWindows()
cap.release()

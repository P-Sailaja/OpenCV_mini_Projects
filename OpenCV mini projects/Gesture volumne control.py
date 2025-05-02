import cv2 as c
import numpy as np
import time
import HandTrackingModule as htm

wCam,hCam = 640,480

cap = c.VideoCapture(0,c.CAP_DSHOW)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector()

while True:
    succes, img = cap.read()
    img = detector.findHands(img)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    c.putText(img, f'FPS: {int(fps)}',(40,50), c.FONT_HERSHEY_COMPLEX,
              1, (255,0,0),3)
    
    c.imshow("img",img)
    c.waitKey(1)

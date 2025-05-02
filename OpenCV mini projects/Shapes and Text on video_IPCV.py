#Draw date time and figures on video

import cv2 as c
import datetime

cap = c.VideoCapture("E:\\Data\\Vid1.mp4")
print("For width ===", cap.get(c.CAP_PROP_FRAME_WIDTH))
print("For height ===", cap.get(c.CAP_PROP_FRAME_HEIGHT))
print("Width ===", cap.get(3)) #Here 3 for width
print("Height ===", cap.get(4)) #Here 4 for heoght

while(cap.isOpened()):
    ret,frame = cap.read()
    frame = c.resize(frame,(500,400))
    if ret == True:
        font = c.FONT_HERSHEY_COMPLEX_SMALL
        text = 'Height: '+ str(cap.get(4)) + 'Width: ' +str(cap.get(3))
        frame = c.putText(frame,text,(10, 20), font, 1,
                           (0,120,0), 1, c.LINE_AA)

        date_data = "Date: " +str(datetime.datetime.now())
        frame = c.putText(frame, date_data, (20, 50), font, 1,
                          (100, 5, 255), 1, c.LINE_AA)
        c.rectangle(frame, (384,10), (510, 128), (0,100,255),8)
        c.imshow('frame',frame)
        

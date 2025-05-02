import cv2

'''
cap= cv2.VideoCapture("E:\\Data\\Vid1.mp4")

while True:
    ret, frame= cap.read() #here read the frame
    frame= cv2.resize(frame,(400,400))
    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Colorframe',frame)
    cv2.imshow("Gray Frame", gray)
    if cv2.waitKey(100) & 0xFF == ord('q'): #Press q to exit
        break

#Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
'''

cap= cv2.VideoCapture(0,cv2.CAP_DSHOW)

#DIVX, XVID, MJPG, X264, WHV1, WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID")
#It contain 4 parameter: name, codec,frames,resolution
output = cv2.VideoWriter("E:\\Data\\output1.avi",fourcc,20.0,(400,400),0)

while cap.isOpened():
    ret, frame= cap.read() #here read the frame
    if ret == True:
        #frame= cv2.resize(frame,(400,400))
        gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        frame = cvr.flip(frame,0)
        cv2.imshow('Colorframe',frame)
        cv2.imshow("Gray Frame", gray)
        output.write(gray)
        if cv2.waitKey(1) & 0xFF == ord('q'): #Press q to exit
            break

#Release everything if job is finished
cap.release()
output.release()
cv2.destroyAllWindows()

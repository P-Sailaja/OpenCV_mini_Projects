
'''
#Here with the help of videoCapture function we easily ready any video.

cap= cv2.VideoCapture("E:\\Data\\test1.mp4")

while True:
    ret, frame= cap.read() #here read the frame
    frame= cv2.resize(frame,(700,500))
    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Colorframe',frame)
    cv2.imshow("Gray Frame", gray)
    if cv2.waitKey(25) & 0xFF == ord('q'): #Press q to exit
        break

#RElease everything if job is finished
cap.release()
cv2.destroyAllWindows()
'''
import cv2
import datetime

#Create the videoCapture object to access the default camera
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW) #Here parameter 0 is a path of any video
print("for width ===", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("for height ===", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3, 800)
cap.set(4, 800) #Here $ for height

#Check if the camera was opened successfully
print("check ===", cap.isOpened())

#Set a timer for 10 seconds
start_time =cv2.getTickCount()

#it is 4 byte code which is use to specify the video codec
#Various codec -- DIVX, XVID, MJPG, X264, WMV1, WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID") #*"XVID"
#It contain $ parameter, name, codec, fps, resolution
output=cv2.VideoWriter("output.avi",fourcc, 20.0,(640,480),0)

while(cap.isOpened()):
    #Read a frame from the camera
    ret,frame = cap.read() #here read the frame
    #Check if a frame was successfully read
    if ret==True:

        
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        text= 'Heigth: ' + str(cap.get(4)) + 'width: ' + str(cap.get(3))
        date_data = "Date: "+str(datetime.datetime.now())
        frame = cv2.putText(frame, text, (20,30), font, 1, (255,155,255),1)

        frame = cv2.putText(frame, date_data, (50,100), font, 1, (0,255,255),1)
        #Display the frame
        cv2.imshow("Colored FRame", frame)
        
        #Calculate elapsed time
        elapsed_ms = (cv2.getTickCount() - start_time)/ cv2.getTickFrequency() * 1000

        #Check if 10 seconds have passed
        if elapsed_ms >= 10000:
            milliseconds = 10000
            break
        
        #Exit the loop if q is pressed    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        else:
            break


#Release everything if job is finished
cap.release()
cv2.destroyAllWindows()















        

import cv2
#-------------------Capture video from Mobile--------------------------
'''
camera = "http://192.168.29.124:8080/video"

cap= cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.open(camera)
print("Check ===", cap.isOpened())
#DIVX, XVID, MJPG, X264, WHV1, WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID")
#It contain 4 parameter: name, codec,frames,resolution
output = cv2.VideoWriter("E:\\Data\\Vidoutput.mp4",fourcc,20.0,(400,400),0)

while cap.isOpened():
    ret, frame= cap.read() #here read the frame
    if ret == True:
        frame = cv2.resize(frame,(500,500))
        cv2.imshow('Colorframe',frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'): #Press q to exit
            break

#Release everything if job is finished
cap.release()
output.release()
cv2.destroyAllWindows()
'''
#-------------------------Capture Video from Youtube--------------------
import pafy

url = "https://youtu.be/n4OFVR3V6G8?si=OiQFpjhwi7b0n84n"
data = pafy.new(url)
data = data.getbest(preftype = "mp4")


cap= cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.open(data.url)
print("Check ===", cap.isOpened())


while cap.isOpened():
    ret, frame= cap.read() #here read the frame
    if ret == True:
        frame = cv2.resize(frame,(500,500))
        
        cv2.imshow('Colorframe',frame)
        
        if cv2.waitKey(200) & 0xFF == ord('q'): #Press q to exit
            break

#Release everything if job is finished
cap.release()

cv2.destroyAllWindows()

#---------------Screen Recorder--------------------
'''
import cv2
import pyautogui as p
import numpy as np

#create resolution
rs = p.size()

#filename in which we store recording
fn = input("Please Enter any file name and path: ")
# Fix the frame rate
fps = 60.0


fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter(fn,fourcc,fps,rs)

#create recording module
cv2.namedWindow("Live_Recording", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live_Recording",(600,400))

while True:
    img = p.screenshot()
    f = np.array(img)
    f = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)
    output.write(f)
    cv2.imshow("Live_Recording",f)
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
'''

#-----------------Break Video into Multiple images-------------------
import cv2 as c

vidcap = c.VideoCapture("E:\\Data\\Vid1.mp4")
ret,image = vidcap.read()

count = 0
while True:
    if ret == True:
        c.imwrite("E:\\Frames\\imgN%d.jpg"%count,image)
        vidcap.set(c.CAP_PROP_POS_MSEC,(count**100))
        ret,image = vidcap.read()
        c.imshow("res",image)
        print(count)
        count+=1

        if c.waitKey(1) & 0xFF == ord("q"):
            break
            c.destroyAllWindows()


vidcap.release()
c.destroyAllWindows()


            
        

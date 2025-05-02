#Mouse callback functions

import cv2 as c
import numpy as np
'''
def draw(event, x, y,flags,param):
    print("x == ",x)
    print("y == ",y)
    print("flags == ",flags)
    print("param == ",param)
    if event == c.EVENT_LBUTTONDBLCLK:
        c.circle(img, (x,y), 100, (125,0,255), 5)
    if event == c.EVENT_RBUTTONDBLCLK:
        c.rectangle(img,(x,y), (x+100, y+75),
                    (125,125,255),2)

c.namedWindow(winname = "res")

img = np.zeros((512,512,3), np.uint8)
c.setMouseCallback("res",draw)

while True:
    c.imshow("res", img)
    if c.waitKey(1) & 0xFF == 27: #esc
        break

c.destroyAllWindows()
'''
#create a function which help to find coordinate of any pixel and its color

def mouse_event(event, x, y, flags, param):
    print("x == ",x)
    print("y == ",y)
    print("flags == ",flags)
    print("param == ",param)
    font = c.FONT_HERSHEY_PLAIN
    if event == c.EVENT_LBUTTONDOWN:
        print(x, ', ',y)

        cord = ", " +str(x) + ', '+str(y)
        c.putText(img,cord,(x,y), font, 1,(155,125,100),2)
        c.imshow('image',img)

    if event == c.EVENT_RBUTTONDOWN:
        b = img[y, x, 0]#for blue channel is 0
        g = img[y, x, 1] #for green channel is 1
        r = img[y, x, 2]#for red channel is 2

        color_bgr = ". "+str(b) + ', '+str(g) +', '+str(r)
        c.putText(img, color_bgr, (x,y),font, 1, (152,255,130),2)
        #c.imshow('image', img)

c.namedWindow(winname = 'res')

img = np.zeros((512,512,3), np.uint8)
img = c.imread('E:\\Data\\Pic2.jpg')
c.setMouseCallback('res',mouse_event)

while True:
    c.imshow('res',img)
    if c.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()

















        
        

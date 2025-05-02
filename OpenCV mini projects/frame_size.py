import cv2

img = cv2.imread("E:\\Data\\Pic2.jpg")
img = cv2.resize(img, (700,800))

#Here line accepts 5 parameters (img,starting,ending,color,thickness)
img= cv2.line(img, (0,0), (200,400), (14, 92, 30), 2) #color format BGR


#arrowed line accept also accept 5 parameter (img, starting, ending, color,thickness)
img = cv2.arrowedLine(img, (0,125), (255,255), (255,0,125), 10)


#REctangle - accept parameter(img,start_co, end_co,colot, thickness)
img = cv2.rectangle(img, (100,10), (510, 500), (128, 0, 255), 8)


#Circle - accepts (img, star_co, color, thickness)
img = cv2.circle(img, (447,125), 63, (214, 255, 0), -5)


font = cv2.FONT_ITALIC
#puttext - accept (img, text, start_co, font, fontscale, color, thickness)
img = cv2.putText(img, 'Sailu', (400,600),cv2.FONT_HERSHEY_SIMPLEX, 2, (0,180, 155), 5)

#Ellipse - accept(img, start_co, (length, height), color, thickness)
img = cv2.ellipse(img, (400,600),(100,50), 0, 0, 180,155,5)

cv2.imshow("colored image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

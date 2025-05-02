import cv2 as c
import numpy as np
from matplotlib import pyplot as plt

image = c.imread('Pic4.jpg')
image = c.cvtColor(image,c.COLOR_BGR2GRAY)

#hist = c.calcHist(image, channels, mask, histsize, ranges)
hist = c.calcHist([image],[0],None, [256],[0-255])

c.imshow('winname',image)
plt.plot(hist)
plt.show()
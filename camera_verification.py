#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 11:55:31 2020

@author: jacobksu
"""


import numpy as np
import cv2


cap = cv2.VideoCapture(0)

Fx = 1013.4176 #pixels
Fy = 1011.2264 #pixels
Or = 659.5295 #pixels
Oc = 355.5793 #pixels
r = 650     #pixels
c = 540     # pixels
z = 747.54 #pixels ### #1219.2 * .61314#mm to pixels 


def capture_img():
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            cv2.imwrite('rec.png',frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
           
                break
        else:
            break


def calculate_x_y(Or, Oc, r, c, Fx, Fy, z):
    x = ((Or - r)/Fx)*z
    y = ((Oc - c)/Fy)*z
    x = x/0.61314
    y = y/0.61314
    print (x, y ) 
    return (x,y)  
  
#capture_img()



calculate_x_y(Or, Oc, r, c, Fx, Fy, z)



cap.release()
cv2.destroyAllWindows()
## Load image
#im = cv2.imread('rec.png')
#
## Convert to grayscale and threshold
#imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
#ret,thresh = cv2.threshold(imgray,1,255,0)
#
## Find contours, draw on image and save
#if cv2.getVersionMajor() in [2, 4]:
#    # OpenCV 2, OpenCV 4 case
#    contours, hier = cv2.findContours(
#                    thresh.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
#else:
#    # OpenCV 3 case
#    image, contours, hier = cv2.findContours(
#                    thresh.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
#
##imgray, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(im, contours, -1, (0,255,0), 3)
#cv2.imwrite('result.png',im)
#
## Show user what we found
#for cnt in contours:
#   (x,y),radius = cv2.minEnclosingCircle(cnt)
#   center = (int(x),int(y))
#   radius = int(radius)
#   print('Contour: centre {},{}, radius {}'.format(x,y,radius))
#   
#cap.release()
#cv2.destroyAllWindows()
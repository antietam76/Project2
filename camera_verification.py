#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 11:55:31 2020

@author: jacobksu
"""


import numpy as np
import cv2
import matplotlib.pyplot as plt
#import sympy as sym

cap = cv2.VideoCapture(0)

Fx = 1013.4176 #pixels
Fy = 1011.2264 #pixels
#Or = 659.5295 #pixels
#Oc = 355.5793 #pixels
#r = 650     #pixels
#c = 540     # pixels
#z = 747.54 #pixels ### #1219.2 * .61314#mm to pixels 
R = np.array([[-0.9995, -0.0135, -0.0293],
               [0.0110, -0.9966,  0.0812],
              [-0.0303,  0.0809,  0.9963],
              [96.1631,  330.2148, 1359.4]])
K = np.array([[1385.5868,    0,         0],
              [0,        1377.2714,     0],
              [648.061,    264.0641,     1]])
Z = [-150, -70, -150, -80, 0]

#x = sym.Symbol('x')
#y = sym.Symbol('y')


    

ret, frame = cap.read()


plt.figure(0)
plt.clf()
plt.imshow(frame)
            
source = np.asarray(plt.ginput(1),np.float32)
#            if cv2.waitKey(1) & 0xFF == ord('q'):
#     
r = source[0,0]
c = source [0,1]   
i_f =np.array([[r, c, 1]])   

 
for z in Z:
    C= np.array([[1, 1, z, 1]])
    aall = C.dot(R.dot(K))
    wow = np.linalg.solve(aall,np.transpose(i_f))
 
cap.release()

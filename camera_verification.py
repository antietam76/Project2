#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 11:55:31 2020

@author: Jacob Burnett, Sam Epeagba, Yueyan Yang
"""

## Click the center of the power supply 
## where the two pieces of tape meet. 
import numpy as np
import cv2
import matplotlib.pyplot as plt

image = (["/home/jacobksu/Pictures/1.jpg","/home/jacobksu/Pictures/2.jpg","/home/jacobksu/Pictures/3.jpg","/home/jacobksu/Pictures/4.jpg","/home/jacobksu/Pictures/5.jpg"])
for i in image:
    g = cv2.imread(i)
    
    Fx = 1385.5868 #pixels
    Fy = 1377.2714 #pixels
    Or = 648.061 #pixels
    Oc = 264.0641 #pixels
    z = 1260 
    H_matrix = np.array([[-0.9995, -0.0135, -0.0293, 96.1631 ],
                         [0.0110,  -0.9966,  0.0812, 330.2148],
                         [-0.0303,  0.0809,  0.9963, 1359.4  ],
                         [0,        0,       0,      1    ]])
        
    plt.figure(0)
    plt.clf()
    plt.imshow(g)
                
    source = np.asarray(plt.ginput(1),np.float32)
    
    r = source[0,0]
    c = source [0,1]   
    i_f =np.array([[r, c, 1]])   
    print("Object Coordinates", str(r) + ', ' + str(c))
     
    
    x = z * ((Or - r)/Fx)
    y = z * ((Oc - c)/Fy)
    cF_coord = [[x], [y], [z], [1]]
    cFrame = np.array(cF_coord)
    wFrame = np.multiply(cFrame, H_matrix)
    
    print("The x coordinate is: " + str(wFrame[0][0]))
    print("The y coordinate is: " + str(wFrame[0][1]))
    
    
     
    plt.clf()
#K = np.array([[1385.5868,    0,         0],
    #              [0,        1377.2714,     0],
    #              [648.061,    264.0641,     1]])
    #Z = [-150, -70, -150, -80, 0]
    
    #x = sym.Symbol('x')
    #y = sym.Symbol('y')
    
    #ret, frame = cap.read()
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 11:42:44 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt


#Define all variables
W1 = 10
W2 = 20
L1 = 3
L2 = 4
L3 = 4
L = 8

x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
x6 = 0
x7 = 0
x8 = 0
x9 = 0

y1 = L
y2 = 0 
y3 = 1
y3 = 1
y4 = 1
y5 = 1
y6 = 0
y7 = 0
y8 = 0
y9 = 0 


#define functions 
y1 = L1*(np.cos(th1)) + L2*(np.cos(th2)) + L3*(np.cos(th3))
y2 = L1*(np.sin(th1)) + L2*(np.sin(th2)) + L3*(np.sin(th3))
y3 = np.sin(th1)**2 + np.cos(th1)**2
y4 = np.sin(th2) + np.cos(th2)**2
y5 = np.sin(th3)**2 + np.cos(th3)**2
y6 = T1*(np.sin(th1)) - T2*(np.sin(th2)) - W1
y7 = T1*(np.cos(th1)) - T2*(np.cos(th2))
y8 = T2*(np.sin(th1)) + T3*(np.sin(th3)) - W2
y9 = T2*(np.cos(th2)) + T3*(np.cos(th3)) 

#find the partials for the functions per y
yy1 = 0 + 0 + 0 + L1 + L2 + L3 + 0 + 0 + 0 
yy2 = L1 + L2 + L3 + 0 + 0 + 0 + 0 + 0 + 0
yy3 = 2sin(th1) + 2cos(th1) + 0 + 0 + 0 + 0 + 0 + 0 + 0
yy4 = 2sin(th2) + 2cos(th2) + 0 + 0 + 0 + 0 + 0 + 0 + 0
yy5 = 2sin(th3) + 2cos(th3) + 0 + 0 + 0 + 0 + 0 + 0 + 0
yy6 = T1 - T2 +0 + 0 + 0 + 0 + sin(th1) - sin(th2)
yy7 = 0 + 0 + 0 + T1 - T2 + 0 + cos(th1) - cos(th2) + 0
yy8 = 0 + T2 + T3 + 0 + 0 + 0 + sin(th3) + sin(th3) + 0
yy9 = 0 + 0 + 0 + 0 + T2 - T3 + 0 + cos(th2) - cos(th3)

print(yy1,yy2,yy3,yy4,yy5,yy6,yy7,yy8,yy9)






# Other functions to use:
y1 = 3*x4 + 4*x5 + 4* x6 - 8
y2 = 3*x1 + 4*x2 - 4*x3
y3 = x7*x4 - x8*x2 - 10
y4 = x7*x4 - x8*x5
y5 = x8*x2 + x9*x3 - 20
y6 = x8*x5 - x9*x6
y7 = x1**2 + x4**2 - 1
y8 = x2**2 + x5**2 - 1
y9 = x3**2 + x6**2 - 1

#find the partials of the functions per y:
dy1 = 0 + 0 + 0 + 3 + 4 + 4 + 0 + 0 + 0
dy2 = 3 + 4 -4 + 0 + 0 + 0 + 0 + 0 + 0
dy3 = 0 + x8 + 0 + x7 + 0 + 0 + x4 + x2 + 0
dy4  = 0 + 0 + 0 + x7 + x8 + 0 + x4 + x5 + 0
dy5 = 0 + x8 + x9 + 0 + 0 + 0 + 0 + x2 + x6
dy6 = 0 + 0 + 0 + 0 + x8 + x9 + 0 +x5 + x6 
dy7 = 2*x1 + 0 + 0 + 2*x4 + 0 + 0 + 0 + 0 + 0
dy8 = 0 + 2*x2 + 0 + 0 + 2* x5 + 0 + 0 + 0 + 0
dy9 = 0 + 0 + 3*x3 + 0 + 0 + 2*x6 + 0 + 0 + 0 

print(dy1, dy2, dy3, dy4, dy5, dy6, dy7, dy8, dy9)














          
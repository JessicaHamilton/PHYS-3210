# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 11:42:44 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt


#Define all known variables
W1 = 10
W2 = 20
L1 = 3
L2 = 4
L3 = 4
L = 8

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


#unknow variables and the initial guesses
th1=30
th2=15
th3=50
T1=1
T2=1
T3=1 


#Variables for functions
a = np.sin(th1)
b = np.sin(th2)
c = np.sin(th3)
d = np.cos(th1)
e = np.cos(th2)
f = np.cos(th3)



#define functions 
y1 = L1*d + L2*e + L3*f
y2 = L1*a + L2*b + L3*c
y3 = a**2 + d**2
y4 = b**2 + e**2
y5 = c**2 + f**2
y6 = T1*a - T2*b - W1
y7 = T1*d - T2*e
y8 = T2*a + T3*c - W2
y9 = T2*e + T3*f

#find the partials for the functions per y
yy1 = 0 + 0 + 0 + L1 + L2 + L3 + 0 + 0 + 0 
yy2 = L1 + L2 + L3 + 0 + 0 + 0 + 0 + 0 + 0
yy3 = 2*a + 2*d + 0 + 0 + 0 + 0 + 0 + 0 + 0
yy4 = 2*b + 2*e + 0 + 0 + 0 + 0 + 0 + 0 + 0
yy5 = 2*c + 2*f + 0 + 0 + 0 + 0 + 0 + 0 + 0
yy6 = T1 - T2 +0 + 0 + 0 + 0 + a - d
yy7 = 0 + 0 + 0 + T1 - T2 + 0 + d - e + 0
yy8 = 0 + T2 + T3 + 0 + 0 + 0 + b + c + 0
yy9 = 0 + 0 + 0 + 0 + T2 - T3 + 0 + e - f

#print(yy1,yy2,yy3,yy4,yy5,yy6,yy7,yy8,yy9)

jac = [[L1 + L2 + L3][L1+L2+L3][2*a+2*d][2*b+2*e][T1-T2+a-d][T1-T2+d-e][T2+T3+b+c][T2-T3+e-f]]
















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














          
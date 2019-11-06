# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 10:39:16 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt




#Outside of boundaries
#from left

k_sq = 2
m=1
x_match = 1
a = 2 
h=0.1
y_array = []
x_array = []
V_o = -83.0 
V = 0
ynew = 0
xnew = -20
x_array = np.arange(-20,20,h)
for value in x_array:
    if abs(value) <= a:
        ynew = ynew + ((-0.0483*V_o*ynew + k_sq*ynew)/m)*h
    elif abs(value) > a:
        ynew = -k_sq*np.exp((-k_sq)*abs(value))
        
    
    #update values and append to an array
    y_array.append(ynew)

plt.plot(x_array, y_array)
plt.show() 






#Just looking out out function
x = np.arange(-20,20,0.1)
yy = []
for each in x:
    y = -k_sq*np.exp((-k_sq)*abs(each))
    yy.append(y)
plt.plot(x,yy)




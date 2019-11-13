# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 10:04:39 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#define variables
m = 0.5
delta_b = 0.05
b = 0.25 # between -1 and 1
next_x = 1
next_y = 1
next_vx = 0
next_vy = 0.5
h = 0.0001



#Define array
x_arr = []
y_arr = []
vx_arr = []
vy_arr = []


#begin loop
time = np.arange(0,50,h)
for t in time:
    #define functions
    F_x = 2*next_x*next_y**2*(1-next_x**2)*np.exp(-1*(next_x**2+next_y**2))
    F_y = 2*next_y*next_x**2*(1-next_y**2)*np.exp(-1*(next_x**2+next_y**2))
    
    #update values
    next_vx = next_vx + F_x*h
    next_vy = next_vy + F_y*h
    next_x = next_x + next_vx*h
    next_y = next_y + next_vy*h
    
    #append new values
    x_arr.append(next_x)
    y_arr.append(next_y)
    vx_arr.append(next_vx)
    vy_arr.append(next_vy)
    #theta = np.arctan(next_vy/next_vx)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_arr,y_arr, time)
plt.show()


plt.plot(time, x_arr)
plt.title('Position-X vs Time')
plt.show()
plt.plot(time, y_arr)
plt.title('Position-Y vs Time')
plt.show()
plt.plot(time, vx_arr)
plt.show()
plt.plot(time, vx_arr)
plt.show()


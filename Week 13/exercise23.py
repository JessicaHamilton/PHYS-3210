# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 10:04:39 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt

#define variables
m = 0.5
delta_b = 0.05
b = 0.25 # between -1 and 1
next_x = 0
next_y = 0
next_vx = 0
next_vy = 0.5


#define functions
y_0 = x
y_1 = y
y_2 = 2*y_1**2*y_0*(1-y_0**2)*np.exp(-(y_0**2+y_1**2))
y_3 = 2*y_0**2*y_1**2*(1-y_1**2)*np.exp(-(y_0**2+y_1**2))

#Define array
x_arr = []
y_arr = []
vx_arr = []
vy_arr = []


#begin loop
time = np.arange(0,100, 0.001)
for t in time:
    next_x = next_x + (next_x*np.cos(theta))+((y_2*np.cos(theta))/m*(delta_b))
    x_arr.append(next_x)
    next_y = next_y + (y_1*np.sin(theta))+((y_3*np.sin(theta))/m*(delta_b))
    y_arr.append(next_y)
    next_vx = next_vx + next_vx*np.cos(theta)
    vx_arr.append(next_vx_arr)
    next_vy = next_vy + next_vy*np.sin(theta) + y_3/m*(delta_b)
    vy_arr.append(next_vy_arr)
    theta = np.arctan(next_vy/next_vx)

plt.plot(x_arr, y_arr)



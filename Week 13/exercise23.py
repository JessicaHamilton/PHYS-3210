# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 10:04:39 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#define variables
m = 0.1
next_x = -0.25
next_y = .15
b = np.sqrt(next_x**2+ next_y**2)
next_vx = 0.001
next_vy = 0.1
h = 0.0001

#best values thus far: x=-0.25, y=0.15, vx=0.001, vy=0.1

#Define array
x_arr = []
y_arr = []
vx_arr = []
vy_arr = []
pot_arr = []
count = 0
#begin loop
time = np.arange(0,200,h)
for t in time:
    if b < 0.95:
        #define functions
        F_x = -2*next_x*next_y**2*(1-next_x**2)*np.exp(-1*(next_x**2+next_y**2))
        F_y = -2*next_y*next_x**2*(1-next_y**2)*np.exp(-1*(next_x**2+next_y**2))
        
        #update values
        next_vx = next_vx + (F_x/m)*h
        next_vy = next_vy + (F_y/m)*h
        next_x = next_x + next_vx*h
        next_y = next_y + next_vy*h
        
        
        #append new values
        x_arr.append(next_x)
        y_arr.append(next_y)
        vx_arr.append(next_vx)
        vy_arr.append(next_vy)
        
        
    else:
        break

#Calculate potential function and values
#Potential func
x_values = np.arange(-4,4.01,0.01)
y_values = np.arange(-4,4.01,0.01)
x_v, y_v = np.meshgrid(x_values,y_values)
def potential(x,y):
    return (x**2*y**2)*np.exp(-1*(x**2+y**2))

z_v = potential(x_v,y_v)
#plot function
fig, ax = plt.subplots(1, 1)
ax.contourf(x_v, y_v, z_v, 10, cmap='Oranges')






plt.plot(x_arr,y_arr)
plt.title('Position-Y vs Position-X')
plt.show()
plt.plot(vx_arr, x_arr)
plt.title('Velocity-X vs. Position-X')
plt.show()
plt.plot(vy_arr, y_arr)
plt.title('Velocity-Y vs. Position-Y')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_arr,y_arr, time)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Time')
plt.show()


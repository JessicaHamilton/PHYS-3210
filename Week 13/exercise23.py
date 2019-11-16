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
        
        #Potential func
        poten = (next_x**2*next_y**2)*np.exp(-1*(next_x**2+next_y**2))
        pot_arr.append(poten)
        
        
        #append new values
        x_arr.append(next_x)
        y_arr.append(next_y)
        vx_arr.append(next_vx)
        vy_arr.append(next_vy)
        
    else:
        break

#print(pot_arr)
#ax.contourf((x_arr, y_arr), pot_arr, 10, cmap='Oranges')
#plt.show()




"""
plt.plot(time, x_arr)
plt.title('Position-X vs Time')
plt.show()
plt.plot(time, y_arr)
plt.title('Position-Y vs Time')
plt.show()
plt.plot(time, vx_arr)
plt.title('Velocity-X vs. Time')
plt.show()
plt.plot(time, vy_arr)
plt.title('Velocity-Y vs. Time')
plt.show()
"""
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


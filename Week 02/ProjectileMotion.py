# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:14:27 2019

@author: hamil
"""
import numpy as np
import matplotlib.pyplot as plt


def projectile(mass,initial_pos,initial_v, launch_angle):
    force_g = 9.8
    time = np.arange(0,100,1)
    final_x_array =[]
    final_y_array =[]
    velocity_x_array =[]
    velocity_y_array =[]
    total_time = 0
    change_time = 0.1
    for each_time in time:
        #calculate output variables and append to array
        final_x = (initial_pos*np.cos(launch_angle))+((initial_v*np.cos(launch_angle))*(change_time))
        final_x_array.append(final_x)
        final_y = (initial_pos*np.sin(launch_angle))+((initial_v*np.sin(launch_angle))*(change_time))
        final_y_array.append(final_y)
        velocity_x = initial_v*np.cos(launch_angle)
        velocity_x_array.append(velocity_x)
        velocity_y = (initial_v*np.sin(launch_angle))+((-(force_g)/mass)*change_time)
        velocity_y_array.append(velocity_y)
        
        #re-define input variables
        initial_v = -(initial_pos*np.sin(launch_angle))+(1(initial_v*np.sin(launch_angle)*change_time))
        initial_pos = np.sqrt(final_y**2 + final_x**2)
        #initial_v = np.sqrt(velocity_y**2 + velocity_x**2)
        #print(initial_v)
        if final_y <= 0:
            break
    total_time = each_time - 0
    #final_x_array = np.unique(final_x_array)
    final_y_array = np.unique(final_y_array)
    return final_x_array,final_y_array,velocity_x_array, velocity_y_array, total_time

test1 = projectile(5,0,10,np.radians(30))
#print(test1[0])
x_values = test1[0]
y_values = test1[1]
plt.scatter(x_values,y_values, s=2)
    
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:14:27 2019

@author: hamil
"""
import numpy as np
import matplotlib.pyplot as plt


def projectile(mass,initial_pos,initial_v, launch_angle):
    force_g = 9.8
    speed_c = 3.0e08
    time = np.linspace(0,50,0.1)
    final_x_array =[]
    final_y_array =[]
    velocity_x_array =[]
    velocity_y_array =[]
    change_time = time[1]-time[0]
    for each_time in time:
        #calculate output variables
        final_x = (initial_pos*np.cos(launch_angle))+((initial_v*np.cos(launch_angle))*change_time)
        final_y = (initial_pos*np.sin(launch_angle))+((initial_v*np.sin(launch_angle))*change_time)
        if final_y < 0:
            continue
        velocity_x = initial_v*np.cos(launch_angle)
        velocity_y = (initial_v*np.sin(launch_angle))+((-(force_g)/mass)*change_time)
        #re-define input variables
        initial_pos = np.tan(final_y/final_x)
        initial_v = np.tan(velocity_y/velocity_x)
        #append to arrays
        final_x_array.append(final_x)
        final_y_array.append(final_y)
        velocity_x_array.append(velocity_x)
        velocity_y_array.append(velocity_y)
    total_time = each_time - time[0]
    return final_x_array,final_y_array,velocity_x_array, velocity_y_array, total_time

test1 = projectile(5,5,10,15)
x_values = test1['final_x_array']
y_values = test1['final_y_array']
plt.scatter(x_values,y_values)
    
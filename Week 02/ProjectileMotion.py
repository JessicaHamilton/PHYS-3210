# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:14:27 2019

@author: hamil
"""
import numpy as np
import matplotlib.pyplot as plt


def projectile(mass,initial_pos,initial_v, launch_angle):
    force_g = 9.8
    final_x_array =[]
    final_y_array =[]
    velocity_x_array =[]
    velocity_y_array =[]
    total_time = 0
    change_time = 0.1
    #calculate output variables and append to array
    final_x = (initial_pos*np.cos(launch_angle))+((initial_v*np.cos(launch_angle))*(change_time))
    final_x_array.append(final_x)
    final_y = (initial_pos*np.sin(launch_angle))+((initial_v*np.sin(launch_angle))*(change_time))
    final_y_array.append(final_y)
    velocity_x = initial_v*np.cos(launch_angle)
    velocity_x_array.append(velocity_x)
    velocity_y = (initial_v*np.sin(launch_angle))+((-(force_g)/mass)*change_time)
    velocity_y_array.append(velocity_y)
    time = np.arange(0,100,0.1)
    for each_time in time:
        final_x= final_x+velocity_x*change_time
        final_x_array.append(final_x)
        final_y = final_y+velocity_y*change_time
        final_y_array.append(final_y)
        velocity_x = velocity_x
        velocity_x_array.append(velocity_x)
        velocity_y= velocity_y+(-force_g/mass)*change_time
        velocity_y_array.append(velocity_y)
        total_time = each_time + 0.1
        if final_y <= 0:
            break
    return final_x_array, final_y_array, total_time


test1 = projectile(5,0,10,np.radians(15))
test2 = projectile(5,0,10,np.radians(30))
test3 = projectile(5,0,10,np.radians(45))

print("total time:", test1[2])
plt.scatter(test1[0],test1[1], s=2, label = "15 deg Launch")
plt.scatter(test2[0], test2[1], s=2, label = "30 deg Launch")
plt.scatter(test3[0],test3[1], s=2, label = "45 deg Launch")
plt.title("Trajectory of projectile at 15, 30 and 45 Degrees")
plt.xlabel("Position in X")
plt.ylabel("Position in Y")
plt.legend()
plt.show()

#Now add in air resistance/Drag and run same tests

def projectile(mass,initial_pos,initial_v, launch_angle):
    force_g = 9.8
    c = 3.0e08
    final_x_array =[]
    final_y_array =[]
    velocity_x_array =[]
    velocity_y_array =[]
    total_time = 0
    change_time = 0.1
    #calculate output variables and append to array
    final_x = (initial_pos*np.cos(launch_angle))+((initial_v*np.cos(launch_angle))*(change_time))
    final_x_array.append(final_x)
    final_y = (initial_pos*np.sin(launch_angle))+((initial_v*np.sin(launch_angle))*(change_time))
    final_y_array.append(final_y)
    f_dragx = c*(initial_v*np.cos(launch_angle)**2)
    f_dragy = c*(initial_v*np.sin(launch_angle)**2)
    velocity_x = (initial_v*np.cos(launch_angle))+(f_dragx/mass)*change_time
    velocity_x_array.append(velocity_x)
    velocity_y = (initial_v*np.sin(launch_angle))+((f_dragy-force_g)/mass)*change_time
    velocity_y_array.append(velocity_y)
    time = np.arange(0,100,0.1)
    for each_time in time:
        final_x= final_x+velocity_x*change_time
        final_x_array.append(final_x)
        final_y = final_y+velocity_y*change_time
        final_y_array.append(final_y)
        f_dragx = c*(velocity_x**2)
        f_dragy = c*(velocity_y**2)
        velocity_x = velocity_x+(f_dragx/mass)*change_time
        velocity_x_array.append(velocity_y)
        velocity_y= velocity_y+((f_dragy-force_g)/mass)*change_time
        velocity_y_array.append(velocity_y)
        total_time = each_time + 0.1
        if final_y <= 0:
            break
    return final_x_array, final_y_array, total_time


test1 = projectile(5,0,10,np.radians(15))
test2 = projectile(5,0,10,np.radians(30))
test3 = projectile(5,0,10,np.radians(45))

print("total time:", test1[2])
plt.scatter(test1[0],test1[1], s=2, label = "15 deg Launch")
plt.scatter(test2[0], test2[1], s=2, label = "30 deg Launch")
plt.scatter(test3[0],test3[1], s=2, label = "45 deg Launch")
plt.title("Trajectory of projectile with added drag")
plt.xlabel("Position in X")
plt.ylabel("Position in Y")
plt.legend()


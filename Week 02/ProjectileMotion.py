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
    return final_x_array, final_y_array, total_time, final_x


test_1 = projectile(5,0,10,np.radians(15))
test_2 = projectile(5,0,10,np.radians(30))
test_3 = projectile(5,0,10,np.radians(45))
test_4 = projectile(5,0,10,np.radians(60))

print("Final x position:", test_1[3])
print("total time for test1:", test_1[2])
print("Total time for test2:", test_2[2])
print("Total time for test3:", test_3[2])
print("Total time for test4:", test_4[2])
plt.scatter(test_1[0],test_1[1], s=3, label = "15 deg Launch")
plt.scatter(test_2[0], test_2[1], s=3, label = "30 deg Launch")
plt.scatter(test_3[0],test_3[1], s=3, label = "45 deg Launch")
plt.scatter(test_4[0],test_4[1], s=3, label = "60 deg Launch")
plt.title("Trajectory of 5kg projectile at 15, 30, 45, and 60 Degrees")
plt.xlabel("Position in X")
plt.ylabel("Position in Y")
plt.legend()
plt.savefig("ProjectileMotionPart1.pdf")
plt.show()

#Now add in air resistance/Drag and run same tests

def projectile(mass,initial_pos,initial_v, launch_angle):
    force_g = 9.8
    c = 2.0e-03
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
    return final_x_array, final_y_array, total_time,velocity_y_array


test1 = projectile(6,0,10,np.radians(15))
test2 = projectile(6,0,10,np.radians(30))
test3 = projectile(6,0,10,np.radians(45))


print("total time for test1:", test1[2])
print("Total time for test2:", test2[2])
print("Total time for test3:", test3[2])
plt.scatter(test_1[0],test_1[1], s=3, c= "#BB8FCE")
plt.scatter(test_2[0], test_2[1], s=3, c="#3498DB")
plt.scatter(test_3[0],test_3[1], s=3, c= "#5B2C6F")
plt.scatter(test1[0],test1[1], s=2, c= "#BB8FCE", label = "15 deg Launch")
plt.scatter(test2[0], test2[1], s=2, c= "#3498DB", label = "30 deg Launch")
plt.scatter(test3[0],test3[1], s=2, c= "#5B2C6F", label = "45 deg Launch")
plt.title("Trajectory of 8 kg projectile with added drag")
plt.xlabel("Position in X")
plt.ylabel("Position in Y")
plt.xlim(0,110)
plt.ylim(0,30)
plt.legend()
plt.savefig("ProjectileMotionPart2.pdf")

x =10*np.cos(np.radians(15))*(2.7)
print(x)
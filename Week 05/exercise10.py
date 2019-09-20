# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 10:09:32 2019

@author: hamil
"""

import random as rand
import numpy as np
import matplotlib.pyplot as plt


#create the a and y values for the square
N = 2000000
N_pond = N
x = []
y = []
y_circle = []
for n in range(N):
        x.append((rand.random() - 0.5)*2.0)
        y.append((rand.random() - 0.5)*2.0)

x = np.array(x)
y = np.array(y)
xy_array=[x,y]

plt.scatter(x,y, color='blue', s=2)


#Calculate distance for each point from square's center  
for each in xy_array:
    value1 = np. square(xy_array[0])
    value2 = np.square(xy_array[1])
    dist_array = np.sqrt(value1 + value2)
    for value in dist_array:
        if value <= 1:
            N_pond = N_pond + 1
#plt.scatter(xy_array[0], xy_array[1], color = 'pink')
    
"""    
x = np.square(x)
y = np.square(y)
dist_array = np.sqrt(x + y)


#add more points to N_pond for less than 1
N_pond = N
for number in dist_array:
    if number <= 1:
        N_pond = N_pond + 1

"""        
ratio = N_pond / N
print("Ratio of N_pond / N, approx for pi:", ratio)

    
    


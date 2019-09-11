# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 10:22:47 2019

@author: hamil
"""

import random as rand
import numpy as np
import matplotlib.pyplot as plt

#Define the x,y,N initilize the coordinate array
x = 0
y = 0
x_y_array = [[0,0]]
N = 40
#loop for determining the new coordinates
for each_value in range(N):
    #define the random int for x and y = to -1,0,1
    x_next = rand.randint(-1,1)
    y_next = rand.randint(-1,1)
    
    # the two do not match:
    if abs(x_next) != abs(y_next):
        x_maybe = x + x_next
        y_maybe = y + y_next
        if abs(x_maybe) <= 5 or abs(y_maybe) <=5:
            coord = [x_maybe,y_maybe]
            if coord in x_y_array:
                continue
            else:
                x = x_maybe
                y = y_maybe
                x_y_array.append(coord)

print("This is the array of coordinates:", x_y_array)
x_y_array = np.array(x_y_array)
x_values = x_y_array[:,0]
y_values = x_y_array[:,1]
plt.plot(x_values, y_values)
plt.title("Random Walker Self-Avoiding Path")
plt.show()
    
        
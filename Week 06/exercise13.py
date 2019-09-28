# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:01:04 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rand

N = 50
funct_array = []
random_array= []
x_array = []
y_array = []
y1_array = []
for numbers in range(N):
    #define function to relate back to with random point
    x = rand.uniform(0,10)
    x_array.append(x)
    #generate corresponding y value for function
    y = x**2
    point = [x,y]
    funct_array.append(point)
    #now generate random y value to compare
    y1 = rand.uniform(1,100)
    if y > y1:
        y1_array.append(y1)
    else:
        y_array.append(y1)

print(len(x_array), len(y_array), len(y1_array))
#plt.scatter(x_array, y_array, s=2, color = 'blue')
#plt.scatter(x_array, y1_array,s=2,  color = 'green')






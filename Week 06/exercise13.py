# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:01:04 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rand

N = 500
funct_array = []
random_array= []
x_array = []
y_array = []
xy_array = []
xy2_array = []
y_array = rand.uniform(0,10,100)
for each in range(0,len(y_array)):
    x = rand.uniform(0,10)
    x_array.append(x)
    y = x**2
    if y >= each:
        xy = [x, each]
        xy_array.append(xy)
    else:
        xy2 = [x,each]
        xy2_array.append(xy)
        
print(len(x_array), len(y_array), len(xy_array), len(xy2_array))        
"""        
for numbers in range(N):
    #define function to relate back to with random point
    #calculate the two different y values in question
    #generate corresponding y value for function
    x = rand.uniform(0,10)
    x_array.append(x)
    y = rand.uniform(0,10)
    y_array.append(y)
    
"""



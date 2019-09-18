# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:09:32 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt

x_values = np.arange(0,20,1)
y_values = x_values**2

def integral_funct(h, initial, final):
    #determine the rectangle and the area using left side of rectangle
    value = y_values[0]
    area_array = []
    bound_array =np.arange(initial, final,1)
    for each_value in bound_array:
        area = 0.5*h*((value)**2)
        area_array.append(area)
        value = value + h
    total_sum = np.sum(area_array)
    return area_array, total_sum
    
test1 = integral_funct(0.5,0,10)
test1_area = test1[0]
print("This is the individual area array:",test1_area)
test1_sum = test1[1]  
print("This is the total area:",test1_sum)  
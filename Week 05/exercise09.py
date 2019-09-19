# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:09:32 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt

#Create function to take the integral of / area under the curve
x_values = np.arange(0,10,0.5)
y_values = x_values**2

#Define function that will use definition of the sum of the rectangle areas underneath curve
def integral_funct(h, initial, final):
    #determine the rectangle and the area using left side of rectangle
    area_array = []
    x_values = 
    y_values = x_values**2
    for each_num in y_values:
        area = each_num*h
        area_array.append(area)
    total_sum = np.sum(area_array)
    return area_array, total_sum
    
test1 = integral_funct(0.5,0,10)
test1_area = test1[0]
print("This is the individual area array:",test1_area)
test1_sum = test1[1]  
print("This is the total area:",test1_sum)  
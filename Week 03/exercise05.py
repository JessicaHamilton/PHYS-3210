# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 10:03:35 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt



def up_harmonic(value_n):
    H_up = 0.0
    summ_array1 = []
    new_x = value_n + 1
    x_array1 = np.arange(1,new_x)
    for each_value in x_array1:
        numm1 = 1/each_value
        H_up = H_up + numm1
        summ_array1.append(H_up)
    return H_up, summ_array1, x_array1
test = up_harmonic(20)
up_values = test[1]
x_values = test[2]
print("Sum up value is:", test[0]) 
print("The Up values are:", up_values)



def down_harmonic(value_n):
    H_down = 0.0
    summ_array2 = []
    new_x = value_n + 1
    x_array = np.arange(1,new_x)
    x_array2 = x_array[::-1]
    for each_value in x_array2:
        numm2 = 1/each_value
        H_down = H_down + numm2
        summ_array2.append(H_down)
    return H_down, summ_array2, x_array2

test1 = down_harmonic(20)
down_values = test1[1]
print("Sum down value is:", test1[0])
print("The down values are:", down_values)


x_values = np.arange(1,20)
#sub = np.subtract(up_values, down_values)
#abs_add = np.sum(np.abs(up_values), np.abs(down_values))
#fraction = sub / abs_add
#plt.plot(x_values,fraction)


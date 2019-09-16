# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:07:36 2019

@author: hamil
"""
import numpy as np
import matplotlib.pyplot as plt



#Step one create two arrays for x values and the sin of those x values
sinx_array = []
x_array = np.arange(-2*np.pi, 2*np.pi, np.pi/6)
for each_number in x_array:
    value = np.sin(each_number)
    sinx_array.append(value)



#create a function to derive the sin(x)

def deriv_function(funct, x_array, h):
    y_array = []
    for new_values in x_array:
        nummer = funct(new_values+h) - funct(new_values)
        result = nummer / h
        y_array.append(result)
        
    return y_array, result
    
value1,value2 = deriv_function(np.sin, x_array, 1)

#Compare with the numpy function for the gradient
def builtin_function(funct, x_array):
    y_array2 = []
    for each_number in x_array:
        new = np.gradient(funct(each_number))
        y_array2.append(new)
        
    return y_array2, new

value3, value4 = builtin_function(np.sin, x_array)
print(value3)


plt.plot(x_array, value3, color = "purple", label = "Python's Gradient Function")
plt.plot(x_array, value1,color = 'blue', label = "Forward Difference")
plt.plot(x_array, sinx_array, color= 'green', label= "Python's Sin Function")
plt.legend()






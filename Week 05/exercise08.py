# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:07:36 2019

@author: hamil
"""
import numpy as np
import matplotlib.pyplot as plt



#Step one create two arrays for x values and the sin of those x values
sinx_array = []
cosx_array = []
x_array = np.arange(-2*np.pi, 2*np.pi, np.pi/6)
for each_number in x_array:
    sin_value = np.sin(each_number)
    sinx_array.append(sin_value)
    cos_value = np.cos(each_number)
    cosx_array.append(cos_value)



#create a function to derive the sin(x)
def deriv_function(funct, x_array, h):
    y_array = []
    for new_values in x_array:
        value_H = funct(new_values + h)
        value = funct(new_values)
        nummer = value_H - value
        result = nummer / h
        y_array.append(result)
        
    return y_array, result
    
value1,value2 = deriv_function(np.sin, x_array, 1)

#Calculate the gradient of the x values
value3 = np.gradient(np.sin(x_array))

#Compare with the numpy function for the gradient
plt.plot(x_array, value33, color = "purple", label = "Python's Gradient Function")
plt.plot(x_array, value1, color = 'blue', label = "Forward Difference")
plt.plot(x_array, sinx_array, color= 'green', label= "Python's Sin Function")
plt.plot(x_array, cosx_array, color = 'red', label= "Python's Cos Function")
plt.legend()
plt.title("Comparing The Three functions")
plt.show()

#Determine the relative error for each function
forward_error = []
gradient_error = []

top1 = np.subtract(value1, cosx_array)
top2 = np.subtract(value3, cosx_array)
forward_error = abs(top1)/cosx_array
gradient_error = abs(top2)/cosx_array

plt.plot(forward_error, cosx_array)
plt.plot(gradient_error, cosx_array)
plt.title("Relative Error versus Exact value")




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
plt.plot(x_array, value3, color = "purple", label = "Python's Gradient Function")
plt.plot(x_array, value1, color = 'blue', label = "Forward Difference")
plt.plot(x_array, sinx_array, color= 'green', label= "Python's Sin Function")
plt.plot(x_array, cosx_array, linestyle= 'dashed', color = 'gray', label= "Python's Cos Function")
plt.legend()
plt.title("Comparing Three functions for First Deratives")
plt.show()

#Determine the relative error for each function
forward_error = []
gradient_error = []

absolute1 = np.subtract(value1, cosx_array)
absolute2 = np.subtract(value3, cosx_array)
condition = absolute2 <= 10**-13
condition |= absolute1 <=10**-13
absolute2[condition]= 0
absolute1[condition] = 0


forward_error = np.divide(absolute1,cosx_array)
gradient_error = np.divide(absolute2, cosx_array)


plt.errorbar(x_array, value3, yerr=gradient_error)
plt.errorbar(x_array, value1, yerr=forward_error)
plt.title("Relative Error for First Derative")
plt.show()


#Now compute the second deratives using both ways and plot to compare
value5, value6 = deriv_function(np.cos, x_array,1)
value7 = np.gradient(np.cos(x_array))
negsinx_array = np.negative(sinx_array)

#now comute the relative error for this group
absolute3 = np.subtract(value5,negsinx_array)
absolute4 = np.subtract(value7, negsinx_array)
forward_err = np.divide(value5, negsinx_array)
gradient_err = np.divide(value7,negsinx_array)

plt.plot(x_array, value7, color = "purple", label = "Python's Gradient Function")
plt.plot(x_array, value5, color = 'blue', label = "Forward Difference")
plt.plot(x_array, negsinx_array, color= 'green', label= "Python's Neg. Sin Function")
plt.plot(x_array, cosx_array, linestyle = 'dashed', color = 'gray', label= "Python's Cos Function")
plt.legend()
plt.title("Comparing Three functions for Second Deratives")
plt.show()

plt.errorbar(x_array, value5, yerr = forward_err)
plt.errorbar(x_array, value7, yerr= gradient_err)
plt.title("Relative Error for Second Derative")


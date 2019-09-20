# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:09:32 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import integrate

#Create function to take the integral of / area under the curve
#x_values = np.arange(0,10,0.1)
#y_values = x_values**2

#Define function that will use definition of the sum of the rectangle areas underneath curve
def integral_funct(h, initial, final):
    #determine the rectangle and area using left side y-value of rectangle
    area_array = []
    y_values = []
    x_values = np.arange(initial,final,0.1)
    for numm in x_values:
        new_value = numm**2
        y_values.append(new_value)
    y_values = y_values[:-1]
    total_sum = np.sum(area_array)
    for each_num in y_values:
        area = h*each_num
        area_array.append(area)
    total_sum = np.sum(area_array)
    return area_array, total_sum

#Test the integral function for x**2 from x=1 to x=10

test1 = integral_funct(0.01,0,10)
test1_area = test1[0]
#print("This is the individual area array:",test1_area)
#test1_sum = test1[1]  
print("Total area calculated by my function:",test1_sum)  

#This is not as close in value as I thought it would be. Analytically, the value
#for the example test is about 333.33. 

#Now compare to the trapz function
test_trapz = np.trapz(y_values,x_values, dx=0.01)
print("Total integral calculated by the Numpy's Trapz funct:",test_trapz)

#This is a better comparison to my function versus the analytical value. The value
#provided by the trapz is in between the two other values.

#Now use different functions from scipy to compute the integral
attempt1 = scipy.integrate.trapz(y_values,x_values, dx=0.01)
attempt2 = scipy.integrate.simps(y_values,x_values, dx=0.01)
def x_squared(x):
    y = x**2
    return y
attempt3 = scipy.integrate.romberg(x_squared, a=0, b=10)
#sum_attempt3 = np.sum(attempt3)

print("The integral calculated by the Scipy trapz funct:", attempt1)
print("The integral calculated by the Scipy simps funct:", attempt2)
print("The integral calculated by the Scipy romberg function:", attempt3)

#Here we can see the the two scipy functions trapz and simps have similiar values 
#as the numpy trapz which is not too far off from my function. But the Scipy 
#romberg function actually provides the calculated answer for the analytical value



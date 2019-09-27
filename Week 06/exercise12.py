# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 10:11:39 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rand
from numpy import histogram as hist



#define a function that will take previous mean value function to N-D
def meanvalue_Int(N, initial,final):
    #for loop for N-D
    sum_array = []
    mean_array = []
    x_array = []
    y_array = []
    for n in range(N):
        #Generate the sampling values for x  and calculate y values
        #for n in range(N):
        x = rand.uniform(initial,final)
        x_array.append(x)
        sum_x = np.sum(x)
        y = sum_x**2
        y_array.append(y)
        
    #calculate mean value and append to array
    mean_some = 1
    y_mean = np.sum(y)
    result = 1*y_mean
    """
    first = y_array[0]
    last = y_array[-1]
    mean_value = abs(last - first)
    mean_array.append(mean_value)
        
    total_mean = np.prod(mean_array)
    total_sum = np.sum(sum_array)
    result = (total_mean*total_sum)/N
    """
    return y_mean, result, x_array, #y_array
    
    

a,aa,aaa = meanvalue_Int(1000,0,10)
b,bb,bbb = meanvalue_Int(1000,0,10)
c,cc,ccc = meanvalue_Int(1000,0,10)
d,dd,ddd = meanvalue_Int(1000,0,10)

print(a,b,c,d)
#print(aaa)

    
 
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
    D = 10
    #set up iteration for function
    for numm in range(N):
        #Generate the sampling values for x
        for s in range(final):
            x = rand.uniform(initial,final,final)
            #x_array.append(x)
        #sum the x values
        sum_x = np.sum(x)
        #square the sum to find y_value
    y = sum_x**2
    result = y/N
    return result,x


##Testing function 
a = meanvalue_Int(100,0,10)
b = meanvalue_Int(100,0,10)
c = meanvalue_Int(100,0,10)
d = meanvalue_Int(100,0,10)

print("This is the results for four different runs:",a,b,c,d)

#The analytical solution is 25.83333. This shows that my function will be relatively close to the 
#the value, but not very precise. My numbers ranging from 17 to 30. 

#Getting an average value for 50 runs.
total_array =[]
for values in range(50):
    new = meanvalue_Int(100,0,10)
    total_array.append(new)
    ave_ans = np.mean(total_array)
print("This is the average value for 50 runs:", ave_ans)

    
 
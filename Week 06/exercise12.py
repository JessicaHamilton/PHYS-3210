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
    return result


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
ave_ans = np.mean(new)
print("This is the average value for 50 runs and 100 iterations:", ave_ans)
#when running the code 50 times to iterate 100 times for the mean value integral, the average is pretty
#close to what we expect. 23.855 to 25.833. Although, the value actually ranges pretty bug still. 

#now we will try to up the iterations...
tot_array = []
for val in range(10000):
    new1 = meanvalue_Int(100,0,10)
    tot_array.append(new1)
ave_answer = np.mean(new1)
print("This is the average value for 10000 runs:", ave_answer)
#When changing the iterations, if the value of iterations were too small, the result was too large, if the value
#of N was too big, the result was too small. For me, about 100 was good.
#This method of determining the integral seems faster in computing. The code does take a second,
#but it is far better than I expected.

#Testing extra dimensions
new = meanvalue_Int(100,0,20)
print("New result:", new)
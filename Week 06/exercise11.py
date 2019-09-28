# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 10:02:57 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rand
from numpy import histogram as hist

#define a function to calculate the integral using mean value 
def meanvalue_Int(N, initial,final):
    #Generate the sampling values for x
    #for n in range(N):
    x = rand.uniform(initial,final, N)
        #calculate f(x) / y values for the function
    #y = np.square(x) 
    y = x**2
        #calculate the sum and mean of the y_array
    sum_function = np.sum(y)
    mean_value = (final - initial) / N
        #calculate the result
    f_result = mean_value*sum_function
    
    return f_result, x, y

#test function 
test, x_values, y_values = meanvalue_Int(10000, 0,10)
answer = test 
print("This is the approx value:", answer)
plt.plot(x_values, y_values, '.')
plt.show()
#Given how we approached the function, the graph of the x and y values generated
#makes sense and it is what is expected. When running the function several times, the output 
#value varies a quite a bit more than I thought it would.The output value ranges from
#315 to 341 whereas the analytical value is 333.333.. in the several times I ran the code.
  
#When increasing the sampling size to 10000, it actually brought the overall output to a more
#acceptable value. It actually decreases the error. The value ranges from 329 to 339 the several
#times I ran the code. 


#Now run the simulation 100 times and calculate the mean and median values for the simulation
answer_array = []
for n in range(100):
    trial, x_array, y_array = meanvalue_Int(1000, 0,10)
    answer_array.append(trial)

mean_num = np.mean(answer_array)
median_num = np.median(answer_array)
st_div = np.std(answer_array)
print("Mean value of 100 runs:", mean_num)
print("Median value of 100 runs:", median_num)
print("Error in 100 trials:", st_div)
x_array = np.arange(0,100,1)
plt.hist(answer_array)
plt.plot()

#The mean and median values are relatively close to the analytical value where
# It is difficult to say which, mean or median, is better at estimating the actual value
#of the integral. There is still the spread in values with just using 1000 samples.

#When comparing my calculated error with equation 5.80 from the book, 
st_div2 = 1/(np.sqrt(1000))*100
st_div3 = 1/ np.sqrt(1000)
print("book version for error:",st_div2)
print("error for large N:", st_div3)
#The two different values for the standard deviation are quite quite different 
#than my calculated value for the standard deviation




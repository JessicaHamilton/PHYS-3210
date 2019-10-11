# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:12:42 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import optimize 
from datetime import datetime

#Begin by plotting the function with varying m values
#define the function
def funct1(t,m):
    return (np.tanh(m / t) - m)

#Define variables
t = 0.5
m = np.arange(-5,5,0.1)
m = np.array(m)
#calculate the y values and plot
for each in m:
    y = (np.tanh(m/t) -m)
plt.scatter(m,y, s= 2)
plt.grid()
plt.title("Initial plot of function of Y_values vs. m_values")
plt.ylabel('f(m)')
plt.xlabel('m')
plt.xlim(-1,2)
plt.show()




#Now to find a the values of a function with fixed t's and constant m
t1 = np.arange(0.1,1,0.1)
t2 = np.arange(1,5, 0.5)
for tt in t1:
    m = np.arange(0,2,0.5)
    m = np.array(m)
    #calculate the y values and plot
    for each in m:
        y1 = (np.tanh(m/tt) -m)
    plt.plot(m,y1)
    plt.grid()
    plt.title('Plots of fixed t values between 0 and 1 with varying m values')

plt.show()

for ttt in t2:
    m = np.arange(0,2,0.5)
    m = np.array(m)
    #calculate the y values and plot
    for each in m:
        y2 = (np.tanh(m/ttt) -m)
    plt.plot(m,y2)
    plt.grid()
    plt.title('Plots of fixed t values above 1 with varying m values')
    
plt.show()

#Now find the roots of the equation using t = 0.5
def funct2(m):
    return (np.tanh(m / 0.5) - m)

test1 = optimize.bisect(funct2,0.5,1.5)
print("Root from Bisection method:", test1)


test2 = optimize.newton(funct2,1)
print("Root from Newton/Raphson method:", test2)    

#Estimate the time it takes to find estimates for each method
initial = datetime.now()
test1 = optimize.bisect(funct2,0.5,1.5)
print("Root from Bisection method:", test1)
final = datetime.now()

sec_initial = datetime.now()
test2 = optimize.newton(funct2,1)
print("Root from Newton/Raphson method:", test2)    
sec_final = datetime.now()

total_test1 = (final - initial)
total_test2 = (sec_final - sec_initial)
print(total_test1, total_test2)


#According to the timestamps, it seems the bisection method. This is surprising to me
#since this is the 



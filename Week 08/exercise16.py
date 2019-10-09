# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:12:42 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import optimize 

#define the function
def funct1(t,m):
    return (np.tanh(m / t) - m)

#Define variables
t = 1
m = np.arange(-5,5,0.1)
m = np.array(m)
for each in range(0,len(m)):
    y = (np.tanh(m/t) -m)
plt.scatter(m,y, s= 2)
plt.grid()
plt.title("Initial plot of function of Y_values vs. m_values")
plt.show()
#Now to find a the values of a function with fixed t's and m's
t1 = np.arange(0.01,5,0.1)
for new in range(0, len(t1)):
    y = funct1(new,1)
    plt.scatter(t1,y, s=2)
    
    
    




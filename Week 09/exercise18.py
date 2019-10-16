# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:17:06 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy 
from scipy import optimize




data = np.loadtxt('pi_meson_decays.dat')
time = data[:,0]
decay = data[:,1]

plt.scatter(time, decay, s=3)
plt.title("Decay versus time")
plt.show()
#Looking at the provided data table, the graph looks reasonable compared to figure 7.7 in the book.


#Now calculate the uncertainity and replot the data with the uncertainities
uncert = 1 / np.sqrt(len(decay))
plt.errorbar(time,decay, yerr = uncert, linestyle = "None")
plt.title("Decay versus time with uncertainities")
plt.show()



#define the function to fit the data
N = len(decay)
lamb = 1/ time
y = N*np.e**(-lamb*time)
def func(time, N, lamb):
    return N*np.e**(-lamb*time)  
    

curve1, curve2 = optimize.curve_fit(func, time, decay)
print(curve1, curve2)

"""
#Plot fit
x = np.arange(0,125,1)
y = fit_eq(x)
plt.plot(x,y)
plt.scatter(time,decay)
plt.title("Decay versus time with fitted model")
plt.show()
"""

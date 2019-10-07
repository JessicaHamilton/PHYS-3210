# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 10:13:51 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import optimize 

#Plot the function to determine what the finction looks like to helps estimate a value
Eb = np.arange(0,10, 0.1)
y = (np.sqrt(10 - Eb)*np.tan(np.sqrt(10-Eb)) - np.sqrt(Eb))


plt.plot(Eb, y)
plt.ylim(-50,50)
plt.grid()
plt.show()


#Now use the Bisection method to determine where F(Eb) = 0
def funct(Eb):
    return (np.sqrt(10 - Eb)*np.tan(np.sqrt(10-Eb)) - np.sqrt(Eb))


guess = optimize.bisect(funct, 8, 9)
print("Guess for the Bisection Method:", guess)



#Now use the Newton / Raphson Method to determine where F(Eb) = 0
x0 = 8.5

newguess = optimize.newton(funct, x0)
print("Guess for the Newton/Raphson Method:", newguess)

#When looking at the two results, there are quite similar to 10^-8 decimal place.

#Here we can run a quick loop for each method to determine a range of values to compare
set1_array = []
set2_array = []
for n in range(50):
    set1 = optimize.bisect(funct, 8,9)
    set1_array.append(set1)
    set2 = optimize.newton(funct,x0)
    set2_array.append(set2)
plt.plot(set1,set2)
plt.show()

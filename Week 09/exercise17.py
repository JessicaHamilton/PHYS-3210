# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 10:15:31 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import optimize 
from scipy.interpolate import lagrange



e = [0,25,50,75,100,125,150,175,200]
g_e = [10.6, 16.0, 45.0, 83.5, 52.8, 19.9, 10.8, 8.25, 4.7]
err = [9.34, 17.9, 41.5, 85.5, 51.5, 21.5, 10.8, 6.29, 4.14]

plt.scatter(e,g_e, s=5)
plt.title("Initial Plot of the table values")
plt.ylabel('G(E)')
plt.xlabel('E')
plt.show()

answer1 = lagrange(e,g_e)
print('Coeffs for lagrange interpolation', answer1.coeffs)
eq = np.poly1d(answer1)
print(np.poly1d(answer1))

#Now use this poly to plot the cross sections every 5 MeV
x = np.arange(0,210, 5)
y = eq(x)
y = np.array(y)
plt.plot(x,y)
plt.scatter(e, g_e, color = 'pink')
plt.title("Plot of cross sections of data with interpolated function")
plt.show()
    
#Using this produced graph we can determine the peak position
max_value = np.max(y)
print("Peak position:", max_value)

#Now to find the FWHM
#locate the two values near the half-way point on the curve then determine the distance between
half_way = max_value / 2
x_array = []
y_array = []
for numm in x:
    y = eq(numm)
    y_array.append(y)
    if y <= (half_way + 4) and y >= (half_way - 4): 
        x_array.append(numm)

dist = x_array[3] - x_array[2]
print("The FWHM:", dist)




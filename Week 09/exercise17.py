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


#My experimental values and predicted theory are in agreement for the full width half maximum. There is not
#as much agreement for the peak positing. My peak position is slightly greater in value by about 5 points. 
#I find this interesting. Even though the peak is off, the FWHM is actually on par.



#Now use interpolate over 3 data points
e1 = [e[0], e[1], e[2]]
g_e1 = [g_e[0], g_e[1], g_e[2]]

e2 = [e[1], e[2], e[3]]
g_e2 = [g_e[1], g_e[2], g_e[3]]

e3 = [e[2], e[3], e[4]]
g_e3 = [g_e[2], g_e[3], g_e[4]]

e4 = [e[3], e[4], e[5]]
g_e4 = [g_e[3], g_e[4], g_e[5]]

e5 = [e[4], e[5], e[6]]
g_e5 = [g_e[4], g_e[5], g_e[6]]

e6 = [e[4], e[5], e[6]]
g_e6 = [g_e[4], g_e[5], g_e[6]]

step1 = lagrange(e1,g_e1)
eq1 = np.poly1d(step1)
print(step1)
step2 = lagrange(e2, g_e2)
eq2 = np.poly1d(step2)
print(step2)
step3 = lagrange(e3, g_e3)
eq3 = np.poly1d(step3)
print(step3)
step4 = lagrange(e4, g_e4)
eq4 = np.poly1d(step4)
print(step4)
step5 = lagrange(e5, g_e5)
eq5 = np.poly1d(step5)
print(step5)
step6 = lagrange(e6, g_e6)
eq6 = np.poly1d(step6)
print(step6)



x1 = np.arange(0,205, 5)
y1 = eq(x1)
x2 = np.arange(0,205, 5)
y2 = eq2(x2)
x3 = np.arange(0,205, 5)
y3 = eq3(x3)
x4 = np.arange(0,205, 5)
y4 = eq4(x4)
x5 = np.arange(0,205, 5)
y5 = eq4(x5)
x6 = np.arange(0,205, 5)
y6 = eq4(x6)



plt.plot(x6, y6)
plt.plot(x5, y5)
plt.plot(x4, y4)
plt.plot(x3, y3)
plt.plot(x2, y2)
plt.plot(x1, y1)
plt.scatter(e,g_e)



"""
def three_lagr(e,g_e):
    a = 0
    b = 1
    c = 2
    total_eq = []
    for n in range(7):
        new_e = [e[a], e[b], e[c]]
        new_g = [g_e[a], g_e[b], g_e[c]]
        step = lagrange(new_e, new_g)
        #print('Coeffs for lagrange interpolation', step.coeffs)
        eq1 = np.poly1d(step)
        print(np.poly1d(step))
        total_eq.append(step)
        a = a + 1
        b = b + 1
        c = c + 1
        if c > len(e):
            return total_e


test1 = three_lagr(e,g_e)
print(test1)
"""


 




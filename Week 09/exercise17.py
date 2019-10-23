# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 10:15:31 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import optimize 
from scipy import interpolate
from scipy.interpolate import lagrange
from scipy.interpolate import interp1d
from scipy.interpolate import CubicSpline


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



#Now use interpolate over 3 data point sections
#determine the 3 x and y values for each set
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

e6 = [e[5], e[6], e[7]]
g_e6 = [g_e[5], g_e[6], g_e[7]]

e7 = [e[6], e[7], e[8]]
g_e7 = [g_e[6], g_e[7], g_e[8]]


#approx the fit and determine the equation
step1 = lagrange(e1,g_e1)
eq1 = np.poly1d(step1)
#print(step1)
step2 = lagrange(e2, g_e2)
eq2 = np.poly1d(step2)
#print(step2)
step3 = lagrange(e3, g_e3)
eq3 = np.poly1d(step3)
#print(step3)
step4 = lagrange(e4, g_e4)
eq4 = np.poly1d(step4)
#print(step4)
step5 = lagrange(e5, g_e5)
eq5 = np.poly1d(step5)
#print(step5)
step6 = lagrange(e6, g_e6)
eq6 = np.poly1d(step6)
#print(step6)
step7 = lagrange(e7, g_e7)
eq7 = np.poly1d(step7)
#print(step6)



#use equation to create sample x and y values to plot everything
x1 = np.arange(0,205, 5)
y1 = eq(x1)
y2 = eq2(x1)
y3 = eq3(x1)
y4 = eq4(x1)
y5 = eq5(x1)
y6 = eq6(x1)
y7 = eq7(x1)

#Plot everything
plt.plot(x1, y7, label = 'set-7')
plt.plot(x1, y6, label = 'set-6')
plt.plot(x1, y5, label = 'set-5')
plt.plot(x1, y4, label = 'set-4')
plt.plot(x1, y3, label = 'set-3')
plt.plot(x1, y2, label = 'set-2')
plt.plot(x1, y1, label = 'set-1')
plt.scatter(e,g_e)
plt.title("All Lagrange Interpolations for groups of 3")
plt.legend()
plt.show()


#Looking at the first set closer:
plt.plot(x1, y1, label = 'set-1')
plt.scatter(e,g_e)
plt.title('Lagrange Interpolation of first set of 3 points')
plt.show()

#Try a 1d linear interpolation and a 1d cubic spline
answer2 = interp1d(e, g_e, kind= 'linear')
answer3 = CubicSpline(e,g_e)
lin_y = answer2(x1)
cubic_y = answer3(x1)


plt.plot(x1, lin_y)
plt.scatter(e, g_e)
plt.title('Linear 1D Interpolation')
plt.show()

plt.plot(x1,cubic_y)
plt.scatter(e, g_e)
plt.title('Cubic Spline Interpolation')
plt.show()

#When looking at each graph for the different types of interpolation, it seems the cubic spline
#is providing the best fit curve for the data provided that goes through each of the points.
#When stepping through the dataset every three points, the first set provides the best curvefit when is
#comparable to the lagrange interpolation. Both the lagrange interpolation and the first set fit the data,
#but has issues with the end points. When viewing the different sets of 3, each one is fitting for the particular
#set of points, and therefore, if combined, would probably look like the first set, pretty close, but still off 
#a bit. The linear 1-D interpolation, also fit the data well, from point ot point, but it is pretty severe
#and most likely not like the actual function. The Cubic spline is the better curved version of the linear 1-
#version so to speak. It hits all the points, but is continuous.


 




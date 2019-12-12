# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 14:49:24 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt



def pend(m,l,theta):
    g = 9.8
    omega = np.sqrt(g/l)
    h = 0.001
    tnew = np.radians(10)
    tdotnew = 0
    
    time = np.arange(0,5, h)
    tnew_array = []
    tdotnew_array = []
    x_array = []
    y_array = []
    xdot_array = []
    ydot_array = []
    
    for t in time:
        tnew_1 = tnew + tdotnew*h
        tdotnew_1 = tdotnew - ((g/l)*np.sin(tnew))*h
        tnew_array.append(tnew_1)
        tdotnew_array.append(tdotnew_1)
        x = l*np.sin(tnew_1)
        y = l - l*np.cos(tnew_1)
        x_dot = l*np.sin(tdotnew_1)
        y_dot = l-l*np.cos(tdotnew_1)
        x_array.append(x)
        y_array.append(y)
        xdot_array.append(x_dot)
        ydot_array.append(y_dot)
        tnew = tnew_1
        tdotnew = tdotnew_1
        
    period = 2*np.pi*(np.sqrt(l/g))
    return tnew_array, tdotnew_array, time, period, x_array, y_array, xdot_array, ydot_array
a1, a2, a3, a4, a5, a6, a7, a8 = pend(5, 1.5, np.radians(15))
plt.plot(a1, a3)
plt.title('Theta vs. Time')
plt.show()
print('Period:', a4)
plt.plot(a7, a8)
plt.title('Velocity X vs. Velocity Y')
plt.show()
plt.plot(a3, a5)
plt.title('Position X over Time')
plt.show()
plt.plot(a5,a6)
plt.title('Position X by Position Y')
plt.show()
plt.plot(a1,a2)
plt.title('Theta vs. D_Theta')
plt.show()


#Change initial thetas for periods and for theta and d_theta graphs

b1,b2,b3,b4,b5,b6,b7,b8 = pend(1,1.5,np.radians(10))
c1,c2,c3,c4,c5,c6,c7,c8 = pend(1,1.5,np.radians(30))
d1,d2,d3,d4,d5,d6,d7,d8 = pend(1,1.5,np.radians(45))
print('Periods for changing Thetas:', b4,c4,d4)

#Changing rod lengths for periods
e1,e2,e3,e4,e5,e6,e7,e8 = pend(1, 2, np.radians(15))
f1,f2,f3,f4,f5,f6,f7,f8 = pend(1, 5, np.radians(15))
g1,g2,g3,g4,g5,g6,g7,g8 = pend(1, 7, np.radians(15))
print('Periods for changing Rod lengths:', e4,f4,g4)

#plot the tetha vs theta dot for changing thetas
plt.plot(b1,b2)
plt.title('Theta vs D_theta: 10')
plt.show()
plt.plot(c1,c2)
plt.title('Theta vs D_theta: 30')
plt.show()
plt.plot(d1,d2)
plt.title('Theta vs D_theta: 45')
plt.show()
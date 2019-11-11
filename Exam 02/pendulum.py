# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 14:49:24 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt

def pend(m,l,theta):
    g = 9.8
    A = 0.15
    omega = np.sqrt(g/l)
    h = 0.0001
    tnew = 5
    tdotnew = 0
    
    time = np.arange(0,100, h)
    tnew_array = []
    tdotnew_array = []
    x_array = []
    y_array = []
    xdot_array = []
    ydot_array = []
    
    for t in time:
        tdotnew = tdotnew + (omega*A*np.sin(omega*t + theta))*h
        tnew = tnew + tdotnew*h
        period = 2*np.pi*(np.sqrt(l/g))
        tnew_array.append(tnew)
        tdotnew_array.append(tdotnew)
        x = l*np.sin(tnew)
        y = l - l*np.cos(tnew)
        x_dot = l*np.sin(tdotnew)
        y_dot = l-l*np.cos(tdotnew)
        x_array.append(x)
        y_array.append(y)
        xdot_array.append(x_dot)
        ydot_array.append(y_dot)
    return tnew_array, tdotnew_array, time, period, x_array, y_array, xdot_array, ydot_array

a,aa,aaa,aaaa,aaaaa,aaaaaa,aaaaaaa,aaaaaaaa = pend(1,1.5,15)
print('Period:', aaaa)
plt.plot(aaaaaaa,aaaaaaaa)
plt.title('Velocity X vs. Velocity Y')
plt.show()
plt.plot(aaaaa,aaaaaa)
plt.title('Position X vs. Position Y')
plt.show()
plt.plot(aaa, a)
plt.title('Theta vs. Time')
plt.show()
plt.plot(aaa,aa)
plt.title('Theta_dot vs. Time')
plt.show()
plt.plot(aaa, aaaaa)
plt.title('Position X vs. Time')
plt.show()
plt.plot(a,aa)
plt.title('Theta_dot vs. theta')
plt.show()
"""
#Change initial thetas
a,a1,a2,a3,a4,a5,a6,a7 = pend(1,1.5,5)
b,b1,b2,b3,b4,b5,b6,b7 = pend(1,1.5,10)
c,c1,c2,c3,c4,c5,c6,c7 = pend(1,1.5,15)
d,d1,d2,d3,d4,d5,d6,d7 = pend(1,1.5,30)

plt.plot(a4,a2)
plt.plot(b4,b2)
plt.plot(c4,c2)
plt.title('Position X vs. Time: Change in Theta')
plt.show()

plt.plot(a2,a)
plt.plot(b2,b)
plt.plot(c2,c)
plt.title('Theta vs. Time: Change in Theta')
print('Periods for changing Thetas:', a3,b3,c3)

plt.show()
"""
#a,a1,a2,a3,a4,a5,a6,a7 = pend(1,1,10)
#b,b1,b2,b3,b4,b5,b6,b7 = pend(1,2,10)
#c,c1,c2,c3,c4,c5,c6,c7 = pend(1,3,10)
#d,d1,d2,d3,d4,d5,d6,d7 = pend(1,4,10)

a,a1,a2,a3,a4,a5,a6,a7 = pend(1,1,5)
b,b1,b2,b3,b4,b5,b6,b7 = pend(1,1,25)
c,c1,c2,c3,c4,c5,c6,c7 = pend(1,1,35)
d,d1,d2,d3,d4,d5,d6,d7 = pend(1,1,75)
print('Periods for changing Angles:', a3,b3,c3,d3)


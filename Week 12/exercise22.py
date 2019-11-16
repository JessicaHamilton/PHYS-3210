# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 10:39:16 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt




#define variables
E = -14
g = 0.0483
kappa_2 = -g*E
kappa = np.sqrt(kappa_2)
a = 2
x_match = 1
dx = 0.0001
V_o = -83.0 

#initialize variables and arrays
dp = 0
p = 0
dp_array1 = []
p_array1 = []
dp_array2 = []
p_array2 = []

#define functions to use
def psi(x):
    return np.exp(-kappa*abs(x))
def d_psi(x):
    return -(np.sign(x))*kappa*np.exp(-kappa*abs(x))
def d_2psi(x):
    return kappa**2*np.exp(-kappa*abs(x))

def d_2psi_in(x):
    return (V*g + kappa_2)*psi(x)


#create arrays and iterate over functions
x_array1 = np.arange(-5,x_match, dx)
x_array2 = np.arange(x_match, 5, dx)
for value in x_array1:
    if abs(value) < a:
        V = 0
        dp = dp + (d_2psi_in(value))*dx
        p = p + dp*dx
    else:
        V = V_o
        dp = dp + (d_2psi_in(value))*dx
        p = p + dp*dx
    
    dp_array1.append(dp)
    p_array1.append(p)
    
    
for value in x_array2:
    if abs(value) < a:
        V = 0
        dp = dp + d_2psi_in(value)*dx
        p = p + dp*dx
    else:
        V = V_o
        dp = dp + d_2psi_in(value)*dx
        p = p + dp*dx
    
    dp_array2.append(dp)
    p_array2.append(p)    


plt.plot(x_array1, p_array1)
plt.plot(x_array2, p_array2)
plt.title('Potential vs. Position')
plt.show()

plt.plot(x_array1, dp_array1)
plt.plot(x_array2, dp_array2)
plt.title('D-potential versus Position')
plt.show()







#Just looking a reference function
x = np.arange(-20,20,0.1)

yy = []
for each in x:
    y = -kappa*82*np.exp((-kappa**2)*abs(each))
    yy.append(y)
plt.plot(x,yy)
plt.title('Regular function for reference')
plt.show()



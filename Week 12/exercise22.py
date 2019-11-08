# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 10:39:16 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt




#define variables
E = -3
kappa = np.sqrt(2*m*E/ 1.112e-68)
m = 9.11e-31
m = 1
#a = 2
a = 2e-15
x_match = a
dx = 0.0001
V_o = -83.0 
dp = 0
p = 0
g = -0.0483
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
    return (V*g + kappa**2)*psi(x)


#create arrays and iterate over functions
x_array1 = np.arange(-5,x_match, dx)
x_array2 = np.arange(x_match, 5, -dx)

for value in x_array1:
    if abs(value) > a:
        V = 0
    else:
        V = V_o
    dp = dp + d_2psi_in(value)*dx
    p = p + dp*dx
    
    dp_array1.append(dp)
    p_array1.append(p)
    
    
for value in x_array2:
    if abs(value) > a:
        V = 0
    else:
        V = V_o
    dp = dp + d_2psi_in(value)*dx
    p = p + dp*dx
    
    dp_array2.append(dp)
    p_array2.append(p)    


plt.plot(x_array1, p_array1)
plt.plot(x_array2, p_array2)
plt.show()

#plt.plot(x_array1, dp_array1)
#plt.plot(x_array2, dp_array2)
#plt.show()

















"""
#Functions for inside and outside 'a'
def y_opos(x):
    return np.exp(-k_sq*abs(x))
def y_oneg(x):
    return np.exp(k_sq*abs(x))
def y1_opos(x):
    return -k_sq*np.exp(-k_sq*abs(x))
def y1_outneg(x):
    return k_sq*np.exp(k_sq*abs(x))
def y1_in(x):
    return -0.0483*V_o*(np.exp((-k_sq)*abs(x))) + k_sq*(np.exp((-k_sq)*abs(x)))
            


x_array1 = np.arange(-20,x_match, h)
x_array2 = np.arange(x_match, 20, h)

for value in x_array2:
    if abs(value) >= a:
        if value < a:
            ynew = ynew + y1_outneg(value)
        elif value > a:
            ynew = ynew + y1_outpos(value)
    else:
        continue
    y_array2.append(ynew)

for v in x_array1:
    if abs(v) <= a:
        ynew = ynew + (y1_in(v))*h
    else:
        if v < a:
            ynew = ynew + y1_outneg(v)
        elif v > a:
            ynew = ynew + y1_outpos(v)
        
    y_array1.append(ynew)
    
plt.plot(x_array1, y_array1)
plt.plot(x_array2, y_array2)
plt.show()


   
x_array = np.arange(-20,20,h)
for value in x_array:
    if abs(value) <= a:
        ynew = ynew + ((-0.0483*V_o*np.exp((-k_sq)*abs(value)) + k_sq*np.exp((-k_sq)*abs(value)))/m)*h
        
    elif abs(value) > a:
        ynew = -k_sq*np.exp((-k_sq)*abs(value))

    
    #update values and append to an array
    y_array.append(ynew)

plt.plot(x_array, y_array)
plt.show() 
"""





#Just looking out out function
x = np.arange(-20,20,0.1)

yy = []
for each in x:
    y = -k_sq*np.exp((-k_sq)*abs(each))
    yy.append(y)
plt.plot(x,yy)
plt.title('Regular function for reference')
plt.show()



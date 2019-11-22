# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 10:39:16 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt




    
#define variables
E = -16.059999999995185# -15.9988 # Must be negative
g = 0.0483 # value provided in book
kappa_2 = -g*E # overall positive
kappa = np.sqrt(kappa_2) #overall positive
a = 2. #Boundry of well
x_match = 1. #Matching point
dx = 0.001 #step- size
V_o = -83.0 # value provided in book

#initialize arrays
dp_array1 = []
p_array1 = []
dp_array2 = []
p_array2 = []
dE_arr1 = []
dE_arr2 = []

#define functions to use
def psi(x): # potential function where exp is overall neg
    return np.exp(-(np.sign(x))*kappa*x)
def d_psi(x): #deriv of potential function exp is overall neg and kappa is neg 
    return -(np.sign(x))*kappa*np.exp(-kappa*abs(x))
def d_2psi(x): #not used
    return kappa**2*np.exp(-kappa*abs(x))
def d_2psi_in(x,V): #sec deriv of potential function where V is defined by sign (x) and kappa**2 is overall neg * psi function 
    return (V*g + kappa_2)


#create arrays and initial variables using boundary conditions 
x_array1 = np.arange(-5,x_match, dx)
x_array2 = np.arange(5, x_match, -dx)
p1 = psi(x_array1[0])
dp1 = d_psi(x_array1[0])


#Interate over functions
#set initial variables for LEFT direction/ x_array1
dp = dp1
p = p1
x_prior = x_array1[0]
#loop over array 1, should go from left to right until reaches boundary and then goes to elif statement
for value in x_array1:
    if abs(value) > a:
        V = 0 
        dp = dp + d_2psi_in(x_prior,V)*p*dx
        p = p + dp*dx
    elif abs(value) <= a:
        V = V_o
        dp = dp + d_2psi_in(x_prior,V)*p*dx
        p = p + dp*dx
    x_prior = x_prior + dx
    dp_array1.append(dp)
    p_array1.append(p)
    deltaE = dp/p 
    dE_arr1.append(deltaE)

#set initial variables for RIGHT direction / x_array2    
dp = dp1
p = p1
x_prior = x_array2[0]
#loop over array 2, should go right to left until it reaches boundary and switches to elif statement    
for value in x_array2:
    if abs(value) > a:
        V = 0
        dp = dp + d_2psi_in(x_prior,V)*p*dx
        p = p + dp*dx
    elif abs(value) <= a:
        V = V_o
        dp = dp + d_2psi_in(x_prior,V)*p*dx
        p = p + dp*dx
        
    x_prior = value
    dp_array2.append(dp)
    p_array2.append(p)    
    deltaE = dp/p 
    dE_arr2.append(deltaE)

dE_arr1 = np.array(dE_arr1)
dE_arr2 = np.array(dE_arr2)
dE_top = dE_arr1[-1]-dE_arr2[-1]
dE_bot = dE_arr1[-1]+dE_arr2[-1]
dE_total = dE_top/dE_bot


plt.plot(x_array1, p_array1)
plt.plot(x_array2, p_array2)
plt.title('Potential vs. Position')
plt.show()





def energy(E):
    #define variables
    g = 0.0483 # value provided in book
    kappa_2 = -g*E # overall positive
    kappa = np.sqrt(kappa_2) #overall positive
    a = 2. #Boundry of well
    x_match = 1. #Matching point
    dx = 0.001 #step- size
    V_o = -83.0 # value provided in book
    
    #initialize arrays
    dp_array1 = []
    p_array1 = []
    dp_array2 = []
    p_array2 = []
    dE_arrL = []
    dE_arrR = []
    
    #define functions to use
    def psi(x): # potential function where exp is overall neg
        return np.exp(-(np.sign(x))*kappa*x)
    def d_psi(x): #deriv of potential function exp is overall neg and kappa is neg 
        return -(np.sign(x))*kappa*np.exp(-kappa*abs(x))
    def d_2psi(x): #not used
        return kappa**2*np.exp(-kappa*abs(x))
    def d_2psi_in(x,V): #sec deriv of potential function where V is defined by sign (x) and kappa**2 is overall neg * psi function 
        return (V*g + kappa_2)
    
    
    #create arrays and initial variables using boundary conditions 
    x_array1 = np.arange(-5,x_match, dx)
    x_array2 = np.arange(5, x_match, -dx)
    p1 = psi(x_array1[0])
    dp1 = d_psi(x_array1[0])
    
    
    #Interate over functions
    #set initial variables for LEFT direction/ x_array1
    dp = dp1
    p = p1
    x_prior = x_array1[0]
    #loop over array 1, should go from left to right until reaches boundary and then goes to elif statement
    for value in x_array1:
        if abs(value) > a:
            V = 0 
            dp = dp + d_2psi_in(x_prior,V)*p*dx
            p = p + dp*dx
        elif abs(value) <= a:
            V = V_o
            dp = dp + d_2psi_in(x_prior,V)*p*dx
            p = p + dp*dx
        x_prior = x_prior + dx
        dp_array1.append(dp)
        p_array1.append(p)
        deltaE = dp/p 
        dE_arrL.append(deltaE)
    
    #set initial variables for RIGHT direction / x_array2    
    dp = dp1
    p = p1
    x_prior = x_array2[0]
    #loop over array 2, should go right to left until it reaches boundary and switches to elif statement    
    for value in x_array2:
        if abs(value) > a:
            V = 0
            dp = dp + d_2psi_in(x_prior,V)*p*dx
            p = p + dp*dx
        elif abs(value) <= a:
            V = V_o
            dp = dp + d_2psi_in(x_prior,V)*p*dx
            p = p + dp*dx
            
        x_prior = value
        dp_array2.append(dp)
        p_array2.append(p)    
        deltaE = dp/p 
        dE_arrR.append(deltaE)
    
    dE_arrL = np.array(dE_arrL)
    dE_arrR = np.array(dE_arrR)
    dE_total = (dE_arrL[-1]-dE_arrR[-1])/(dE_arrL[-1]+dE_arrR[-1])
    return dE_total

e_array = np.arange(-20,-10, dx)
for value in e_array:
    total = energy(value)
    if total < dx:
        break
print('Estimated value for initial energy:', value)

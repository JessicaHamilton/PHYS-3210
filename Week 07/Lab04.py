# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 11:42:44 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt


#Define all variables and initial guesses
W1 = 1
W2 = 20
L1 = 3
L2 = 4
L3 = 4
L = 8
sth1 = 0.500
sth2 = 0.2588
sth3 = 0.7071
cth1 = 0.8660
cth2 = 0.9659
cth3 = 0.7971
T1 = 5
T2 = 5
T3 = 5 


#define functions and calculate initial function values
y1 = L1*cth1 + L2*cth2 + L3*cth3
y2 = L1*sth1 + L2*sth2 + L3*sth3
y3 = sth1**2 + cth1**2
y4 = sth2**2 + cth2**2
y5 = sth3**2 + cth3**2
y6 = T1*sth1 - T2*sth2 - W1
y7 = T1*cth1 - T2*cth2
y8 = T2*sth2 + T3*sth3 - W2
y9 = T2*cth2 + T3*cth3

f_vector = np.array([[y1],[y2],[y3],[y4],[y5],[y6],[y7],[y8],[y9]])
print(f_vector)
#find the partials for the functions per y
yy1 = 0 + 0 + 0 + L1 + L2 + L3 + 0 + 0 + 0 
yy2 = L1 + L2 + L3 + 0 + 0 + 0 + 0 + 0 + 0
yy3 = 2*sth1 + 0 + 0 + 2*cth1 + 0 + 0 + 0 + 0
yy4 = 0 + 2*sth2 + 0 + 0 + 2*cth2 + 0 + 0 + 0 + 0
yy5 = 0 + 0 + 2*sth3 + 0 + 0 + 2*cth3 + 0 + 0 + 0
yy6 = T1 - T2 + 0 + 0 + 0 + 0 + 0 + sth1 - sth2
yy7 = 0 + 0 + 0 + T1 - T2 + 0 + cth1 - cth2 + 0
yy8 = 0 + T2 + T3 + 0 + 0 + 0 + sth2 + sth3 + 0
yy9 = 0 + 0 + 0 + 0 + T2 - T3 + 0 + cth2 - cth3

jac = np.array([[yy1],[yy2],[yy3],[yy4],[yy5],[yy6],[yy7],[yy8],[yy9]])
print(jac)
inv_jac = 1 / jac
print(inv_jac)

#Start iteration for determining values
for n in range(20):
    #calculate dx
    dx = np.negative(inv_jac)*f_vector
    break
    #update guesses with dx
    sth1 = sth1 + dx
    sth2 = sth2 + dx
    sth3 = sth3 + dx
    cth1 = cth1 + dx
    cth2 = cth2 + dx
    cth3 = cth3 + dx
    T1 = T1 + dx
    T2 = T2 + dx
    T3 = T3 + dx
    #update function values 
    y1 = L1*cth1 + L2*cth2 + L3*cth3
    y2 = L1*sth1 + L2*sth2 + L3*sth3
    y3 = sth1**2 + cth1**2
    y4 = sth2**2 + cth2**2
    y5 = sth3**2 + cth3**2
    y6 = T1*sth1 - T2*sth2 - W1
    y7 = T1*cth1 - T2*cth2
    y8 = T2*sth2 + T3*sth3 - W2
    y9 = T2*cth2 + T3*cth3
    #redefine f_vector
    f_vector = np.array([[y1],[y2],[y3],[y4],[y5],[y6],[y7],[y8],[y9]])
    print(f_vector)
    #set condition to exit for loop
    for d in range(0, len(dx)):
        if d <= 10e-6:
            break
print(T1,T2,T3,sth1,sth2,sth3,cth1,cth2,cth3)








          
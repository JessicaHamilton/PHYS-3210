# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:29:01 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt



def func(x_int, v_int, h,P):
    k = 0.5
    m = 1
    x_array = []
    v_array = []
    #create new variables
    x_t = (-k/(P+1)*m)*x_int**(P+1)
    v_t = (-k/(P*m))*(x_int**P)
    a_t = (-k/m)*x_int**(P-1)
    #create initial values
    xnew = x_int + v_t*h
    vnew = v_int + a_t*h
    time = np.arange(0,30,0.01)
    for t in time:
        x_eq = -k*xnew**(P+1)/((m*P**2)+m*P)
        v_eq = (-k/P*m)*xnew**P
        a_eq = (-k/m)*x_eq**(P-1)
        
        xnew = xnew + v_eq*h
        x_array.append(xnew)
        vnew = vnew + a_eq*h
        v_array.append(vnew)
    return v_array, x_array, time

trialv, trialx, trialt = func(2,0.5,0.1,2)
plt.scatter(trialx,trialt)
plt.show()

#varying P
P = np.arange(2,12,2)
for point in P:
    testv, testx, time = func(2,0.5,0.1,point)
    plt.scatter(time, testx, s=3)
    plt.show()

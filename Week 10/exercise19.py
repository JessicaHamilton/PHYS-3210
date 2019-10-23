# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:29:01 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt



def func(x_int, v_int, h, m,P):
    k = 0.5
    #create variables
    xnew = x_int + v_int*h
    anew = (-k/m)*x_int**(P-1)
    vnew = v_int + anew*h
    x_array = []
    v_array = []
    time = np.arange(0,50,0.1)
    for t in time:
        xnew = xnew + vnew*h
        x_array.append(xnew)
        vnew = vnew + anew*h
        v_array.append(vnew)
    return v_array, x_array, time

trialv, trialx, trialt = func(1,1,0.1,1,4)
plt.scatter(time,trialx)
plt.show()
#varying P
P = np.arange(2,12,2)
for point in P:
    testv, testx, time = func(2,0.5,0.1,1,point)
    plt.scatter(time, testx, s=3)

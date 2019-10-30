# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 10:02:22 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt


def rkfunc(x_int, v_int, h, P):
    k = 5
    m = 1
    g = -9.8
    mu = 0.1
    x_array = []
    v_array = []
    #create initial steps
    xnew = x_int
    vnew = v_int
    time = np.arange(0,10, 0.0001)
    for t in time:
        #calculate half steps
        N = -(m*g)
        vmag1 = abs(vnew)
        f_static1 = -mu*N
        f_kin1 = -mu*N*(vnew/vmag1)
        f_rest = -k*(h/2)*(xnew**(P-1))
        v_half = vnew + ((f_static1 + f_kin1) + f_rest)/m
        x_half = xnew + vnew*(h/2)
        #update x and v values
        vmag2 = abs(v_half)
        f_static2 = -mu*N
        f_kin2 = -mu*N*(v_half/vmag2)
        f_rest2 = -k*(h/2)*(x_half**(P-1))
        vnew = vnew + ((f_static2 + f_kin2)*(h/2) + f_rest2)/m
        xnew = xnew + h*(v_half)
        #append to arrays
        v_array.append(vnew)
        x_array.append(xnew)
        if vnew == 0:
            if f_rest > f_static:
                continue
            else:
                break
    return v_array, x_array, time


test1, test11, test111 = rkfunc(0, 0.001, 0.0001, 2)
plt.plot(test11, test111)
plt.title('Position vs. time')
plt.xlabel('Position')
plt.ylabel('time')
plt.show()


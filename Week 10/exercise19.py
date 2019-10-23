# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:29:01 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt



def func(x_int, v_int, h, m,P):
    x_array = []
    v_array = []
    v = 0
    k = 1
    time = np.arange(0,50,1)
    for t in time:
        v = v_int + (h/m)*(-k*((x_int)**(point-1)))
        v_array.append(v)
    return v_array
P = np.arange(2,12,2)
time = np.arange(0,50,1)
for point in P:
    test = func(2,0,0.1,1,P)
    plt.scatter(time, test)
    
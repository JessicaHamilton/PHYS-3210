# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:49:31 2019

@author: hamil
"""
import numpy as np
import matplotlib.pyplot as plt


def func(x_int, v_int, h,P):
    k = 0.5
    m = 1
    x_array = []
    v_array = []
    
    #create initial step
    xnew = x_int
    vnew = v_int
    time = np.arange(0,10,0.0001)
    for t in time:
        #update values
        vnew = vnew + (-k*h*(xnew**(P-1)))/m
        xnew = xnew + vnew*h
        #append to arrays
        v_array.append(vnew)
        x_array.append(xnew)
    return v_array, x_array, time


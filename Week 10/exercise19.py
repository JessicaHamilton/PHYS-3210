# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:29:01 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt




def func(x_int, v_int, h, m, P):
    x_array = []
    v_array = []
    k = 1
    time = np.arange(0,20,h)
    for t in time:
        v = v_int + (h/m)*(-k*((x_int)**(p-1)))
        v_array.append(v)


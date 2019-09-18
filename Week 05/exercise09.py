# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:09:32 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt

def integral_funct(function, h, left, initial, final):
    #determine the values for the function
    x_values = np.arange(0,20,1)
    y_values = x_values**2
    #determine the rectangle
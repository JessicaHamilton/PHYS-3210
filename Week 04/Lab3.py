# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 10:22:47 2019

@author: hamil
"""

import random as rand
import numpy as np
import matplotlib.pyplot as plt

x = 0
y = 0
x_y_array = [[0,0]]
N = 15

for each_value in range(N):
    x_next = rand.randint(-1,1)
    y_next = rand.randint(-1,1)
    if np.abs(x_next) == np.abs(y_next):
        continue
    x = x + x_next
    y = y + y_next
    coord = [x,y]
    if coord in x_y_array == True:
        continue
    else:
        x_y_array.append(coord)
    if np.abs(x_next) >= 5 or np.abs(y_next) >=5:
        break


#x_y_array = np.array(x_y_array)
print(x_y_array)
plt.plot(x_y_array[0],x_y_array[1])
plt.show()
    
        